# Copyright (C) 2020 azrim.
# All rights reserved.
"""
   Heroku manager for your userbot
"""

import heroku3
import asyncio

from userbot import CMD_HELP, LOGS, HEROKU_APP_NAME, HEROKU_API_KEY, BOTLOG, BOTLOG_CHATID
from userbot.events import register

heroku_conn = heroku3.from_key(HEROKU_API_KEY)

@register(pattern="^.hlist(?: |$)(.*)", outgoing=True)
async def heroku_list(list):
    """ Getting Information From Heroku Account """
    if HEROKU_API_KEY is not None:
        heroku_str = list.pattern_match.group(1)
        if heroku_str == "app":
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
                await list.edit("Please setup your **HEROKU_APP_NAME** Config Variable")
        elif heroku_str == "var":
            if HEROKU_APP_NAME is not None:
                app = heroku_conn.apps()[HEROKU_APP_NAME]
                config = str(app.config())
                vlist = config.replace(",", "\n\n").replace("'", "`").replace("{", "").replace("}", "")
                if BOTLOG:
                    await list.edit(f"List of `Config Variable` has been sent to your `BOTLOG Group`")
                    await list.client.send_message(BOTLOG_CHATID, (f"**List Config Variable on Your {HEROKU_APP_NAME}:**\n\n{vlist}"))
                else:
                    await list.edit(f"Sorry, Can't send `Config Variable` to Public.\nPlease setup your **BOTLOG Group**")
            else:
                await list.edit("Please setup your **HEROKU_APP_NAME** Config Variable")
        else:
            await list.edit("Please enter valid command\nSee `.help heroku`")
    else:
        await list.edit("Please setup your **HEROKU_API_KEY** Config Variable")

#created by Adek Maulana
@register(outgoing=True, pattern=r"^.(set|del) var(?: |$)(.*)")
async def variable(var):
    """ Manage most of ConfigVars setting, set new var, or delete var... """
    if HEROKU_APP_NAME is not None:
        app = heroku_conn.app(HEROKU_APP_NAME)
    else:
        return await var.edit("`[HEROKU]:"
                              "\nPlease setup your` **HEROKU_APP_NAME**")
    exe = var.pattern_match.group(1)
    heroku_var = app.config()
    if exe == "set":
        await var.edit("`Setting information...`")
        val = var.pattern_match.group(2).split()
        try:
            val[1]
        except IndexError:
            return await var.edit("`.set var <config name> <value>`")
        await asyncio.sleep(1.5)
        if val[0] in heroku_var:
            await var.edit(f"**{val[0]}** `successfully changed to` **{val[1]}**")
        else:
            await var.edit(f"**{val[0]}** `successfully added with value:` **{val[1]}**")
        heroku_var[val[0]] = val[1]
    elif exe == "del":
        await var.edit("`Getting information to deleting vars...`")
        try:
            val = var.pattern_match.group(2).split()[0]
        except IndexError:
            return await var.edit("`Please specify config vars you want to delete`")
        await asyncio.sleep(1.5)
        if val in heroku_var:
            await var.edit(f"**{val}** `successfully deleted`")
            del heroku_var[val]
        else:
            return await var.edit(f"**{val}** `is not exists`\nDo `.hlist var` in saved message or your private group to see variable list")


CMD_HELP.update({
    "heroku":
    ".hlist <app>\
    \nUsage: List all app on your heroku account\
    \n\n.hlist <worker>\
    \nUsage: List all worker on your app\
    \n\n.hlist <var>\
    \nUsage: List all Cofig Variable on your app.\n**BE CAREFULL** It will expose your Config Var.\nDon't do this command on group!!\
    \n\n.set var <NEW VAR> <VALUE>\
    \nUsage: add new variable or update existing value variable\
    \n!!! WARNING !!!, after setting a variable the bot will restarted\
    \nThis returns all of your private information, please be caution...\
    \n\n.del var <VAR>\
    \nUsage: delete existing variable\
    \n!!! WARNING !!!, after deleting variable the bot will restarted"
})
