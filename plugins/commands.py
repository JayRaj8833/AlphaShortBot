import contextlib
import datetime
import logging
import traceback
import aiohttp
from validators import domain
from config import (
    ADMINS,
    LOG_CHANNEL,
    SOURCE_CODE,
    WELCOME_IMAGE,
)
from database import db
from database.users import get_user, is_user_exist, total_users_count, update_user_info
from helpers import temp
from pyrogram import Client, filters
from pyrogram.types import Message
from plugins.filters import private_use
from translation import *
from utils import extract_link, get_me_button, get_size

logger = logging.getLogger(__name__)

user_commands = [
    "mdisk_api",
    "shortener_api",
    "header",
    "footer",
    "username",
    "banner_image",
    "base_site",
    "settings",
]
avl_web = [
    "earn4links.site",
]

avl_web1 = "".join(f"- {i}\n" for i in avl_web)


@Client.on_message(filters.command("start") & filters.private)
@private_use
async def start(c: Client, m: Message):
    if len(m.command) >=2 and m.text.split()[1].startswith("api"):
        api_key = m.text.split()[1].split("_")[1]
        user_id = m.from_user.id
        if await is_user_exist(user_id):
            user = await get_user(user_id)
            if user["shortener_api"] is not None:
                await update_user_info(user_id, {"shortener_api": api_key})
                await m.reply_text(f"Shortener API Updated")
                return
            await update_user_info(user_id, {"shortener_api": api_key})
            await m.reply_text(f"Yᴏᴜʀ earn4links.site API Cᴏɴɴᴇᴄᴛᴇᴅ Sᴜᴄᴄᴇssғᴜʟʟʏ.")
        return
    NEW_USER_REPLY_MARKUP = [
        [
            InlineKeyboardButton("Ban", callback_data=f"ban#{m.from_user.id}"),
            InlineKeyboardButton("Close", callback_data="delete"),
        ]
    ]
    is_user = await is_user_exist(m.from_user.id)

    reply_markup = InlineKeyboardMarkup(NEW_USER_REPLY_MARKUP)

    if not is_user and LOG_CHANNEL:
        await c.send_message(
            LOG_CHANNEL,
            f"#NewUser\n\nUser ID: `{m.from_user.id}`\nName: {m.from_user.mention}",
            reply_markup=reply_markup,
        )
    new_user = await get_user(m.from_user.id)
    t = START_MESSAGE.format(
        m.from_user.mention, new_user["method"], new_user["base_site"]
    )

    if WELCOME_IMAGE:
        return await m.reply_photo(
            photo=WELCOME_IMAGE, caption=t, reply_markup=START_MESSAGE_REPLY_MARKUP
        )
    await m.reply_text(
        t, reply_markup=START_MESSAGE_REPLY_MARKUP, disable_web_page_preview=True, protect_content=True
    )


@Client.on_message(filters.command("help") & filters.private)
@private_use
async def help_command(c, m: Message):
    s = HELP_MESSAGE.format(
        firstname=temp.FIRST_NAME,
        username=temp.BOT_USERNAME,
        repo=SOURCE_CODE,
        owner="@JayRaj8833",
    )

    if WELCOME_IMAGE:
        return await m.reply_photo(
            photo=WELCOME_IMAGE, caption=s, reply_markup=HELP_REPLY_MARKUP
        )
    await m.reply_text(s, reply_markup=HELP_REPLY_MARKUP, disable_web_page_preview=True, protect_content=True)


@Client.on_message(filters.command("about"))
@private_use
async def about_command(c, m: Message):
    reply_markup = ABOUT_REPLY_MARKUP

    bot = await c.get_me()
    if WELCOME_IMAGE:
        return await m.reply_photo(
            photo=WELCOME_IMAGE,
            caption=ABOUT_TEXT.format(bot.mention(style="md")),
            reply_markup=reply_markup,
        )
    await m.reply_text(
        ABOUT_TEXT.format(bot.mention(style="md")),
        reply_markup=reply_markup,
        disable_web_page_preview=True,
    )

