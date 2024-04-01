from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import random
import requests
from DAXXMUSIC import app 

SUPPORT_CHAT = "+_0XRE7EVJPFkN2I0"

@app.on_message(filters.command("آرزو"))
async def wish(_, m):
    if len(m.command) < 2:
        await m.reply("🪆آرزویت را اضافه کن عزیزم🪆")
        return 

    api = requests.get("https://nekos.best/api/v2/happy").json()
    url = api["results"][0]['url']
    text = m.text.split(None, 1)[1]
    wish_count = random.randint(1, 100)
    wish = f"✨ سلام! {m.from_user.first_name}! "
    wish += f"✨ آرزوی تو: {text} "
    wish += f"✨ ممکن است به: {wish_count}%"
    
    await app.send_animation(
        chat_id=m.chat.id,
        animation=url,
        caption=wish,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🦋گروه پشتیبانی🦋", url=f"https://t.me/{SUPPORT_CHAT}")]])
    )
            
    
BUTTON = [[InlineKeyboardButton("🦋گروه پشتیبانی🦋", url=f"https://t.me/{SUPPORT_CHAT}")]]
CUTIE = "https://t.me/rahaneshsource/118"

@app.on_message(filters.command("جذاب"))
async def cute(_, message):
    if not message.reply_to_message:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
    else:
        user_id = message.reply_to_message.from_user.id
        user_name = message.reply_to_message.from_user.first_name

    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    CUTE = f"🍑 {mention} {mm}% جذاب بچه🥰"

    await app.send_document(
        chat_id=message.chat.id,
        document=CUTIE,
        caption=CUTE,
        reply_markup=InlineKeyboardMarkup(BUTTON),
        reply_to_message_id=message.reply_to_message.message_id if message.reply_to_message else None,
    )
    
help_text = """
» 🔮چیستی این (آروز)🔮
🪄دراینجا شما هر نوع درخواستی را میتوانید با استفاده از این ربات برآورده کنید🪅!
مثال: /wish : من می‌خواهم بهترین در کلاس باشم
» /wish : من یک آیفون جدید می‌خواهم
» /cute : چقدر من خوشگل هستم 
"""
