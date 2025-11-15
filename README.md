# MCP Core — FastAPI skeleton

Простой шаблон FastAPI приложения для MCP с Dockerfile и конфигурацией для Render.

Запуск локально (Docker):
1. Собрать образ:
   docker build -t mcp-core:local .

2. Запустить контейнер:
   docker run -e PORT=10000 -p 10000:10000 mcp-core:local

Локально (без Docker):
1. Установить зависимости:
   pip install -r requirements.txt

2. Запустить uvicorn:
   PORT=10000 uvicorn app.main:app --host 0.0.0.0 --port 10000 --reload

Развёртывание на Render:
- Репозиторий подключается к Render; .render.yaml настроен на автодеплой.
- Render создаст сервис типа Docker, использующий Dockerfile в корне.

Endpoints:
- GET /healthz — проверка статуса
- GET /api/ — пример корневого маршрута

Добавление новых маршрутов:
- Создайте модуль в app/, подключите роутеры в app.main
