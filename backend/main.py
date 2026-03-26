from fastapi import FastAPI

from backend.database import create_db_and_tables
from backend.routers import payment_router
from backend.routers import order_router

app = FastAPI(title="FastAPI Sandbox", version="0.1.0")


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/")
async def root():
    return {"message": "Hello World!!"}


app.include_router(payment_router.router)
app.include_router(order_router.router)
