# Установка зависимостей для бэкенда и фронтенда
install:
 pip install -r backend/requirements.txt
 cd front && npm install

# Команды запуска
BACKEND_COMMAND = python backend/main.py
FRONTEND_COMMAND = npm start --prefix ./front

# Запуск Бэкенда
backend:
 @echo "Запуск бэкенда..."
 @$(BACKEND_COMMAND) &

# Запуск Фронтенда
frontend:
 @echo "Запуск фронтенда..."
 @$(BACKEND_COMMAND) &

# Правило для запуска бэкенда и фронтенда
start:
 @echo "Запуск бэкенда..."
 @$(BACKEND_COMMAND) &
 @echo "Запуск фронтенда..."
 @$(FRONTEND_COMMAND) &

# Запуск тестов для бэкенда и фронтенда
test-backend:
 cd backend && pytest

test-frontend:
 npm test --prefix ./front

# Инициализация базы данных
init-db:
 cd backend && alembic init migrations
# Создание url для sqlalchemy
DB_USER ?= user
DB_PASS ?= 12345
DB_HOST ?= 172.20.10.5
DB_PORT ?= 5432
DB_NAME ?= mydatabase

.PHONY: generate-db-url
generate-db-url:
 echo "sqlalchemy.url = postgresql://$(DB_USER):$(DB_PASS)@$(DB_HOST):$(DB_PORT)/$(DB_NAME)" > .\backend\alembic.ini

# Управление миграциями базы данных
migrate:
 cd backend && alembic upgrade
# Добавление моделки
.PHONY: add-db-models
add-db-models:
 echo 'from db.models import Base\n\ntarget_metadata = Base.metadata' >> .\backend\migrations\env.py

# Pre-commit:
pre-commit-run:
 pre-commit run --all-files

build:
 docker-compose -f docker-compose.yml build $(c)

up:
 docker-compose -f docker-compose.yml up -d $(c)

start:
 docker-compose -f docker-compose.yml start $(c)

