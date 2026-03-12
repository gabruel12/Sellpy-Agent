
from database import models
from database.connect import Sessionlocal
from average_daily import average_daily_income
from goal_prediction import predict_goal

def goal_forecast():

    db = Sessionlocal()
    goal = db.query(models.Goals).first()
    avg_income = average_daily_income(db)
    days = predict_goal(goal, avg_income)
    db.close()

    if days:
        return f"Se continuar assim, você alcança sua meta em aproximadamente {days} dias."
    
    return "Ainda não há dados suficientes para prever sua meta."