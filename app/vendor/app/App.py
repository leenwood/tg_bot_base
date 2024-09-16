from vendor.logger.Logger import Logger
from vendor.telegram_bot.BotConfig import BotConfig
from vendor.telegram_bot.BotHandler import BotHandler


class App:
    def __init__(self, env: str, token: str, logger: Logger):
        """Тут вся логика что есть в приложение"""
        self.env = env
        self.logger = logger
        self.token = token
        self.stop_application = False

    def start_bot(self):
        bot_config = BotConfig(self.token, self.logger)
        BotHandler(bot_config, self.logger)

    def start(self):
        while True:
            pass