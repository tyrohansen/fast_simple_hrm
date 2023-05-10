from fastapi.testclient import TestClient

from core.main import app

client = TestClient(app)

def test_list_users():
    response = client.get("/api/v1/users/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}