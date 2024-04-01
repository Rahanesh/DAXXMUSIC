from pyrogram import Client, filters
from pyrogram.types import Message
from DAXXMUSIC import app

@app.on_message(filters.command(["اطلاعات گروه", "/groupinfo", "مشخصات گروه"]))
async def get_group_status(_, message: Message):
    if len(message.command) != 2:
        await message.reply("لطفاً نام کاربری گروه را وارد کنید. مثال: `/groupinfo نام_کاربری_گروه`")
        return
    
    group_username = message.command[1]
    
    try:
        group = await app.get_chat(group_username)
    except Exception as e:
        await message.reply(f"خطا: {e}")
        return
    
    total_members = await app.get_chat_members_count(group.id)
    group_description = group.description
    premium_acc = banned = deleted_acc = bot = 0  # شما باید این متغیرها را با تعدادهای واقعی جایگزین کنید.

    response_text = (
        f"➖➖➖➖➖➖➖\n"
        f"➲ نام گروه : {group.title} ✅\n"
        f"➲ گروه ID : {group.id}\n"
        f"➲ تعداد اعضا : {total_members}\n"
        f"➲ توضیحات گروه : {group_description or 'N/A'}\n"
        f"➲ یوزرنیم : @{group_username}\n"
       
        f"➖➖➖➖➖➖➖"
    )
    
    await message.reply(response_text)

@app.on_message(filters.command(["وضعیت", "/وضعیت", "/status"]))
async def group_status(client, message):
    if message.chat:
        chat = message.chat  # Chat where the command was sent
        status_text = f"شناسه گروه: {chat.id}\n" \
                      f"عنوان: {chat.title}\n" \
                      f"نوع: {chat.type}\n"
                      
        if chat.username:  # Not all groups have a username
            status_text += f"نام‌کاربری: @{chat.username}"
        else:
            status_text += "نام‌کاربری: ندارد"

        await message.reply_text(status_text)
    else:
        await message.reply_text("این دستور باید در یک گروه استفاده شود.")

#########

""" ***                                                                       
────────────────────────────────────────────────────────────────────────
─████████████────██████████████──████████──████████──████████──████████─
─██░░░░░░░░████──██░░░░░░░░░░██──██░░░░██──██░░░░██──██░░░░██──██░░░░██─
─██░░████░░░░██──██░░██████░░██──████░░██──██░░████──████░░██──██░░████─
─██░░██──██░░██──██░░██──██░░██────██░░░░██░░░░██──────██░░░░██░░░░██───
─██░░██──██░░██──██░░██████░░██────████░░░░░░████──────████░░░░░░████───
─██░░██──██░░██──██░░░░░░░░░░██──────██░░░░░░██──────────██░░░░░░██─────
─██░░██──██░░██──██░░██████░░██────████░░░░░░████──────████░░░░░░████───
─██░░██──██░░██──██░░██──██░░██────██░░░░██░░░░██──────██░░░░██░░░░██───
─██░░████░░░░██──██░░██──██░░██──████░░██──██░░████──████░░██──██░░████─
─██░░░░░░░░████──██░░██──██░░██──██░░░░██──██░░░░██──██░░░░██──██░░░░██─
─████████████────██████──██████──████████──████████──████████──████████─
────────────────────────────────────────────────────────────────────────**"""


####

