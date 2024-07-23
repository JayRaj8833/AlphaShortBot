import asyncio
import aiohttp
import contextlib
import datetime
import logging
import os
import re
import sys
import traceback

from validators import domain
from database import db


from config import ADMINS, OWNER_ID, SOURCE_CODE, UPDATE_CHANNEL
from database import update_user_info
from database.users import get_user, is_user_exist, total_users_count, update_user_info
from helpers import Helpers, temp
from pyrogram import Client, enums, filters
from pyrogram.errors import UserNotParticipant
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message
from translation import (
    ABOUT_REPLY_MARKUP,
    ABOUT_TEXT,
    ADMINS_MESSAGE,
    BACK_REPLY_MARKUP,
    BATCH_MESSAGE,
    CHANNELS_LIST_MESSAGE,
    CUSTOM_ALIAS_MESSAGE,
    HELP_MESSAGE,
    HELP_REPLY_MARKUP,
    METHOD_MESSAGE,
    METHOD_REPLY_MARKUP,
    START_MESSAGE,
    START_MESSAGE_REPLY_MARKUP,
    USER_ABOUT_MESSAGE, 
    STATSX, 
    ACCOUNT_TXT, 
    FULL_ACCOUNT_TXT
)
from utils import get_me_button

logger = logging.getLogger(__name__)


@Client.on_callback_query(filters.regex("sub_refresh"))
async def refresh_cb(c, m):
    owner = c.owner
    if UPDATE_CHANNEL:
        try:
            user = await c.get_chat_member(UPDATE_CHANNEL, m.from_user.id)
            if user.status == "kicked":
                with contextlib.suppress(Exception):
                    await m.message.edit("**Hey You Are Banned**")
                return
        except UserNotParticipant:
            await m.answer(
                "You Have Not Yet Joined Our Channel. First Join And Then Press Refresh Button",
                show_alert=True,
            )

            return
        except Exception as e:
            print(e)
            await m.message.edit(
                f"Something Wrong. Please Try Again Later Or Contact {owner.mention(style='md')}"
            )

            return
    await m.message.delete()


@Client.on_callback_query(filters.regex(r"^ban"))
async def ban_cb_handler(c: Client, m: CallbackQuery):
    try:
        user_id = m.data.split("#")[1]
        user = await get_user(int(user_id))

        if user:
            if not user["banned"]:
                temp.BANNED_USERS.append(int(user_id))
                await update_user_info(user_id, {"banned": True})
                try:
                    owner = await c.get_users(int(OWNER_ID))
                    await c.send_message(
                        user_id,
                        f"You Are Now Banned From The Bot By Admin. Contact {owner.mention(style='md')} Regarding This",
                    )
                except Exception as e:
                    logging.error(e)
                reply_markup = InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "Unban", callback_data=f"unban#{user_id}"
                            ),
                            InlineKeyboardButton("Close", callback_data="delete"),
                        ]
                    ]
                )
                await m.edit_message_reply_markup(reply_markup)
                await m.answer(
                    f"User [{user_id}] Has Been Banned From The Bot", show_alert=True
                )
            else:
                await m.answer("User Is Already Banned", show_alert=True)
        else:
            await m.answer("User Doesn't Exist", show_alert=True)
    except Exception as e:
        logging.exception(e, exc_info=True)


@Client.on_callback_query(filters.regex("^unban"))
async def unban_cb_handler(c, m: CallbackQuery):
    user_id = m.data.split("#")[1]
    user = await get_user(int(user_id))
    if user:
        if user["banned"]:
            temp.BANNED_USERS.remove(int(user_id))
            await update_user_info(user_id, {"banned": False})
            with contextlib.suppress(Exception):
                await c.send_message(
                    user_id,
                    "You Are Now Free To Use The Bot. You Have Been Unbanned By The Admin",
                )
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Ban", callback_data=f"ban#{user_id}"),
                        InlineKeyboardButton("Close", callback_data="delete"),
                    ]
                ]
            )
            await m.edit_message_reply_markup(reply_markup)
            await m.answer("User Is Unbanned", show_alert=True)
        else:
            await m.answer("User Is Not Banned Yet", show_alert=True)
    else:
        await m.answer("User Doesn't Exist", show_alert=True)


