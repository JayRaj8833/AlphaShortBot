from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


STATSX = "HII"

START_MESSAGE = """
<b>𝖧𝖾𝗅𝗅𝗈, {} ❤✨

𝖨 𝖢𝖺𝗇 𝖢𝗈𝗇𝖼𝖾𝗋𝗍 𝖫𝗂𝗇𝗄 𝖳𝗈 𝖲𝗁𝗈𝗋𝗍𝖫𝗂𝗇𝗄. 𝖲𝖾𝗇𝖽 𝖬𝖾 𝖠𝗇𝗒 𝖯𝗈𝗌𝗍 𝖶𝗂𝗅𝗅 𝖲𝗁𝗈𝗋𝗍𝖾𝗇 𝖠𝗅𝗅 𝖫𝗂𝗇𝗄 𝖨𝗇 𝗂𝖿 𝖢𝗈𝗇𝗏𝖾𝗋𝗍 𝖳𝗈 Da𝖫𝗂𝗇𝗄

1. 𝖦𝗈 𝗍𝗈 👉 earn4links.site
2. 𝖳𝗁𝖾𝗇 𝖢𝗈𝗉𝗒 𝖠𝖯𝖨 𝖪𝖾𝗒 
3. 𝖳𝗁𝖾𝗇 𝖳𝗒𝗉𝖾 /set_api 𝖳𝗁𝖺𝗇 𝖦𝗂𝗏𝖾 𝖠 𝖲𝗂𝗇𝗀𝗅𝖾 𝖲𝗉𝖺𝖼𝖾 𝖠𝗇𝖽 𝖳𝗁𝖾𝗇 𝖯𝖺𝗌𝗍𝖾 𝖸𝗈𝗎𝗋 𝖠𝖯𝖨 𝖪𝖾𝗒 (𝖲𝖾𝖾 𝖤𝗑𝖺𝗆𝗉𝗅𝖾 𝖳𝗈 𝖴𝗇𝖽𝖾𝗋𝗌𝗍𝖺𝗇𝖽 𝖬𝗈𝗋𝖾...)

[𝖲𝖾𝖾 𝖳𝗁𝖾 𝖤𝗑𝖺𝗆𝗉𝗅𝖾 👇]

𝖤𝗑𝗆𝗉𝗅𝖾 ➛ <code>/set_api 1234567890abcdef1234567890abcdef12345678</code>

𝖠𝗇𝗒𝗈𝗇𝖾 𝖶𝗁𝗈 𝖶𝖺𝗇𝗍 𝖳𝗈 𝖴𝗌𝖾 𝖠𝗇𝗒 𝖮𝗍𝗁𝖾𝗋 𝖲𝗁𝗈𝗋𝗍𝗇𝖾𝗋 𝖨𝗇𝗌𝗍𝖾𝖺𝖽 𝖮𝖿 earn4links.site 𝖳𝗁𝖾𝗇 𝖢𝗈𝗇𝗍𝖺𝖼𝗍 𝖠𝗍 👉 @JayRaj8833 (𝖠𝗅𝗅 𝖲𝗁𝗈𝗋𝗍𝗇𝖾𝗋𝗌 𝖲𝗎𝗉𝗉𝗈𝗋𝗍 𝖠𝗏𝗂𝗅𝖺𝖻𝗅𝖾.)

𝖨𝖿 𝖸𝗈𝗎 𝖧𝖺𝗏𝖾 𝖠𝗇𝗒 𝖡𝗎𝗀𝗌 𝖮𝗋 𝖰𝗎𝖾𝗌𝗍𝗂𝗈𝗇𝗌 𝖠𝖻𝗈𝗎𝗍 𝖧𝗈𝗐 𝖳𝗈 𝖴𝗌𝖾 𝖬𝖾 , 𝖢𝗁𝖾𝖼𝗄 𝖮𝗎𝗍 𝖬𝗒 [𝖶𝖾𝖻𝗌𝗂𝗍𝖾](https://earn4links.site/#popup1) 𝖮𝗋 𝖢𝗈𝗇𝗍𝖺𝖼𝗍 ➛ @earn4links.site_Bot </b>
"""

