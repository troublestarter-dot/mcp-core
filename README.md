# MCP Core

Универсальное ядро MCP — автономный сервер FastAPI, обеспечивающий взаимодействие между ИИ-агентами, базами данных, файлами и внешними системами. Используется как центральный узел Родной GPT.

## Возможности

- **Управление карточками**: CRUD операции для работы с карточками/документами
- **Управление событиями**: Создание и отслеживание событий в системе
- **Управление файлами**: Загрузка, хранение и управление файлами
- **Интеграция с LangChain**: Поддержка обработки AI/ML задач
- **Подключение к базе данных**: PostgreSQL через SQLAlchemy
- **REST API**: Полноценный RESTful API с документацией
- **Развертывание**: Готовая конфигурация для деплоя на Render

## Быстрый старт

### За 3 шага:

1. **Клонируйте и установите зависимости:**
```bash
git clone https://github.com/troublestarter-dot/mcp-core.git
cd mcp-core
pip install -r requirements.txt
```

2. **Запустите сервер:**
```bash
./start.sh
```

3. **Откройте документацию API:**
Перейдите на http://localhost:8000/docs

### Локальная установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/troublestarter-dot/mcp-core.git
cd mcp-core
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Создайте файл `.env` на основе `.env.example`:
```bash
cp .env.example .env
```

4. Настройте переменные окружения в `.env`:
```env
DATABASE_URL=postgresql://user:password@localhost:5432/mcp_core
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_ORIGINS=*
FILE_STORAGE_PATH=./uploads
```

5. Запустите сервер:
```bash
uvicorn main:app --reload
```

Сервер будет доступен по адресу: http://localhost:8000

API документация: http://localhost:8000/docs

## Развертывание на Render

### Одна кнопка для деплоя

1. Форкните репозиторий на GitHub
2. Перейдите на [Render](https://render.com) и войдите в аккаунт
3. Нажмите "New +" → "Blueprint"
4. Подключите ваш GitHub репозиторий
5. Render автоматически обнаружит `render.yaml` и развернет приложение
6. Настройте DATABASE_URL в переменных окружения (можно использовать бесплатную PostgreSQL БД от Render)

### Переменные окружения на Render

- `DATABASE_URL`: URL подключения к PostgreSQL
- `SECRET_KEY`: Секретный ключ (генерируется автоматически)
- `DEBUG`: false (для production)
- `ALLOWED_ORIGINS`: Список разрешенных источников для CORS
- `FILE_STORAGE_PATH`: Путь для хранения файлов

## API Endpoints

### Карточки (Cards)

- `POST /cards/` - Создать новую карточку
- `GET /cards/` - Получить список карточек
- `GET /cards/{card_id}` - Получить карточку по ID
- `PUT /cards/{card_id}` - Обновить карточку
- `DELETE /cards/{card_id}` - Удалить карточку

### События (Events)

- `POST /events/` - Создать новое событие
- `GET /events/` - Получить список событий
- `GET /events/{event_id}` - Получить событие по ID
- `DELETE /events/{event_id}` - Удалить событие

### Файлы (Files)

- `POST /files/upload` - Загрузить файл
- `GET /files/` - Получить список файлов
- `GET /files/{file_id}` - Получить метаданные файла
- `DELETE /files/{file_id}` - Удалить файл

### Сервисные endpoints

- `GET /` - Корневой endpoint с информацией об API
- `GET /health` - Проверка здоровья сервиса

## Примеры использования

### Создание карточки

```bash
curl -X POST "http://localhost:8000/cards/" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Моя первая карточка",
    "content": "Содержание карточки",
    "metadata": {"tags": ["test", "example"]}
  }'
```

### Создание события

```bash
curl -X POST "http://localhost:8000/events/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Тестовое событие",
    "description": "Описание события",
    "event_type": "user_action",
    "metadata": {"user_id": 123}
  }'
```

### Загрузка файла

```bash
curl -X POST "http://localhost:8000/files/upload" \
  -F "file=@/path/to/your/file.txt"
```

## Структура проекта

```
mcp-core/
├── app/
│   ├── config/          # Конфигурация приложения
│   │   ├── settings.py  # Настройки
│   │   └── database.py  # Подключение к БД
│   ├── models/          # Модели данных
│   │   ├── database.py  # SQLAlchemy модели
│   │   └── schemas.py   # Pydantic схемы
│   ├── routers/         # API роутеры
│   │   ├── cards.py     # Endpoints для карточек
│   │   ├── events.py    # Endpoints для событий
│   │   └── files.py     # Endpoints для файлов
│   └── services/        # Бизнес-логика
│       └── langchain_service.py  # LangChain интеграция
├── main.py              # Точка входа приложения
├── requirements.txt     # Зависимости Python
├── render.yaml          # Конфигурация для Render
├── .env.example         # Пример файла окружения
└── README.md            # Документация

```

## Технологии

- **FastAPI**: Современный веб-фреймворк для создания API
- **SQLAlchemy**: ORM для работы с базой данных
- **PostgreSQL**: Реляционная база данных
- **Pydantic**: Валидация данных и настройки
- **LangChain**: Фреймворк для AI/ML приложений
- **Uvicorn**: ASGI сервер

## Разработка

### Установка зависимостей для разработки

```bash
pip install -r requirements.txt
```

### Запуск в режиме разработки

```bash
# Используйте скрипт start.sh
./start.sh

# Или напрямую с uvicorn
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Тестирование API

Запустите автоматические тесты для проверки работоспособности API:

```bash
# Убедитесь, что сервер запущен, затем в другом терминале:
./test_api.sh

# Или протестируйте удаленный сервер:
./test_api.sh https://your-app.onrender.com
```

## Лицензия

MIT
