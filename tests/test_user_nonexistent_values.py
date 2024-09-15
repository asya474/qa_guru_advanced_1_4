from model.reqres import Reqres
import pytest
from http import HTTPStatus
@pytest.mark.parametrize("user_id", [99])
def test_user_nonexistent_values(env, user_id):
    result_response_user_nonexistent_values = Reqres(env).get_user({user_id})
    assert result_response_user_nonexistent_values.status_code == HTTPStatus.NOT_FOUND