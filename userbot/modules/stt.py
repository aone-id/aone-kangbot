# Copyright (C) 2020 yincen17.
# All rights reserved.
"""
   Speech to text for your userbot
"""
import datetime
import asyncio
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot import bot, CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^.stt(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message() 
    chat = "@voicybot"
    await event.edit("Processsing```")
    async with bot.conversation(chat) as conv:
          await asyncio.sleep(2)
          await event.edit("`Converting Speech To text`")
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=259276793))
              await bot.forward_messages(chat, reply_message)
              respond = await response
          except YouBlockedUserError:
              await event.reply("```Please unblock @voicybot and try again```")
              return
          await event.delete()
          await asyncio.sleep(20)
          await bot.forward_messages(event.chat_id, respond.message)

CMD_HELP.update({
"stt":
".stt usage \
\nreply to audio files to convert audio speech to text.\n"})
