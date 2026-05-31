import telebot
import json

with open("config.json") as config_file:
    config = json.load(config_file)

TOKEN = config["token"]
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك في متجر شحن الـ UC! كيف يمكنني مساعدتك اليوم؟")

bot.polling()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك في متجر شحن الـ UC! كيف يمكنني مساعدتك اليوم؟")

bot.polling()