HELP_MESSAGE = """
<b>𝖧𝖾𝗒 𝗍𝗁𝖾𝗋𝖾! 𝖬𝗒 𝗇𝖺𝗆𝖾 𝗂𝗌 {firstname} 𝖴𝖱𝖫 𝖢𝗈𝗇𝗏𝖾𝗋𝗍𝖾𝗋 𝖡𝖮𝗍 𝖺𝗇𝖽 𝖨'𝗆 𝖺 𝗅𝗂𝗇𝗄 𝖼𝗈𝗇𝗏𝖾𝗋𝗍𝗈𝗋 𝖺𝗇𝖽 𝗌𝗁𝗈𝗋𝗍𝖾𝗇𝖾𝗋 𝖻𝗈𝗍 𝗁𝖾𝗋𝖾 𝗍𝗈 𝗆𝖺𝗄𝖾 𝗒𝗈𝗎𝗋 𝗐𝗈𝗋𝗄 𝖾𝖺𝗌𝗂𝖾𝗋 𝖺𝗇𝖽 𝗁𝖾𝗅𝗉 𝗒𝗈𝗎 𝖾𝖺𝗋𝗇 𝗆𝗈𝗋𝖾 💰.

Here Is The List Of My Features :

- [𝖧𝗒𝗉𝖾𝗋𝗅𝗂𝗇𝗄](https://t.me/{username})  𝗌𝗎𝗉𝗉𝗈𝗋𝗍 🔗
- 𝖡𝗎𝗍𝗍𝗈𝗇 𝖼𝗈𝗇𝗏𝖾𝗋𝗌𝗂𝗈𝗇 𝗌𝗎𝗉𝗉𝗈𝗋𝗍 🔘
- 𝖣𝗈𝗆𝖺𝗂𝗇 𝗂𝗇𝖼𝗅𝗎𝗌𝗂𝗈𝗇 𝖺𝗇𝖽 𝖾𝗑𝖼𝗅𝗎𝗌𝗂𝗈𝗇 𝗈𝗉𝗍𝗂𝗈𝗇𝗌 🌐
- 𝖧𝖾𝖺𝖽𝖾𝗋 𝖺𝗇𝖽 𝖿𝗈𝗈𝗍𝖾𝗋 𝗍𝖾𝗑𝗍 𝗌𝗎𝗉𝗉𝗈𝗋𝗍 📝
- 𝖱𝖾𝗉𝗅𝖺𝖼𝖾 𝗎𝗌𝖾𝗋𝗇𝖺𝗆𝖾 𝖿𝗎𝗇𝖼𝗍𝗂𝗈𝗇 📎
- 𝖡𝖺𝗇𝗇𝖾𝗋 𝗂𝗆𝖺𝗀𝖾 𝗌𝗎𝗉𝗉𝗈𝗋𝗍 🖼️

𝖨𝖿 𝖸𝗈𝗎 𝖧𝖺𝗏𝖾 𝖠𝗇𝗒 𝖡𝗎𝗀𝗌 𝖮𝗋 𝖰𝗎𝖾𝗌𝗍𝗂𝗈𝗇𝗌 𝖠𝖻𝗈𝗎𝗍 𝖧𝗈𝗐 𝖳𝗈 𝖴𝗌𝖾 𝖬𝖾, 𝖢𝗁𝖾𝖼𝗄 𝖮𝗎𝗍 𝖬𝗒 [𝖶𝖾𝖻𝗌𝗂𝗍𝖾](https://earn4links.site/#popup1) 𝖮𝗋 𝖢𝗈𝗇𝗍𝖺𝖼𝗍 ➛ @earn4links.site_Bot

𝖠𝗏𝖺𝗂𝗅𝖺𝖻𝗅𝖾 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌:

- **/set_api**
- **/set_header**
- **/set_footer**
- **/set_username**
- **/set_banner_image**
- **/settings**

𝖴𝗌𝖾 𝗍𝗁𝖾𝗌𝖾 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝗍𝗈 𝗅𝖾𝖺𝗋𝗇 𝗆𝗈𝗋𝖾 𝖺𝖻𝗈𝗎𝗍 𝖾𝖺𝖼𝗁 𝖿𝖾𝖺𝗍𝗎𝗋𝖾. </b>
"""


