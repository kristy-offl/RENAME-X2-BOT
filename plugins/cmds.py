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
          text=Scripted.START_TEXT.format(update.from_user.first_name),
          parse_mode="html",
          disable_web_page_preview=True,
 

@Clinton.on_message(filters.command(["help"]))
async def helpme(bot, update):
          await bot.send_message(
          chat_id=update.chat.id,
          text=Scripted.HELP_TEXT,
          parse_mode="html",
          disable_web_page_preview=True,

@Clinton.on_message(filters.command(["about"]))
async def abot(bot, update):
          await bot.send_message(
          chat_id=update.chat.id,
          text=Scripted.ABOUT_TEXT,
          parse_mode="html",
          disable_web_page_preview=True,


@Clinton.on_message(filters.command(["upgrade"]))
async def upgra(bot, update):
          await bot.send_message(
          chat_id=update.chat.id,
          text=Scripted.UPGRADE_TEXT,
          parse_mode="html",
          disable_web_page_preview=True,



@Clinton.on_callback_query()
async def button(bot, update):
 
      if  'DM'  in update.data:
                await update.message.delete()
