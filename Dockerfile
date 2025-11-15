# Используем slim-образ Python
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Кэшируем установку зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код
COPY . .

# Запуск от не-root пользователя (рекомендуется в продакшн)
RUN addgroup --system app && adduser --system --ingroup app app || true
USER app

# Порт по умолчанию; Render передаёт PORT в окружении
EXPOSE 10000

# Используем gunicorn + uvicorn worker; PORT разрешается из окружения
ENTRYPOINT ["sh","-c","gunicorn -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:${PORT:-10000} --workers ${WEB_CONCURRENCY:-2} --timeout 120"]
