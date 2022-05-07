#pylint:disable=C0114
import logging
import os
from pyrogram import Client
from pyrogram.errors import RPCError
from pyrogram.errors import BadRequest

logging.basicConfig(level=logging.INFO)



bot = Client(
    'bot',
    api_id= "5465540",
    api_hash="c7dca7582d73d24d99889a3f2dd079cf",
    bot_token="5359922788:AAHnkVAC01ED4gin15xgLCXXd-sQBmkGaB4",
    plugins=dict(root="plugins"),
    parse_mode="html")


try:
    bot.run()
except Exception as e:
    print(e)
        
