import telebot
import re




# Create bot

bot = telebot.TeleBot('a6873ad54d02e43ddb74bc9f0246488f45535485')

# Handler for /start command

@bot.message_handler(commands=["start"])

def start(m):

    bot.send_message(m.chat.id, 'Send Any Text')

# User message handler

@bot.message_handler(content_types=["text"])

def handle_text(message):

    bot.send_message(message.chat.id, message.text)

# Start bot

bot.polling(non_stop=True, interval=0)
