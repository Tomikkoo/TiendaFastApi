## Tienda API - CRUD con FastAPI

Este proyecto es una API desarrollada con **FastAPI** para gestionar productos de una tienda. Permite realizar operaciones CRUD completas (crear, leer, actualizar y eliminar), utilizando SQLite como base de datos.

---

## Tecnologías utilizadas

- Python 3.10+
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn
- python-dotenv

---

## Estructura del proyecto

```
TiendaFastAPI/
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── crud.py
│   ├── database.py
│   ├── logs.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
├── .env
├── requirements.txt
└── README.md
```

---

##  Instalación y ejecución

### 1. Crear y activar entorno virtual

```bash
python -m venv venv
venv\Scripts\activate       # En Windows
# source venv/bin/activate  # En Linux/Mac
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

O manualmente:

```bash
pip install fastapi sqlalchemy uvicorn python-dotenv
```

### 3. Ejecutar el servidor

```bash
uvicorn app.main:app --reload
```

### 4. Acceder desde el navegador

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Variables de entorno

En el archivo `.env`:

```
DATABASE_URL=sqlite:///./tienda.db
```

---

## Endpoints esperados 

- `GET /productos/` → Lista todos los productos
- `GET /productos/{id}` → Devuelve un producto
- `POST /productos/` → Crea un producto
- `PUT /productos/{id}` → Actualiza un producto
- `DELETE /productos/{id}` → Elimina un producto

---
