import os

from .. import *
from pyrogram import filters


@app.on_message(commandz(["😋🥰", "op", "wow", "super", "😋😍"])
    & filters.private & filters.me)
async def self_media(client, message):
    replied = message.reply_to_message
    if not replied:
        return
    if not (replied.photo or replied.video):
        return
    location = await client.download_media(replied)
    await client.send_document("me", location)
    os.remove(location)


NAME = "Self"
MENU = f"""
**📤 دانلود و ذخیره خود\n» عکس یا ویدیوی حذف شونده زماندار⌛️
در پیام ذخیره شده خود ✨**

.op - Use This Command By\nReplying On Self-Destructed
Photo/Video.

🌿 دستورات بیشتر:\n=> [😋🥰, wow, super, 😋😍]
"""
