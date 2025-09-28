from telethon import TelegramClient


class TelegramCollector:
    """
    Collects message from Telegram channels/groups
    """

    def __init__(self, api_id, api_hash, channels):
        self.client = TelegramClient("session_name", api_id, api_hash)
        self.channles = channels


    async def fetch_message(self, limit=50):
        messages = []
        async with self.client:
            for channel in self.channles:
                async for message in self.client.iter_messages(channel, limit=limit):
                    if message.text:
                        messages.append(message.text)
        return messages