ABOUT_TEXT = """
<b><u>🤩 earn4links.site Fᴇᴀᴛᴜʀᴇs 😇</u>

➀. Sɪɴɢʟᴇ Pᴀɢᴇ - 1$=80rs
➁. 20 Sᴇᴄᴏɴᴅs Wᴀɪᴛɪɴɢ Tɪᴍᴇ🕖
➂. 4$ CPM 🤑
➃. ᴢᴇʀᴏ PᴏᴘUᴘ Aᴅs ᴀɴᴅ POPUɴᴅᴇʀ Aᴅs 
➄. ᴄʜᴀᴛ sᴜᴘᴘᴏʀᴛ ɪs ᴀᴠᴀɪʟᴀʙʟᴇ 𝟸𝟺x𝟽.
➅. ɪᴘ ᴄᴏᴜɴᴛ ʜᴀs ʙᴇᴇɴ ɪɴᴄʀᴇᴀsᴇᴅ ᴛᴏ 𝟷𝟶.❤
➆. ᴍɪɴɪᴍᴜᴍ ᴡɪᴛʜᴅʀᴀᴡ ɪs 𝟻$.
➇. ᴅᴀɪʟʏ ᴘᴀʏᴍᴇɴᴛ sʏsᴛᴇᴍ ᴄᴏᴍɪɴɢ sᴏᴏɴ..
➈. ᴍɪɴɪᴍᴜᴍ ᴡɪᴛʜᴅʀᴀᴡ ɪs 𝟷$. ᴄᴏᴍɪɴɢ sᴏᴏɴ..

👑 Wᴇʙsɪᴛᴇ ➛ https://earn4links.site

⧁ ᴛᴇsᴛ ʟɪɴᴋ➛  https://earn4links.site/demo

🗣️ ᴀᴅᴍɪɴ sᴜᴘᴘᴏʀᴛ ➛ @earn4links.site_Bot

🆘 ᴀɴʏ ʜᴇʟᴘ ➛ @earn4links.site 

📢 ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ➛ @earn4links.site

💰 ᴘᴀʏᴍᴇɴᴛ ᴘʀᴏᴏғs ➛ @earn4links.site

☫ ʟɪɴᴋ ᴄᴏɴᴠᴇʀᴛᴏʀ ʙᴏᴛ ➛ @earn4links.site

❤️ ᴍᴀᴅᴇ ᴡɪᴛʜ ʟᴏᴠᴇ ʙʏ earn4links.site ❤️</b>
"""

