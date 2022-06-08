
import telebot
from main import main
import json
from telebot import types


bot = telebot.TeleBot('5253523830:AAFAOE1vp6uYOPe8IbuZ9k_nMitNbCZRNCE')


with open('bd.json', 'r') as f:
    res = json.load(f)

title_image_text = res
number = len(res)

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    k = types.InlineKeyboardMarkup(row_width=2)
    buttons = []
    for i in range(20):
        b = types.InlineKeyboardButton(title_image_text[i]['title'][:20]+"...", callback_data=str(i))
        buttons.append(b)
    for i in range(0, 20, 2):
        k.add(buttons[i], buttons[i+1])
    bot.send_message(chat_id, "Bыберите новость", reply_markup=k)
    

@bot.callback_query_handler(func=lambda call: True)
def callback_query(message):
    index = int(message.data)
    bot.send_message(message.from_user.id, title_image_text[index]["title"])
    bot.send_message(message.from_user.id, title_image_text[index]["text"])
    bot.send_photo(message.from_user.id, title_image_text[index]["image"])
    

@bot.message_handler(content_types=['text'])
def bla_bla(message):
    chat_id = message.chat.id
    for y in range(21):
        if message.text == y:
            bot.reply_to(message, text = title_image_text[y] )
    

bot.polling()