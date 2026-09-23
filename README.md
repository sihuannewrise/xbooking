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
| POST | /web/messages | форма создания сообщения |
| GET | /web/docs/{name} | страница с рендером markdown |

Swagger: http://127.0.0.1:8000/docs
Документация: http://127.0.0.1:8000/web/docs/xbooking

## Структура

.
├── api
│   ├── crud.py
│   ├── docs
│   │   └── xbooking.md
│   ├── docs_loader.py
│   ├── __init__.py
│   └── routes.py
├── LICENSE
├── main.py
├── README.md
├── requirements.txt
└── web
    ├── __init__.py
    ├── pages.py
    ├── static
    │   ├── css
    │   │   └── style.css
    │   └── favicon.ico
    ├── templates
    │   ├── base.html
    │   ├── create.html
    │   ├── detail.html
    │   ├── docs.html
    │   ├── error.html
    │   └── index.html
    └── templating.py
