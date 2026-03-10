from fastapi import FastAPI
from agents.sellpy_agent import sellpy_agent

app = FastAPI()

@app.post("/chat")
async def chat(data: dict):
    message = data["message"]
    response = sellpy_agent(message)
    return {"response": response}
