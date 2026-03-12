
from database import models
from database.connect import Sessionlocal

def get_task(task_id):

    db = Sessionlocal()
    task = db.query(models.Tasks).filter(models.Tasks.id == task_id).first()
    db.close()

    return task