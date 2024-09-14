import time
import datetime
import telebot
from datetime import datetime
from telebot import types

token1="7545888045:AAFmKfXBbRPUyteypzDWSlCX5jCY_5aZe2k"
bot=telebot.TeleBot(token=token1)

def log(mes):
    file = open("msg.txt", "a",encoding='utf-8')
    file.write('\n'+"["+str(datetime.now())+"]"+str(mes))
    file.close()

#команда старт с добавлением кнопок
@bot.message_handler(commands=['start'])
def start(message):
    markup1=types.InlineKeyboardMarkup(row_width=1)
    ite1=types.InlineKeyboardButton("пукпук💩",callback_data="1")
    ite2=types.InlineKeyboardButton("не пукпук❌💩",callback_data="2")
    markup1.add(ite1,ite2)
    bot.send_message(message.chat.id,"Давай познакомимся?✨💋🥰",reply_markup=markup1)
    log(message)

@bot.message_handler(commands=['idigulyat'])
def idigulyat(message):
    markup2 = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("прекол", url='https://a9fm.github.io/lightshot')
    markup2.add(button1)
    bot.send_message(message.chat.id,"тут прэкол",reply_markup=markup2)
    log(message)


#должны обрабатываться кнопки но РАБОТАЕТ АААААААА, но пришлось убрать редактирование прошлого сообщение
@bot.callback_query_handler(func=lambda call: True)
def check_callback_data(call):
        if call.data == "1":
            bot.send_message(chat_id=call.message.chat.id,text="Ураура🥰🥰🥰 держи конфетку🍬")
            time.sleep(2)
            bot.send_photo(chat_id=call.message.chat.id,photo="https://imgur.com/a/1KIcDd8")
        elif call.data=="2":
            bot.send_message(chat_id=call.message.chat.id,text="АААААААААААААААА")
            time.sleep(2)
            bot.send_photo(chat_id=call.message.chat.id, photo="https://imgur.com/a/juzlon9")



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
