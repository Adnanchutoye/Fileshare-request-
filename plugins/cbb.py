#TELEGRAM > @ifeelscam

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>⌬ ᴏᴡɴᴇʀ : <a href=https://t.me/Madhav_S9>❰⏤͟͞ 𝗠.𝗥 𝗦𝗢𝗟𝗢-//-❱</a>\n⌬ ᴍʏ ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/OngoingAnime_Htx'>ᴏɴɢᴏɪɴɢ ʜᴛx</a>\n⌬ ᴀɴɪᴍᴇ ɪɴᴅᴜsᴛʀʏ : <a href='https://t.me/anime_hindi_sub_industry'>ᴀɴɪᴍᴇ ɪɴᴅᴜsᴛʀʏ</a>\n⌬ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : <a href='https://t.me/team_society_1'>ʙᴏᴛ sᴏᴄɪᴇᴛʏ</a>\n⌬ ʜᴛx ᴄʜᴀᴛ ᴢᴏɴᴇ : <a href='https://t.me/HTXANIMEGROUP'>ᴄʜᴀᴛ ᴢᴏɴᴇ</a>\n࿂ Dᴇᴠᴇʟᴏᴘᴇᴅ Bʏ : <a href='https://t.me/i_killed_my_clan'>❰⏤‌‌ 𝚯𝗕𝗜𝗧𝗢 -//-❱</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [ 
                  [
                        InlineKeyboardButton("⚡ʙᴀᴄᴋ ", callback_data = "home"),
                        InlineKeyboardButton("⚡ᴄʟᴏsᴇ ", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except: 
            pass
    elif data == "home":
        await query.message.edit_text(
            text=f"Kᴏɴɴɪᴄʜɪᴡᴀ!! {mention}⚡,\n\n<b>ɪ ᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ,</b>",
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup(
                [
                [
                    InlineKeyboardButton("⚡ᴀʙᴏᴜᴛ", callback_data = "about"),
                    InlineKeyboardButton("⚡ᴄʟᴏsᴇ", callback_data = "close")
                ]
            ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except: 
            pass
    
    elif data == "me":
            await query.message.edit(
                text=f"<b>sᴏʀʀʏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ɪɴ ᴛʜɪꜱ ʙᴏᴛ</b>",
                disable_web_page_preview=True,
                reply_markup = InlineKeyboardMarkup(
                    [
                        [ InlineKeyboardButton("⚡sᴜᴘᴘᴏʀᴛ",url = "https://t.me/anime_hindi_sub_industry")],
                        [ InlineKeyboardButton("⚡ʙᴀᴄᴋ", callback_data = "home"),
                         InlineKeyboardButton( "⚡ᴄʟᴏsᴇ", callback_data = "close")]
                    ]
                )
         )

    
