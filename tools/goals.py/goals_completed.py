
from database import models
from database.connection import SessionLocal

def goals_complete():

    db.delete(goal)
    db.commit()

    return "🎉 Parabéns! Você completou sua meta!"