
from database import models
from database.connection import SessionLocal

def format_task(task):
    
    if not task:
        return "Tarefa não encontrada."

    return f"""
📌 Tarefa: {task.title}

📝 Descrição: {task.description}

📊 Status: {task.status}
"""