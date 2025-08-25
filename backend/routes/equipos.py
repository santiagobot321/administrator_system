# backend/routes/equipos.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.db import get_connection

# 👉 Definimos un router, NO un FastAPI()
router = APIRouter()

# Modelo de datos
class Equipo(BaseModel):
    hostname: str
    MAC: str
    IP: str
    estado: str

# -------------------------------
# GET: Listar todos los equipos
# -------------------------------
@router.get("/")
def get_equipos():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM equipos")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

# -------------------------------
# POST: Crear un nuevo equipo
# -------------------------------
@router.post("/")
def create_equipo(equipo: Equipo):
    conn = get_connection()
    cursor = conn.cursor()

    query = "INSERT INTO equipos (hostname, MAC, IP, estado) VALUES (%s, %s, %s, %s)"
    values = (equipo.hostname, equipo.MAC, equipo.IP, equipo.estado)
    cursor.execute(query, values)
    conn.commit()

    cursor.close()
    conn.close()
    return {"message": "✅ Equipo creado exitosamente", "equipo": equipo.dict()}

# -------------------------------
# PUT: Actualizar equipo por ID
# -------------------------------
@router.put("/{id}")
def update_equipo(id: int, equipo: Equipo):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    UPDATE equipos
    SET hostname = %s, MAC = %s, IP = %s, estado = %s
    WHERE id = %s
    """
    values = (equipo.hostname, equipo.MAC, equipo.IP, equipo.estado, id)
    cursor.execute(query, values)
    conn.commit()

    if cursor.rowcount == 0:
        cursor.close()
        conn.close()
        raise HTTPException(status_code=404, detail="Equipo no encontrado")

    cursor.close()
    conn.close()
    return {"message": "✅ Equipo actualizado exitosamente", "id": id, "equipo": equipo.dict()}

# -------------------------------
# DELETE: Eliminar equipo por ID
# -------------------------------
@router.delete("/{id}")
def delete_equipo(id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM equipos WHERE id = %s", (id,))
    conn.commit()

    if cursor.rowcount == 0:
        cursor.close()
        conn.close()
        raise HTTPException(status_code=404, detail="Equipo no encontrado")

    cursor.close()
    conn.close()
    return {"message": f"🗑️ Equipo con id {id} eliminado exitosamente"}
