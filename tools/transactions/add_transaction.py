
from database.connection import SessionLocal
from database.models import Transaction

def add_transaction(date, description, type, value):

    db = SessionLocal()

    transaction = Transaction(
        date=date,
        description=description,
        type=type,
        value=value
    )

    db.add(transaction)
    db.commit()
    db.close()
    