@Client.on_message(filters.command("admin"))
@private_use
async def about_command(c, m: Message):
    reply_markup = ADMIN_HELP_REPLY_MARKUP
    if m.reply_to_message:
        await m.reply_to_message.delete() 
    bot = await c.get_me()
    if WELCOME_IMAGE:
        await m.reply_photo(
            photo=WELCOME_IMAGE,
            caption=ADMINX.format(bot.mention(style="md")),
            reply_markup=reply_markup,
        )
    else:
        await m.reply_text(
            ADMINX.format(bot.mention(style="md")),
            reply_markup=reply_markup,
            disable_web_page_preview=True,
        )


@Client.on_message(filters.command("method") & filters.private)
@private_use
async def method_handler(c: Client, m: Message):
    user_id = m.from_user.id
    user = await get_user(user_id)
    cmd = m.command
    if len(cmd) == 1:
        s = METHOD_MESSAGE.format(method=user["method"], shortener=user["base_site"])
        return await m.reply(s, reply_markup=METHOD_REPLY_MARKUP)
    elif len(cmd) == 2:
        method = cmd[1]
        if method not in ["mdisk", "mdlink", "shortener"]:
            return await m.reply(METHOD_MESSAGE.format(method=user["method"]))
        await update_user_info(user_id, {"method": method})
        await m.reply(f"Method Updated Successfully To {method}")


@Client.on_message(filters.command("restart") & filters.user(ADMINS) & filters.private)
@private_use
async def restart_handler(c: Client, m: Message):
    RESTARTE_MARKUP = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Sure", callback_data="restart"),
                InlineKeyboardButton("Disable", callback_data="delete"),
            ]
        ]
    )
    await m.reply(
        "Are You Sure You Want To Restart/Re-Deploy The Server ?",
        reply_markup=RESTARTE_MARKUP,
    )


@Client.on_message(filters.command("stats") & filters.private & filters.user(ADMINS))
@private_use
async def stats_handler(c: Client, m: Message):
    try:
        txt = await m.reply("`Fetching Stats...`")
        size = await db.get_db_size()
        free = 536870912 - size
        size = await get_size(size)
        free = await get_size(free)
        link_stats = await db.get_bot_stats()
        runtime = datetime.datetime.now()

        t = runtime - temp.START_TIME
        runtime = str(datetime.timedelta(seconds=t.seconds))
        total_users = await total_users_count()

        msg = f"""
<b>╭─────❪ 𝗦𝗧𝗔𝗧𝗨𝗦 ❫─────⍟
│
├⍟ Aᴄᴛɪᴠᴇ Uꜱᴇʀꜱ : `{total_users}`
│
├⍟ Tᴏᴛᴀʟ Posᴛs Sᴇɴᴛ : `{link_stats['posts']}`
│
├⍟ Tᴏᴛᴀʟ Lɪɴᴋs Sʜᴏʀᴛᴇɴᴇᴅ : `{link_stats['links']}`
│
├⍟ Tᴏᴛᴀʟ Sʜᴏʀᴛᴇɴᴇʀ Lɪɴᴋs Sʜᴏʀᴛᴇɴᴇᴅ
├᳃ `{link_stats['shortener_links']}`
│
├⍟ Dɪꜱᴋ Sɪᴢᴇ : `523.42 MB` 
│
├⍟ Dɪꜱᴋ Uꜱᴇᴅ : `{size}`
│
├⍟ Fʀᴇᴇ Dɪꜱᴋ : `{free}`
│
├⍟ Rᴜɴᴛɪᴍᴇ : `{runtime}`
│
╰────❪ 𝗦𝗧𝗔𝗧𝗨𝗦 ❫────⍟</b>
"""


        return await txt.edit(msg)
    except Exception as e:
        logging.error(e, exc_info=True)


@Client.on_message(filters.command("logs") & filters.user(ADMINS) & filters.private)
@private_use
async def log_file(bot, message):
    """Send log file"""
    try:
        await message.reply_document("TelegramBot.log")
    except Exception as e:
        await message.reply(str(e))


@Client.on_message(filters.command("mdisk_api") & filters.private)
@private_use
async def mdisk_api_handler(bot, message: Message):
    user_id = message.from_user.id
    user = await get_user(user_id)
    cmd = message.command
    if len(cmd) == 1:
        return await message.reply(MDISK_API_MESSAGE.format(user["mdisk_api"]))
    elif len(cmd) == 2:
        api = cmd[1].strip()
        await update_user_info(user_id, {"mdisk_api": api})
        await message.reply(f"Mdisk API Updated Successfully To {api}")


