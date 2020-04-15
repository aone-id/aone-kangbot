#created by @eve_enryu

import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot import bot, CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^.firmware(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@XiaomiGeeksBot"
    firmware = f"firmware"
    await event.edit("```Processing```")
    async with bot.conversation("@XiaomiGeeksBot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=774181428))
              await conv.send_message(f'/{firmware} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @XiaomiGeeksBot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)
                
                
@register(outgoing=True, pattern="^.eu(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@XiaomiGeeksBot"
    mieu = f"eu"
    await event.edit("```Processing```")
    async with bot.conversation("@XiaomiGeeksBot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=774181428))
              await conv.send_message(f'/{mieu} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @xiaomiGeeksBot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)
                
                
@register(outgoing=True, pattern="^.fastboot(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@XiaomiGeeksBot"
    fboot = f"fastboot"
    await event.edit("```Processing```")
    async with bot.conversation("@XiaomiGeeksBot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=774181428))
              await conv.send_message(f'/{fboot} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @XiaomiGeeksBoot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)
                
                
@register(outgoing=True, pattern="^.recovery(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@XiaomiGeeksBot"
    recovery = f"recovery"
    await event.edit("```Processing```")
    async with bot.conversation("@XiaomiGeeksBot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=774181428))
              await conv.send_message(f'/{recovery} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @ofoxr_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)
                
                
                
@register(outgoing=True, pattern="^.spec(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@XiaomiGeeksBot"
    spec = f"specs"
    await event.edit("```Processing```")
    async with bot.conversation("@XiaomiGeeksBot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=774181428))
              await conv.send_message(f'/{spec} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @ofoxr_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)
                
                
@register(outgoing=True, pattern="^.pb(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@XiaomiGeeksBot"
    pitch = f"pb"
    await event.edit("```Processing```")
    async with bot.conversation("@XiaomiGeeksBot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=774181428))
              await conv.send_message(f'/{pitch} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @ofoxr_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

CMD_HELP.update({
"oprek":
"For Xiaomeme devices only!\
.firmware (codename)\
     \n\nUsage : Get lastest Firmware\
.pb (codename)\
     \n\nUsage : Get latest PBRP\
.spec (codename)\
     \n\nUsage : Get quick spec information about device\
.fastboot (codename)\
     \n\nUsage : Get latest fastboot MIUI\
.recovery (codename))\
     \n\nUsage : Get latest recovery MIUI"})
