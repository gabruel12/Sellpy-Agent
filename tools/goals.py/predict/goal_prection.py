
from database import models 
from database.connection import SessionLocal

def predict_goal():

    remaining = goal.target_amount - goal.current_amount

    if avg_income <= 0:
        return None

    days_needed = remaining / avg_income

    return round(days_needed)