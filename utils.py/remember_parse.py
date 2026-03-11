from datetime import datetime, timedelta
from database import SessionLocal

def parse_remind_time(text: str) -> datetime:
    
    now = datetime.now()
    text = text.lower()

    if "daqui a pouco" in text:
        return now + timedelta(minutes=15)
    
    if "mais tarde" in text:
        return now + timedelta(hours=2)
    
    if "daqui meia hora" in text:
        return now + timedelta(minutes=30)

    if "amanhã" in text:
        return now + timedelta(days=1)

    if "semana que vem" in text:
        return now + timedelta(days=7)
    
    return None