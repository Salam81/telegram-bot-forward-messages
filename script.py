from telethon import TelegramClient, events, sync
from os import environ

API_ID = environ['API_ID']
API_HASH = environ['API_HASH']
GROUP = environ['GROUP']
RECIPIENT = environ['RECIPIENT']

client = TelegramClient('bot', API_ID, API_HASH)

@client.on(events.NewMessage(chats=GROUP))
async def newMessageListener(event):
    msg = event.message
    print('Message: ' + msg.message)
    await client.forward_messages(entity=RECIPIENT, messages=msg)

with client:
    client.run_until_disconnected()