
from database import models
from database.connect import SessionLocal

def edit_note(note_id, title=None, content=None):

    db = SessionLocal()

    note = db.query(models.Notes).filter(models.Notes.id == note_id).first()
    if not note:
        db.close()
        return "Nota não encontrada"
        
    if title:
        note.title = title
    if content:
        note.content = content

    db.commit()
    db.close()

    return "Nota editada com sucesso!"