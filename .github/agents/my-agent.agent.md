---
name: MCP Core Builder
description: >
  Автоматический агент для развёртывания и обновления ядра MCP. 
  Создаёт инфраструктуру FastAPI-сервера с Dockerfile, .render.yaml, 
  автодеплоем на Render и базовой структурой Rodnaya GPT.

# My Agent

Этот агент автоматически создаёт структуру файлов MCP Core:
- app_backup.py с FastAPI и хранилищем /opt/render/project/src/data/obsidian
- Dockerfile и .render.yaml для деплоя
- README с кнопкой Deploy to Render
- requirements.txt с FastAPI, Uvicorn, LangChain и зависимостями.

После активации агент готовит репозиторий для мгновенного запуска ядра MCP.
