#    Friendly Telegram (telegram userbot)
#    Copyright (C) 2018-2019 The Authors

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
----------------------------------------------------------------
All Thenks goes to Emily ( The creator of This Plugin)
\nSome credits goes to me ( @kirito6969 ) for ported this plugin to uniborg
\nSome credits goes to me ( @azrim89 ) for ported this plugin to userbot
\nand `SnapDragon for` Helping me.
----------------------------------------------------------------

Type `.poto` for get **All profile pics of that User**
\nOr type `.poto (number)` to get the **desired number of photo of a User** .
"""

from userbot import CMD_HELP
from userbot.events import register

from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_input_location
import asyncio


if 1 == 1:
    name = "Profile Photos"
    client = "userbot"

@register(outgoing=True, pattern="^.poto(?: |$)(.*)", disable_errors=True)
async def potocmd(event):
    """Gets the profile photos of replied users, channels or chats"""
    id = "".join(event.raw_text.split(maxsplit=2)[1:])
    user = await event.get_reply_message()
    chat = event.input_chat
    await event.edit(f"`Processing........`")
    if user:
        photos = await event.client.get_profile_photos(user.sender)
        u = True
    else:
        photos = await event.client.get_profile_photos(chat)
        u = False
    if id.strip() == "":
        if len(photos) > 0:
            await event.client.send_file(event.chat_id, photos)
            await event.edit(f"`Photos uploaded successfully`")
        else:
            try:
                if u is True:
                    photo = await event.client.download_profile_photo(user.sender)
                else:
                    photo = await event.client.download_profile_photo(event.input_chat)
                await event.client.send_file(event.chat_id, photo)
                await event.edit(f"`Photos uploaded successfully`")
            except a:
                await event.edit("**This user has no photos!**")
                return
    else:
        try:
            id = int(id)
            if id <= 0:
                await event.edit("`ID number Invalid!` **Are you kidding Me ?**")
                return
        except:
            await event.edit(f"`Are you kidding me ?`")
            return
        if int(id) <= (len(photos)):
            send_photos = await event.client.download_media(photos[id - 1])
            await event.client.send_file(event.chat_id, send_photos)
        else:
            await event.edit(f"`No photos found`")
            await asyncio.sleep(8)
            return


CMD_HELP.update({
    "poto":
    ".poto <reply message>\
\nUsage: Upload all profile pictures of user"
})
