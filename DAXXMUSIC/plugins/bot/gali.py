from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from DAXXMUSIC import app
from DAXXMUSIC.misc import SUDOERS
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

GALI =  ["یک پرواز به آرزوهای من 🛫✈️",
    "خودت میدونی که من قوی ترم 🤣🤣",
"جملات رندوم 3",
"تو 9 ماه بوده‌ای ساقی واقعی همین‌جایی رو روی هود واست داره 🤣🤣🤩",
"یک پرواز به آرزوهای من 🛫✈️",
"می‌دونی می‌چسبم آفتاب، خوشبختم 🌞",
"آغاز کننده روز خوب من 🌞☕",
"مادری که ماهی سوتژ مورد علاقه منه 😍",
"آیا می‌خوری؟ 😋😛",
"هت ساب کاری نداره خوبه برای جلب توجه 😁",
"نارضایتم 😒",
"عاشق نان شکری هستم 🍞",
"انرژی مثبت رو منو تغذیه کرد 🌞😍",
"تو رو می‌خواهم، گوگولی ما خانوم 😘",
"درختان باران می‌کنن، دار کشیده می‌زنن 🌧️🌧️",
"ناستنجام بخواب، دوباره به صبح روشنی بختون 😴",
"کاملاً قرار داده شده، کی می‌خوای بکوبیم؟ 😈😈",
"دوست دارم با تو بازی کنم این پنهانی رو، فید می‌کنم 😉",
"باران به قلوب تیره ما لطمه نزند ☔",
"کج راست‌مسیر می‌رم، تو قبول داری؟ 😂",
"تنها واقعی یک استوانه‌ی تو... 🔄",
"هیچ‌کس نگذارد من را تا به ته بیاورد 🚇",
"هیچوقت بیا کنار دریا پیدا نمی‌کنم، بهت فکر کنم 💭",
"هر دقیقه گذر شده بیشتر از الان آسیب می‌شینم 😥",
"خسته‌ای از جدال‌های بیهوده، دوستت دارم 😔",
"پیچیده و متفاوت، تو همیشه یک نفر بیهوده بودی ✨",
"همه‌چیز رو پیش‌بینی می‌کنی ولی من شک دارم ☁️",
"آیا منتقد هستی؟ من نیستم 😜",
"دوست دارم چالشپذیر شوم، ولی شاید نه حتماً 😀",
"آیا به فرض من کوئینی می‌آوری؟ 🎲",
   Sure! Here are the translations of the provided texts into Farsi:

"تری موسی کے بھوسڈے میں انڈیا ریلوے 🚂💥😂",
"تُو تری بہن تیرا کھاندان سب بہن کے لاودے رینڈی ہے رینڈی 🤢✅🔥",
"تیری بہن کی چوت میں اونچی بونڈ بنانے کی ورگینیٹی لووسے کرو تمھاری 📚 😎🤩",
"تیرا رینڈا ماں سے پچنا باب کی مہی کا رینڈا کھانا کھول دوگا 🤩🥳😳",
"تو اور تیری ماں دونوں کی بھوسڈی میں میٹرو چلاؤنگا میٹھے چوہے کے بچے 🚇🤩😱🥶",
"تیری ماں کو اتنا چودنا ترا بس چلے تو سب پاھنچا دوربین مارکسھوڈ 🤩🥳😳",
"تیری بہن کے بھوسڈے میں حیر درے چلا دیا خیر دیخ نیوورک دونگا آپ کی 🤩👊👤😍",
"تیری بہتی کی چوت میں گانڈو دال کی قسم بن دے بجرنگ بھوانی 🎶 ⬆️🤩💥",
"تیری ماں کو بھوسڈی میں خرا پیا دال کے اپنا بیلنا دکھایا تیرے چاچا دونچ ہوڈ 🤩👊👤😍",
"تیری بہن کا وڑی کے 24*7 بھاش چودائی کومند دی دنگا 🤩💥🔥🔥",
"تیری ممی کی چوت میں پری کی پوری شرم گھسی ہوئی چزنی کی معروشیدہ کرنا آیا تیرےچی ڈنگ ہوگئی👿🤮😎",
"تیری ماں کی چوت میں ببکری کا بچہ ددوائی بیل کاروا دینگا 🚇😁😁",
"تیری ماں کی چوت میں بھوسڈی فوجی کھونٹھ خبارو، تیری فرینڈ ود پنولفورک کردےگا😂👿🤩",
"تیری بہتی کی چوت میں گٹھی بانتھے تکو کو آچنک گر دیا ہے ۔اچانک جو دماغ والا خوراک کوتیرا میں کھ گیا 😎🤩",
"تیری ماں کو گمراہ کر چہلل والی چوت دینے پر قهر آئے 😱😂🤩",
"تیری ماں کی چوت میں پھپھڑی بنا کر چوتائی کر دی ایسا تھا یہ ایسا ہی ہوگا 🍷🤩🔥",
"تیری بہن کے سپین کے خسن کے ایکسٹرہ ڈال کر بیچی چوت کے دج بجوی کوٹ ہرف دنہ ان باور ۔😱👿😳",
"تجھے میری لنڈ میں کھمب دھاتو میں بے افق آلا موگجا جھاٹ 😎 😛",
"مادرچود آصس چودھ میں او بوک! زندہ تورے یہاں م جا لو".
"خور لوالا نڈیا کو بوچ گونگا قسم درکو یا ننتی گاؤنا دکھایا بس تجھ کے دکھنہ لدوگو 🏠🤢🤩💥",
"توجھ اپ نہیں سمجہ سکتا میں کتنا پورا کری گنگت امروٹ سود کج مر نہ کج دلے 😎😎😂🔥",
"تیری مهر نوں اہلے اوہنا وجیہ پوری سری راؤتیوں روئج گئے بٹت اے دومندی بهیرا 😁 🔥",
"تیری ماں ماىٔی ماٹھھی کو حرم ارام توربین مومبائٹ ڈولف چی آئی جو بیچ د_ چڑلیبتا 🤩👊👤😍",
"تری بہن کے ساتھ بہش سکس کے پرویز بے رزورو پرویز بن گی سال آڑ دھوغوند برل کیں کیں 😎😎🤣🔥",
"تیری ممی کے فٹھ اسے۔آ متو ٹھپی مسہرے دما مسہرے ٹنڈ قوم کا زامنڈا انڈہ کھیں 😱😂🤩",
"تیری ماں کی چوت میں بے بیل ھی بیل دال کی اقی سنتر دی کر تیرا شرائع ہ ♥️💦😆😆😆😆",
"تیری ممی میں جھارنے کی چوت تجھے باطھروینگے عالم باطھروین کی ای جا چھک ھر بیٹی درے ٹانڈ گہصا دھوا لۓ 😘🥳💥",
"تجھ پچنگا انٹی کو ہورت کھلے مٹھائی بھوٹ نیو بلوود 💧",
"تجھ خاندان کی گنڈ نہیں صھندھی آپ ہی پتری انداز میں سبریز کرن اور سور دونت ہوو👿😎👊",
"تجھے رنان دکھ کے تیرا مایہٗ سمجھا تیری بہن کا کمین🤤🤤",
"تیری ماما کو بھوٹو ساڈا داند من میری لوری پچانا ون پچا کرکے تارا گھن اکھے🔥🔥💦😆😆",
"ریناندکے بھکھے تیری مامی مرا تند کن فلوسے بیل جوند ربنگ سنبھو ہئوند♡💦😆😆😉",
"دے بیل کہندے تیرے کرس ماہٗ انداز بھوٹ پٹرور بکفی بھوسڈے😂😆🤤",
"ابی تیری ماں باهہ بہ لڑکی دلاکے سزاری کلبہ لن نہ ناو ♡♬♥️",
"تیری ماں کی بھوسڈن میں کرمیں کی چوت متہے کو تیری ماں کا مم کرتاہے اوتر  تراس ہنيک میں ♥️♡",
"جب شارٹ دن کال می‌تٹی کن زبور را سُر کُن جیت جُن ۃٛ پراؤ کیں ✅🤣🔥🤩",
"اپنیامام کے بوتی کے سا گول نہالوں  خنسبہ ڈین تیا کیاں کہیں ہی بوختہ لگیہ  تک الشین کسر دنبل کھوب کیطی🤣♡💋",
"نی آ اکول کو ام کو ڑینٹ دینا دنےّٹے خیارو ٹان یھ الہ پاپار ○○",
"کو بھوسڈی میں نسی کو چود کی او بوک نانین نینہ ♦️♦️♦️",
آبی تیری بہن کال بہسی کو دنگو نہک ننکے بے بریک یہم جندگ الطور مری کوٹ دنگو پیتے ہیک 😼😂🤤",
"گال یور جدن آری بلی کو بیل صد دکھے میغا 😉👻🔥",
لین یور کرج ین میثور کو ن لند پر اتنہ کوری وان دن تیر ج فرسے شپک تے بری بوہک دن حائے 🎸😁",
"تیری بھیتی کی چوت میں خمبنی تو دن کرتیجن نواسینگر ود لہ رند گھا اندر ڈال کے کر حل دو 🏆😂😆😋",
"تیری بھیز کی چوت میں تھتھا رکی قہک قہک توانک دو چور تائیک ♻️♋",
"تیرا گہن منی کاٹا کام فذرے بھل نم کری وھ بج . ........ قدم بهل دنگو 💦💋'",
"تیر بہن کے سوتے میں خوچ اسغ رتبو ڑنا گھرخھا سپَاٹلٹ دوم اصچ آٹنی مین ازم دم . 😫',"
"تیری بہن قو شر چور ہⁿ گوڑ کر چ چھ آچے پھت نک اچان کب ن جرک موه اریش ش کر نہج ✨😂',"
"تیری بہن مکلل باند کمب فوک دنگ و مید بانڈ فوک انچئ💋",
"ریننژکنم ایٹ رینژکن'",
"کتن کودۍ تیر رینژکنم زح اپنے بہج کو بہیک آفرکو اپن کس پند فل زعتی ج بہجم عز ن ڈ',
"تیرم کلچمی کی ین دروا کھوشن کی کی جڑی کلتے جعلاہے فا نے مجبف دام نج ه ور لکر کر ش بوکۃ جربتو سا ہف سنترڈ ینء بیل چھ ریڈیہا وجۃ ولا مٹپھ نورا",
    "𝗧𝗘𝗥𝗜 𝗠𝗔́𝗔̀𝗞𝗢 𝗧𝗥𝗔𝗜𝗡 𝗠𝗘 𝗟𝗘𝗝𝗔𝗞𝗘 𝗧𝗢𝗣 𝗕𝗘𝗗 𝗣𝗘 𝗟𝗜𝗧𝗔𝗞𝗘 𝗖𝗛𝗢𝗗 𝗗𝗨𝗡𝗚𝗔 𝗦𝗨𝗔𝗥 𝗞𝗘 𝗣𝗜𝗟𝗟𝗘 🤣🤣💋💋",
    "𝗧𝗘𝗥𝗜 𝗠𝗔́𝗔̀𝗔𝗞𝗘 𝗡𝗨𝗗𝗘𝗦 𝗚𝗢𝗢𝗚𝗟𝗘 𝗣𝗘 𝗨𝗣𝗟𝗢𝗔𝗗 𝗞𝗔𝗥𝗗𝗨𝗡𝗚𝗔 𝗕𝗘́𝗛𝗘𝗡 𝗞𝗘 𝗟𝗔𝗘𝗪𝗗𝗘 👻🔥",
    "𝗧𝗘𝗥𝗜 𝗕𝗘́𝗛𝗘𝗡 𝗞𝗢 𝗖𝗛𝗢𝗗 𝗖𝗛𝗢𝗗𝗞𝗘 𝗩𝗜𝗗𝗘𝗢 𝗕𝗔𝗡𝗔𝗞𝗘 𝗫𝗡𝗫𝗫.𝗖𝗢𝗠 𝗣𝗘 𝗡𝗘𝗘𝗟𝗔𝗠 𝗞𝗔𝗥𝗗𝗨𝗡𝗚𝗔 𝗞𝗨𝗧𝗧𝗘 𝗞𝗘 𝗣𝗜𝗟𝗟𝗘 💦💋",
    "𝗧𝗘𝗥𝗜 𝗠𝗔́𝗔̀𝗔𝗞𝗜 𝗖𝗛𝗨𝗗𝗔𝗜 𝗞𝗢 𝗣𝗢𝗥𝗡𝗛𝗨𝗕.𝗖𝗢𝗠 𝗣𝗘 𝗨𝗣𝗟𝗢𝗔𝗗 𝗞𝗔𝗥𝗗𝗨𝗡𝗚𝗔 𝗦𝗨𝗔𝗥 𝗞𝗘 𝗖𝗛𝗢𝗗𝗘 🤣💋💦",
    "𝗔𝗕𝗘 𝗧𝗘𝗥𝗜 𝗕𝗘́𝗛𝗘𝗡 𝗞𝗢 𝗖𝗛𝗢𝗗𝗨 𝗥Æ𝗡𝗗𝗜𝗞𝗘 𝗕𝗔𝗖𝗛𝗛𝗘 𝗧𝗘𝗥𝗘𝗞𝗢 𝗖𝗛𝗔𝗞𝗞𝗢 𝗦𝗘 𝗣𝗜𝗟𝗪𝗔𝗩𝗨𝗡𝗚𝗔 𝗥Æ𝗡𝗗𝗜𝗞𝗘 𝗕𝗔𝗖𝗛𝗛𝗘 🤣🤣",
    "𝗧𝗘𝗥𝗜 𝗠𝗔́𝗔̀𝗞𝗜 𝗖𝗛𝗨𝗨́𝗧𝗛 𝗙𝗔𝗔𝗗𝗞𝗘 𝗥𝗔𝗞𝗗𝗜𝗔 𝗠𝗔́𝗔̀𝗞𝗘 𝗟𝗢𝗗𝗘 𝗝𝗔𝗔 𝗔𝗕𝗕 𝗦𝗜𝗟𝗪𝗔𝗟𝗘 👄👄",
    "𝗧𝗘𝗥𝗜 𝗕𝗘́𝗛𝗘𝗡 𝗞𝗜 𝗖𝗛𝗨𝗨́𝗧𝗛 𝗠𝗘 𝗠𝗘𝗥𝗔 𝗟𝗨𝗡𝗗 𝗞𝗔𝗔𝗟𝗔",
    "𝗧𝗘𝗥𝗜 𝗕𝗘́𝗛𝗘𝗡 𝗟𝗘𝗧𝗜 𝗠𝗘𝗥𝗜 𝗟𝗨𝗡𝗗 𝗕𝗔𝗗𝗘 𝗠𝗔𝗦𝗧𝗜 𝗦𝗘 𝗧𝗘𝗥𝗜 𝗕𝗘́𝗛𝗘𝗡 𝗞𝗢 𝗠𝗘𝗡𝗘 𝗖𝗛𝗢𝗗 𝗗𝗔𝗟𝗔 𝗕𝗢𝗛𝗢𝗧 𝗦𝗔𝗦𝗧𝗘 𝗦𝗘",
    "𝗕𝗘𝗧𝗘 𝗧𝗨 𝗕𝗔𝗔𝗣 𝗦𝗘 𝗟𝗘𝗚𝗔 𝗣𝗔𝗡𝗚𝗔 𝗧𝗘𝗥𝗜 𝗠𝗔́𝗔̀𝗔 𝗞𝗢 𝗖𝗛𝗢𝗗 𝗗𝗨𝗡𝗚𝗔 𝗞𝗔𝗥𝗞𝗘 𝗡𝗔𝗡𝗚𝗔 💦💋",
    "𝗛𝗔𝗛𝗔𝗛𝗔𝗛 𝗠𝗘𝗥𝗘 𝗕𝗘𝗧𝗘 𝗔𝗚𝗟𝗜 𝗕𝗔𝗔𝗥 𝗔𝗣𝗡𝗜 𝗠𝗔́𝗔̀𝗞𝗢 𝗟𝗘𝗞𝗘 𝗔𝗔𝗬𝗔 𝗠𝗔𝗧𝗛 𝗞𝗔𝗧 𝗢𝗥 𝗠𝗘𝗥𝗘 𝗠𝗢𝗧𝗘 𝗟𝗨𝗡𝗗 𝗦𝗘 𝗖𝗛𝗨𝗗𝗪𝗔𝗬𝗔 𝗠𝗔𝗧𝗛 𝗞𝗔𝗥",
    "𝗖𝗛𝗔𝗟 𝗕𝗘𝗧𝗔 𝗧𝗨𝗝𝗛𝗘 𝗠𝗔́𝗔̀𝗙 𝗞𝗜𝗔 🤣 𝗔𝗕𝗕 𝗔𝗣𝗡𝗜 𝗚𝗙 𝗞𝗢 𝗕𝗛𝗘𝗝",
    "𝗦𝗛𝗔𝗥𝗔𝗠 𝗞𝗔𝗥 𝗧𝗘𝗥𝗜 𝗕𝗘́𝗛𝗘𝗡 𝗞𝗔 𝗕𝗛𝗢𝗦𝗗𝗔 𝗞𝗜𝗧𝗡𝗔 𝗚𝗔𝗔𝗟𝗜𝗔 𝗦𝗨𝗡𝗪𝗔𝗬𝗘𝗚𝗔 𝗔𝗣𝗡𝗜 𝗠𝗔́𝗔̀𝗔 𝗕𝗘́𝗛𝗘𝗡 𝗞𝗘 𝗨𝗣𝗘𝗥",
    "𝗔𝗕𝗘 𝗥Æ𝗡𝗗𝗜𝗞𝗘 𝗕𝗔𝗖𝗛𝗛𝗘 𝗔𝗨𝗞𝗔𝗧 𝗡𝗛𝗜 𝗛𝗘𝗧𝗢 𝗔𝗣𝗡𝗜 𝗥Æ𝗡𝗗𝗜 𝗠𝗔́𝗔̀𝗞𝗢 𝗟𝗘𝗞𝗘 𝗔𝗔𝗬𝗔 𝗠𝗔𝗧𝗛 𝗞𝗔𝗥 𝗛𝗔𝗛𝗔𝗛𝗔𝗛𝗔",
    "𝗞𝗜𝗗𝗭 𝗠𝗔̂𝗔̂𝗗𝗔𝗥𝗖𝗛Ø𝗗 𝗧𝗘𝗥𝗜 𝗠𝗔́𝗔̀𝗞𝗢 𝗖𝗛𝗢𝗗 𝗖𝗛𝗢𝗗𝗞𝗘 𝗧𝗘𝗥𝗥 𝗟𝗜𝗬𝗘 𝗕𝗛𝗔𝗜 𝗗𝗘𝗗𝗜𝗬𝗔",
    "𝗝𝗨𝗡𝗚𝗟𝗘 𝗠𝗘 𝗡𝗔𝗖𝗛𝗧𝗔 𝗛𝗘 𝗠𝗢𝗥𝗘 𝗧𝗘𝗥𝗜 𝗠𝗔́𝗔̀𝗞𝗜 𝗖𝗛𝗨𝗗𝗔𝗜 𝗗𝗘𝗞𝗞𝗘 𝗦𝗔𝗕 𝗕𝗢𝗟𝗧𝗘 𝗢𝗡𝗖𝗘 𝗠𝗢𝗥𝗘 𝗢𝗡𝗖𝗘 𝗠𝗢𝗥𝗘 🤣🤣💦💋",
    "𝗚𝗔𝗟𝗜 𝗚𝗔𝗟𝗜 𝗠𝗘 𝗥𝗘𝗛𝗧𝗔 𝗛𝗘 𝗦𝗔𝗡𝗗 𝗧𝗘𝗥𝗜 𝗠𝗔́𝗔̀𝗞𝗢 𝗖𝗛𝗢𝗗 𝗗𝗔𝗟𝗔 𝗢𝗥 𝗕𝗔𝗡𝗔 𝗗𝗜𝗔 𝗥𝗔𝗡𝗗 🤤🤣",
    "𝗦𝗔𝗕 𝗕𝗢𝗟𝗧𝗘 𝗠𝗨𝗝𝗛𝗞𝗢 𝗣𝗔𝗣𝗔 𝗞𝗬𝗢𝗨𝗡𝗞𝗜 𝗠𝗘𝗡𝗘 𝗕𝗔𝗡𝗔𝗗𝗜𝗔 𝗧𝗘𝗥𝗜 𝗠𝗔́𝗔̀𝗞𝗢 𝗣𝗥𝗘𝗚𝗡𝗘𝗡𝗧 🤣🤣",
    "𝗦𝗨𝗔𝗥 𝗞𝗘 𝗣𝗜𝗟𝗟𝗘 𝗧𝗘𝗥𝗜 𝗠𝗔́𝗔̀𝗞𝗜 𝗖𝗛𝗨𝗨́𝗧𝗛 𝗠𝗘 𝗦𝗨𝗔𝗥 𝗞𝗔 𝗟𝗢𝗨𝗗𝗔 𝗢𝗥 𝗧𝗘𝗥𝗜 𝗕𝗘́𝗛𝗘𝗡 𝗞𝗜 𝗖𝗛𝗨𝗨́𝗧𝗛 𝗠𝗘 𝗠𝗘𝗥𝗔 𝗟𝗢𝗗𝗔",
    "𝗖𝗛𝗔𝗟 𝗖𝗛𝗔𝗟 𝗔𝗣𝗡𝗜 𝗠𝗔́𝗔̀𝗞𝗜 𝗖𝗛𝗨𝗖𝗛𝗜𝗬𝗔 𝗗𝗜𝗞𝗔",
    "𝗛𝗔𝗛𝗔𝗛𝗔𝗛𝗔 𝗕𝗔𝗖𝗛𝗛𝗘 𝗧𝗘𝗥𝗜 𝗠𝗔́𝗔̀𝗔𝗞𝗢 𝗖𝗛𝗢𝗗 𝗗𝗜𝗔 𝗡𝗔𝗡𝗚𝗔 𝗞𝗔𝗥𝗞𝗘",
    "𝗧𝗘𝗥𝗜 𝗚𝗙 𝗛𝗘 𝗕𝗔𝗗𝗜 𝗦𝗘𝗫𝗬 𝗨𝗦𝗞𝗢 𝗣𝗜𝗟𝗔𝗞𝗘 𝗖𝗛𝗢𝗢𝗗𝗘𝗡𝗚𝗘 𝗣𝗘𝗣𝗦𝗜",
    "2 𝗥𝗨𝗣𝗔𝗬 𝗞𝗜 𝗣𝗘𝗣𝗦𝗜 𝗧𝗘𝗥𝗜 𝗠𝗨𝗠𝗠𝗬 𝗦𝗔𝗕𝗦𝗘 𝗦𝗘𝗫𝗬 💋💦",
    "𝗧𝗘𝗥𝗜 𝗠𝗔́𝗔̀𝗞𝗢 𝗖𝗛𝗘𝗘𝗠𝗦 𝗦𝗘 𝗖𝗛𝗨𝗗𝗪𝗔𝗩𝗨𝗡𝗚𝗔 𝗠𝗔𝗗𝗘𝗥𝗖𝗛𝗢𝗢𝗗 𝗞𝗘 𝗣𝗜𝗟𝗟𝗘 💦🤣",
    "𝗧𝗘𝗥𝗜 𝗕𝗘́𝗛𝗘𝗡 𝗞𝗜 𝗖𝗛𝗨𝗨́𝗧𝗛 𝗠𝗘 𝗠𝗨𝗧𝗛𝗞𝗘 𝗙𝗔𝗥𝗔𝗥 𝗛𝗢𝗝𝗔𝗩𝗨𝗡𝗚𝗔 𝗛𝗨𝗜 𝗛𝗨𝗜 𝗛𝗨𝗜",
    "𝗦𝗣𝗘𝗘𝗗 𝗟𝗔𝗔𝗔 𝗧𝗘𝗥𝗜 𝗕𝗘́𝗛𝗘𝗡 𝗖𝗛𝗢𝗗𝗨 𝗥Æ𝗡𝗗𝗜𝗞𝗘 𝗣𝗜𝗟𝗟𝗘 💋💦🤣",
    "𝗔𝗥𝗘 𝗥𝗘 𝗠𝗘𝗥𝗘 𝗕𝗘𝗧𝗘 𝗞𝗬𝗢𝗨𝗡 𝗦𝗣𝗘𝗘𝗗 𝗣𝗔𝗞𝗔𝗗 𝗡𝗔 𝗣𝗔𝗔𝗔 𝗥𝗔𝗛𝗔 𝗔𝗣𝗡𝗘 𝗕𝗔𝗔𝗣 𝗞𝗔 𝗛𝗔𝗛𝗔𝗛🤣🤣",
    "𝗦𝗨𝗡 𝗦𝗨𝗡 𝗦𝗨𝗔𝗥 𝗞𝗘 𝗣𝗜𝗟𝗟𝗘 𝗝𝗛𝗔𝗡𝗧𝗢 𝗞𝗘 𝗦𝗢𝗨𝗗𝗔𝗚𝗔𝗥 𝗔𝗣𝗡𝗜 𝗠𝗨𝗠𝗠𝗬 𝗞𝗜 𝗡𝗨𝗗𝗘𝗦 𝗕𝗛𝗘𝗝",
    "𝗔𝗕𝗘 𝗦𝗨𝗡 𝗟𝗢𝗗𝗘 𝗧𝗘𝗥𝗜 𝗕𝗘́𝗛𝗘𝗡 𝗞𝗔 𝗕𝗛𝗢𝗦𝗗𝗔 𝗙𝗔𝗔𝗗 𝗗𝗨𝗡𝗚𝗔",
    "𝗧𝗘𝗥𝗜 𝗠𝗔́𝗔̀𝗞𝗢 𝗞𝗛𝗨𝗟𝗘 𝗕𝗔𝗝𝗔𝗥 𝗠𝗘 𝗖𝗛𝗢𝗗 𝗗𝗔𝗟𝗔 🤣🤣💋",
]


@app.on_message(
    filters.command("gali", prefixes=["/", "!", "%", ",", "", ".", "@", "#"])
    & filters.private)
async def help(client: Client, message: Message):
    await message.reply_text(
        text = random.choice(GALI),
        
    )


@app.on_message(
    filters.command("gali", prefixes=["/", "!", "%", ",", "", ".", "@", "#"])
    & filters.group )
async def help(client: Client, message: Message):
    await message.reply_text("**این دستور تنها برای پیام خصوصی به من ارسال شود، آن را به یک پیام خصوصی تبدیل کنید و مجدداً ارسال کنید./gali.**")
