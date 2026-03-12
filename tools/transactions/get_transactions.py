
from openai import OpenAI
import os

from database import models
from database.connect import SessionLocal
from database.models import Transaction

def get_transactions():

    db = SessionLocal()
    data = db.query(Transaction).all()
    db.close()
    return data
