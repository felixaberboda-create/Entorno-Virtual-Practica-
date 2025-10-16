import typer
from task import add_task, list_tasks, update_task, delete_task, complete_task

app = typer.Typer()

DB_NAME = "todo.db"

@app.command()
def initdb():
    """Crea la base de datos y la tabla"""
    conn = connect_database(DB_NAME)
    create_table(conn)
    typer.echo("✅ Base de datos inicializada.")

@app.command()
def create(title: str):
    """Crea una nueva tarea"""
    add_task(title)
    typer.echo("🆕 Tarea creada correctamente.")

@app.command()
def list():
    """Lista todas las tareas"""
    tasks = list_tasks()
    if not tasks:
        typer.echo("📭 No hay tareas registradas.")
        return
    for t in tasks:
        status = "✅" if t[2] else "❌"
        typer.echo(f"{t[0]}. {t[1]} - {status}")

@app.command()
def update(id: int, title: str):
    """Actualiza el título de una tarea"""
    update_task(id, title)
    typer.echo("✏️ Tarea actualizada correctamente.")

@app.command()
def delete(id: int):
    """Elimina una tarea"""
    delete_task(id)
    typer.echo("🗑️ Tarea eliminada correctamente.")

# ✅ Este es el comando que debes agregar, con la misma indentación
@app.command()
def complete(id: int):
    """Marca una tarea como completada"""
    complete_task(id)
    typer.echo("✅ Tarea marcada como completada.")

if __name__ == "__main__":
    app()
