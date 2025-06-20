import asyncio
from datetime import datetime, timezone
from .DB import search_collection, stream_collection


_indexes_initialized = False


async def ensure_indexes():
    global _indexes_initialized
    if _indexes_initialized:
        return
    await search_collection.create_index("query", unique=True)
    await stream_collection.create_index("url_hash", unique=True)
    _indexes_initialized = True

# --- Search Cache ---
async def get_cached_search(query: str):
    return await search_collection.find_one({"query": query.lower()})

async def add_cached_search(query: str, result: dict):
    await search_collection.insert_one({
        "query": query.lower(),
        "result": result,
        "timestamp": datetime.now(timezone.utc)
    })

# --- Stream Cache ---
async def get_cached_stream(url_hash: str):
    return await stream_collection.find_one({"url_hash": url_hash})

async def add_cached_stream(url_hash: str, stream_url: str, video_url: str, path: str):
    await stream_collection.insert_one({
        "url_hash": url_hash,
        "video_url": video_url,
        "stream_url": stream_url,
        "path": path,
        "timestamp": datetime.now(timezone.utc)
    })
