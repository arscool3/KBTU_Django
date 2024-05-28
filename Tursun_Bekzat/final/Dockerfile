# Используем базовый образ Python
FROM python:3.9

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы с зависимостями (например, requirements.txt) в контейнер
COPY requirements.txt /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем оставшиеся файлы проекта в контейнер
COPY . /app/

# Выполняем команду collectstatic для сбора статических файлов
RUN python manage.py collectstatic --noinput

# Открываем порт 8000 для доступа к контейнеру
EXPOSE 8000

# Определяем команду запуска контейнера
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "final.wsgi:application"]
