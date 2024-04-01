from DAXXMUSIC import app
from os import environ
from config import BOT_USERNAME
import config
from pyrogram import Client, filters
from pyrogram.types import ChatJoinRequest, InlineKeyboardButton, InlineKeyboardMarkup
from PIL import Image, ImageDraw, ImageFont
from typing import Union, Optional

# --------------------------------------------------------------------------------- #

get_font = lambda font_size, font_path: ImageFont.truetype(font_path, font_size)
resize_text = (
    lambda text_size, text: (text[:text_size] + "...").upper()
    if len(text) > text_size
    else text.upper()
)

# --------------------------------------------------------------------------------- #

async def get_userinfo_img(
    bg_path: str,
    font_path: str,
    user_id: Union[int, str],    
    profile_path: Optional[str] = None
):
    bg = Image.open(bg_path)

    if profile_path:
        img = Image.open(profile_path)
        mask = Image.new("L", img.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.pieslice([(0, 0), img.size], 0, 360, fill=255)

        circular_img = Image.new("RGBA", img.size, (0, 0, 0, 0))
        circular_img.paste(img, (0, 0), mask)
        resized = circular_img.resize((400, 400))
        bg.paste(resized, (440, 160), resized)

    img_draw = ImageDraw.Draw(bg)

    img_draw.text(
        (529, 627),
        text=str(user_id).upper(),
        font=get_font(46, font_path),
        fill=(255, 255, 255),
    )

    path = f"./userinfo_img_{user_id}.png"
    bg.save(path)
    return path

# --------------------------------------------------------------------------------- #

bg_path = "DAXXMUSIC/assets/userinfo.png"
font_path = "DAXXMUSIC/assets/sultan.ttf"

# --------------------------------------------------------------------------------- #

# Extract environment variables or provide default values
chat_id_env = environ.get("CHAT_ID")
CHAT_ID = [int(app) for app in chat_id_env.split(",")] if chat_id_env else []

TEXT = environ.get("APPROVED_WELCOME_TEXT", "**❅─────✧❅✦❅✧─────❅**\n**🌹HI {mention}**\n\n**🏓به گروه جدید خوش آمدید✨**\n\n**➻** {title}\n\n**💞میدونم که اینجا دوستای جدیدی پیدا میکنی سعی کن تو این گروه یکم بیشتر فعال باشی 🥳**\n**❅─────✧❅✦❅✧─────❅**")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

# List of random photo links
random_photo_links = [
    "https://dinu.ir/wp-content/uploads/2020/12/ariana-grande-reebok-photoshoot-5k_1536952308.jpg",
    "https://dl.topnaz.com/2017/05/Singers-Actors.jpg",
    "https://blog.netnazar.com/wp-content/uploads/2017/01/%D8%A8%D9%87%D8%AA%D8%B1%DB%8C%D9%86-%D8%A8%D8%A7%D8%B2%DB%8C%DA%AF%D8%B1-%D9%85%D8%B1%D8%AF-%D8%A7%DB%8C%D8%B1%D8%A7%D9%86-%DA%A9%DB%8C%D8%B3%D8%AA%D8%9F.jpg",
     "https://www.tasvirezendegi.com/wp-content/uploads/2022/08/Shabnam-Qolikhani-Nina-Dobrev.jpg",
     "https://static2.rokna.net/servev2/UR67R3s43aek/Db2f077dXpA,/%D8%A2%D8%B1%DB%8C%D8%A7%D9%86%D8%A7+%DA%AF%D8%B1%D8%A7%D9%86%D8%AF%D9%87.jpg",
      "https://cdn.vaghtesobh.com/thumbnail/NYHJjoAmNWpN/ekf95ccTp5Pj867cDeZ7Rq3IRtC_LzavC11yPIYtHdNcdfZqUZ2hzrDWS6_3q29Qg4oe5hxAa5HzrDa4doCbJ-BPZ0E05y0s1r3NwILrdGrSRnBYS43z8w,,/%D8%B4%D8%A7%D8%AF%DB%8C+%D9%85%D8%AE%D8%AA%D8%A7%D8%B1%DB%8C.jpg",
      "https://dl.topnaz.com/2017/05/Singers-Actors.jpg",
      



    
    # Add more links as needed
]

# Define an event handler for chat join requests
@app.on_chat_join_request((filters.group | filters.channel) & filters.chat(CHAT_ID) if CHAT_ID else (filters.group | filters.channel))
async def autoapprove(client: app, message: ChatJoinRequest):
    chat = message.chat  # Chat
    user = message.from_user  # User

    # Check if user has a profile photo
    photo = None
    if user.photo:
        photo = await app.download_media(user.photo.big_file_id)

    # Fix the indentation here
    welcome_photo = await get_userinfo_img(
        bg_path=bg_path,
        font_path=font_path,
        user_id=user.id,
        profile_path=photo,
    )

    print(f"{user.first_name} Joined 🤝")  # Logs

    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)

    if APPROVED == "on":
        await client.send_photo(
            chat_id=chat.id,
            photo=welcome_photo,
            caption=TEXT.format(mention=user.mention, title=chat.title),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            " ๏ افزون به  ๏ ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                    ]
                ]
            ),
    )
    
