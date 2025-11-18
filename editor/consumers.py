# import json
# from channels.generic.websocket import AsyncWebsocketConsumer

# class CodeEditorConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.room_name = self.scope['url_route']['kwargs']['room_name']
#         await self.channel_layer.group_add(self.room_name, self.channel_name)
#         await self.accept()

#     async def disconnect(self, close_code):
#         await self.channel_layer.group_discard(self.room_name, self.channel_name)

#     async def receive(self, text_data):
#         data = json.loads(text_data)
#         await self.channel_layer.group_send(
#             self.room_name,
#             {
#                 'type': 'editor_update',
#                 'text': data.get('text', ''),
#                 'cursor': data.get('cursor', None),
#                 'username': self.scope.get('user').username if self.scope.get('user') and self.scope.get('user').is_authenticated else 'Anonymous',

#             }
#         )
    


#     async def editor_update(self, event):
#         msg = {
#         'text': event['text'],
#         'cursor': event.get('cursor'),
#         'username': event.get('username'),
#     }
#         await self.send(text_data=json.dumps(msg))



import json
from channels.generic.websocket import AsyncWebsocketConsumer

class CodeEditorConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'editor_{self.room_name}'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        print(f"✅ User connected to room: {self.room_name}")

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        print(f"❌ User disconnected from room: {self.room_name}")

    async def receive(self, text_data):
        data = json.loads(text_data)
        
        # Broadcast to all users in the room
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'broadcast_message',
                'data': data
            }
        )

    async def broadcast_message(self, event):
        data = event['data']
        
        # Send message to WebSocket
        await self.send(text_data=json.dumps(data))
