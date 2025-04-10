import requests
from utils.payloads import valid_user_payload

def test_create_user(base_url, headers):
    payload = valid_user_payload()
    response = requests.post(f"{base_url}/users", json=payload, headers=headers)
    assert response.status_code == 201
    assert "id" in response.json().get("data", {})

def test_get_user_invalid_id(base_url):
    response = requests.get(f"{base_url}/users/99999")
    assert response.status_code == 404

def test_create_user_missing_fields(base_url, headers):
    payload = {"first_name": "John"}
    response = requests.post(f"{base_url}/users", json=payload, headers=headers)
    assert response.status_code == 400
