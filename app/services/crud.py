from sqlalchemy.orm import Session
from app.schemas import schemas
from app.models import models

def get_productos(db: Session):
    return db.query(models.Producto).all()

def get_producto(db: Session, id: int):
    return db.query(models.Producto).filter(models.Producto.id == id).first()

def create_producto(db: Session, producto: schemas.ProductoCreate):
    db_p = models.Producto(**producto.dict())
    db.add(db_p); db.commit(); db.refresh(db_p)
    return db_p

def update_producto(db: Session, db_p: models.Producto, update: schemas.ProductoCreate):
    for key, val in update.dict().items():
        setattr(db_p, key, val)
    db.commit(); db.refresh(db_p)
    return db_p

def delete_producto(db: Session, id: int):
    db_p = get_producto(db, id)
    if db_p:
        db.delete(db_p)
        db.commit()
    return db_p

