import pytest

BASE_URL = "http://localhost:3000/api"

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture
def headers():
    return {"Content-Type": "application/json"}
