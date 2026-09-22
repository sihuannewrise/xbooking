from fastapi import FastAPI
from api.docs import XBOOKING_DESC


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


@app.get("/", tags=["common"],)
async def root():
    """
    Корневой маршрут, подтверждающий, что API работает.
    """
    return {"message": "Добро пожаловать в API интернет-магазина!"}
