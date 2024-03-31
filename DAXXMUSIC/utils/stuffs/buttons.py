from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums

class BUTTONS(object):
    MBUTTON = [[InlineKeyboardButton("چت جی‌پی‌تی💬", callback_data="mplus HELP_ChatGPT"),InlineKeyboardButton("گروه‌ها🧩", callback_data="mplus HELP_Group"),InlineKeyboardButton("استیکرها🥁", callback_data="mplus HELP_Sticker")],
    [InlineKeyboardButton("برچسب‌گذاری همه🔅", callback_data="mplus HELP_TagAll"),
    InlineKeyboardButton("اطلاعات❗️", callback_data="mplus HELP_Info"),InlineKeyboardButton("اضافی", callback_data="mplus HELP_Extra")],
    [InlineKeyboardButton("تصویر🖼", callback_data="mplus HELP_Image"),
    InlineKeyboardButton("عملیات⚜️", callback_data="mplus HELP_Action"),InlineKeyboardButton("جستجو🔍", callback_data="mplus HELP_Search")],    
    [InlineKeyboardButton("فونت🖊", callback_data="mplus HELP_Font"),
    InlineKeyboardButton("بازی‌ها🎮", callback_data="mplus HELP_Game"),InlineKeyboardButton("تلگراف🛜", callback_data="mplus HELP_TG")],
    [InlineKeyboardButton("تقلب🤹‍♀️", callback_data="mplus HELP_Imposter"),
    InlineKeyboardButton("حقیقت یا جرات🎭", callback_data="mplus HELP_TD"),InlineKeyboardButton("هشتگ🎵", callback_data="mplus HELP_HT")], 
    [InlineKeyboardButton("متن به صدا🔊", callback_data="mplus HELP_TTS"),
    InlineKeyboardButton("سرگرمی🏓", callback_data="mplus HELP_Fun"),InlineKeyboardButton("نقل قول🪧", callback_data="mplus HELP_Q")],          
    [InlineKeyboardButton("<", callback_data=f"settings_back_helper"), 
    InlineKeyboardButton(">", callback_data=f"managebot123 settings_back_helper"),
    ]]
