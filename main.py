from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from api import api_router
from web import pages_router

BASE_DIR = Path(__file__).resolve().parent


app = FastAPI(
    title = "FastAPI Интернет-магазин",
    summary = "Corp application for booking of a meeting room",
    description = XBOOKING_DESC,
    openapi_url = "/api/v1/openapi.json",
    version = "1.0.0",
    contact = {
        "name": "KNH cloud",
        "url": "https://xwick.ru",
        "email": "info@xwick.ru",
        },
    license_info = {
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
        },
    terms_of_service = "https://xwick.ru/terms/",
    root_path = "/api/v1",
)


app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "web" / "static"),
    name="static",
)

app.include_router(api_router)
app.include_router(pages_router)
