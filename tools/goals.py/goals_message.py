
from datetime import datetime
from database.connect import SessionLocal

def goals_message(value):

    db = SessionLocal()
    goal = db.query(models.Goals).first()
    progress, remaining = goal_progress(goal)
    db.close()

    return f"""
💰 Entrada registrada: R${value}

🎯 Meta: {goal.title}

📊 Progresso: {progress:.1f}%
💸 Faltam: R${remaining}
"""