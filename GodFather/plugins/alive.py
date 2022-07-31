import datetime
import random
import time

from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from GodFather.sql.gvar_sql import gvarstat
from . import *

#-------------------------------------------------------------------------------

ALIVE_TEMP = """
╔════❰𓆩༒Alive-linux𓆩༒❱═❍⊱❁
║╭━━━━━━━━━━━━━━━➣
║┣⪼<i><b>↼ Øwñêr ⇀</i></b> : 『 <a href='tg://user?id={}'>{}</a> 』
║┣⪼𓆩༒Developer༒𓆪⭆[𝕲𝖔𝖉𝕱𝖆𝖙𝖍𝖊𝖗](t.me/GodFatherAkkii) 
║┣⪼𓆩༒X-Developer༒𓆪⭆[𝕃𝕖𝕘𝕖𝕟𝕕𝕏-ℙ𝕣𝕠](t.me/LegendHacker_IIN)
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱
╔══❰𓆩༒Ⲃⲟⲧ Ⲓⲛϝⲟʀⲙⲁⲧⲓⲟⲛ𓆩༒❱═➣
║╭━━━━━━━━━━━━━━━➣
║┣⪼𓆩༒Ⲟⲱⲛⲉʀ༒𓆪⭆[𝕲𝖔𝖉𝕱𝖆𝖙𝖍𝖊𝖗](t.me/godfatherakkii)
║┣⪼𓆩༒Ⲋⲧⲁⲧυⲋ༒𓆪⭆Ⲟⲛⳑⲓⲛⲉ
║┣⪼𓆩༒Ⲃⲟⲧ Ⳳⲉʀⲋⲓⲟⲛ༒𓆪⭆ <a href='tg://user?id={}'>{}</a>
║┣⪼𓆩༒Ⳙⲣⲧⲓⲙⲉ༒𓆪⭆      </b> <i>{}</i>
║┣⪼𓆩༒Ⲃⲟⲧ Ⲣⲓⲛⳋ༒𓆪⭆        290.09.8
║┣⪼𓆩༒𝖀𝖘𝖊𝖗𝕭𝖔𝖙༒𓆪⭆   𝕬1.0
║┣⪼𓆩༒Os:༒𓆪⭆    [Kali GNU/Linux](https://pkg.kali.org/derivative/kali-roll/) 
║┣⪼𓆩༒Ⲧⲉⳑⲉⲧⲏⲟⲛ༒𓆪⭆ </b> <i>{}</i>
║┣⪼[𓆩༒𝔾𝕆𝔻𝔽𝔸𝕋ℍ𝔼ℝ┣⪼ 𝐔𝐬𝐞𝐫𝐛𝐨𝐭༒𓆪](https://t.me/godfatherakkii)
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁
<b><i>✨✨✨ <a href='https://t.me/GodFatherUserbot'>[𝕿𝖍𝖊 𝕲𝖔𝖉𝕱𝖆𝖙𝖍𝖊𝖗𝕭𝖔𝖙]</a> ✨✨✨</i></b>
"""

msg = """{}\n
<b><i>🏅 𝙱𝚘𝚝 𝚂𝚝𝚊𝚝𝚞𝚜 🏅</b></i>
<b>Telethon ≈</b>  <i>{}</i>
<b>GodFatherẞø† ≈</b>  <i>{}</i>
<b>Uptime ≈</b>  <i>{}</i>
<b>Abuse ≈</b>  <i>{}</i>
<b>Sudo ≈</b>  <i>{}</i>
"""
#-------------------------------------------------------------------------------

@hell_cmd(pattern="alive$")
async def up(event):
    cid = await client_id(event)
    godfatherakkii, HELL_USER, hell_mention = cid[0], cid[1], cid[2]
    start = datetime.datetime.now()
    hell = await eor(event, "`Building Alive....`")
    uptime = await get_time((time.time() - StartTime))
    a = gvarstat("ALIVE_PIC")
    pic_list = []
    if a:
        b = a.split(" ")
        if len(b) >= 1:
            for c in b:
                pic_list.append(c)
        PIC = random.choice(pic_list)
    else:
        PIC = "https://telegra.ph/file/cfd870a5bf8b7d373717d.jpg"
    end = datetime.datetime.now()
    ling = (end - start).microseconds / 1000
    omk = ALIVE_TEMP.format(godfatherakkii, HELL_USER, tel_ver, hell_ver, is_sudo, uptime, ling)
    await event.client.send_file(event.chat_id, file=PIC, caption=omk, parse_mode="HTML")
    await hell.delete()



@hell_cmd(pattern="hell$")
async def hell_a(event):
    cid = await client_id(event)
    godfatherakkii, HELL_USER, hell_mention = cid[0], cid[1], cid[2]
    uptime = await get_time((time.time() - StartTime))
    am = gvarstat("ALIVE_MSG") or "<b>»» GodFtaher вσт ιѕ σиℓιиє ««</b>"
    try:
        hell = await event.client.inline_query(Config.BOT_USERNAME, "alive")
        await hell[0].click(event.chat_id)
        if event.sender_id == godfatherakkii:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg.format(am, tel_ver, hell_ver, uptime, abuse_m, is_sudo), parse_mode="HTML")


CmdHelp("alive").add_command(
  "alive", None, "Shows the Default Alive Message"
).add_command(
  "hell", None, "Shows Inline Alive Menu with more details."
).add_warning(
  "✅ Harmless Module"
).add()
