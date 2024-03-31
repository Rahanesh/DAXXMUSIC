import random 
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from DAXXMUSIC.plugins.tools.pretenderdb import impo_off, impo_on, check_pretender, add_userdata, get_userdata, usr_data
from DAXXMUSIC import app

MISHI = [
    "https://www.digikala.com/mag/wp-content/uploads/2023/01/Baymax-1.jpg",
    "https://media.mehrnews.com/d/2015/02/02/3/776179.jpg?ts=1486462047399",
    "https://media.mehrnews.com/d/2015/02/02/3/776194.jpg",
    "https://cdn.downloadefilm.ir/images/bfa23f80-1e42-11ee-970f-b5491249dc0d.jpg",
    "https://cdn.downloadefilm.ir/images/2f0bed60-9fa0-11ee-8e99-81873ab2d2be.jpg",
    "https://cdn.nody.ir/files/2021/08/13/nody2-%D9%BE%D8%B1%D9%88%D9%81%D8%A7%DB%8C%D9%84-%DA%AF%D8%B1%D9%88%D9%87-%D8%B9%D8%B4%D9%82%D9%88%D9%84%DB%8C%D8%A7-1628861680.jpg",
    "https://cdn.nody.ir/files/2021/08/13/nody2-%D8%B9%DA%A9%D8%B3-%D9%BE%D8%B1%D9%88%D9%81%D8%A7%DB%8C%D9%84-%DA%AF%D8%B1%D9%88%D9%87-%D8%AF%D8%AE%D8%AA%D8%B1%D9%88%D9%86%D9%87-%D8%B4%D8%A7%D8%AE-1628861668.jpg",
    "https://cdn.nody.ir/files/2021/08/13/nody2-%D8%B9%DA%A9%D8%B3-%D8%B4%D8%B4-%D9%86%D9%81%D8%B1%D9%87-%D8%AF%D9%88%D8%B3%D8%AA%D8%A7%D9%86%D9%87-%D8%AF%D8%AE%D8%AA%D8%B1%D8%A7%D9%86%D9%87-1628861671.jpg"
    "https://cdn.nody.ir/files/2021/08/13/nody2-%D8%B9%DA%A9%D8%B3-%D8%A8%D8%B1%D8%A7%DB%8C-%DA%AF%D8%B1%D9%88%D9%87-%D9%88%D8%A7%D8%AA%D8%B3%D8%A7%D9%BE-%D8%AF%D8%AE%D8%AA%D8%B1%D8%A7%D9%86%D9%87-1628861674.jpg",
    "https://www.samatak.com/image/2018/04/2/1025577380-samatak-com.jpg",
    "https://www.talab.org/wp-content/uploads/2016/01/1955408517-talab-ir.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRhQKwy_FVRtPEX887p-t5LPadyw3sXNFxuOpV96fdKDRFZv6GR6tg2tpU7wge4oZPyWk&usqp=CAU",
    "https://www.samatak.com/image/2018/04/2/1530307583-samatak-com.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRhQKwy_FVRtPEX887p-t5LPadyw3sXNFxuOpV96fdKDRFZv6GR6tg2tpU7wge4oZPyWk&usqp=CAU",
    "https://www.khalayegh.com/wp-content/uploads/2018/05/39-Copy-7.jpg",
    "https://www.technolife.ir/wp-content/uploads/2023/07/%D8%A8%D9%87%D8%AA%D8%B1%DB%8C%D9%86-%D8%A7%D9%86%DB%8C%D9%85%DB%8C%D8%B4%D9%86-%D9%87%D8%A7%DB%8C-%D8%AF%D9%86%DB%8C%D8%A7-1536x864.jpg",
    "https://www.technolife.ir/wp-content/uploads/2023/04/enchanto-800x450.jpg",
    "https://mag.teepset.ir/wp-content/uploads/2022/11/minimal_style_5.jpg",
]


ROY = [
    [
        InlineKeyboardButton(
            text="افزون من به گروه",
            url=f"https://t.me/MusicStarterBot?startgroup=true"),
        InlineKeyboardButton(text="بروزرسانی", url=f"https://t.me/Rahanesh")
    ],
]


@app.on_message(filters.group & ~filters.bot & ~filters.via_bot, group=69)
async def chk_usr(_, message: Message):
    if message.sender_chat or not await check_pretender(message.chat.id):
        return
    if not await usr_data(message.from_user.id):
        return await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    usernamebefore, first_name, lastname_before = await get_userdata(message.from_user.id)
    msg = ""
    if (
        usernamebefore != message.from_user.username
        or first_name != message.from_user.first_name
        or lastname_before != message.from_user.last_name
    ):
        msg += f"""
**♥︎ اطلاعات کاربر ♥︎**

**๏ نام** ➛ {message.from_user.mention}
**๏ آیدی عددی** ➛ {message.from_user.id}
"""
    if usernamebefore != message.from_user.username:
        usernamebefore = f"@{usernamebefore}" if usernamebefore else "NO USERNAME"
        usernameafter = (
            f"@{message.from_user.username}"
            if message.from_user.username
            else "NO USERNAME"
        )
        msg += """
**♥︎ نام کاربری تغییر کرد ♥︎**

**๏ آیدی قبلی** ➛ {bef}
**๏ آیدی کنونی** ➛ {aft}
""".format(bef=usernamebefore, aft=usernameafter)
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    if first_name != message.from_user.first_name:
        msg += """
**♥︎ نام اکانت تلگرامی تغییر کرد ♥︎**

**๏ نام قبلی** ➛ {bef}
**๏ نام کنونی** ➛ {aft}
""".format(
            bef=first_name, aft=message.from_user.first_name
        )
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    if lastname_before != message.from_user.last_name:
        lastname_before = lastname_before or "NO LAST NAME"
        lastname_after = message.from_user.last_name or "NO LAST NAME"
        msg += """
**♥︎ نام خانوادگی اکانت تلگرامی کاربر تغییر یافت ♥︎**

**๏ نام خانوادگی قبلی** ➛ {bef}
**๏ نام خانوادگی اکنون** ➛ {aft}
""".format(
            bef=lastname_before, aft=lastname_after
        )
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    if msg != "":
        await message.reply_photo(random.choice(MISHI), caption=msg, reply_markup=InlineKeyboardMarkup(ROY),)


@app.on_message(filters.group & filters.command("imposter") & ~filters.bot & ~filters.via_bot)
async def set_mataa(_, message: Message):
    if len(message.command) == 1:
        return await message.reply("**استفاده از کاربران تقلبی شناسایی شده: تقلبی روشن|خاموش**")
    if message.command[1] == "enable":
        cekset = await impo_on(message.chat.id)
        if cekset:
            await message.reply("**حالت تقلبی قبلاً فعال شده است.**")
        else:
            await impo_on(message.chat.id)
            await message.reply(f"**حالت تقلبی با موفقیت فعال شد برای** {message.chat.title}")
    elif message.command[1] == "disable":
        cekset = await impo_off(message.chat.id)
        if not cekset:
            await message.reply("**حالت تقلبی قبلاً غیرفعال شده است.**")
        else:
            await impo_off(message.chat.id)
            await message.reply(f"**حالت تقلبی با موفقیت غیرفعال شد برای** {message.chat.title}")
    else:
        await message.reply("**استفاده از کاربران تقلبی شناسایی شده: تقلبی روشن|خاموش**")

    
