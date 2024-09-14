import time
import datetime
import telebot
from datetime import datetime
from telebot import types

token1="6649149061:AAFoKJcvKMI4RCgZ9cpuYH40snpKT-BjRa4"
bot=telebot.TeleBot(token=token1)

def log(mes):
    file = open("msg.txt", "a",encoding='utf-8')
    file.write('\n'+"["+str(datetime.now())+"]"+str(mes))
    file.close()

#команда старт с добавлением кнопок
@bot.message_handler(commands=['start'])
def start(message):
    markup=types.InlineKeyboardMarkup(row_width=1)
    ite1=types.InlineKeyboardButton("пукпук💩",callback_data="item1")
    ite2=types.InlineKeyboardButton("не пукпук❌💩",callback_data="item2")
    markup.add(ite1,ite2)
    msg=bot.send_message(message.chat.id,"Давай познакомимся?✨💋🥰",reply_markup=markup)
    log(message)

#должны обрабатываться кнопки но нихуя не работает почему то
@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == "item1":
            bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.msg.message_id,text="Ураура🥰🥰🥰 держи конфетку🍬")
            time.sleep(2)
            bot.send_photo(chat_id=call.message.chat.id,photo="ура.jpg")
        elif call.data=="item2":
            bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.msg.message_id,text="АААААААААААААААА")
            time.sleep(2)
            bot.send_photo(chat_id=call.message.chat.id, photo="неура.jpg")


#обработка любых других соо кроме команд
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)
    print("юзер:",message.chat.id,"| соо:",message.text)
    log(message)

while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(10)