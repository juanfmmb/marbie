from fastapi.testclient  import TestClient
from app.main import app

client = TestClient(app)

def test_post_valid_apikey():
    login_payload = {
        "username": "admin",
        "password": "devopsapitest"
    }

    login_response = client.post("/login", json=login_payload)
    assert login_response.status_code == 200

    token = login_response.json()["access_token"]

    response = client.post(
        "/DevOps",
        headers={
            "X-Parse-REST-API-Key": "2f5ae96c-b558-4c7b-a590-a501ae1c3f6c",
            "X-JWT-KWY": f"Bearer {token}",
            "Content-Type": "application/json"
        },
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