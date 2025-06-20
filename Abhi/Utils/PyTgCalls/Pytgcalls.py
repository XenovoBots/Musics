"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎵 ϻᴜsɪᴄ ᴘʟᴧʏєʀ ᴍᴏᴅᴜʟᴇ
📍 Telegram: @AboutRealAbhi
©️ 2025 All Rights Reserved
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

import os
import asyncio
from Abhi.Clients import xenovo
from pytgcalls.types import MediaStream, VideoQuality, AudioQuality


SAMPLE_AUDIO = "http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4"

QUALITY_MAP = {
    "uhd_4k": VideoQuality.UHD_4K,
    "qhd_2k": VideoQuality.QHD_2K,
    "fhd_1080p": VideoQuality.FHD_1080p,
    "hd_720p": VideoQuality.HD_720p,
    "sd_480p": VideoQuality.SD_480p,
    "sd_360p": VideoQuality.SD_360p,
}


async def xenovo_audio(chat_id: int, audio_file: str = SAMPLE_AUDIO):
    try:
        stream = MediaStream(
            media_path=audio_file,
            audio_parameters=AudioQuality.STUDIO,
            video_flags=MediaStream.Flags.IGNORE
        )
        await xenovo.play(chat_id, stream)
        return True, None
    except Exception as e:
        return False, f"** єʀʀᴏʀ ᴘʟᴀʏɪɴɢ ᴀᴜᴅɪᴏ**:\n<code>{e}</code>"


async def xenovo_video(chat_id: int, video_file: str, quality: str = "sd_480p"):
    try:
        video_quality = QUALITY_MAP.get(quality.lower(), VideoQuality.SD_480p)

        stream = MediaStream(
            media_path=video_file,
            audio_parameters=AudioQuality.MEDIUM,
            video_parameters=video_quality
        )
        await xenovo.play(chat_id, stream)
        return True, None
    except Exception as e:
        return False, f"**єʀʀᴏʀ ᴘʟᴀʏɪɴɢ ᴠɪᴅᴇᴏ**:\n<code>{e}</code>"


# ╭────────────────────────────────╮
# │    ϻᴜsɪᴄ ᴘʟᴧʏєʀ ᴄᴏɴᴛʀᴏʟꜱ & ʀᴇᴘʟɪᴇꜱ    │
# ╰────────────────────────────────╯

async def pause(chat_id: int, user_mention: str, chat_name: str):
    try:
        await call.pause(chat_id)
        return f"** ѕᴛʀєᴀᴍ ᴘᴀᴜѕєᴅ** \n** ʙʏ {user_mention}**\n **ɪɴ {chat_name}**"
    except Exception as e:
        return f"** єʀʀᴏʀ ᴘᴀᴜѕɪɴɢ**:\n<code>{e}</code>"


async def resume(chat_id: int, user_mention: str, chat_name: str):
    try:
        await call.resume(chat_id)
        return f"**ѕᴛʀєᴀᴍ ʀєѕᴜᴍєᴅ** \n **ʙʏ {user_mention}**\n** ɪɴ {chat_name}**"
    except Exception as e:
        return f"** єʀʀᴏʀ ʀєѕᴜᴍɪɴɢ**:\n<code>{e}</code>"


async def mute(chat_id: int, user_mention: str, chat_name: str):
    try:
        await call.mute(chat_id)
        return f"**ѕᴛʀєᴀᴍ ᴍᴜᴛєᴅ **\n** ʙʏ {user_mention}**\n** ɪɴ {chat_name}**"
    except Exception as e:
        return f"** єʀʀᴏʀ ᴍᴜᴛɪɴɢ**:\n<code>{e}</code>"


async def unmute(chat_id: int, user_mention: str, chat_name: str):
    try:
        await call.unmute(chat_id)
        return f"** ѕᴛʀєᴀᴍ ᴜɴᴍᴜᴛєᴅ** \n **ʙʏ {user_mention}**\n** ɪɴ {chat_name}**"
    except Exception as e:
        return f"** єʀʀᴏʀ ᴜɴᴍᴜᴛɪɴɢ**:\n<code>{e}</code>"


async def change_volume(chat_id: int, volume: int, user_mention: str, chat_name: str):
    try:
        await call.change_volume(chat_id, volume)
        return f"**🎧 νᴏʟᴜᴍє ѕєᴛ ᴛᴏ** <b>{volume}%</b> \n **ʙʏ {user_mention}**\n ɪɴ** {chat_name}**"
    except Exception as e:
        return f"** єʀʀᴏʀ ѕєᴛᴛɪɴɢ νᴏʟᴜᴍє**:\n<code>{e}</code>"


async def stop(chat_id: int, user_mention: str, chat_name: str):
    try:
        await call.leave_call(chat_id)
        return f"**ѕᴛʀєᴀᴍ ѕᴛᴏᴘᴘєᴅ **\n** ʙʏ {user_mention}**\n** ɪɴ {chat_name}**"
    except Exception as e:
        return f"**єʀʀᴏʀ ѕᴛᴏᴘᴘɪɴɢ**:\n<code>{e}</code>"
      
