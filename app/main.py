from fastapi import FastAPI
from app.routers import producto

app = FastAPI()

app.include_router(producto.router)

