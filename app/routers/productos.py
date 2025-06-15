from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services import producto_service
from app.database import get_db
from app.schemas import schemas

router = APIRouter(prefix="/productos", tags=["Productos"])

@router.get("/", response_model=list[schemas.ProductoOut])
def listar_productos(db: Session = Depends(get_db)):
    return producto_service.get_productos(db)

@router.get("/{id}", response_model=schemas.ProductoOut)
def obtener_producto(id: int, db: Session = Depends(get_db)):
    producto = producto_service.get_producto(db, id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@router.post("/", response_model=schemas.ProductoOut)
def crear_producto(producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    return producto_service.create_producto(db, producto)

@router.put("/{id}", response_model=schemas.ProductoOut)
def actualizar_producto(id: int, update: schemas.ProductoCreate, db: Session = Depends(get_db)):
    producto = producto_service.get_producto(db, id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto_service.update_producto(db, producto, update)

@router.delete("/{id}")
def eliminar_producto(id: int, db: Session = Depends(get_db)):
    producto = producto_service.delete_producto(db, id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"ok": True}
