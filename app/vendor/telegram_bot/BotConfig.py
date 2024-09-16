import telebot
from telebot import types
from telebot.types import Message, CallbackQuery
import time
from vendor.logger.Logger import Logger


class BotConfig:
    """
    Класс для конфигурации бота.
    """
    def __init__(self, token: str, logger: Logger):
        self.bot = self._load_bot(token)
        self.logger = logger
        self.setup_handlers()

    def _load_bot(self, token: str) -> telebot.TeleBot:
        return telebot.TeleBot(token)

    def setup_handlers(self):
        """
        Метод для настройки обработчиков команд и сообщений.
        """
        @self.bot.message_handler(commands=['start'])
        def handle_start(message: Message):
            """
            Обработчик команды /start с добавлением кнопок.
            """
            markup1 = types.InlineKeyboardMarkup(row_width=1)
            ite1 = types.InlineKeyboardButton("пукпук💩", callback_data="1")
            ite2 = types.InlineKeyboardButton("не пукпук❌💩", callback_data="2")
            markup1.add(ite1, ite2)
            self.bot.send_message(message.chat.id, "Давай познакомимся?✨💋🥰", reply_markup=markup1)
            self.logger.log(message)

        @self.bot.message_handler(commands=['idigulyat'])
        def handle_idigulyat(message: Message):
            """
            Обработчик команды /idigulyat.
            """
            markup2 = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("прекол", url='https://a9fm.github.io/lightshot')
            markup2.add(button1)
            self.bot.send_message(message.chat.id, "тут прэкол", reply_markup=markup2)
            self.log(message)

        @self.bot.callback_query_handler(func=lambda call: True)
        def check_callback_data(call: CallbackQuery):
            """
            Обработчик нажатий на кнопки.
            """
            if call.data == "1":
                self.bot.send_message(chat_id=call.message.chat.id, text="Ураура🥰🥰🥰 держи конфетку🍬")
                time.sleep(2)
                self.bot.send_photo(chat_id=call.message.chat.id, photo="https://i.imgur.com/nHG4oPD.jpg")
            elif call.data == "2":
                self.bot.send_message(chat_id=call.message.chat.id, text="АААААААААААААААА")
                time.sleep(2)
                self.bot.send_photo(chat_id=call.message.chat.id, photo="https://i.imgur.com/PWc8vZd.jpg")

        @self.bot.message_handler(func=lambda message: True)
        def echo_message(message: Message):
            """
            Обработчик любых текстовых сообщений.
            """
            self.bot.reply_to(message, message.text)
            print("юзер:", message.chat.id, "| соо:", message.text)
            self.log(message)

    def get_bot(self):
        return self.bot