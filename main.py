Python
import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        "Salom! Bu @Kulguvator_bot — sizga eng kulgili videolarni yetkazuvchi bot!\n\nBuyruqlar:\n/video — Reels videosini ko‘rish\n/about — Biz haqimizda"
    )

@bot.message_handler(commands=['video'])
def send_video(message):
    video_url = 'https://yourdomain.com/Yana_kulishamiz_bot_video.mp4'
    bot.send_message(message.chat.id, f"Mana sizga kulgili video!\n{video_url}")

@bot.message_handler(commands=['about'])
def send_about(message):
    bot.send_message(
        message.chat.id,
        "Sahifa: instagram.com/_yana_kulishamiz\nTelegram: @Exclusive5000\nReklama va hamkorlik uchun murojaat qiling."
    )

bot.infinity_polling()
