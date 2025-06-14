from fastapi import FastAPI
from app.routers.productos import router as productos_router

app = FastAPI()

app.include_router(productos_router)

