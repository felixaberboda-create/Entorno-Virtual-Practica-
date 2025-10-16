from connect_database import connect_database

DB_NAME = "todo.db"

def add_task(title: str):
    conn = connect_database(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (title, done) VALUES (?, ?)", (title, False))
    conn.commit()
    conn.close()

def list_tasks():
    conn = connect_database(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, done FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def update_task(task_id: int, new_title: str):
    conn = connect_database(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET title = ? WHERE id = ?", (new_title, task_id))
    conn.commit()
    conn.close()

def delete_task(task_id: int):
    conn = connect_database(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

def complete_task(task_id: int):
    """Marca una tarea como completada"""
    conn = connect_database(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET done = 1 WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

def complete_task(task_id: int):
    """Marca una tarea como completada"""
    conn = connect_database(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET done = 1 WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
