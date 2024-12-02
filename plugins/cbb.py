#TG > @i_killed_my_clan

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
                        InlineKeyboardButton("⛩️ Hᴏᴍᴇ", callback_data = "home"),
                        InlineKeyboardButton("Cʟᴏsᴇ", callback_data = "close")
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
            text=f"Hᴇʟʟᴏ!! {mention}⚡,\n\n<b>ɪ ᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ, ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ.\n\n𝐌ᴀɪɴ 𝐂ʜᴀɴɴᴇʟ : <a href='https://t.me/RyumaHindiSubAnime'>𝐑ʏᴜᴍᴀ 𝐀ɴɪᴍᴇ</a></b>",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("• ғᴏʀ ᴍᴏʀᴇ •", url='https://t.me/anime_hindi_sub_industry')],
                    [InlineKeyboardButton("• ᴀʙᴏᴜᴛ", callback_data='about'),
                     InlineKeyboardButton("ʜᴇʟᴘ •", url='https://t.me/Anime_Support_Industry')],
                    [InlineKeyboardButton("• ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ •", url='https://t.me/TEAM_HTX')],
                ])
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
                        [ InlineKeyboardButton("Sᴜᴘᴘᴏʀᴛ",url = "https://t.me/HTXANIMEGROUP")],
                        [ InlineKeyboardButton("⛩️ Hᴏᴍᴇ", callback_data = "home"),
                         InlineKeyboardButton( "Cʟᴏsᴇ", callback_data = "close")]
                    ]
                )
         )

    
