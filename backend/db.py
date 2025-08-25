import mysql.connector

# Configuración centralizada de la DB
Conexion = {
    "user": "root",
    "host": "localhost",
    "password": "1234",
    "database": "proyectoIntegrador",
    "port": 3306
}

# Función para abrir una nueva conexión
def get_connection():
    return mysql.connector.connect(**Conexion)
