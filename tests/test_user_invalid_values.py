import pytest
from http import HTTPStatus
from model.reqres import Reqres

@pytest.mark.parametrize("user_id", [-1, 0, "fafaf"])
def test_user_invalid_values(app_url, user_id):
    result_response_get_user = Reqres(env).get_user({user_id})
    assert result_response_get_user.status_code == HTTPStatus.UNPROCESSABLE_ENTITY