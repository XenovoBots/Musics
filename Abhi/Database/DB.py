from motor.motor_asyncio import AsyncIOMotorClient
#from Config import Config

client = AsyncIOMotorClient("mongodb+srv://Music:Sinchu@cluster0.afnf5ch.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["MusicBot"]

search_collection = db["search_cache"]
stream_collection = db["stream_cache"]
