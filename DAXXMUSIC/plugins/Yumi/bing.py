from DAXXMUSIC import app
import requests as r
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import filters

API_URL = "https://sugoi-api.vercel.app/search"

# تعریف دستور برای بررسی کلمات "بینگ" و "bingsearch"
@app.on_message(filters.command(["بینگ", "bingsearch"]))
async def bing_search(michiko, message):
    try:
        if len(message.command) == 1:
            await message.reply_text("❓لطفاً یک کلمه کلیدی برای جستجو وارد کنید.")
            return

        # استخراج کلمه کلیدی از پیام
        keyword = " ".join(message.command[1:])
        params = {"keyword": keyword}
        response = r.get(API_URL, params=params)

        if response.status_code == 200:
            results = response.json()
            if not results:
                await message.reply_text("نتیجه‌ای یافت نشد♨️")
            else:
                message_text = ""
                for result in results[:7]:
                    title = result.get("\x74\x69\x74\x6C\x65", "")
                    link = result.get("\x6C\x69\x6E\x6B", "")
                    message_text += f"{title}\n{link}\n\n"
                await message.reply_text(message_text.strip())
        else:
            await message.reply_text("متاسفانه مشکلی در جستجو رخ داده است🥲")
    except Exception as e:
        await message.reply_text(f"یک خطا رخ داده است: {str(e)}")
