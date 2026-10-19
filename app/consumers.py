import json

from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    """Broadcast validated text messages to everyone in the same room."""

    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data=None, bytes_data=None):
        if not text_data:
            return
        try:
            payload = json.loads(text_data)
        except json.JSONDecodeError:
            await self.send(text_data=json.dumps({"error": "Invalid JSON payload."}))
            return

        message = payload.get("message") if isinstance(payload, dict) else None
        if not isinstance(message, str):
            await self.send(text_data=json.dumps({"error": "The message must be a string."}))
            return
        message = message.strip()
        if not message:
            await self.send(text_data=json.dumps({"error": "The message cannot be empty."}))
            return
        if len(message) > 2000:
            await self.send(text_data=json.dumps({"error": "The message is too long (maximum 2000 characters)."}))
            return

        await self.channel_layer.group_send(self.room_group_name, {"type": "chat.message", "message": message})

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({"message": event["message"]}))
