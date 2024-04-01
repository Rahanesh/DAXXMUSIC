import requests
import random
from DAXXMUSIC import app, userbot
from DAXXMUSIC.misc import SUDOERS
from pyrogram import * 
from pyrogram.types import *
from DAXXMUSIC.utils.daxx_ban import admin_filter

# پیام‌های متنوع
Yumikoo_text = [
    "خواهشا سر به سرم نزار",
    "شما کی هستید؟",
    "تا الان کجا بودی",
    "آدرس خونه رو بفرس پی بام خواستگاری",
    "خواهش می‌کنم،برام لالایی بخون بخابم .",
    "هان بولو، چه کار دارید؟",
    "ببینید، من الان مشغول هستم.",
    "خواهش می‌کنم، من مشغولم",
    "آیا متوجه نمی‌شوید؟",
    "مرا تنها بزار ",
    "دوست من چه اتفاقی افتاده ",
]

# پیام‌های مربوط به محدودیت کاربران
strict_txt = [
    "نمی‌توانم برای دوستانم محدودیت اعمال کنم",
    "آیا جدی هستید که نمی‌توانم دوستانم را محدود کنم",
    "بیخیال چرا کاربران خودم را محدود کنم؟",
    "ادمین واقن که",
    "آره، این اولین کاری هست که انجام می‌دهیم، بیایید یکدیگر را بزنیم!",
    "نمی‌تونم! اون بهترین دوست منه.",
    "من دوستش دارم لطفاً این کاربر را محدود نکنید."
]

# لیست دستورات مختلف
ban = ["ban","boom","gaand",]
unban = ["unban",]
mute = ["mute","silent","shut"]
unmute = ["unmute","speak","free"]
kick = ["kick", "out","nikaal","nikal"]
promote = ["promote","adminship"]
fullpromote = ["fullpromote","fulladmin"]
demote = ["demote","lelo"]
group = ["group"]
channel = ["channel"]

# ========================================= #


@app.on_message(filters.command(["aby","aby"], prefixes=["b", "B"]) & admin_filter)
async def restriction_app(app :app, message):
    reply = message.reply_to_message
    chat_id = message.chat.id
    if len(message.text) < 2:
        return await message.reply(random.choice(Yumikoo_text))
    bruh = message.text.split(maxsplit=1)[1]
    data = bruh.split(" ")
    
    if reply:
        user_id = reply.from_user.id
        for banned in data:
            print(f"موجود {banned}")
            if banned in ban:
                if user_id in SUDOERS:
                    await message.reply(random.choice(strict_txt))          
                else:
                    await app.ban_chat_member(chat_id, user_id)
                    await message.reply("بله عزیزم 😘😘، این کاربر مزاحم بود! ممنون که بنش کردی.")
                    
        for unbanned in data:
            print(f"موجود {unbanned}")
            if unbanned in unban:
                await app.unban_chat_member(chat_id, user_id)
                await message.reply(f"بله عزیزم 😘😘، به درخواست شما کاربر را آزاد کردم") 
                
        for kicked in data:
            print(f"موجود {kicked}")
            if kicked in kick:
                if user_id in SUDOERS:
                    await message.reply(random.choice(strict_txt))
                
                else:
                    await app.ban_chat_member(chat_id, user_id)
                    await app.unban_chat_member(chat_id, user_id)
                    await message.reply("بله عزیزم 😘😘! کاربر را بیرون کشیدم!") 
                    
        for muted in data:
            print(f"موجود {muted}") 
            if muted in mute:
                if user_id in SUDOERS:
                    await message.reply(random.choice(strict_txt))
                
                else:
                    permissions = ChatPermissions(can_send_messages=False)
                    await message.chat.restrict_member(user_id, permissions)
                    await message.reply(f"بله عزیزم 😘😘، کاربر با موفقیت ساکت شد! آدمهای بی ادب.")
                    
        for unmuted in data:
            print(f"موجود {unmuted}")            
            if unmuted in unmute:
                permissions = ChatPermissions(can_send_messages=True)
                await message.chat.restrict_member(user_id, permissions)
                await message.reply(f"آه، خوب، سرکار!")   


        for promoted in data:
            print(f"موجود {promoted}")            
            if promoted in promote:
                await app.promote_chat_member(chat_id, user_id, privileges=ChatPrivileges(
                    can_change_info=False,
                    can_invite_users=True,
                    can_delete_messages=True,
                    can_restrict_members=False,
                    can_pin_messages=True,
                    can_promote_members=False,
                    can_manage_chat=True,
                    can_manage_video_chats=True,
                       )
                     )
                await message.reply("بله عزیزم 😘😘، ارتقا داده شد!")
                    
        for demoted in data:
            print(f"موجود {demoted}")            
            if demoted in demote:
                await app.promote_chat_member(chat_id, user_id, privileges=ChatPrivileges(
                    can_change_info=False,
                    can_invite_users=False,
                    can_delete_messages=False,
                    can_restrict_members=False,
                    can_pin_messages=False,
                    can_promote_members=False,
                    can_manage_chat=False,
                    can_manage_video_chats=False,
                       )
                     )
                await message.reply("بله عزیزم 😘😘، عزل پیدا کرد!")
                
        for fullpromoted in data:
            print(f"موجود {fullpromoted}")            
            if fullpromoted in fullpromote:
                await app.promote_chat_member(chat_id, user_id, privileges=ChatPrivileges(
                    can_change_info=True,
                    can_invite_users=True,
                    can_delete_messages=True,
                    can_restrict_members=True,
                    can_pin_messages=True,
                    can_promote_members=True,
                    can_manage_chat=True,
                    can_manage_video_chats=True,
                   )
                 )
                await message.reply("بله عزیزم 😘😘، به عنوان مدیر کل انتخاب شد!")
