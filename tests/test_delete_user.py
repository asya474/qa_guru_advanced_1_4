from http import HTTPStatus
from model.reqres import Reqres

def test_delete_user(env):
        result_response_delete_response = Reqres(env).delete_user(2)
        assert result_response_delete_response.status_code == HTTPStatus.OK