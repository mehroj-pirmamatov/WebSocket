from django.test import SimpleTestCase, override_settings
from channels.testing import WebsocketCommunicator

from config.asgi import application


@override_settings(
    ALLOWED_HOSTS=["testserver"],
    CHANNEL_LAYERS={"default": {"BACKEND": "channels.layers.InMemoryChannelLayer"}},
)
class ChatConsumerTests(SimpleTestCase):
    async def test_message_is_broadcast_to_room(self):
        headers = [(b"origin", b"http://testserver")]
        first = WebsocketCommunicator(application, "/ws/chat/room1/", headers=headers)
        second = WebsocketCommunicator(application, "/ws/chat/room1/", headers=headers)
        connected, _ = await first.connect()
        self.assertTrue(connected)
        connected, _ = await second.connect()
        self.assertTrue(connected)
        await first.send_json_to({"message": "hello"})
        self.assertEqual(await first.receive_json_from(), {"message": "hello"})
        self.assertEqual(await second.receive_json_from(), {"message": "hello"})
        await first.disconnect()
        await second.disconnect()

    async def test_empty_message_is_rejected(self):
        communicator = WebsocketCommunicator(
            application,
            "/ws/chat/room1/",
            headers=[(b"origin", b"http://testserver")],
        )
        connected, _ = await communicator.connect()
        self.assertTrue(connected)
        await communicator.send_json_to({"message": "  "})
        self.assertEqual(await communicator.receive_json_from(), {"error": "The message cannot be empty."})
        await communicator.disconnect()
