
from database.connect import Sessionlocal
from database import models

def goal_progress(goal):

    progress = (goal.current_amount / goal.target_amount) * 100
    remaining = goal.target_amount - goal.current_amount

    return progress, remaining

def goals_message(value):

    db = Sessionlocal()
    goal = db.query(models.Goals).first()
    progress, remaining = goal_progress(goal)
    db.close()

    return f"""
💰 Entrada registrada: R${value}

🎯 Meta: {goal.title}

📊 Progresso: {progress:.1f}%
💸 Faltam: R${remaining}
"""