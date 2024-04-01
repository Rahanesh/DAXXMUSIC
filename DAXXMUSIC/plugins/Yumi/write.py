from pyrogram import filters
from pyrogram import *
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import  BOT_USERNAME
from datetime import datetime
from DAXXMUSIC import app as app
import requests

# Command to write text on a white page
@app.on_message(filters.command("write"))
async def handwrite(_, message: Message):
    if message.reply_to_message:
        text = message.reply_to_message.text
    else:
        text =message.text.split(None, 1)[1]
    m =await message.reply_text( "لطفاً صبر کنید...,\n\nدر حال نوشتن متن شما...")
    write = requests.get(f"https://apis.xditya.me/write?text={text}").url

    caption = f"""
متن با موفقیت نوشته شد 💘
✨ نوشته شده توسط : [لینکدونی𓆪](https://t.me/fapiqr)
🥀 درخواست شده توسط : {message.from_user.mention}
"""
    await m.delete()
    await message.reply_photo(photo=write,caption=caption)

mod_name = "ابزار نوشتن"

help = """

 این دستور متن داده شده را روی یک صفحه سفید با یک قلم 🖊 می نویسد

❍ /write <متن> *:* متن داده شده را می نویسد.
 """

#----------

# Command to convert date to day
@app.on_message(filters.command("day"))
def date_to_day_command(client: Client, message: Message):
    try:
        # Extract the date from the command message......
        command_parts = message.text.split(" ", 1)
        if len(command_parts) == 2:
            input_date = command_parts[1].strip()
            date_object = datetime.strptime(input_date, "%Y-%m-%d")
            day_of_week = date_object.strftime("%A")

            # Reply with the day of the week
            message.reply_text(f"The day of the week for {input_date} is {day_of_week}.")

        else:
            message.reply_text("لطفاً یک تاریخ معتبر در قالب `/day 2024-08-15` وارد کنید")

    except ValueError as e:
        message.reply_text(f"خطا: {str(e)}")
