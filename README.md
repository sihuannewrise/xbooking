# API for booking services

# XBooking

Учебный проект на FastAPI: JSON API + HTML-страницы на Jinja2.

## Запуск

python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload

## Эндпоинты

| Метод | URL | Описание |
|-------|-----|----------|
| GET | /api/messages | список сообщений |
| POST | /api/messages | создать сообщение |
| GET | /api/messages/{id} | получить одно |
| PUT | /api/messages/{id} | обновить |
| DELETE | /api/messages/{id} | удалить |
| DELETE | /api/messages | удалить все |
| GET | /web/messages | HTML-список |
| GET | /web/messages/{id} | HTML-детали |
| GET | /web/messages/create | HTML-форма |

Swagger: http://127.0.0.1:8000/docs

## Структура

...краткое дерево...