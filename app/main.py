from fastapi import FastAPI
from app.routers import productos
from app.database import Base, engine

app = FastAPI(title="Tienda API")

# Crear tablas
Base.metadata.create_all(bind=engine)

# Incluir rutas
app.include_router(productos.router)

