
from database import models
from database.connect import SessionLocal

def add_task(title, description, status):

    db = SessionLocal()

    task = models.Tasks(
        title=title,
        description=description,
        status=status
    )

    db.add(task)
    db.commit()
    db.close()