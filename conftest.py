import pytest
import requests

BASE_URL = "https://petstore.swagger.io/v2"


@pytest.fixture
def base_url():
    return BASE_URL


@pytest.fixture
def pet_data():
    return {
        "id": 0,
        "category": {"id": 1, "name": "dogs"},
        "name": "Rex",
        "photoUrls": ["http://example.com/rex.jpg"],
        "tags": [{"id": 1, "name": "friendly"}],
        "status": "available"
    }
