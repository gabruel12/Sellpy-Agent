import time
from datetime import datetime
from database import SessionLocal
import models
from services.tasks_service import remember_task

def remind_task():

    while True:

        db = SessionLocal()
        agora = datetime.now()

        tasks = db.query(models.Tasks)\
            .filter(models.Tasks.remind_at <= agora)\
            .filter(models.Tasks.status == "pendente")\
            .all()

        for task in tasks:
            message = remember_task(task.id)
            print(message)
            task.remind_at = None

        db.commit()
        db.close()

        time.sleep(60)