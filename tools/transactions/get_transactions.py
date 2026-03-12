
from openai import OpenAI
import os

from database import models
from database.connect import Sessionlocal
from database.models import Transaction

def get_transactions():

    db = Sessionlocal()
    data = db.query(Transaction).all()
    db.close()
    return data