@Client.on_message(filters.command(["api","set_api","shortener_api"]) & filters.private)
@private_use
async def shortener_api_handler(bot, m: Message):
    user_id = m.from_user.id
    user = await get_user(user_id)
    cmd = m.command
    if len(cmd) == 1:
        s = SHORTENER_API_MESSAGE.format(
            base_site=user["base_site"], shortener_api=user["shortener_api"]
        )

        return await m.reply(s, disable_web_page_preview=True)
    elif len(cmd) == 2:
        api = cmd[1].strip()
        if cmd[1].lower() == "remove":
            api = None
        await update_user_info(user_id, {"shortener_api": api})
        await m.reply(f"Shortener API Updated Successfully.")


@Client.on_message(filters.command(["header","set_header"]) & filters.private)
@private_use
async def header_handler(bot, m: Message):
    user_id = m.from_user.id
    cmd = m.command
    user = await get_user(user_id)
    if m.reply_to_message:
        header_text = m.reply_to_message.text.html
        await update_user_info(user_id, {"header_text": header_text})
        await m.reply("Header Text Updated Successfully")
    elif "remove" in cmd:
        await update_user_info(user_id, {"header_text": ""})
        return await m.reply("Header Text Removed Successfully")
    else:
        return await m.reply(
            HEADER_MESSAGE
            + "\n\nCurrent Header Text : "
            + user["header_text"].replace("\n", "\n")
        )


@Client.on_message(filters.command(["footer","set_footer"]) & filters.private)
@private_use
async def footer_handler(bot, m: Message):
    user_id = m.from_user.id
    cmd = m.command
    user = await get_user(user_id)
    if not m.reply_to_message:
        if "remove" not in cmd:
            return await m.reply(
                FOOTER_MESSAGE
                + "\n\nCurrent Footer Text : "
                + user["footer_text"].replace("\n", "\n")
            )

        await update_user_info(user_id, {"footer_text": ""})
        return await m.reply("Footer Text Removed Successfully")
    elif m.reply_to_message.text:
        footer_text = m.reply_to_message.text.html
        await update_user_info(user_id, {"footer_text": footer_text})
        await m.reply("Footer Text Updated Successfully")


@Client.on_message(filters.command(["username","set_username"]) & filters.private)
@private_use
async def username_handler(bot, m: Message):
    user_id = m.from_user.id
    user = await get_user(user_id)
    cmd = m.command
    if len(cmd) == 1:
        username = user["username"] or None
        return await m.reply(USERNAME_TEXT.format(username=username))
    elif len(cmd) == 2:
        if "remove" in cmd:
            await update_user_info(user_id, {"username": ""})
            return await m.reply("Username Removed Successfully")
        else:
            username = cmd[1].strip().replace("@", "")
            await update_user_info(user_id, {"username": username})
            await m.reply(f"Username Updated Successfully To {username}")


@Client.on_message(filters.command(["banner_image","set_banner_image"]) & filters.private)
@private_use
async def banner_image_handler(bot, m: Message):
    user_id = m.from_user.id
    user = await get_user(user_id)
    cmd = m.command
    if len(cmd) == 1:
        if not m.reply_to_message or not m.reply_to_message.photo:
            return (
                await m.reply_photo(user["banner_image"], caption=BANNER_IMAGE)
                if user["banner_image"]
                else await m.reply("Current Banner Image URL : None\n" + BANNER_IMAGE)
            )

        fileid = m.reply_to_message.photo.file_id
        await update_user_info(user_id, {"banner_image": fileid})
        return await m.reply_photo(fileid, caption="Banner Image Updated Successfully")
    elif len(cmd) == 2:
        if "remove" in cmd:
            await update_user_info(user_id, {"banner_image": ""})
            return await m.reply("Banner Image Removed Successfully")
        else:
            image_url = cmd[1].strip()
            valid_image_url = await extract_link(image_url)
            if valid_image_url:
                await update_user_info(user_id, {"banner_image": image_url})
                return await m.reply_photo(
                    image_url, caption="Banner Image Updated Successfully"
                )

            else:
                return await m.reply_text("Image URL is Invalid")


