import time

async def SearchYt(query: str):
    await ensure_indexes()

    normalized_query = query.lower().strip()
    start = time.time()  # Start timing

    cached = await get_cached_search(normalized_query)
    if cached:
        print("✅ Using cached search result")
        item = cached["result"]
    else:
        print("🔍 Performing fresh search...")
        results = await Search(query, limit=1)
        if not results or not results.get("main_results"):
            raise Exception("❌ No results found.")

        item = results["main_results"][0]
        await add_cached_search(normalized_query, item)

    end = time.time()  # End timing
    print(f"⏱️ Search Time Taken: {end - start:.2f} seconds")

    # Format output
    search_data = [{
        "title": item.get("title"),
        "artist": item.get("artist_name"),
        "channel": item.get("channel_name"),
        "duration": item.get("duration"),
        "views": item.get("views"),
        "thumbnail": item.get("thumbnail"),
        "url": item.get("url")
    }]

    return search_data, item["url"]
