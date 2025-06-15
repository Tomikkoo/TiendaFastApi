from app.services.producto_service import guardar_producto

def crear_producto(producto_data: dict):
    return guardar_producto(producto_data)
