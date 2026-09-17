from fastapi import FastAPI

from app.routers import categories, products


app = FastAPI(
    title="FastAPI Интернет-магазин",
    version="1.0.0",
)

app.include_router(categories.router)
app.include_router(products.router)


@app.get("/", tags=["common"],)
async def root():
    """
    Корневой маршрут, подтверждающий, что API работает.
    """
    return {"message": "Добро пожаловать в API интернет-магазина!"}
