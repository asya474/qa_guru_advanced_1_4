from model.reqres import Reqres
from schemas.reqres import response_list_users
from pytest_voluptuous import S
import pytest
from http import HTTPStatus
@pytest.mark.usefixtures(env)
def test_users(env):
    result_users_response = Reqres(env).get_users()
    assert result_users_response.status_code == HTTPStatus.OK

def test_response_list_users(reqresin):
    response = reqresin.get("/api/users", verify=False)
    assert S(response_list_users) == response.json()