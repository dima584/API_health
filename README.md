# 🏋️‍♂️ Virtus Fit API Backend

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-009688?logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-336791?logo=postgresql)
![Redis](https://img.shields.io/badge/Redis-7-DC382D?logo=redis)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker)
![Pytest](https://img.shields.io/badge/Pytest-Testing-green?logo=pytest)

Асинхронный REST API микросервис для фитнес-ассистента Virtus Fit. Обеспечивает безопасное управление биометрическими данными пользователей, расчет статистики и кеширование сложных аналитических запросов.

## 🚀 Стек технологий

* **Веб-фреймворк:** FastAPI (асинхронная архитектура)
* **База данных:** PostgreSQL с использованием драйвера `asyncpg`
* **ORM:** SQLAlchemy 2.0 (строгая типизация)
* **Миграции:** Alembic
* **Кеширование:** Redis (для оптимизации расчетов среднего веса/пульса)
* **Тестирование:** Pytest (интеграционные тесты с `httpx` и `pytest-asyncio`)
* **Инфраструктура:** Docker & Docker Compose (полная контейнеризация)

## ⚙️ Быстрый старт (Локальный запуск)

Для запуска проекта на вашей машине вам потребуется только установленный [Docker Desktop](https://www.docker.com/products/docker-desktop/).

1. **Клонируйте репозиторий:**
   ```bash
   git clone [https://github.com/dimunyra/virtus-fit-api.git](https://github.com/dimunyra/virtus-fit-api.git)
   cd virtus-fit-api
