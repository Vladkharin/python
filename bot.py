import telebot

bot = telebot.TeleBot('5034420681:AAG26d1IjF4oPWhtElbrGCNQArbSX0nBvN0')


@bot.message_handler(commands=['start'])

def start(message):
    bot.send