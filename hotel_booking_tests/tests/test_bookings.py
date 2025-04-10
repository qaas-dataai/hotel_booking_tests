import requests
from utils.payloads import valid_booking_payload

def test_create_booking(base_url, headers):
    """
    Test creating a new booking with valid user_id and room_id.

    Verifies:
    - Booking is created successfully.
    - Response status code is 201 (Created).
    - Response contains a booking ID.
    """
    payload = valid_booking_payload(user_id=1, room_id=1)
    response = requests.post(f"{base_url}/bookings", json=payload, headers=headers)
    assert response.status_code == 201
    assert "id" in response.json().get("data", {})

def test_get_booking_invalid_id(base_url):
    """
    Test retrieving a booking with an invalid/non-existent booking ID.

    Verifies:
    - Response status code is 404 (Not Found).
    """
    response = requests.get(f"{base_url}/bookings/99999")
    assert response.status_code == 404

def test_update_booking_status(base_url, headers):
    """
    Test updating the status of an existing booking.

    Verifies:
    - Booking status is updated successfully.
    - Acceptable response status codes are 200 (Success) or 404 (Booking not found).
    """
    payload = {"status": "confirmed"}
    response = requests.patch(f"{base_url}/bookings/1", json=payload, headers=headers)
    assert response.status_code in [200, 404]

def test_cancel_booking(base_url, headers):
    """
    Test cancelling an existing booking.

    Verifies:
    - Booking is cancelled successfully.
    - Acceptable response status codes are 200 (Success) or 404 (Booking not found).
    """
    response = requests.patch(f"{base_url}/bookings/1/cancel", headers=headers)
    assert response.status_code in [200, 404]

def test_delete_booking(base_url, headers):
    """
    Test deleting an existing booking.

    Verifies:
    - Booking is deleted successfully.
    - Acceptable response status codes are 200 (Success) or 404 (Booking not found).
    """
    response = requests.delete(f"{base_url}/bookings/1", headers=headers)
    assert response.status_code in [200, 404]

def test_create_booking_invalid_dates(base_url, headers):
    """
    Test creating a booking where the check-in date is after the check-out date.

    Verifies:
    - API rejects the booking with a 400 (Bad Request) status code.
    """
    payload = {
        "user_id": 1,
        "room_id": 1,
        "check_in_date": "2025-04-30",
        "check_out_date": "2025-04-20",
        "guests": 2
    }
    response = requests.post(f"{base_url}/bookings", json=payload, headers=headers)
    assert response.status_code == 400
