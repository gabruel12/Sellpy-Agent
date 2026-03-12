
from database.connect import Sessionlocal
from database.models import Transaction

def add_transaction(date, description, type, value):

    db = Sessionlocal()

    transaction = Transaction(
        date=date,
        description=description,
        type=type,
        value=value
    )

    db.add(transaction)
    db.commit()
    db.close()
    