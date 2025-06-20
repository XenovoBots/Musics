from motor.motor_asyncio import AsyncIOMotorClient
from Config import Config

client = AsyncIOMotorClient(Config.MONGO_URI)
db = client["MusicBot"]

search_collection = db["search_cache"]
stream_collection = db["stream_cache"]
