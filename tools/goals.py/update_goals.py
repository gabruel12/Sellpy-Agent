
from database import models
from database.connect import Sessionlocal

def update_goals(value):

    db = Sessionlocal()

    goals = db.query(models.EarningsTarget).all()

    for goal in goals:

        goal.current_amount += value

    db.commit()
    db.close()