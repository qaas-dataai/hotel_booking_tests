
# 🔧 Detailed Bug Reports

---

# Table of Contents
- [HACKBUG-1: Missing Data Folder](#hackbug-1-missing-data-folder)
- [HACKBUG-2: User Creation Fails Despite Valid Inputs](#hackbug-2-user-creation-fails-despite-valid-inputs)
- [HACKBUG-3: Incorrect Responses for Booking Creation with Invalid Inputs](#hackbug-3-incorrect-responses-for-booking-creation-with-invalid-inputs)
- [HACKBUG-4: File Specification Attribute Name Mismatch](#hackbug-4-file-specification-attribute-name-mismatch)
- [HACKBUG-5: File Specification Data Type Mismatch](#hackbug-5-file-specification-data-type-mismatch)
- [HACKBUG-6: Unable to Create Booking Using File Spec and Payload Examples](#hackbug-6-unable-to-create-booking-using-file-spec-and-payload-examples)
- [HACKBUG-7: PATCH Booking Not Implemented](#hackbug-7-patch-booking-not-implemented)
- [HACKBUG-8: User Object Contract Mismatch](#hackbug-8-user-object-contract-mismatch)
- [HACKBUG-9: Booking Cancellation Works Fine](#hackbug-9-booking-cancellation-works-fine)

---

## HACKBUG-1: Missing Data Folder

**Description:**  
The required `data` folder is missing in the project repository, preventing tests and payload loading.

**Steps to Reproduce:**
1. Clone the project repository.
2. Check for the `data` folder.

**Expected Result:**  
The project should contain a `data` folder with required files.

**Actual Result:**  
`data` folder is missing.

**Additional Info:**  
Manual folder creation may be needed to proceed.

---

## HACKBUG-2: User Creation Fails Despite Valid Inputs

**Description:**  
Creating a user with all required fields fails, returning a "Missing required fields" error.

**Steps to Reproduce:**
1. Send a POST request to `/api/users` with payload:
   ```json
   {
     "name": "John Doe",
     "email": "john.doe@example.com",
     "phone": "+1234567890"
   }
   ```

**Expected Result:**  
User should be created successfully.

**Actual Result:**  
```json
{
  "success": false,
  "error": "Missing required fields"
}
```

**Additional Info:**  
No additional fields mentioned in spec or API documentation.

---

## HACKBUG-3: Incorrect Responses for Booking Creation with Invalid Inputs

**Description:**  
Booking creation with invalid inputs shows unclear or misleading error responses.

**Steps to Reproduce:**
1. Send an invalid booking creation request (e.g., missing mandatory fields).

**Expected Result:**  
API should return specific validation errors indicating what fields are missing or incorrect.

**Actual Result:**  
API returns generic or incorrect error messages.

**Additional Info:**  
Detailed field-level validation is missing.

---

## HACKBUG-4: File Specification Attribute Name Mismatch

**Description:**  
Attribute names in API responses do not match those in the file specification.

**Steps to Reproduce:**
1. Create a user or booking.
2. Compare API response attributes against the file spec.

**Expected Result:**  
Attribute names should match exactly, e.g., `userId` in both API and spec.

**Actual Result:**  
API returns attributes like `user_id` instead of `userId`.

**Additional Info:**  
Could lead to contract test failures if unchecked.

---

## HACKBUG-5: File Specification Data Type Mismatch

**Description:**  
API returns fields with data types different from the specification.

**Steps to Reproduce:**
1. Create a booking.
2. Observe the `roomid` field in the response.

**Expected Result:**  
`roomid` should be a string.

**Actual Result:**  
`roomid` is returned as an integer.

**Additional Info:**  
Could cause integration issues with clients expecting specific types.

---

## HACKBUG-6: Unable to Create Booking Using File Spec and Payload Examples

**Description:**  
Example payloads provided in file spec do not work as-is, and code updates were needed.

**Steps to Reproduce:**
1. Use payload examples from the file spec to create a booking.

**Expected Result:**  
Bookings should be created successfully using example payloads.

**Actual Result:**  
Booking creation fails with errors until code changes are made.

**Additional Info:**  
Examples may be outdated or incorrect.

---

## HACKBUG-7: PATCH Booking Not Implemented

**Description:**  
PATCH method is not implemented for updating a booking.

**Steps to Reproduce:**
1. Send a PATCH request to `/api/bookings/1`.

**Expected Result:**  
Booking details should be updated.

**Actual Result:**  
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Error</title>
</head>
<body>
  <pre>Cannot PATCH /api/bookings/1</pre>
</body>
</html>
```

**Additional Info:**  
PATCH route needs to be implemented in backend code.

---

## HACKBUG-8: User Object Contract Mismatch

**Description:**  
API returns `first_name` and `last_name` separately instead of a single `name` field as per spec.

**Steps to Reproduce:**
1. Create or retrieve a user.
2. Review the structure of the returned user object.

**Expected Result:**  
User object should have a single `name` field.

**Actual Result:**  
User object has two separate fields: `first_name` and `last_name`.

**Additional Info:**  
This causes contract test failures.

---



---

# 🔥 Summary Table

| Bug ID     | Title                                     | Status          |
|------------|-------------------------------------------|-----------------|
| HACKBUG-1  | Missing Data Folder                       | Open            |
| HACKBUG-2  | User Creation Fails Despite Valid Inputs  | Open            |
| HACKBUG-3  | Incorrect Responses for Booking Creation  | Open            |
| HACKBUG-4  | File Spec Attribute Name Mismatch         | Open            |
| HACKBUG-5  | File Spec Data Type Mismatch              | Open            |
| HACKBUG-6  | Unable to Create Booking with File Spec   | Open            |
| HACKBUG-7  | PATCH Booking Not Implemented             | Open            |
| HACKBUG-8  | User Object Contract Mismatch             | Open            |
| HACKBUG-9  | Booking Cancellation Works Fine           | Passed ✅       |
