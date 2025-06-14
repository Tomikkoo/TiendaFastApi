from fastapi import FastAPI
from app.routers import productos
from app.database import Base, engine

app = FastAPI(title="Tienda API")

Base.metadata.create_all(bind=engine)

app.include_router(productos.router)

