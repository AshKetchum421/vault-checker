#pylint:disable=C0114
import logging
import os
from pyrogram import Client
from pyrogram.errors import RPCError
from pyrogram.errors import BadRequest

logging.basicConfig(level=logging.INFO)



bot = Client(
    'bot',
    api_id= "",
    api_hash="",
    bot_token="",
    plugins=dict(root="plugins"),
    parse_mode="html")


try:
    bot.run()
except Exception as e:
    print(e)
        
