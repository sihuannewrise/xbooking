from fastapi import FastAPI
from app.docs import XBOOKING_DESC




app = FastAPI(
    title="FastAPI Интернет-магазин",
    summary="Corp application for booking of a meeting room",
    description=XBOOKING_DESC,
    version="1.0.0",
)


@app.get("/", tags=["common"],)
async def root():
    """
    Корневой маршрут, подтверждающий, что API работает.
    """
    return {"message": "Добро пожаловать в API интернет-магазина!"}
