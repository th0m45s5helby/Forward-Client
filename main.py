# (c) @AbirHasan2005
# This is Telegram Messages Forwarder UserBot!

import asyncio
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from configs import Config
from datetime import datetime


User = Client(session_name=Config.STRING_SESSION, api_hash=Config.API_HASH, api_id=Config.API_ID)
'''async def forward():
    async for message in User.iter_history(chat_id=-1001441836066):
        try:
            await message.copy(int(Config.FORWARD_TO_CHAT_ID))
        except FloodWait as e:
            await User.send_message(chat_id="me", text=f"#FloodWait: Stopping Forwarder for `{e.x}s`!")
            await asyncio.sleep(e.x)
        except Exception as err:
            await User.send_message(chat_id="me", text=f"#ERROR: `{err}`")
    await User.send_message(chat_id="me",text="Channel files successfully kanged")'''



@User.on_message(filters.text | filters.media & ~filters.edited)
async def main(client, message):
    # Checks
#     if not Config.FORWARD_TO_CHAT_ID or not Config.FORWARD_FROM_CHAT_ID or not Config.USER_ID:
#         await client.send_message(chat_id="me",
#                                   text=f"#VARS_MISSING: Please Set `FORWARD_FROM_CHAT_ID` & `FORWARD_TO_CHAT_ID` & `USER_ID` Config!")
#         return

    if message.text == "!start" and message.from_user.id == int(Config.USER_ID):
        await message.edit(text="Don't worry I am alive",parse_mode="Markdown",disable_web_page_preview=True)
        #await message.edit(text="Hi, Myself!\nI am Alive XD", parse_mode="Markdown", disable_web_page_preview=True)
    elif message.text == "!help" and message.from_user.id == int(Config.USER_ID):
        await message.edit(
            text="This UserBot can forward messages from any Chat to any other Chat XD\n\nDeveloper: @AbirHasan2005",
            parse_mode="Markdown", disable_web_page_preview=True)
    elif message.chat.id in [-1001489565747,-1001469623910,-1001303847036]:
        try:
            if message.document or message.video:
                await message.copy(int(Config.FORWARD_TO_CHAT_ID))
        except Exception as err:
            await client.send_message(chat_id="me",text=f"#ERROR: `{err}`")
           
    elif 1 : #message.chat.id == (int(Config.FORWARD_FROM_CHAT_ID)):
        try:
            await message.copy(int(Config.FORWARD_TO_CHAT_ID))
        except FloodWait as e:
            await client.send_message(chat_id="me", text=f"#FloodWait: Stopping Forwarder for `{e.x}s`!")
            await asyncio.sleep(e.x)
        except Exception as err:
            await client.send_message(chat_id="me", text=f"#ERROR: `{err}`")


User.run()
