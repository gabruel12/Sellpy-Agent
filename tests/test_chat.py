from fastapi.testclient import TestClient
from main import app
import main

client = TestClient(app)

def fake_agent(message):
    return "resposta"

def test_chat_route():

    main.sellpy_agent = fake_agent
    response = client.post("/chat", json={
        "message": "oi"
    })
    assert response.status_code == 200
    assert response.json() == {
        "response": "resposta"
    }