FULL_ACCOUNT_TXT = """
<b>╒═『 Account Details 』
┠ ᴜsᴇʀɴᴀᴍᴇ : <code><spoiler>{username}</code></spoiler>
┖ ᴇᴍᴀɪʟ : <code><spoiler>{main_email}</code></spoiler>

╒═『 𝖡𝗂𝗅𝗅𝗂𝗇𝗀 𝖠𝖽𝖽𝗋𝖾𝗌𝗌 』
┠ ғɪʀsᴛ ɴᴀᴍᴇ : <code><spoiler>{first_name}</code></spoiler>
┠ ʟᴀsᴛ ɴᴀᴍᴇ : <code><spoiler>{last_name}</code></spoiler>
┠ ᴀᴅᴅʀᴇss : <code><spoiler>{address1}</code></spoiler>
┠ ᴄɪᴛʏ : <code><spoiler>{city}</code></spoiler>
┠ sᴛᴀᴛᴇ : <code><spoiler>{state}</code></spoiler>
┠ ᴢɪᴘ : <code><spoiler>{zip}</code></spoiler>
┠ ᴄᴏᴜɴᴛʀʏ : <code><spoiler>{country}</code></spoiler>
┠ ᴍᴀɪɴ ᴇᴍᴀɪʟ : <code><spoiler>{main_email} </code></spoiler>
┖ ᴛᴇᴍᴘ ᴇᴍᴀɪʟ : <code><spoiler>{temp_email}</code></spoiler>

╒═『 𝖯𝖺𝗒𝗆𝖾𝗇𝗍 𝖣𝖾𝗍𝖺𝗂𝗅𝗌 』
┠ ᴘᴀʏᴍᴇɴᴛ ᴍᴇᴛʜᴏᴅ : <code><spoiler>{withdrawal_method}</code></spoiler>
┖ ᴘᴀʏᴍᴇɴᴛ ᴀᴄᴄᴏᴜɴᴛ : <code><spoiler>{withdrawal_account}</code></spoiler>

╒═『 𝖶𝗂𝗍𝗁𝖽𝗋𝖺𝗐𝖺𝗅 𝖣𝖾𝗍𝖺𝗂𝗅𝗌 』
┠ ᴛᴏᴛᴀʟ W/D : <code><spoiler>{total_withdrawn}</code></spoiler>
┠ ᴘᴇɴᴅɪɴɢ W/D : <code><spoiler>{pending_withdrawn}</code></spoiler>
┖ W/D's : <code><spoiler>{withdraws}</code></spoiler></b>
"""

ACCOUNT_TXT = """
══『 Account Details 』══

𝖴𝗌𝖾𝗋𝗇𝖺𝗆𝖾 : ➛ {username}
𝖤𝗆𝖺𝗂𝗅 : ➛ {email}

══『 𝖡𝗂𝗅𝗅𝗂𝗇𝗀 𝖠𝖽𝖽𝗋𝖾𝗌𝗌 』══

𝖥𝗂𝗋𝗌𝗍 𝖭𝖺𝗆𝖾 ➛ {first_name}
𝖫𝖺𝗌𝗍 𝖭𝖺𝗆𝖾 ➛ {last_name}
𝖠𝖽𝖽𝗋𝖾𝗌𝗌 1 ➛ {address1}
𝖠𝖽𝖽𝗋𝖾𝗌𝗌 2 ➛ {address2}
𝖢𝗂𝗍𝗒 ➛ {city}
𝖲𝗍𝖺𝗍𝖾 ➛ {state}
𝖹𝖨𝖯 ➛ {zip}
𝖢𝗈𝗎𝗇𝗍𝗋𝗒 ➛ {country}
𝖢𝗈𝗇𝗍𝖺𝖼𝗍 𝖤𝗆𝖺𝗂𝗅➛ {email}


══『 𝖯𝖺𝗒𝗆𝖾𝗇𝗍 𝖣𝖾𝗍𝖺𝗂𝗅𝗌 』══

𝖯𝖺𝗒𝗆𝖾𝗇𝗍 𝖬𝖾𝗍𝗁𝗈𝖽 ➛ {withdrawal_method}
𝖯𝖺𝗒𝗆𝖾𝗇𝗍 𝖠𝖼𝖼𝖼𝗈𝗎𝗇𝗍 ➛ {withdrawal_account}

══『 Edit Profile 』══
"""

ADMINX = """
/batch - To Convert Link For Channel 
/logs - To Get The Log Messages
/restart - Restarts Or Re-Deploys The Bot
/ban - To Ban User 
/unban - To Unban User
/info - To Get User Info
/stats - To Displays Statistics Of The Server And Bot
"""

##################### BUTTON MARKUP #####################

ADMIN_HELP_REPLY_MARKUP = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("ᴍᴇᴛʜᴏᴅs", callback_data="method_command"),
            InlineKeyboardButton("ʙᴀᴛᴄʜ", callback_data="cbatch_command"),
        ],
        [
            InlineKeyboardButton("ᴄᴜsᴛᴏᴍ ᴀʟɪᴀs", callback_data="alias_conf"),
            InlineKeyboardButton("ᴀᴅᴍɪɴs", callback_data="admins_list"),
        ],
        [
            InlineKeyboardButton("ᴄʜᴀɴɴᴇʟs", callback_data="channels_list"),
            InlineKeyboardButton("ʜᴏᴍᴇ", callback_data="start_command"),
        ],
    ]
)

