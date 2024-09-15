from datetime import datetime
from http import HTTPStatus
from ..model.reqres import Reqres
from ..model.response_update_user import ResponseUpdateUser
from ..schemas.reqres import response_update_user
from pytest_voluptuous import S

def test_update_user(env):

    expected_response_update_user = ResponseUpdateUser(data=ResponseUpdateUser(
        name="morpheus",
        job="zion resident",
        updatedAt=datetime.datetime.now(datetime.UTC)
    ))

    result_response_update_user = Reqres(env).update_user(2)
    assert result_response_update_user.status_code == HTTPStatus.OK
    assert result_response_update_user.json == expected_response_update_user.json

def test_response_update_user(reqresin):
    response = Reqres(env).update_user(2)
    assert S(response_update_user) == response.json()