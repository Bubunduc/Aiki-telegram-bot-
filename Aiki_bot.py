import telebot
from telebot import types
from telebot.types import ReplyKeyboardMarkup
from youtubesearchpython import Search
import requests
import time
bot = telebot.TeleBot('1933230063:AAGUBfqzOK5rnMAm8PAPho6QtwaFgS7NfAQ')
@bot.message_handler(commands=['start'])
def Startbot(message):# Name for function not important
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Поиск техники')
    button2 = types.KeyboardButton('Айкимудрость')
    markup.add(button1,button2)
    bot.send_message(message.chat.id, "Привет {}  {}! С помощь меня ты сможешь быстро и лекго найти нужную тебе технику айкидо,чтобы узнать подробнее напишите /help".format(message.chat.first_name,message.chat.last_name),reply_markup=markup)
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,'Кнопка "Айкимудрость" генерирует случайную мудрость по теме айкидо c помощью сервиса балабоба')
    bot.send_message(message.chat.id,'С помощью кнопки "Поиск техники" можно получить необходимую вам технику(Желательно вводить название на английском)')
@bot.message_handler(content_types=['text'])
# the function will be executed when sending any message to the bot, since handler with text type specified if message.text is important
def some(message):
    if message.chat.type == 'private':
        if message.text == 'Поиск техники':
            msg = bot.send_message(message.chat.id, 'Что будем искать?')
            bot.register_next_step_handler(msg, some_1)
        if message.text == 'Айкимудрость':
            bot.send_message(message.chat.id,'Составляю...')
            time.sleep(3)
            API_URL = 'https://yandex.ru/lab/api/yalm/text3'
            data = {"query": "Айкидо", "intro": 11, "filter": 1}
            request = requests.post(url=API_URL, json=data)
            request = request.json()
            bot.send_message(message.chat.id, request['query'] + request['text'])


def some_1(message):
    print(f'на предыдущем шаге введено {message.text}')
    bot.send_message(message.chat.id, Search(message.text, limit=1).result()['result'][0]['link'])


bot.polling(none_stop=True)