HELP_REPLY_MARKUP = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("⛺ Hᴏᴍᴇ", callback_data="start_command"),
            InlineKeyboardButton('📘 Aʙᴏᴜᴛ', callback_data='about_command'),
        ],
        [InlineKeyboardButton("✗ Cʟᴏsᴇ", callback_data="close")],
    ]
)

ABOUT_REPLY_MARKUP = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("⛺ Hᴏᴍᴇ", callback_data="start_command"),
            InlineKeyboardButton("⚙️ Hᴇʟᴘ", callback_data="help_command"),
        ],
        [InlineKeyboardButton("✗ Cʟᴏsᴇ", callback_data="close")],
    ]
)

START_MESSAGE_REPLY_MARKUP = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('📢 Uᴘᴅᴀᴛᴇ', url='https://telegram.me/earn4links.site'),
            InlineKeyboardButton('📘 Aʙᴏᴜᴛ', callback_data='about_command')
        ],
        [
            InlineKeyboardButton('💵 ʙᴀʟᴀɴᴄᴇ 💳', callback_data='balance_command')
        ], 
        [
            InlineKeyboardButton('💡 Hᴇʟᴘ', callback_data="help_command"),
            InlineKeyboardButton('🛠 Sᴇᴛᴛɪɴɢs', callback_data="settings_command")
        ],
        [
            InlineKeyboardButton('☫ Cᴏɴɴᴇᴄᴛ Tᴏ Dalink ☫', url='https://earn4links.site/member/tools/api?bot=true')
        ],
    ]

)

METHOD_REPLY_MARKUP = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "ᴍᴅɪsᴋ + sʜᴏʀᴛᴇɴᴇʀ", callback_data="change_method#mdlink"
            ),
            InlineKeyboardButton(
                "sʜᴏʀᴛᴇɴᴇʀ", callback_data="change_method#shortener"
            ),
        ],
        [
            InlineKeyboardButton("≺≺ Bᴀᴄᴋ", callback_data="help_command"),
            InlineKeyboardButton("✗ ᴄʟᴏsᴇ", callback_data="delete"),
        ],
    ]
)

BACK_REPLY_MARKUP = InlineKeyboardMarkup(
    [[InlineKeyboardButton("≺≺ Bᴀᴄᴋ", callback_data="help_command")]]
)

##################### NON USE TEXT #####################

USER_ABOUT_MESSAGE = """**
❤️ 𝖶𝖾𝗅𝖼𝗈𝗆𝖾 𝖳𝗈 earn4links.site 𝖠𝗇𝖽 𝖡𝗈𝗍 !!

🌐 Wᴇʙsɪᴛᴇ ➙ {base_site}

 🔌 API ➙ {shortener_api}

➡️ Mdisk API ➙ {mdisk_api}

 📎 Usᴇʀɴᴀᴍᴇ ➙ @{username}

📝 Hᴇᴀᴅᴇʀ Tᴇxᴛ ↯
{header_text}

📝 Fᴏᴏᴛᴇʀ Tᴇxᴛ ↯
{footer_text}

🖼️ Bᴀɴɴᴇʀ Iᴍᴀɢᴇ➙ ➙ {banner_image}

👇 𝖢𝗅𝗂𝖼𝗄 𝖮𝗇 𝖳𝗁𝗂𝗌 𝖡𝗎𝗍𝗍𝗈𝗇𝗌 𝖠𝗇𝖽 𝖮𝗇/𝖮𝖿𝖿 𝖥𝖾𝖺𝗍𝗎𝗋𝖾𝗌.
**"""

METHOD_MESSAGE = """ Methods Available :

➡️ `Mdisk + Shortener (MDLINK)` - Change All The Links Of The Post To Your MDisk Account First And Then Short To earn4links.site Link.

➡️ `Shortener` - Short All The Links Of The Post To earn4links.site Link Directly.
    
**Current Method :** {method}
    
Click Below Button To Set/Change Method :"""

