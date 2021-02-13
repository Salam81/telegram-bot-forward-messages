# telegram-bot-forward-messages
Telegram bot which will forward a message from a channel/chat to another chat.


# Installation

Requires [Telethon](https://github.com/LonamiWebs/Telethon)

```sh
# Install Telethon
$ pip3 install -U telethon --user

# Verify Telethon's version:
$ python3 -c "import telethon; print(telethon.__version__)"
```

# API Keys
The script requires your Telegram API keys.
  - Proceed to https://my.telegram.org
  - Enter your phone number and confirmation code.
  - Click on **API development tools** -> **App configuration**
  - Copy **App api_id** and **App api_hash**

# Variables
```python
# Telegram 'api_id' Key
API_ID = environ['API_ID']

# Telegram 'api_hash' Key
API_HASH = environ['API_HASH']

# Channel/Chat's name for incoming messages
GROUP = environ['GROUP']

# The recipient of the message. @username or me 
RECIPIENT = environ['RECIPIENT']
```