import asyncio
from YouTubeMusic.Search import Search
from Abhi.Database import ensure_indexes, get_cached_search, add_cached_search

async def SearchYt(query: str):
    await ensure_indexes()

    cached = await get_cached_search(query)
    if cached:
        item = cached["result"]
    else:
        results = await Search(query, limit=1)
        if not results or not results.get("main_results"):
            raise Exception("No results found.")

        item = results["main_results"][0]
        await add_cached_search(query, item)

    search_data = [{
        "title": item.get("title"),
        "artist": item.get("artist_name"),
        "channel": item.get("channel_name"),
        "duration": item.get("duration"),
        "views": item.get("views"),
        "thumbnail": item.get("thumbnail"),
        "url": item.get("url")
    }]

    song_link = item["url"]
    return search_data, song_link
