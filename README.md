# hotel-api-tests

# 🏨 Hotel Booking API - Pytest Automation Framework

This repository contains API integration and contract tests for the Hotel Booking API.

---

## 📦 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/qaas-dataai/hotel_booking_tests.git
cd hotel_booking_tests
```

### 2. (Optional) Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## Running Tests

### Run All Tests
```bash
pytest
```

### Run a Specific Test File
```bash
pytest tests/test_users.py
```

### Run Only Contract (Schema) Tests
```bash
pytest -m contract
```

---

## 📄 Generate HTML Report
```bash
pytest --html=report.html --self-contained-html
```
✅ After running, open the `report.html` file in your browser to view the full test results.

---
