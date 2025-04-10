import requests

def test_get_all_hotels(base_url):
    response = requests.get(f"{base_url}/hotels")
    assert response.status_code == 200
    assert isinstance(response.json().get("data"), list)

def test_get_hotel_invalid_id(base_url):
    response = requests.get(f"{base_url}/hotels/99999")
    assert response.status_code == 404
