from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_list_messages():
    r = client.get("/api/messages")
    assert r.status_code == 200
    assert isinstance(r.json(), list)


def test_create_and_get():
    r = client.post("/api/messages", json={"content": "hi"})
    assert r.status_code == 201
    new_id = r.json()["id"]

    r = client.get(f"/api/messages/{new_id}")
    assert r.status_code == 200
    assert r.json()["content"] == "hi"


def test_get_missing_message():
    r = client.get("/api/messages/999999")
    assert r.status_code == 404


def test_delete_missing_message():
    r = client.delete("/api/messages/999999")
    assert r.status_code == 404