@Client.on_message(filters.command(["base_site007"]) & filters.private)
@private_use
async def base_site_handler(bot, m: Message):
    user_id = m.from_user.id
    user = await get_user(user_id)
    cmd = m.command
    site = user["base_site"]
    text = f"`/base_site (base_site)`\n\nCurrent Base Site : {site}\n\n EX: `/base_site shareus.in`\n\nAvailable Base Sites:\n{avl_web1}\nAnd All alternate sites to droplink.co"
    if len(cmd) == 1:
        return await m.reply(text=text, disable_web_page_preview=True)
    elif len(cmd) == 2:
        base_site = cmd[1].strip()
        if not domain(base_site):
            return await m.reply(text=text, disable_web_page_preview=True)
        await update_user_info(user_id, {"base_site": base_site})
        await m.reply("Base Site Updated Successfully")


@Client.on_message(filters.command("settings") & filters.private)
@private_use
async def me_handler(bot, m: Message):
    user_id = m.from_user.id
    user = await get_user(user_id)

    user_id = m.from_user.id
    user = await get_user(user_id)
    res = USER_ABOUT_MESSAGE.format(
        base_site=user["base_site"],
        method=user["method"],
        shortener_api=user["shortener_api"],
        mdisk_api=user["mdisk_api"],
        username=user["username"],
        header_text=user["header_text"].replace(r"\n", "\n")
        if user["header_text"]
        else None,
        footer_text=user["footer_text"].replace(r"\n", "\n")
        if user["footer_text"]
        else None,
        banner_image=user["banner_image"],
    )

    buttons = await get_me_button(user)
    reply_markup = InlineKeyboardMarkup(buttons)
    return await m.reply_text(
        res, reply_markup=reply_markup, disable_web_page_preview=True
    )


@Client.on_message(filters.command("include_domain") & filters.private)
@private_use
async def include_domain_handler(bot, m: Message):
    user = await get_user(m.from_user.id)
    inc_domain = user["include_domain"]
    tdl = ""
    if inc_domain:
        for i in inc_domain:
            tdl += f"- `{i}`\n"
    else:
        tdl = "None\n"
    if len(m.command) == 1:
        return await m.reply(INCLUDE_DOMAIN_TEXT.format(tdl))
    try:
        cmd = m.command
        cmd.remove("include_domain")
        if "remove_all" in cmd:
            domain_list = []
        elif "remove" in cmd:
            cmd.remove("remove")
            domain_list_cmd = "".join(cmd).strip().split(",")
            for i in list(domain_list_cmd):
                with contextlib.suppress(Exception):
                    inc_domain.remove(i)
            domain_list = list(set(list(inc_domain)))
        else:
            domain_list_cmd = "".join(cmd).strip().split(",")
            domain_list = list(set(domain_list_cmd + list(inc_domain)))
        await update_user_info(m.from_user.id, {"include_domain": domain_list})
        return await m.reply("Updated Include Domain List Successfully")
    except Exception as e:
        logging.exception(e, exc_info=True)
        return await m.reply("Some Error Updating Include Domain List")


@Client.on_message(filters.command("exclude_domain") & filters.private)
@private_use
async def exclude_domain_handler(bot, m: Message):
    user = await get_user(m.from_user.id)
    ex_domain = user["exclude_domain"]
    tdl = ""
    if ex_domain:
        for i in ex_domain:
            tdl += f"- `{i}`\n"
    else:
        tdl = "None\n"
    if len(m.command) == 1:
        return await m.reply(EXCLUDE_DOMAIN_TEXT.format(tdl))
    try:
        cmd = m.command
        cmd.remove("exclude_domain")
        if "remove_all" in cmd:
            domain_list = []
        elif "remove" in cmd:
            cmd.remove("remove")
            domain_list_cmd = "".join(cmd).strip().split(",")
            for i in list(domain_list_cmd):
                with contextlib.suppress(Exception):
                    ex_domain.remove(i)

            domain_list = list(set(list(ex_domain)))
        else:
            domain_list_cmd = "".join(cmd).strip().split(",")
            domain_list = list(set(domain_list_cmd + list(ex_domain)))
        x = await update_user_info(m.from_user.id, {"exclude_domain": domain_list})
        return await m.reply("Updated Exclude Domain List Successfully")
    except Exception as e:
        logging.exception(e, exc_info=True)
        return await m.reply("Some Error Updating Exclude Domain List")


