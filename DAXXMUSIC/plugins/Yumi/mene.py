from pyrogram import Client, filters
import requests
from DAXXMUSIC import app 

# تعریف یک دستور برای دستور /میم
@app.on_message(filters.command(["میم", "meme"]))
def meme_command(client, message):
    # آدرس API برای میم‌های تصادفی
    api_url = "https://meme-api.com/gimme"

    try:
        # ارسال درخواست به API
        response = requests.get(api_url)
        data = response.json()

        # استخراج آدرس تصویر میم
        meme_url = data.get("url")
        title = data.get("title")

        # افزودن نام کاربری ربات در زیرنویس
        caption = f"{title}\n\nدرخواست شده توسط {message.from_user.mention}\nنام کاربری ربات: @{app.get_me().username}"

        # ارسال تصویر میم به کاربر با زیرنویس تغییر یافته
        message.reply_photo(
            photo=meme_url,
            caption=caption
        )

    except Exception as e:
        print(f"خطا در دریافت میم: {e}")
        message.reply_text("با عرض پوزش، در حال حاضر نمی‌توان میمی را دریافت کرد.")
