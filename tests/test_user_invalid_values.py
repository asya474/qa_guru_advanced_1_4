from model.reqres import Reqres
import pytest
from http import HTTPStatus
@pytest.mark.parametrize("user_id", [-1, 0, "fafaf"])
def test_user_invalid_values(env, user_id):
    result_response_get_user = Reqres(env).get_user({user_id})
    assert result_response_get_user.get_user({user_id}) == HTTPStatus.UNPROCESSABLE_ENTITY