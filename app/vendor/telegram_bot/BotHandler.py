from vendor.logger.Logger import Logger
from vendor.telegram_bot.BotConfig import BotConfig
import telebot
from telebot import types
from telebot.types import Message, CallbackQuery
import time


class BotHandler:
    """
    Класс для управления и взаимодействия с ботом.
    """
    def __init__(self, config: BotConfig, logger: Logger):
        """
        Инициализация класса BotHandler с экземпляром бота.
        """
        self.bot = config.get_bot()
        self.logger = logger
        self.start()

    def send_message(self, message: Message, ):
        self.bot.send_message(message.chat.id, message.text)

    def start(self):
        """
        Метод для запуска бота.
        """
        print("bot start")
        self.bot.infinity_polling()
        self.logger.log("bot start")