# Приложение для математического моделирования взаимодействия ВИЧ и иммунной системы человека

## Запуск с Docker

1. Установите [Docker](https://www.docker.com/products/docker-desktop/)
2. Склонируйте репозиторий
3. Выполните в терминале:

```bash
docker-compose up -d
```

## Запуск без Docker

### Запуск backend

1. Клонировать проект 

2. ```bash 
   cd backend
   ```
3. Создать виртуальное окружение
```bash
    python -m venv venv
   ```
4. Установка зависимостей
```bash
    pip install -r requirements.txt
   ```
5. Запуск сервера
```bash
   uvicorn app.api:app --reload --port 8000
```

### Запуск frontend

1. ```bash
   cd frontend

2. Установка зависимостей
    ```bash
    npm install
    ```
3. Запуск дев-сервера
    ```bash
   npm run dev
   ```

Фронтенд запустится по адресу: http://127.0.0.1:5173 (но лучше проверить порт в консоли, возможно там порт 5174, 5175)