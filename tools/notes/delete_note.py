
from database import models
from database.connect import SessionLocal

def delete_note(note_id):

    db = SessionLocal()

    note = db.query(models.Notes).filter(models.Notes.id == note_id).first()
    if not note:
        db.close()
        return "Nota não encontrada"
        
    db.delete(note)
    db.commit()
    db.close()

    return "Nota deletada com sucesso!"