# Используем официальный образ Python 3.12
FROM python:3.12-slim

# Устанавливаем необходимые системные пакеты (если нужно)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файлы приложения в контейнер
COPY . /app

# Устанавливаем зависимости из requirements.txt
RUN pip install -r requirements.txt

# Команда запуска приложения (замените на свою команду)
CMD ["python", "main.py"]