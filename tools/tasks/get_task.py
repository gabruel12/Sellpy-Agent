
from database import models
from database.connection import SessionLocal

def get_task(task_id):

    db = SessionLocal()
    task = db.query(models.Tasks).filter(models.Tasks.id == task_id).first()
    db.close()

    return task