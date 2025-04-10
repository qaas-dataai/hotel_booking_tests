import requests
import pytest
from utils.payloads import valid_user_payload, valid_booking_payload


"""
These tests ensures that contract definition is still intact for every push
This checks against correct expecteted contract/file spec vetted values versus what is coming back
from API response - currently file spec is incorrect"""

@pytest.mark.contract
def test_hotels_list_schema(base_url):
    """
    Contract Test:
    Validate schema for GET /hotels
    """
    response = requests.get(f"{base_url}/hotels")
    assert response.status_code == 200
    hotels = response.json().get("data", [])
    if hotels:
        hotel = hotels[0]
        expected_fields = [
            "id", "name", "location", "description",
            "images", "amenities", "rating", "priceRange"
        ]
        for field in expected_fields:
            assert field in hotel, f"Missing field {field} in hotel"
        assert isinstance(hotel["images"], list)
        assert isinstance(hotel["priceRange"], dict)

@pytest.mark.contract
def test_hotel_by_id_schema(base_url):
    """
    Contract Test:
    Validate schema for GET /hotels/{id}
    """
    response = requests.get(f"{base_url}/hotels/1")
    if response.status_code == 200:
        hotel = response.json().get("data", {})
        assert isinstance(hotel, dict)
        expected_fields = [
            "id", "name", "location", "description",
            "images", "amenities", "rating", "priceRange"
        ]
        for field in expected_fields:
            assert field in hotel, f"Missing field {field} in hotel"

@pytest.mark.contract
def test_create_user_and_schema(base_url, headers):
    """
    Contract Test:
    Create a user and validate response schema
    """
    payload = valid_user_payload()
    response = requests.post(f"{base_url}/users", json=payload, headers=headers)
    assert response.status_code in [201, 409]  # 409 if user already exists
    if response.status_code == 201:
        user = response.json().get("data", {})
        expected_fields = ["id", "first_name", "last_name", "email", "phone", "created_at", "updated_at"]
        for field in expected_fields:
            assert field in user, f"Missing field {field} in user"

@pytest.mark.contract
def test_get_user_by_id_schema(base_url):
    """
    Contract Test:
    Validate schema for GET /users/{id}
    """
    response = requests.get(f"{base_url}/users/1")
    if response.status_code == 200:
        user = response.json().get("data", {})
        expected_fields = ["id", "first_name", "last_name", "email", "phone", "created_at", "updated_at"]
        for field in expected_fields:
            assert field in user, f"Missing field {field} in user"

@pytest.mark.contract
def test_create_booking_and_schema(base_url, headers):
    """
    Contract Test:
    Create a booking and validate response schema
    """
    payload = valid_booking_payload(user_id=1, room_id=1)
    response = requests.post(f"{base_url}/bookings", json=payload, headers=headers)
    assert response.status_code in [201, 400]  # 400 if bad data
    if response.status_code == 201:
        booking = response.json().get("data", {})
        expected_fields = [
            "id", "user_id", "hotel_id", "room_id", "check_in_date",
            "check_out_date", "guests", "total_price", "status",
            "created_at", "updated_at"
        ]
        for field in expected_fields:
            assert field in booking, f"Missing field {field} in booking"

@pytest.mark.contract
def test_get_booking_by_id_schema(base_url):
    """
    Contract Test:
    Validate schema for GET /bookings/{id}
    """
    response = requests.get(f"{base_url}/bookings/1")
    if response.status_code == 200:
        booking = response.json().get("data", {})
        expected_fields = [
            "id", "user_id", "hotel_id", "room_id", "check_in_date",
            "check_out_date", "guests", "total_price", "status",
            "created_at", "updated_at"
        ]
        for field in expected_fields:
            assert field in booking, f"Missing field {field} in booking"

@pytest.mark.contract
def test_update_booking_status_schema(base_url, headers):
    """
    Contract Test:
    Update booking status and validate success response
    """
    payload = {"status": "confirmed"}
    response = requests.patch(f"{base_url}/bookings/1", json=payload, headers=headers)
    assert response.status_code in [200, 404]

@pytest.mark.contract
def test_cancel_booking_schema(base_url, headers):
    """
    Contract Test:
    Cancel booking and validate success response
    """
    response = requests.patch(f"{base_url}/bookings/1/cancel", headers=headers)
    assert response.status_code in [200, 404]

@pytest.mark.contract
def test_delete_booking_schema(base_url, headers):
    """
    Contract Test:
    Delete booking and validate success response
    """
    response = requests.delete(f"{base_url}/bookings/1", headers=headers)
    assert response.status_code in [200, 404]
