#https://github.com/Clinton-Abraham/RENAMER-BOT


import os
import sqlite3
import logging
import pyrogram

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

logging.getLogger("pyrogram").setLevel(logging.WARNING)

if bool(os.environ.get("WEBHOOK", False)):

    from sample_config import Config
else:
    from config import Config

from pyrogram import filters
from mtb import mtb
from pyrogram import Client as Clinton
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton



@Clinton.on_message(filters.command(["start"]))
async def start(bot, update):
          await bot.send_message(
          chat_id=update.chat.id,
          text=mtb.START_TXT.format(update.from_user.first_name),
          parse_mode="html",
          disable_web_page_preview=True,
          reply_markup=mtb.START_BUTTONS
        )           
