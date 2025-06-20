from pyrogram import Client
from Config import Config

app = Client(
    name="UserBot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    session_string=Config.SESSION_STRING,
    in_memory=True
)
