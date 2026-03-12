
import datetime

from database import models
from database.connect import Sessionlocal

def goals_complete():

    db = Sessionlocal()
    goals = db.query(models.Goals).filter(models.Goals.end_date <= datetime.now()).all()
    
    db.delete(goals)
    db.commit()

    return "🎉 Parabéns! Você completou sua meta!"