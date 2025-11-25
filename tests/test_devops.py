from fastapi.testclient  import TestClient
from app.main import app

client = TestClient(app)

def test_post_valid_apikey():
    response = client.post(
        "/DevOps",
        headers={"X-Parse-REST-API-Key": "2f5ae96c-b558-4c7b-a590-a501ae1c3f6c"},
        json={
            "message": "Prueba metodo post",
            "to": "Juan Felipe",
            "from_": "Melanie",
            "timeToLifeSec": 20
        }
    )
    assert response.status_code == 200
    assert "Hello Juan Felipe" in response.json()["message"]

def test_invalid_apikey():
    response = client.post(
        "/DevOps",
        headers={"X-Parse-REST-API-Key": "123123123"},
        json={}
    )
    assert response.status_code == 401

def test_invalid_method():
    response = client.get("/DevOps")
    assert response.status_code == 405
    assert response.json()["error"] == "ERROR"