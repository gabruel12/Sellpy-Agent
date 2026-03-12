import time
from datetime import datetime
from database.connect import Sessionlocal

from database import models
from tools.tasks.get_task import get_task
from tools.tasks.task_message_remind import format_task

def remind_task():

    while True:

        db = Sessionlocal()
        agora = datetime.now()

        tasks = db.query(models.Tasks)\
            .filter(models.Tasks.remind_at <= agora)\
            .filter(models.Tasks.status == "pendente")\
            .all()

        for task in tasks:
            message = format_task(task.id)
            print(message)
            task.remind_at = None

        db.commit()
        db.close()

        time.sleep(60)