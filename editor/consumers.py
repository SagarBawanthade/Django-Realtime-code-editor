import json
from channels.generic.websocket import AsyncWebsocketConsumer

class CodeEditorConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        await self.channel_layer.group_add(self.room_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'editor_update',
                'text': data.get('text', ''),
                'cursor': data.get('cursor', None),
                'username': self.scope.get('user').username if self.scope.get('user') and self.scope.get('user').is_authenticated else 'Anonymous',

            }
        )
    


    async def editor_update(self, event):
        msg = {
        'text': event['text'],
        'cursor': event.get('cursor'),
        'username': event.get('username'),
    }
        await self.send(text_data=json.dumps(msg))

