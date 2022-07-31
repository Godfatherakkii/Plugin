import asyncio
import datetime
import importlib
import inspect
import logging
import math
import os
import re
import sys
import time
import traceback
from pathlib import Path
from time import gmtime, strftime

from telethon import events
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantCreator, InputMessagesFilterDocument

from GodFather import *
from GodFather.clients import *
from GodFather.helpers import *
from GodFather.config import *
from GodFather.utils import *


# ENV
ENV = bool(os.environ.get("ENV", False))
if ENV:
    from GodFather.config import Config
else:
    if os.path.exists("Config.py"):
        from Config import Development as Config


# load plugins
def load_module(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import GodFather.utils

        path = Path(f"PluginGod/plugins/{shortname}.py")
        name = "PluginGod.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        LOGS.info("𝔊𝔬𝔡𝔉𝔞𝔱𝔥𝔢𝔯𝔅𝔬𝔱 - 𝔖𝔲𝔠𝔠𝔢𝔰𝔰𝔣𝔲𝔩𝔩𝔶 𝔦𝔪𝔭𝔬𝔯𝔱𝔢𝔡 " + shortname)
    else:
        import GodFather.utils

        path = Path(f"PluginGod/plugins/{shortname}.py")
        name = "PluginGod.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.bot = Hell
        mod.H1 = Hell
        mod.H2 = H2
        mod.H3 = H3
        mod.H4 = H4
        mod.H5 = H5
        mod.Hell = Hell
        mod.GodFather = GodFather
        mod.tbot = GodFather
        mod.tgbot = bot.tgbot
        mod.command = command
        mod.CmdHelp = CmdHelp
        mod.client_id = client_id
        mod.logger = logging.getLogger(shortname)
        # support for uniborg
        sys.modules["uniborg.util"] = GodFather.utils
        mod.Config = Config
        mod.borg = bot
        mod.GodFather = bot
        mod.edit_or_reply = edit_or_reply
        mod.eor = edit_or_reply
        mod.delete_hell = delete_hell
        mod.eod = delete_hell
        mod.Var = Config
        mod.admin_cmd = admin_cmd
        mod.hell_cmd = hell_cmd
        mod.sudo_cmd = sudo_cmd
        # support for other userbots
        sys.modules["userbot.utils"] = GodFather.utils
        sys.modules["userbot"] = GodFather
        # support for paperplaneextended
        sys.modules["userbot.events"] = GodFather
        spec.loader.exec_module(mod)
        # for imports
        sys.modules["PluginGod.plugins." + shortname] = mod
        LOGS.info("💥𝔊𝔬𝔡𝔉𝔞𝔱𝔥𝔢𝔯𝔅𝔬𝔱💥- 𝔖𝔲𝔠𝔠𝔢𝔰𝔰𝔣𝔲𝔩𝔩𝔶 ℑ𝔪𝔭𝔬𝔯𝔱𝔢𝔡" + shortname)


# remove plugins
def remove_plugin(shortname):
    try:
        try:
            for i in LOAD_PLUG[shortname]:
                bot.remove_event_handler(i)
            del LOAD_PLUG[shortname]

        except BaseException:
            name = f"GodFather.plugins.{shortname}"

            for i in reversed(range(len(bot._event_builders))):
                ev, cb = bot._event_builders[i]
                if cb.__module__ == name:
                    del bot._event_builders[i]
    except BaseException:
        raise ValueError


async def plug_channel(client, channel):
    if channel:
        LOGS.info("💥𝕲𝖔𝖉𝕱𝖆𝖙𝖍𝖊𝖗𝕭𝖔𝖙💥- 𝕻𝕷𝖀𝕲𝕴𝕹 𝕮𝕳𝕬𝕹𝕹𝕰𝕷 𝕯𝕰𝕿𝕰𝕮𝕿𝕰𝕯")
        LOGS.info("💥𝕲𝖔𝖉𝕱𝖙𝖆𝖍𝖊𝖗𝕭𝖔𝖙💥 - 𝕾𝖙𝖆𝖗𝖙𝖎𝖓𝖌 𝖙𝖔 𝖑𝖔𝖆𝖉 𝖊𝖝𝖙𝖗𝖆 𝖕𝖑𝖚𝖌𝖎𝖓𝖘")
        plugs = await client.get_messages(channel, None, filter=InputMessagesFilterDocument)
        total = int(plugs.total)
        for plugins in range(total):
            plug_id = plugs[plugins].id
            plug_name = plugs[plugins].file.name
            if os.path.exists(f"PluginGod/plugins/{plug_name}"):
                return
            downloaded_file_name = await client.download_media(
                await client.get_messages(channel, ids=plug_id),
                "PluginGod/plugins/",
            )
            path1 = Path(downloaded_file_name)
            shortname = path1.stem
            try:
                load_module(shortname.replace(".py", ""))
            except Exception as e:
                LOGS.error(str(e))


# GodFather
