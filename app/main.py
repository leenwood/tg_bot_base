from vendor.app.App import App
from vendor.logger.Logger import Logger


def init_logger():
    return Logger()

def init_app(mode: str, token: str, logger: Logger):
    return App(mode, token, logger)

if __name__ == '__main__':
    logger = init_logger()

    print("logger loaded")

    app = init_app('debug', 'token', logger)

    print("app loaded")

    app.start()