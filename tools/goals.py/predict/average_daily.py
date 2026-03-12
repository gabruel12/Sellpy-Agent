
from database import models
from database.connect import SessionLocal

import datetime
from datetime import datetime, timedelta

def average_daily_income(db):

    seven_days_ago = datetime.now() - timedelta(days=7)

    transactions = db.query(models.Transaction)\
        .filter(models.Transaction.type == "ganho")\
        .filter(models.Transaction.created_at >= seven_days_ago)\
        .all()

    total = sum(t.value for t in transactions)

    return total / 7