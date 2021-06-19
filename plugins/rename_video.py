#https://github.com/Clinton-Abraham/RENAMER-BOT



import os
import time
import random
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

from PIL import Image
from pyrogram import filters
from mtb import mtb
from database.database import *
from pyrogram import Client as Clinton
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
from functions.nekmo_ffmpeg import take_screen_shot
from functions.display_progress import progress_for_pyrogram
from pyrogram.errors import UserNotParticipant, UserBannedInChannel
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

#×-×-×-×-×-×-×-×-×-×-×-×-×-×-×-×-×-×-×-×-×-×-×-×-××-×-×-×-×-×-×-×-×-×-×-×-×-×-×-×-×-×-×-×-×-×

@Clinton.on_message(filters.command(["rename_video"]))
async def rename_video(bot, update):

    update_channel = Config.UPDATE_CHANNEL
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked":
               await update.reply_text(Scripted.ACCESS_DENIED)
               return
        except UserNotParticipant:
            await update.reply_text(
                text=Scripted.JOIN_NOW_TEXT,
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="ᴊᴏɪɴ ɴᴏᴡ 🔓", url=f"https://t.me/{Config.UPDATE_CHANNEL}") ]
                ] 
              )
            )
            return
        except Exception:
            await update.reply_text(Scripted.CONTACT_MY_DEVELOPER)
            return

    if (" " in update.text) and (update.reply_to_message is not None):
        cmd, file_name = update.text.split(" ", 1)
        new_file = file_name[:60] + file_name[-4:]
        description = Scripted.CUSTOM_CAPTION.format(file_name)
        download_location = Config.DOWNLOAD_LOCATION + "/"
        c = await bot.send_message(
            chat_id=update.chat.id,
            text=Scripted.PROCESSING_TEXT,
            reply_to_message_id=update.message_id
        )
        c_time = time.time()
        the_real_download_location = await bot.download_media(
            message=update.reply_to_message,
            file_name=download_location,
            progress=progress_for_pyrogram,
            progress_args=(
                Scripted.RENAMING_VIDEO,
                c,
                c_time
            )
        )
        if the_real_download_location is not None:
            try:
                await bot.edit_message_text(
                text=Scripted.RENAMED_SUCCESS,
                chat_id=update.chat.id,
                message_id=c.message_id
                )
            except:
                pass
            new_file_name = download_location + file_name
            os.rename(the_real_download_location, new_file_name)
            await bot.edit_message_text(
            text=Scripted.TRYING_TO_UPLOAD,
            chat_id=update.chat.id,
            message_id=c.message_id
                )
            logger.info(the_real_download_location)
            width = 0
            height = 0
            duration = 0
            metadata = extractMetadata(createParser(new_file_name))
            try:
             if metadata.has("duration"):
                duration = metadata.get('duration').seconds
            except:
              pass
            thumb_image_path = Config.DOWNLOAD_LOCATION + "/" + str(update.from_user.id) + ".jpg"
            if not os.path.exists(thumb_image_path):
                mes = await sthumb(update.from_user.id)
                if mes != None:
                    m = await bot.get_messages(update.chat.id, mes.msg_id)
                    await m.download(file_name=thumb_image_path)
                    thumb_image_path = thumb_image_path
                else:
                    thumb_image_path = None
            else:
                width = 0
                height = 0
                metadata = extractMetadata(createParser(thumb_image_path))
                if metadata.has("width"):
                    width = metadata.get("width")
                if metadata.has("height"):
                    height = metadata.get("height")
                Image.open(thumb_image_path).convert("RGB").save(thumb_image_path)
                img = Image.open(thumb_image_path)
                img.resize((320, height))
                img.save(thumb_image_path, "JPEG")
            c_time = time.time()
            await bot.send_video(
                chat_id=update.chat.id,
                video=new_file_name,
                duration=duration,
                thumb=thumb_image_path,
                caption=description,
                supports_streaming=True,
                #reply_markup=reply_markup,
                reply_to_message_id=update.reply_to_message.message_id,
                progress=progress_for_pyrogram,
                progress_args=(
                    Scripted.UPLOAD_START,
                    c, 
                    c_time
                )
            )
            try:
                os.remove(the_real_download_location)
                os.remove(thumb_image_path)
            except:
                pass
            await bot.edit_message_text(
                  text=Scripted.UPLOAD_SUCCESS,
                  chat_id=update.chat.id,
                  message_id=c.message_id
            )
    else:
        await bot.send_message(
        chat_id=update.chat.id,
        text=Scripted.REPLY_TO_VIDEO,
        reply_to_message_id=update.message_id)
