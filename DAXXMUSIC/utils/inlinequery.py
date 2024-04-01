from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="مکث",
            description=f"جریان پخش فعلی را در چت تصویری یا ویسکال متوقف کنید",
            thumb_url="https://metaraz.ir/wp-content/uploads/2022/07/Music.jpg",
            input_message_content=InputTextMessageContent("مکث"),
        ),
        InlineQueryResultArticle(
            title="Pause",
            description=f"جریان پخش فعلی را در چت تصویری یا ویسکال متوقف کنید",
            thumb_url="https://shadmag.com/wp-content/uploads/2022/07/getty_522795473_307391-1920x930-1-1536x794.jpg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="ادامه",
            description=f"ادامه پخش موسیقی متوقف شده در ویسکال یا چت تصویری",
            thumb_url="https://www.beytoote.com/images/stories/fun/photo-essay-music-9.jpg",
            input_message_content=InputTextMessageContent("ادامه"),
        ),
        InlineQueryResultArticle(
            title="بعدی",
            description=f"رد کردن موزیک در حال پخش و پلی آهنگ بعدی در ویسکال",
            thumb_url="https://saziha.ir/wp-content/uploads/2021/05/word-image-18.jpeg",
            input_message_content=InputTextMessageContent("بعدی"),
        ),
        InlineQueryResultArticle(
            title="پایان",
            description="پایان دادن به پخش موسیقی در حال پخش در چت تصویری یا ویسکال",
            thumb_url="https://cdn.fararu.com/files/fa/news/1402/11/26/1919912_888.jpg",
            input_message_content=InputTextMessageContent("/end"),
        ),
        InlineQueryResultArticle(
            title="تصادفی",
            description="تصادفی کردن موسیقی‌های در صف پخش/پلی لیست داخل ویسکال یا چت تصویری.",
            thumb_url="https://i1.delgarm.com/i/798/0008/12/%D8%B9%DA%A9%D8%B3%20%D9%86%D9%88%D8%B4%D8%AA%D9%87%20%D8%AC%D8%AF%DB%8C%D8%AF/61828e29e2e06.jpg",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="تکرار",
            description="تکرار پخش موسیقی در حال پخش در ویسکال یا چت تصویری.",
            thumb_url="https://shadmag.com/wp-content/uploads/2022/07/442866_909-840x462.jpg",
            input_message_content=InputTextMessageContent("تکرار 3"),
        ),
    ]
)
