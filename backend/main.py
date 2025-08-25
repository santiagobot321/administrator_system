# backend/main.py
from fastapi import FastAPI
from backend.routes import auth, equipos  # Importamos los módulos de rutas

app = FastAPI(
    title="Administrador de PCs",
    description="API para gestionar equipos, usuarios y métricas",
    version="1.0.0"
)

# Incluir routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(equipos.router, prefix="/equipos", tags=["equipos"])

# Ruta raíz
@app.get("/")
def root():
    return {"message": "🚀 Bienvenido a la API del Administrador de PCs"}
