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
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'editor_update',
                'text': text_data,
            }
        )

    async def editor_update(self, event):
        await self.send(text_data=event['text'])
