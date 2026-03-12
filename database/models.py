from sqlalchemy import Column, Integer, String, Float, Date, DateTime
from sqlalchemy.orm import declarative_base
from database.connect import engine
from datetime import datetime, timedelta
from connect import SessionLocal

Base = declarative_base()

class Transaction:
    __tablename__ = "transactions"
    id          = Column(Integer, primary_key=True, index=True)
    date        = Column(String)
    description = Column(String)
    type        = Column(String)
    value       = Column(Float)

class Tasks:
    __tablename__ = "tasks"
    id          = Column(Integer, primary_key=True, index=True)
    title       = Column(String)
    description = Column(String)
    status      = Column(String)
    remind      = Column(DateTime, nullable=True)

class Notes:
    __tablename__ = "notes"
    id          = Column(Integer, primary_key=True, index=True)
    title       = Column(String)
    content     = Column(String)

class EarningsTarget:
    __tablename__ = "earnings_targets"
    id             = Column(Integer, primary_key=True, index=True)
    title          = Column(String)
    amount         = Column(Float)
    current_amount = Column(Float, default=0)
    until_date     = Column(DateTime)

Base.metadata.create_all(bind=engine)

def auto_remind_task(task_id, minutes=60):

    db = SessionLocal()
    task = db.query(Tasks).filter(Tasks.id == task_id).first()

    if not task:
        db.close()
        return "Tarefa não encontrada"

    remind_time = datetime.now() + timedelta(minutes=minutes)
    task.remind = remind_time

    db.commit()
    db.close()

    return remind_time