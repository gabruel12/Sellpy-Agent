
from database import models
from database.connect import SessionLocal

def create_note(title, content):

    db = SessionLocal()

    note = models.Notes(
        title=title,
        content=content
    )
    db.add(note)
    db.commit()
    db.close()

    return "Nota criada com sucesso!"