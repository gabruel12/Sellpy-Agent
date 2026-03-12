
from database import models
from database.connect import Sessionlocal

def create_goal(title, amount, until_date):

    db = Sessionlocal()

    goal = models.EarningsTarget(
        title=title,
        amount=amount,
        until_date=until_date
    )
    db.add(goal)
    db.commit()
    db.close()

    return "Meta criada com sucesso!"