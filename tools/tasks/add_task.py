
from database import models
from database.connect import Sessionlocal

def add_task(title, description, status):

    db = Sessionlocal()

    task = models.Tasks(
        title=title,
        description=description,
        status=status
    )

    db.add(task)
    db.commit()
    db.close()