import asyncio
from YouTubeMusic.Search import Search


async def SearchYt(query: str):
    results = await Search(query, limit=1)

    if not results or not results.get("main_results"):
        raise Exception("No results found.")

    item = results["main_results"][0] 

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
