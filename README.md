# kulguvator-bot
Telegram kulgu bot @kulguvator_bot uchun
import telebot
import os

# Tokenni Railway'dan olamiz
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

# /start komandasi
@bot.message_handler(commands=['start'])
def start_handler(message):
    if message and message.chat and message.chat.id:
        bot.send_message(
            message.chat.id,
            "Salom! Bu @Kulguvator_bot — sizga eng kulgili videolarni yetkazuvchi bot!\n\nBuyruqlar:\n/video — Reels videosini ko‘rish\n/about — Biz haqimizda"
        )

# /video komandasi
@bot.message_handler(commands=['video'])
def video_handler(message):
    if message and message.chat and message.chat.id:
        video_url = 'https://yourdomain.com/Yana_kulishamiz_bot_video.mp4'  # Real video link bilan almashtiring
        bot.send_message(
            message.chat.id,
            f"Mana sizga kulgili video!\n{video_url}"
        )

# /about komandasi
@bot.message_handler(commands=['about'])
def about_handler(message):
    if message and message.chat and message.chat.id:
        bot.send_message(
            message.chat.id,
            "Sahifa: instagram.com/_yana_kulishamiz\nTelegram: @Exclusive5000\nReklama va hamkorlik uchun murojaat qiling."
        )

# Botni ishga tushirish
if name == "main":
    print("Bot ishga tushdi...")
    bot.infinity_polling()
