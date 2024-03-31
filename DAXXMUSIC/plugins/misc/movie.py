from pyrogram import Client, filters
import requests
from DAXXMUSIC import app

TMDB_API_KEY = "23c3b139c6d59ebb608fe6d5b974d888"

# تغییر دستور فرمان از "/movie" به "!فیلم"
COMMAND = "!فیلم"

# استفاده از filters.regex برای تطابق با الگوی "!فیلم"
@app.on_message(filters.regex(COMMAND))
async def movie_command(client, message):
    try:
        # استفاده از دستور split برای جدا کردن نام فیلم از پیام
        movie_name = message.text.split(COMMAND)[1].strip()

        # یافتن اطلاعات فیلم از API TMDb
        movie_info = get_movie_info(movie_name)

        # ارسال اطلاعات فیلم به عنوان پاسخ
        await message.reply_text(movie_info)
    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")

# تابع برای دریافت اطلاعات فیلم از TMDb API
def get_movie_info(movie_name):
    tmdb_api_url = f"https://api.themoviedb.org/3/search/movie"
    params = {"api_key": TMDB_API_KEY, "query": movie_name}
    
    response = requests.get(tmdb_api_url, params=params)
    data = response.json()

    if data.get("results"):
        # گرفتن اطلاعات درباره اولین فیلم در نتایج
        movie = data["results"][0]
        
        # یافتن اطلاعات جزئیات با استفاده از شناسه فیلم
        details_url = f"https://api.themoviedb.org/3/movie/{movie['id']}"
        details_params = {"api_key": TMDB_API_KEY}
        details_response = requests.get(details_url, params=details_params)
        details_data = details_response.json()
        
        # استخراج اطلاعات مربوطه
        title = details_data.get("title", "N/A")
        release_date = details_data.get("release_date", "N/A")
        overview = details_data.get("overview", "N/A")
        providers = details_data.get("providers", "N/A")
        vote_average = details_data.get("vote_average", "N/A")
        
        # استخراج نام هنرپیشگان
        cast_url = f"https://api.themoviedb.org/3/movie/{movie['id']}/credits"
        cast_params = {"api_key": TMDB_API_KEY}
        cast_response = requests.get(cast_url, params=cast_params)
        cast_data = cast_response.json()
        actors = ", ".join([actor["name"] for actor in cast_data.get("cast", [])])
        
        # استخراج کلکسیون کلی
        revenue = details_data.get("revenue", "N/A")
        
        # قالب‌بندی و برگشت اطلاعات فیلم
        info = (
            f"عنوان: {title}\n\n"
            f"تاریخ اکران: {release_date}\n\n"
            f"معرفی: {overview}\n\n"
            f"میانگین امتیاز: {vote_average}\n\n"
            f"بازیگران: {actors}\n\n"
            f"کل مجموعه: {revenue}\n\n"
            f"پلتفرم های موجود: {providers}\n"
        )
        return info
    else:
        return "فیلم یافت نشد🔍 یا درخواست به وبسرویس ناموفق بود⚠️"