@Client.on_callback_query(filters.regex("^setgs"))
async def user_setting_cb(c, query: CallbackQuery):
    _, setting, toggle, user_id = query.data.split("#")
    myvalues = {setting: toggle == "True"}
    await update_user_info(user_id, myvalues)
    user = await get_user(user_id)
    buttons = await get_me_button(user)
    reply_markup = InlineKeyboardMarkup(buttons)
    try:
        await query.message.edit_reply_markup(reply_markup)
        setting = re.sub("is|_", " ", setting).title()
        toggle = "Enabled" if toggle == "True" else "Disabled"
        await query.answer(f"{setting} {toggle} Successfully", show_alert=True)
    except Exception as e:
        logging.error("Error Occurred While Updating User Information", exc_info=True)

base_url = "https://earn4links.site/api?api="

@Client.on_callback_query(filters.regex("account") & filters.private)
async def account_handler_cb(c, m):
    user_id = m.from_user.id
    user_apikey = await get_user(user_id)
    if user_apikey is None or "shortener_api" not in user_apikey:
        await m.answer("User data not found.", show_alert=True)
        return

    api_key = user_apikey["shortener_api"]
    try:
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=100)) as session:
            async with session.get(f"{base_url}{api_key}") as resp:
                data = await resp.json()
                username = data["details"]["username"]
                email_id = data["details"]["email"]
                withdrawal_method = data["details"]["withdrawal_method"]
                withdrawal_account = data["details"]["first_name"]
                first_name = data["details"]["withdrawal_account"]
                share_url = f"https://earn4links.site/ref/{username}"
                message_to_be_sent = f"""
                **
                𝖥𝗂𝗋𝗌𝗍 𝖭𝖺𝗆𝖾 ➛ {first_name}
                𝖴𝗌𝖾𝗋𝗇𝖺𝗆𝖾 : ➛ {username}
                𝖤𝗆𝖺𝗂𝗅 : ➛ {email_id}

                𝖯𝖺𝗒𝗆𝖾𝗇𝗍 𝖬𝖾𝗍𝗁𝗈𝖽 ➛ {withdrawal_method}
                𝖯𝖺𝗒𝗆𝖾𝗇𝗍 𝖠𝖼𝖼𝖼𝗈𝗎𝗇𝗍 ➛ {withdrawal_account}

                🔗 𝖱𝖾𝖿𝖾𝗋𝗋𝖺𝗅 𝖫𝗂𝗇𝗄: - {share_url}

                👇 Click Here To Share Your Referral Link 👇
                **
                """
                await m.reply(message_to_be_sent)  # Reply to the callback query with the message
    except TimeoutError:
        await m.answer("Something Went Wrong\nTry Again Later!", show_alert=True)
    except Exception:
        traceback.print_exc()


@Client.on_callback_query()
async def on_callback_query(bot: Client, query: CallbackQuery):
    user_id = query.from_user.id
    h = Helpers()
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


    if query.data == "settings_command":
        await query.message.edit(
            res, reply_markup=reply_markup, disable_web_page_preview=True
    )

    elif query.data == "help_command":
        await query.message.edit(
            HELP_MESSAGE.format(
                firstname=temp.FIRST_NAME,
                username=temp.BOT_USERNAME,
                repo=SOURCE_CODE,
                owner="@JayRaj8833",
            ),
            reply_markup=HELP_REPLY_MARKUP,
            disable_web_page_preview=True,
        )

    elif query.data == "about_command":
        bot = await bot.get_me()
        await query.message.edit(
            ABOUT_TEXT.format(bot.mention(style="md")),
            reply_markup=ABOUT_REPLY_MARKUP,
            disable_web_page_preview=True,
        )

    elif query.data == "start_command":
        new_user = await get_user(query.from_user.id)
        tit = START_MESSAGE.format(
            query.from_user.mention, new_user["method"], new_user["base_site"]
        )

        await query.message.edit(
            tit, reply_markup=START_MESSAGE_REPLY_MARKUP, disable_web_page_preview=True
        )

    elif query.data.startswith("change_method"):
        method_name = query.data.split("#")[1]
        user = temp.BOT_USERNAME
        await update_user_info(user_id, {"method": method_name})
        REPLY_MARKUP = InlineKeyboardMarkup(
            [[InlineKeyboardButton("Back", callback_data="method_command")]]
        )

        await query.message.edit(
            "Method Changed Successfully To `{method}`".format(
                method=method_name, username=user
            ),
            reply_markup=REPLY_MARKUP,
        )

    elif query.data == "method_command":
        s = METHOD_MESSAGE.format(method=user["method"], shortener=user["base_site"])
        return await query.message.edit(s, reply_markup=METHOD_REPLY_MARKUP)
    elif query.data == "cbatch_command":
        if user_id not in ADMINS:
            return await query.message.edit(
                "Works only for admins", reply_markup=BACK_REPLY_MARKUP
            )

        await query.message.edit(BATCH_MESSAGE, reply_markup=BACK_REPLY_MARKUP)
    elif query.data == "alias_conf":
        await query.message.edit(
            CUSTOM_ALIAS_MESSAGE,
            reply_markup=BACK_REPLY_MARKUP,
            disable_web_page_preview=True,
        )
        
    elif query.data == "statsx":
        await query.answer(text=STATSX, show_alert=True)

