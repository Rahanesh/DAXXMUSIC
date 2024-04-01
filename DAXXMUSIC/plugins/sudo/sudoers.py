from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.types import Message
from strings import get_string, helpers
from DAXXMUSIC import app
from pyrogram.types import InputMediaVideo
from DAXXMUSIC.misc import SUDOERS
from DAXXMUSIC.utils.database import add_sudo, remove_sudo
from DAXXMUSIC.utils.decorators.language import language
from DAXXMUSIC.utils.extraction import extract_user
from DAXXMUSIC.utils.inline import close_markup
from config import BANNED_USERS, OWNER_ID



@app.on_message(filters.command(["addsudo", "افزودن سودو"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & filters.user(OWNER_ID))
@language
async def useradd(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(_["general_1"])
    user = await extract_user(message)
    if user.id in SUDOERS:
        return await message.reply_text(_["sudo_1"].format(user.mention))
    added = await add_sudo(user.id)
    if added:
        SUDOERS.add(user.id)
        await message.reply_text(_["sudo_2"].format(user.mention))
    else:
        await message.reply_text(_["sudo_8"])


@app.on_message(filters.command(["delsudo", "حذف سودو"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & filters.user(OWNER_ID))
@language
async def userdel(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(_["general_1"])
    user = await extract_user(message)
    if user.id not in SUDOERS:
        return await message.reply_text(_["sudo_3"].format(user.mention))
    removed = await remove_sudo(user.id)
    if removed:
        SUDOERS.remove(user.id)
        await message.reply_text(_["sudo_4"].format(user.mention))
    else:
        await message.reply_text(_["sudo_8"])



@app.on_message(filters.command(["sudolist", "listsudo", "لیست سودو"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & ~BANNED_USERS)
async def sudoers_list(client, message: Message):
    keyboard = [[InlineKeyboardButton("๏ نمایش لیست سودو ๏", callback_data="check_sudo_list")]]
    reply_markups = InlineKeyboardMarkup(keyboard)
  
    await message.reply_photo(photo="https://t.me/rahaneshsource/141", caption="**» لیست سودو را با استفاده از دکمه زیر بررسی کنید.**\n\n**» توجه:** تنها کاربران سودو می‌توانند مشاهده کنند.", reply_markup=reply_markups)
    await message.reply_video(video="https://harfetaze.com/wp-content/uploads/2019/01/aks-profil-gitar-4.jpg", caption="**» لیست سودو را با استفاده از دکمه زیر بررسی کنید.**\n\n**» توجه:** تنها کاربران سودو می‌توانند مشاهده کنند.\n│ \n└» ساخته شده توسط دراگون𓆪 ", reply_markup=reply_markups)
    

@app.on_callback_query(filters.regex("^check_sudo_list$"))
async def check_sudo_list(client, callback_query: CallbackQuery):
    keyboard = []
    if callback_query.from_user.id not in SUDOERS:
        return await callback_query.answer("شرمنده دیگه دیر رسیدی تموم شد", show_alert=True)
    else:
        user = await app.get_users(OWNER_ID)

        user_mention = (user.first_name if not user.mention else user.mention)
        caption = f"**˹لیست مدیران˼**\n\n**مالک** ➥ {user_mention}\n\n"

        keyboard.append([InlineKeyboardButton("๏ ادمین ربات ๏", url=f"tg://openmessage?user_id={OWNER_ID}")])
        
        count = 1
        for user_id in SUDOERS:
            if user_id != OWNER_ID:
                try:
                    user = await app.get_users(user_id)
                    user_mention = user.mention if user else f"**🎁 سودو {count} ɪᴅ:** {user_id}"
                    caption += f"**🎁 سودو** {count} **»** {user_mention}\n"
                    button_text = f"๏ کاربران سودو {count} ๏ "
                    keyboard.append([InlineKeyboardButton(button_text, url=f"tg://openmessage?user_id={user_id}")]
                    )
                    count += 1
                except:
                    continue

        # Add a "Back" button at the end
        keyboard.append([InlineKeyboardButton("๏ برگشت ๏", callback_data="back_to_main_menu")])

        if keyboard:
            reply_markup = InlineKeyboardMarkup(keyboard)
            await callback_query.message.edit_caption(caption=caption, reply_markup=reply_markup)

@app.on_callback_query(filters.regex("^back_to_main_menu$"))
async def back_to_main_menu(client, callback_query: CallbackQuery):
    keyboard = [[InlineKeyboardButton("๏ لیست کاربران سودو ๏", callback_data="check_sudo_list")]]
    reply_markupes = InlineKeyboardMarkup(keyboard)
    await callback_query.message.edit_caption(caption="**» بررسی لیست سودو با استفاده از دکمه زیر**\n\n**» توجه:**  فقط کاربران سودو می‌توانند مشاهده کنند \n│ \n└»  ساخته شده توسط ذراگون", reply_markup=reply_markupes)






@app.on_message(filters.command(["delallsudo", "حذف همه سودو"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & filters.user(OWNER_ID))
@language
async def del_all_sudo(client, message: Message, _):
    count = len(SUDOERS) - 1  # Exclude the admin from the count
    for user_id in SUDOERS.copy():
        if user_id != OWNER_ID:
            removed = await remove_sudo(user_id)
            if removed:
                SUDOERS.remove(user_id)
                count -= 1
    await message.reply_text(f"می باشد {count} تعداد کاربران حذف شده از ")
