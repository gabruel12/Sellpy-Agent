from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(env_path)

from fastapi import FastAPI
from agents.sellpy_agent import sellpy_agent

app = FastAPI()

@app.post("/chat")
async def chat(data: dict):
    message = data["message"]
    response = sellpy_agent(message)
    return {"response": response}
