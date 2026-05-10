# Берем легкую официальную версию Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл с зависимостями и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь остальной код проекта
COPY . .

# Команда для запуска нашего сервера
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]