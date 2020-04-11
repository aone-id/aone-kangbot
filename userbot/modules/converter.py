# Copyright (C) 2020 Azrim.

import ffmpy
import time
import asyncio
from userbot.events import register
import os
from userbot import TEMP_DOWNLOAD_DIRECTORY ,bot
from userbot import CMD_HELP
from userbot.util import admin_cmd, humanbytes, progress, time_formatter

@register(outgoing=True, pattern=r"^.togif(?: |$)(.*)")
async def convert_gif(gif):
    if gif.fwd_from:
        return
    if not gif.is_reply:
        await gif.edit("Reply to a media to convert it.")
        return
    mone = await gif.edit("Processing ...")
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
    if gif.reply_to_msg_id:
        reply_message = await gif.get_reply_message()
        try:
            c_time = time.time()
            downloaded_file_name = await bot.download_media(
                reply_message,
                TEMP_DOWNLOAD_DIRECTORY,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, mone, c_time, "trying to download")
                )
            )
            directory_name = downloaded_file_name + ".gif"
            await gif.edit("`Converting your media....`")
            ff = ffmpy.FFmpeg(
                inputs = {downloaded_file_name : None},
                outputs = {directory_name : None})
            ff.run()

        except Exception as e:  # pylint:disable=C0103,W0703
            await mone.edit(str(e))

        except ValueError as e:
            await mone.edit(str(e))

        await asyncio.sleep(7)
        await bot.send_file(
            gif.chat_id,
            directory_name,
            caption="`Enjoy your gif`",
            force_document=False,
            allow_cache=False,
            reply_to=gif.message.id,
        )
        os.remove(directory_name)
        os.remove(downloaded_file_name)
        await gif.delete()


@register(outgoing=True, pattern=r"^.tomp4(?: |$)(.*)")
async def convert_video(mp4):
    if mp4.fwd_from:
        return
    if not mp4.is_reply:
        await mp4.edit("Reply to a media to convert it.")
        return
    mone4 = await mp4.edit("Processing ...")
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
    if mp4.reply_to_msg_id:
        reply_message = await mp4.get_reply_message()
        try:
            c_time = time.time()
            downloaded_file_name4 = await bot.download_media(
                reply_message,
                TEMP_DOWNLOAD_DIRECTORY,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, mone4, c_time, "trying to download")
                )
            )
            directory_name4 = downloaded_file_name4 + ".mp4"
            await mp4.edit("`Converting your media....`")
            ff = ffmpy.FFmpeg(
                inputs = {downloaded_file_name4 : None},
                outputs = {directory_name4 : None})
            ff.run()

        except Exception as e:  # pylint:disable=C0103,W0703
            await mone4.edit(str(e))

        except ValueError as e:
            await mone4.edit(str(e))

        await asyncio.sleep(7)
        await bot.send_file(
            mp4.chat_id,
            directory_name4,
            caption="`Enjoy your Video`",
            force_document=False,
            allow_cache=False,
            reply_to=mp4.message.id,
        )
        os.remove(directory_name4)
        os.remove(downloaded_file_name4)
        await mp4.delete()


@register(outgoing=True, pattern=r"^.tomp3(?: |$)(.*)")
async def convert_music(mp3):
    if mp3.fwd_from:
        return
    if not mp3.is_reply:
        await mp3.edit("Reply to a media to convert it.")
        return
    mone3 = await mp3.edit("Processing ...")
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
    if mp3.reply_to_msg_id:
        reply_message = await mp3.get_reply_message()
        try:
            c_time = time.time()
            downloaded_file_name3 = await bot.download_media(
                reply_message,
                TEMP_DOWNLOAD_DIRECTORY,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, mone3, c_time, "trying to download")
                )
            )
            directory_name3 = downloaded_file_name3 + ".mp3"
            await mp3.edit("`Converting your media....`")
            ff = ffmpy.FFmpeg(
                inputs = {downloaded_file_name3 : None},
                outputs = {directory_name3 : None})
            ff.run()

        except Exception as e:  # pylint:disable=C0103,W0703
            await mone3.edit(str(e))

        except ValueError as e:
            await mone3.edit(str(e))

        await asyncio.sleep(7)
        await bot.send_file(
            mp3.chat_id,
            directory_name3,
            caption="`Enjoy your Music`",
            force_document=True,
            allow_cache=False,
            reply_to=mp3.message.id,
        )
        os.remove(directory_name3)
        os.remove(downloaded_file_name3)
        await mp3.delete()


@register(outgoing=True, pattern=r"^.toflac(?: |$)(.*)")
async def convert_musicac(flac):
    if flac.fwd_from:
        return
    if not flac.is_reply:
        await flac.edit("Reply to a media to convert it.")
        return
    moneac = await flac.edit("Processing ...")
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
    if flac.reply_to_msg_id:
        reply_message = await flac.get_reply_message()
        try:
            c_time = time.time()
            downloaded_file_nameac = await bot.download_media(
                reply_message,
                TEMP_DOWNLOAD_DIRECTORY,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, moneac, c_time, "trying to download")
                )
            )
            directory_nameac = downloaded_file_nameac + ".flac"
            await flac.edit("`Converting your media....`")
            ff = ffmpy.FFmpeg(
                inputs = {downloaded_file_nameac : None},
                outputs = {directory_nameac : '-y -vn -acodec flac -ar 16000 -ac 1'})
            ff.run()

        except Exception as e:  # pylint:disable=C0103,W0703
            await moneac.edit(str(e))

        except ValueError as e:
            await moneac.edit(str(e))

        await asyncio.sleep(7)
        await bot.send_file(
            flac.chat_id,
            directory_nameac,
            caption="`Enjoy your Music`",
            force_document=True,
            allow_cache=False,
            reply_to=flac.message.id,
        )
        os.remove(directory_nameac)
        os.remove(downloaded_file_nameac)
        await flac.delete()


CMD_HELP.update({
    "converter":
    ".togif\
    \nUsage: Reply to media to convert as gif.\
    \n.tomp4\
    \nUsage: Reply to media to convert as mp4.\
    \n.tomp3\
    \nUsage: Reply to media to convert as mp3.\
    \n.toflac\
    \nUsage: Reply to media to convert as flac."
})
