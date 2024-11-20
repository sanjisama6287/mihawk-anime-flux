#Coded by @Its_Tartaglia_Childe

from pyrogram import Client 
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "help":
        await query.message.edit_text(
            text = f"<b>Bot Cammands\n❏ Commands For BOT Admins\n├/start : start the bot or get posts\n├/batch : create link for more than one posts\n├/genlink : create link for one post\n├/users : view bot statistics\n├/broadcast : broadcast any messages to bot users\n└/stats : checking your bot uptime\n\n👨‍💻 Developed by : <a href=https://t.me/Anime_Flux>Anime Flux ™</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ᴄʟᴏꜱᴇ​", callback_data="close"),
                        InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about")
                    ]
                ]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text =f"<b>○ 𝐎ᴡɴᴇʀ : <a href='t.me/ZoroSan110'>𝐑ᴏʀᴏɴᴏᴀ 𝐙ᴏʀᴏ🍅</a>\n○ 𝐀ɴɪᴍᴇ 𝐂ʜᴀɴɴᴇʟ : <a href='https://t.me/Anime_Flux'>𝐀ɴɪᴍᴇ 𝐀ɴɪᴍᴇ 𝐅ʟᴜx</a>\n○ 𝐀ɴɪᴍᴇ 𝐂ʜᴀᴛ : <a href='https://t.me/+pFq16XDLXVM1Yzll'>𝐒ᴛʀᴀᴡ 𝐇ᴀᴛ</a>\n○ 𝐃ᴇᴠʟᴏᴘᴇʀ : <a href='https://t.me/Urr_Sanjiii'>𝐒ᴀɴJɪ 𝐒αᴍᴀ</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data="close"),
                        InlineKeyboardButton("ʜᴇʟᴘ", callback_data="help")
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
