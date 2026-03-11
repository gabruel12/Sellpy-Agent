
from database import models
from database.connection import SessionLocal

def update_goals(value):

    db = SessionLocal()

    goals = db.query(models.EarningsTarget).all()

    for goal in goals:

        goal.current_amount += value

    db.commit()
    db.close()

def goal_progress(goal):

    progress = (goal.current_amount / goal.target_amount) * 100
    remaining = goal.target_amount - goal.current_amount

    return progress, remaining