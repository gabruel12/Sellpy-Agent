
from openai import OpenAI
import os

def get_transactions():

    db = SessionLocal()
    data = db.query(Transaction).all()
    db.close()
    return data
