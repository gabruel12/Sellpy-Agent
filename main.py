from dotenv import load_dotenv
from pathlib import Path

import threading
from workers.remind_worker import remind_task

env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(env_path)

from fastapi import FastAPI
from agents.sellpy_agent import sellpy_agent

app = FastAPI()
threading.Thread(target=remind_task, daemon=True).start()

@app.get("/")
def root():
    return {"Server": "Ok"}

@app.post("/chat")
async def chat(data: dict):
    message = data["message"]
    response = sellpy_agent(message)
    return {"response": response}