CUSTOM_ALIAS_MESSAGE = """ To Use Custom Alias Feature

**Format : [link] | [alias]**

**Example :** https://google.com | demolink

**Note :** This Feature Works Only In Private Mode Only.
"""


ADMINS_MESSAGE = """
List Of Admins Who Has Access To This Bot :
{admin_list}"""


CHANNELS_LIST_MESSAGE = """
Here Is A List Of The Channels :
{channels}"""


BATCH_MESSAGE = BATCH = """**I Will Short All Your Channels Link With earn4links.site. Make Me Admin In Your Channel Withh All Rights And Follow Steps.

Example : `/batch earn4links.site`

You Can Also Use Channel ID Instead Of Channel Username

⚙️ Hit `/settings` To Control Your Settings**
"""

MDISK_API_MESSAGE = """To Add Or Update Your Mdisk API,
            
**Example :** `/mdisk_api 6LZq851sXoPHugiKQq`
            
Get Your Mdisk API From @1231231231323

**To Remove Mdisk API :** `/mdisk_api remove`

**Current Mdisk API :** `{}`

Hit `/settings` To Control Your Settings"""

SHORTENER_API_MESSAGE = """To Add Or Update Your DalinkShort API,
            
**Exᴀᴍᴘʟᴇ :** `/api 6LZq851sXofffPHugiKQq`

Gᴇᴛ Yᴏᴜʀ earn4links.site API Fʀᴏᴍ [Here](https://earn4links.site/member/tools/api?bot=true)

**Tᴏ Rᴇᴍᴏᴠᴇ DalinkShort API :** `/api remove`

**Cᴜʀʀᴇɴᴛ earn4links.site API :** `{shortener_api}`

Hit `/settings` Tᴏ Cᴏɴᴛʀᴏʟ Yᴏᴜʀ Sᴇᴛᴛɪɴɢs"""

HEADER_MESSAGE = """To Set The Header Text For Every Message Caption Or Text.

Reply To Any Text With `/header` To Set It As Header

**To Remove The Header Text :** `/header remove`

**Current Header Text :** {header_text}

Hit `/settings` To Control Your Settings"""

FOOTER_MESSAGE = """To Set The Footer Text For Every Message Caption Or Text.

Reply To Any Text With `/footer` To Set It As Footer

**To Remove The Footer Text :** `/footer remove`

**Current Header Text :** {footer_text}

Hit `/settings` To Control Your Settings"""

USERNAME_TEXT = """To Replace Specific Username From Post.

**Example :** `/username earn4links.site`

**To Remove The Username :** `/username remove`

**Current Username :** {username}

Hit `/settings` To Control Your Settings"""

BANNER_IMAGE = """To Replace The Image From Post.

**Example :** /banner_image link

You Can Also Reply To Any Image With `/banner_image` To Set It As Banner Image.

**To Remove The Banner Image :** `/banner_image remove`

**Current Banner Image :** {banner_image}

Hit `/settings` To Control Your Settings"""

INCLUDE_DOMAIN_TEXT = """Bot Will Short Only Included Domains Only With This Command

**Example :** /include_domain t.me telegram.me

**To Remove The Specific Included Domain :** `/include_domain remove t.me`

**To Remove All Included Domains :** `/include_domain remove_all`

**Current Included Domains :** {}

Hit `/settings` To Control Your Settings"""

EXCLUDE_DOMAIN_TEXT = """Bot Will Not Short Excluded Domains With This Command

**Example :** /exclude_domain t.me telegram.me

**To Remove The Specific Excluded Domain :** `/exclude_domain remove t.me`

**To Remove All Excluded Domains :** `/exclude_domain remove_all`

**Current Excluded Domains :** {}

Hit `/settings` To Control Your Settings"""

BANNED_USER_TXT = """
Usage : `/ban [User ID]`
Usage : `/unban [User ID]`

List Of Banned Users :
{users}"""
