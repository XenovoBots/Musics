from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime, timezone
from Config import Config
from .YouTube import ensure_indexes, get_cached_search, add_cached_search


client = AsyncIOMotorClient(Config.MONGO_URI)
db = client["MusicBot"]

search_collection = db["search_cache"]
stream_collection = db["stream_cache"]
