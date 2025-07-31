import hashlib
import aiohttp
from Abhi.Database import ensure_indexes, get_cached_stream, add_cached_stream
from YouTubeMusic.Stream import get_audio_url

async def is_url_valid(url: str) -> bool:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.head(url, timeout=5) as resp:
                return resp.status == 200
    except:
        return False

async def Ytdl(url: str) -> str:
    await ensure_indexes()
    url_hash = hashlib.md5(url.encode()).hexdigest()

    cached = await get_cached_stream(url_hash)
    if cached and cached.get("stream_url"):
        stream_url = cached["stream_url"]
        if await is_url_valid(stream_url):
            return stream_url

    stream_url = get_audio_url(url, "cookies/cookies.txt")
    if not stream_url:
        raise Exception("Failed to extract stream URL via yt-dlp")

    await add_cached_stream(url_hash, stream_url, url)
    return stream_url
