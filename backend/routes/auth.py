# backend/routes/auth.py
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from backend.db import get_connection
from backend.routes.utils.security import verify_password, create_access_token

router = APIRouter()

# Modelo de datos para el login
class LoginData(BaseModel):
    username: str
    password: str


# Solo login
@router.post("/login")
def login(data: LoginData):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users WHERE username = %s", (data.username,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if not user or not verify_password(data.password, user["password"]):
        raise HTTPException(status_code=401, detail="❌ Usuario o contraseña incorrectos")

    # Generamos un token JWT
    token = create_access_token({"sub": user["username"]})

    return {"access_token": token, "token_type": "bearer"}
