
from database import models
from database.connect import SessionLocal

from datetime import datetime

def check_goal_deadline():

    db = SessionLocal()
    now = datetime.now()

    goals = db.query(models.Goals).filter(models.Goals.end_date <= now).all()

    for goal in goals:
        db.delete(goal)

    db.commit()
    db.close()