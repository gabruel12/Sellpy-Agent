
from database import models
from database.connection import SessionLocal

def create_goal(title, amount, until_date):

    db = SessionLocal()

    goal = models.EarningsTarget(
        title=title,
        amount=amount,
        until_date=until_date
    )
    db.add(goal)
    db.commit()
    db.close()

    return "Meta criada com sucesso!"