##################### EARN4LINKS ACCOUNT DETAILS #####################

    elif query.data == "payment_command":
        await query.answer(text="I'm sorry to inform you that this command is not working at the moment.", show_alert=True)
                                  
    elif query.data == "account_command":
    #elif query.data == "balance_command":
        user_id =  query.from_user.id
        if await is_user_exist(user_id) is True:
            user = await get_user(user_id)
            if user["shortener_api"] is None:
                await query.answer("You Haven't Connected Your earn4links.site API Yet !", show_alert=True)
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
                    first_name = data["details"]["first_name"]
                    referral_earnings = data["details"]["referral_earnings"]
                    publisher_earnings = data["details"]["publisher_earnings"]
            share_url = f"https://earn4links.site/ref/{username}"
            message_to_be_sent = f"""
**
𝖴𝗌𝖾𝗋𝗇𝖺𝗆𝖾 : ➛ {username}
𝖤𝗆𝖺𝗂𝗅 : ➛ {email_id}

𝖯𝖺𝗒𝗆𝖾𝗇𝗍 𝖬𝖾𝗍𝗁𝗈𝖽 ➛ {withdrawal_method}
𝖯𝖺𝗒𝗆𝖾𝗇𝗍 𝖠𝖼𝖼𝖼𝗈𝗎𝗇𝗍 ➛ {withdrawal_account}

🔗 𝖱𝖾𝖿𝖾𝗋𝗋𝖺𝗅 𝖫𝗂𝗇𝗄: - {share_url}

👇 Click Here To Share Your Referral Link 👇
**
"""
            await query.message.edit(message_to_be_sent, reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("sʜᴀƦᴇ ʀᴇҒᴇƦƦᴀʟ ʟꞮɴᴋ",
                    url=f"https://t.me/share/url?url={share_url}")
                ], 
                [
                    InlineKeyboardButton("ᴀᴄᴄᴏᴜɴᴛ Ғᴜʟʟ ᴅᴇᴛᴀɪʟs", callback_data="full_account_command"),
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
        except TimeoutError:
            await query.answer("Something Went Wrong\nTry Again Later!", show_alert=True)
        except Exception:
            traceback.print_exc()

        
    elif query.data == "balance_command":
        user_id =  query.from_user.id
        if await is_user_exist(user_id) is True:
            user = await get_user(user_id)
            if user["shortener_api"] is None:
                await query.answer("You Haven't Connected Your DalinkShort API Yet !", show_alert=True)
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
                    first_name = data["details"]["first_name"]
                    referral_earnings = data["details"]["referral_earnings"]
                    publisher_earnings = data["details"]["publisher_earnings"]
           # share_url = f"https://earn4links.site/ref/{username}"
            message_to_be_sent = f"""
𝖥𝗂𝗋𝗌𝗍 𝖭𝖺𝗆𝖾 ➛ {first_name}
𝖴𝗌𝖾𝗋𝗇𝖺𝗆𝖾 : ➛ {username}
𝖤𝗆𝖺𝗂𝗅 : ➛ {email_id}
𝖯𝖺𝗒𝗆𝖾𝗇𝗍 𝖬𝖾𝗍𝗁𝗈𝖽 ➛ {withdrawal_method}
𝖯𝖺𝗒𝗆𝖾𝗇𝗍 𝖠𝖼𝖼𝖼𝗈𝗎𝗇𝗍 ➛ {withdrawal_account}
𝖯𝗎𝖻𝗅𝗂𝗌𝗁𝖾𝗋 𝖤𝖺𝗋𝗇𝗂𝗇𝗀𝗌 ➛ ${str(publisher_earnings)[:4]}
"""
            message_to_sent = "hii"
            message_to_sent1 = f"𝖤𝗆𝖺𝗂𝗅 : ➛ {first_name}"
            #await query.message.answer(message_to_be_sent, show_alert=True)
            await query.answer(message_to_be_sent,show_alert=True)
            #await query.message.answer(message_to_be_sent, reply_markup=InlineKeyboardMarkup(
            #[
                #[
                   # InlineKeyboardButton("Take Withdrawal Now",
                   # url=f"http://earn4links.site/member/withdraws")
               # ]
          #  ]))
        except TimeoutError:
            await query.answer("Something Went Wrong\nTry Again Later!", show_alert=True)
        except Exception:
            traceback.print_exc()
            
    elif query.data == "full_account_command":
        user_id =  query.from_user.id
        if await is_user_exist(user_id) is True:
            user = await get_user(user_id)
            if user["shortener_api"] is None:
                await query.answer("You Haven't Connected Your DalinkShort API Yet !", show_alert=True)
                return
        user_apikey = await get_user(user_id)
        api_key = user_apikey["shortener_api"]
        try:
            async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=100)) as session:
                async with session.get(f"{base_url}{api_key}") as resp:
                    data = await resp.json()
                FAT = FULL_ACCOUNT_TXT.format(
                    username = data["details"]["username"], 
                    email_id = data["details"]["email"], 
                
                    first_name = data["details"]["first_name"], 
                    last_name = data["details"]["last_name"], 
                    address1 = data["details"]["address1"], 
                    city = data["details"]["city"], 
                    state = data["details"]["state"], 
                    zip = data["details"]["zip"], 
                    country = data["details"]["country"], 
                    main_email = data["details"]["email"], 
                    temp_email = data["details"]["temp_email"], 
                
                    withdrawal_method = data["details"]["withdrawal_method"], 
                    withdrawal_account = data["details"]["withdrawal_account"], 
            
                    total_withdrawn = data["total_withdrawn"], 
                    pending_withdrawn = data["pending_withdrawn"], 
                    withdraws = data["withdraws"], 
                ) 
                    
            #await query.answer(message_to_be_sent,show_alert=True)
            await query.message.edit(FAT, reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Eᴅɪᴛ Pʀᴏғɪʟᴇ",url=f"https://earn4links.site/member/users/profile")
                ],
                [
                    InlineKeyboardButton("Tᴀᴋᴇ Wɪᴛʜᴅʀᴀᴡᴀʟ Nᴏᴡ",
                    url=f"http://earn4links.site/member/withdraws")
                ],
                [
                    InlineKeyboardButton("≺≺ Bᴀᴄᴋ", callback_data="account_command"),
                    InlineKeyboardButton("✗ Cʟᴏsᴇ", callback_data="delete"),
                ],
            ]))
        except TimeoutError:
            await query.answer("Something Went Wrong\nTry Again Later!", show_alert=True)
        except Exception:
            traceback.print_exc()

##################### END EARN4LINKS PAYMENT #####################
    
    elif query.data == "admins_list":
        if user_id not in ADMINS:
            return await query.message.edit(
                "Works Only For Admins", reply_markup=BACK_REPLY_MARKUP
            )

        await query.message.edit(
            ADMINS_MESSAGE.format(admin_list=await h.get_admins),
            reply_markup=BACK_REPLY_MARKUP,
        )

    elif query.data == "channels_list":
        if user_id not in ADMINS:
            return await query.message.edit(
                "Works Only For Admins", reply_markup=BACK_REPLY_MARKUP
            )

        await query.message.edit(
            CHANNELS_LIST_MESSAGE.format(channels=await h.get_channels),
            reply_markup=BACK_REPLY_MARKUP,
        )
    elif query.data == "delete":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            pass
            
    elif query.data == "close": 
        await query.message.delete()
        await query.message.reply_to_message.delete() 

    elif query.data == "restart":
        await query.message.edit("**Restarting.....**")
        await asyncio.sleep(5)
        os.execl(sys.executable, sys.executable, *sys.argv)
    await query.answer()
