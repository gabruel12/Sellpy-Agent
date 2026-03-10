from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import declarative_base
from database.connect import engine

Base = declarative_base()

class Transaction:
    __tablename__ = "transactions"
    id          = Column(Integer, primary_key=True, index=True)
    date        = COlumn(String)
    description = Column(String)
    type        = Column(String)
    value       = Column(Float)

Base.metadata.create_all(bind=engine)