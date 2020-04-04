# Copyright (C) 2020 azrim.
# All rights reserved.
"""
   Heroku manager for your userbot
"""

import heroku3
import asyncio

from userbot import CMD_HELP, LOGS, HEROKU_APP_NAME, HEROKU_API_KEY
from userbot.events import register

heroku_conn = heroku3.from_key(HEROKU_API_KEY)
account = heroku_conn.account()

@register(pattern="^.heroku(?: |$)(.*)", outgoing=True)
async def heroku_list(list):
    if HEROKU_API_KEY is not None:
        heroku_str = list.pattern_match.group(1)
        if heroku_str == "applist":
            applist = str(heroku_conn.apps(order_by='id'))
            plist = applist.replace("[<app '", "").replace("<app '", "").replace("'>,", "\n\n").replace("'>]", "")
            await list.edit(f"**List App on Your Account:**\n\n`{plist}`")
        elif heroku_str == "worker":
            if HEROKU_APP_NAME is not None:
                app = heroku_conn.apps()[HEROKU_APP_NAME]
                dynolist = str(app.dynos(order_by='id'))
                dlist = dynolist.replace("[<Dyno '", "").replace("<Dyno '", "").replace("'>,", "\n\n").replace("'>]", "")
                await list.edit(f"**List Worker on Your {HEROKU_APP_NAME}:**\n\n{dlist}")
            else:
                await list.edit(f"Please setup your HEROKU_APP_NAME Config Variable")
        elif heroku_str == "varlist":
            if HEROKU_APP_NAME is not None:
                app = heroku_conn.apps()[HEROKU_APP_NAME]
                config = str(app.config())
                vlist = config.replace(",", "\n\n").replace("'", "`").replace("{", "").replace("}", "")
                await list.edit(f"**List Config Variable on Your {HEROKU_APP_NAME}:**\n\n{vlist}")
            else:
                await list.edit("Please setup your HEROKU_APP_NAME Config Variable")
        else:
            await list.edit("Please enter valid command")
            return
    else:
        await list.edit("Please setup your HEROKU_API_KEY Config Variable")

CMD_HELP.update({
    "heroku":
    ".heroku <applist>\
    \nUsage: List all app on your heroku account\
    \n\n.heroku <worker>\
    \nUsage: List all worker on your app\
    \n\n.heroku <varlist>\
    \nUsage: List all Cofig Variable on your app.\n**BE CAREFULL** Don't do this command on group!!"
})
