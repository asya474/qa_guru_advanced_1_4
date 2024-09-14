import pytest
import requests
from http import HTTPStatus
@pytest.mark.parametrize("user_id", [99])
def test_user_nonexistent_values(app_url, user_id):
    response = requests.get(f"{app_url}/api/users/{user_id}")
    assert response.status_code == HTTPStatus.NOT_FOUND