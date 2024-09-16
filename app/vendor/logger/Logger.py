from datetime import datetime

class Logger:
    def __init__(self, file_prefix='log'):
        date = datetime.now().strftime('%Y-%m-%d')
        self.filename = f'{file_prefix}_{date}.log'


    def _write_log(self, message: str, level: str):
        with open(f'config/logs/{self.filename}', 'a', encoding='utf-8') as file:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            file.write(f'[{timestamp}|{level}] {message}\n')

    def log(self, message: str, level='info'):
        self._write_log(message, level)
