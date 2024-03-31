import requests
from DAXXMUSIC import app
from pyrogram import Client, filters

JOKE_API_ENDPOINT = 'https://api.codebazan.ir/jok'

@app.on_message(filters.command("hjoke"))
async def joke(_, message):
    response = requests.get(JOKE_API_ENDPOINT)
    if response.status_code == 200:
        joke_text = response.text
        await message.reply_text(joke_text)
    else:
        await message.reply_text("متأسفانه نتوانستیم جوک را دریافت کنیم. لطفاً بعداً دوباره امتحان کنید.")