@Client.on_message(filters.command("ban") & filters.private & filters.user(ADMINS))
@private_use
async def banned_user_handler(c: Client, m: Message):
    try:
        if len(m.command) == 1:
            x = "".join(f"- `{user}`\n" for user in temp.BANNED_USERS)
            txt = BANNED_USER_TXT.format(users=x or "None")
            await m.reply(txt)
        elif len(m.command) == 2:
            user_id = m.command[1]
            user = await get_user(int(user_id))
            if user:
                if not user["banned"]:
                    await update_user_info(user_id, {"banned": True})
                    with contextlib.suppress(Exception):
                        temp.BANNED_USERS.append(int(user_id))
                        await c.send_message(
                            user_id, "You Are Now Banned From The Bot By Admin"
                        )
                    await m.reply(
                        f"User [`{user_id}`] Has Been Banned From The Bot. To Unban, `/unban {user_id}`"
                    )

                else:
                    await m.reply("User Is Already Banned")
            else:
                await m.reply("User Doesn't Exist")
    except Exception as e:
        logging.exception(e, exc_info=True)


@Client.on_message(filters.command("unban") & filters.private & filters.user(ADMINS))
@private_use
async def unban_user_handler(c: Client, m: Message):
    try:
        if len(m.command) == 1:
            x = "".join(f"- `{user}`\n" for user in temp.BANNED_USERS)
            txt = BANNED_USER_TXT.format(users=x or "None")
            await m.reply(txt)
        elif len(m.command) == 2:
            user_id = m.command[1]
            user = await get_user(int(user_id))
            if user:
                if user["banned"]:
                    await update_user_info(user_id, {"banned": False})
                    with contextlib.suppress(Exception):
                        temp.BANNED_USERS.remove(int(user_id))
                        await c.send_message(
                            user_id,
                            "You Are Now Free To Use The Bot. You Have Been Unbanned By The Admin",
                        )

                    await m.reply(
                        f"User [`{user_id}`] Has Been Unbanned From The Bot. To Ban. `/ban {user_id}`"
                    )

                else:
                    await m.reply("User Is Not Banned y\Yet")
            else:
                await m.reply("User Doesn't Exist")
    except Exception as e:
        logging.exception(e, exc_info=True)


@Client.on_message(filters.command("info") & filters.private & filters.user(ADMINS))
@private_use
async def get_user_info_handler(c: Client, m: Message):
    try:
        if len(m.command) != 2:
            return await m.reply_text("Wrong Input!!\n`/Info user_id`")
        user = await get_user(int(m.command[1]))
        if not user:
            return await m.reply_text("User Doesn't Exist")
        res = USER_ABOUT_MESSAGE.format(
            base_site=user["base_site"],
            method=user["method"],
            shortener_api="This is something secret",
            mdisk_api="This is something secret",
            username=user["username"],
            header_text=user["header_text"].replace("\n", "\n")
            if user["header_text"]
            else None,
            footer_text=user["footer_text"].replace("\n", "\n")
            if user["footer_text"]
            else None,
            banner_image=user["banner_image"],
        )

        res = f'User: `{user["user_id"]}`\n{res}'
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Ban", callback_data=f'ban#{user["user_id"]}'),
                    InlineKeyboardButton("Close", callback_data="delete"),
                ]
            ]
        )

        return await m.reply_text(res, reply_markup=reply_markup, quote=True)
    except Exception as e:
        await m.reply_text(e)
        logging.error(e)

base_url = "https://earn4links.site/telegram/api?api="

