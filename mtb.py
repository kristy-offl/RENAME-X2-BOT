from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class mtb(object):
  
  START_TXT = """
  
<b>Hello {},👋
=>I Can Rename Files With Permanant Thumbnail Support 💥
=>I Can Convert Files Too 🙂
Use help Button For More Details
🧨Devoloped & Maintained By : : <a href='https://t.me/Itz_Me_Malayali'>✯°• Kʀɪsᴛʏ Oꜰꜰᴄɪᴀʟ •°✯ 『★Tᴍ★』 #Broken Sed Life 💔</a></b>
  """
  HELP_TXT = """
  
  **Hey 🙋‍♂️It's Not Complicated To Use Me.
➠ Just Send Me A File
➠ Select Your Options
➠ Wait Until Your Requests Gets Complete Don't Spam Here
<\ Available Commands />
• /start - 🎉 Start Message
• /showthumb - 🎆 To Saved Custom Permanent thumbnail
• /delthumb - ❌  Clears Saved Custom Thumbnail To Default
🎉Powerded By : @HiroshiBots**
"""
  
  ABOUT_TXT = """
  
<b>🎆My Name : <a href='https://t.me/RenameMLBot'>Rename Hiroshi Bot</a></b>\n
<b>👩‍🦽Version : <a href='https://t.me/RenameMLBot'>0.9.2 beta</a></b>\n
<b>⛑Source : <a href='https://t.me/WantSourceCode'>Click Here</a></b>\n
<b>⚙️Server : <a href='https://heroku.com'>Heroku</a></b>\n
<b>🛡Library : <a href='https://github.com/pyrogram'>Pyrogram 1.2.8</a></b>\n
<b>🪓Language : <a href='https://www.python.org'>Python 3.9.4</a></b>\n
<b>🎉Developer : <a href='https://t.me/Itz_Me_Malayaali'>✯°• Kʀɪsᴛʏ Oꜰꜰᴄɪᴀʟ •°✯</a></b>\n
<b>🚀Channel : <a href='https://t.me/HiroshiBots'>𝗛𝗶𝗿𝗼𝘀𝗵𝗶 𝗕𝗼𝘁𝘀</a></b>\n
"""
  
  START_BUTTONS = InlineKeyboardMarkup(
    [[
      InlineKeyboardButton("💁🏻 𝑴𝒚 𝑭𝒂𝒕𝒉𝒆𝒓", url="https://t.me/Itz_Me_Malayali"),
      InlineKeyboardButton("⚙️ 𝑯𝒆𝒍𝒑", callback_data="help")
     ],[
      InlineKeyboardButton("𝑨𝒃𝒐𝒖𝒕 📕", callback_data="about"),
      InlineKeyboardButton("𝑪𝒍𝒐𝒔𝒆 🔐", callback_data="close")
    ]]
    )
      
  HELP_BUTTONS = InlineKeyboardMarkup(
    [[
      InlineKeyboardButton("🔙 𝑩𝒂𝒄𝒌", callback_data="home"),
      InlineKeyboardButton("𝑪𝒍𝒐𝒔𝒆 🔐", callback_data="close")
    ]]
    )
  
  ABOUT_BUTTONS = InlineKeyboardMarkup(
    [[
      InlineKeyboardButton("🔙 𝑩𝒂𝒄𝒌", callback_data="home"),
      InlineKeyboardButton("𝑪𝒍𝒐𝒔𝒆 🔐", callback_data="close")
    ]]
    )
  
