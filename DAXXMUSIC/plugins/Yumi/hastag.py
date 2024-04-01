import requests
from bs4 import BeautifulSoup as  BSP
from DAXXMUSIC import app as DAXX
from pyrogram import filters
url = "https://all-hashtag.com/library/contents/ajax_generator.php"

@DAXX.on_message(filters.command(["هشتگ", "هشتک", "hastag", "hashtag"]))
async def hastag(bot, message):
    global content
    try:
        text = message.text.split(' ',1)[1]
        data = dict(keyword=text, filter="top")

        res = requests.post(url, data).text

        content = BSP(res, 'html.parser').find("div", {"class":"copy-hashtags"}).string
    except IndexError:
        return await message.reply_text("مثال:\n\n/hashtag کلمه")
        
    
    await message.reply_text(f"اینجا هشتگ شما است:\n<pre>{content}</pre>", quote=True)
    
mod_name = "هشتگ"
help= """
شما می‌توانید از این ابزار هشتگ استفاده کنید که بر اساس یک کلمه انتخابی، ۳۰ هشتگ برتر و بیشتر را به شما ارائه می‌دهد.
° /hashtag کلمه را وارد کنید تا هشتگ تولید شود.
°مثال:  /hashtag شادمهر """

