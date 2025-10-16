import sqlite3
from sqlite3 import Connection, Error

def connect_database(db_file: str) -> Connection | None:
    """Conecta a la base de datos SQLite y devuelve la conexión"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as err:
        print(f"Error: {err}")
    return conn

def create_table(conn: Connection):
    """Crea la tabla 'tasks' si no existe"""
    try:
        sql = """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            done BOOLEAN NOT NULL DEFAULT 0
        )
        """
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
    except Error as err:
        print(f"Error al crear la tabla: {err}")
