import datetime
import time

from GodFather import *
from GodFather.clients import *
from GodFather.config import Config
from GodFather.helpers import *
from GodFather.utils import *
from GodFather.random_strings import *
from GodFather.version import __hell__
from GodFather.sql.gvar_sql import gvarstat
from telethon import version

hell_logo = "./GodFather/resources/pics/GodFtaher_logo.jpg"
cjb = "./GodFather/resources/pics/cjb.jpg"
restlo = "./GodFather/resources/pics/rest.jpeg"
shuru = "./GodFather/resources/pics/shuru.jpg"
shhh = "./GodFather/resources/pics/chup_madarchod.jpeg"
hl = Config.HANDLER
shl = Config.SUDO_HANDLER
hell_ver = __hell__
tel_ver = version.__version__

async def get_user_id(ids):
    if str(ids).isdigit():
        userid = int(ids)
    else:
        userid = (await bot.get_entity(ids)).id
    return userid

is_sudo = "True" if gvarstat("SUDO_USERS") else "False"

abus = Config.ABUSE
if abus == "ON":
    abuse_m = "Enabled"
else:
    abuse_m ="Disabled"


my_channel = Config.MY_CHANNEL or "GodfatherUserBot"
my_group = Config.MY_GROUP or "Godfatherchat"
if "@" in my_channel:
    my_channel = my_channel.replace("@", "")
if "@" in my_group:
    my_group = my_group.replace("@", "")

chnl_link = "https://t.me/GodfatherUserBot"
hell_channel = f"[𝕲𝖔𝖉𝕱𝖙𝖆𝖍𝖊𝖗]({chnl_link})"
grp_link = "https://t.me/GodfatherChat"
hell_grp = f"[𝕲𝖔𝖉𝕱𝖙𝖆𝖍𝖊𝖗 𝖇𝖔𝖙]({grp_link})"

WELCOME_FORMAT = """**Use these fomats in your welcome note to make them attractive.**
  {mention} :  To mention the user
  {title} : To get chat name in message
  {count} : To get group members
  {first} : To use user first name
  {last} : To use user last name
  {fullname} : To use user full name
  {userid} : To use userid
  {username} : To use user username
  {my_first} : To use my first name
  {my_fullname} : To use my full name
  {my_last} : To use my last name
  {my_mention} : To mention myself
  {my_username} : To use my username
"""
# will add more soon

# GodFtaher
