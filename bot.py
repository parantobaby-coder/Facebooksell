import os
import telebot

TOKEN = os.getenv("8996063667:AAGak9tWY_4f24JXsjzK7Auod4qk0sNy-tY")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    user = message.from_user

    text = f"""
👋 Welcome {user.first_name}!

🆔 User ID: {user.id}
👤 Name: {user.first_name}
📝 Username: @{user.username if user.username else 'Not Set'}
🌐 Language: {user.language_code}
💬 Chat ID: {message.chat.id}
"""

    bot.reply_to(message, text)

print("Bot Started...")
bot.infinity_polling(skip_pending=True)
