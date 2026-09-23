from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_list_messages():
    r = client.get("/api/messages")
    assert r.status_code == 200
    assert isinstance(r.json(), list)
