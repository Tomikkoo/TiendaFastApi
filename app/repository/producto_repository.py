from app.database import SessionLocal
from app.models.producto import Producto 

def insertar_producto(data: dict):
    db = SessionLocal()
    nuevo = Producto(**data)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo
