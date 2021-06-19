#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @KGK06

import os 
import pyrogram

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client as MeGBots
from pyrogram import filters
#from bot import MeGBots
from mtb import mtb

########################### Call Back Help #############################

@MeGBots.on_callback_query(filters.regex('^help$'))
async def cb_help(c, m):
  await m.answer()
  await m.message.edit(
    text=mtb.HELP_TXT.format(m.from_user.mention),
    disable_web_page_preview=True,
    reply_markup=mtb.HELP_BUTTONS
    )
  

########################### Call Back About #############################

@MeGBots.on_callback_query(filters.regex('^about$'))
async def cb_about(c, m):
  await m.answer()
  await m.message.edit(
    text=mtb.ABOUT_TXT.format(m.from_user.first_name),
    disable_web_page_preview=True,
    reply_markup=mtb.ABOUT_BUTTONS
    )


########################### Call Back Close #############################

@MeGBots.on_callback_query(filters.regex('^close$'))
async def cb_close(c, m):
  await m.message.delete()


########################### Call Back Home #############################
  
@MeGBots.on_callback_query(filters.regex('^home$'))
async def cb_home(c, m):
  await m.answer()
  await m.message.edit(
    text=mtb.START_TXT.format(m.from_user.mention),
    disable_web_page_preview=True,
    reply_markup=mtb.START_BUTTONS
    )
    
  
