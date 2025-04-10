def valid_user_payload():
    return {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "phone": "+1234567890"
    }

def valid_booking_payload(user_id, room_id):
    return {
        "user_id": user_id,
        "room_id": room_id,
        "check_in_date": "2025-04-20",
        "check_out_date": "2025-04-25",
        "guests": 2
    }
