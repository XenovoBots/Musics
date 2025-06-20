from pyrogram import Client
from Config import Config

bot = Client(
    "Bot",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    in_memory=True
)