@Client.on_message(filters.command("account") & filters.private)
@private_use
async def account_handler(c: Client, m: Message):
    user_id =  m.from_user.id
    if await is_user_exist(user_id) is True:
        user = await get_user(user_id)
        if user["shortener_api"] is None:
            await m.reply_text("You Haven't Connected Your earn4links.site API Yet !")
            return
    user_apikey = await get_user(user_id)
    api_key = user_apikey["shortener_api"]
    try:
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=100)) as session:
            async with session.get(f"{base_url}{api_key}") as resp:
                data = await resp.json()
                username = data["details"]["username"]
                email_id = data["details"]["email"]
                withdrawal_method = data["details"]["withdrawal_method"]
                withdrawal_account = data["details"]["withdrawal_account"]
        share_url = f"https://earn4links.site/ref/{username}"
        message_to_be_sent =f"""
**
𝖴𝗌𝖾𝗋𝗇𝖺𝗆𝖾 : ➛ {username}
𝖤𝗆𝖺𝗂𝗅 : ➛ {email_id}

𝖯𝖺𝗒𝗆𝖾𝗇𝗍 𝖬𝖾𝗍𝗁𝗈𝖽 ➛ {withdrawal_method}
𝖯𝖺𝗒𝗆𝖾𝗇𝗍 𝖠𝖼𝖼𝖼𝗈𝗎𝗇𝗍 ➛ {withdrawal_account}

🔗 𝖱𝖾𝖿𝖾𝗋𝗋𝖺𝗅 𝖫𝗂𝗇𝗄: - {share_url}

👇 Click Here To Share Your Referral Link 👇
**
"""
        await m.reply_text(message_to_be_sent, reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ᴀᴄᴄᴏᴜɴᴛ ғᴜʟʟ ᴅᴇᴛᴀɪʟs", callback_data="full_account_command"),
                ],
                [
                    InlineKeyboardButton("ʙᴀʟᴀɴᴄᴇ", callback_data="balance_command"),
                    InlineKeyboardButton("ᴘᴀʏᴍᴇɴᴛ", callback_data="payment_command"),
                ], 
                [
                    InlineKeyboardButton("⛺ Hᴏᴍᴇ", callback_data="start_command"),
                    InlineKeyboardButton("✗ Cʟᴏsᴇ", callback_data="delete"),
                ],
            ]))
        
        return
    except TimeoutError:
        m.reply_text("Something Went Wrong\nTry Again Later !")
    except Exception:
        traceback.print_exc()
    return

@Client.on_message(filters.command("balance") & filters.private)
@private_use
async def status_handler(c: Client, m: Message):
    user_id =  m.from_user.id
    if await is_user_exist(user_id) is True:
        user = await get_user(user_id)
        if user["shortener_api"] is None:
            await m.reply_text("You Haven't Connected Your DalinkSupport Api ")
            return
    user_apikey = await get_user(user_id)
    api_key = user_apikey["shortener_api"]
    try:
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=100)) as session:
            async with session.get(f"{base_url}{api_key}") as resp:
                data = await resp.json()
                username = data["details"]["username"]
                referral_earnings = data["details"]["referral_earnings"]
                publisher_earnings = data["details"]["publisher_earnings"]
        message_to_be_sent =f"""
**
👤 𝖠𝖼𝖼𝗈𝗎𝗇𝗍 𝖴𝗌𝖾𝗋𝗇𝖺𝗆𝖾 ➛ {username}

✨ 𝖯𝗎𝖻𝗅𝗂𝗌𝗁𝖾𝗋 𝖤𝖺𝗋𝗇𝗂𝗇𝗀𝗌 ➛ ${str(publisher_earnings)[:4]}
⚡ 𝖱𝖾𝖿𝖾𝗋𝗋𝖺𝗅 𝖤𝖺𝗋𝗇𝗂𝗇𝗀𝗌 ➛ {referral_earnings}

👇 𝖢𝗅𝗂𝖼𝗄 𝖧𝖾𝖺𝗋 𝖳𝗈 𝖶𝗂𝗍𝗁𝖽𝗋𝖺𝗐 𝖸𝗈𝗎𝗋 𝖤𝖺𝗋𝗇𝗂𝗇𝗀𝗌 👇🏻**
"""
        await m.reply_text(message_to_be_sent, reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Take Withdrawal Now",
                    url=f"http://earn4links.site/member/withdraws")
                ]
            ]))
        return
    except TimeoutError:
            m.reply_text("Something Went Wrong\nTry Again Later !")
    except Exception:
            traceback.print_exc()
