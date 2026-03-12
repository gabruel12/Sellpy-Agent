
from database import models

def predict_goal(goal, avg_income):

    remaining = goal.target_amount - goal.current_amount

    if avg_income <= 0:
        return None

    days_needed = remaining / avg_income

    return round(days_needed)