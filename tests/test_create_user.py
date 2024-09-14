from http import HTTPStatus
from datetime import datetime
from model.reqres import Reqres
from model.response_create_user import ResponseCreateUser
from pytest_voluptuous import S
from schemas.reqres import response_create_user

def test_create_user(env):
    expected_response_create_user = ResponseCreateUser(
    name="morpheus", job="leader", id="506", created_at=datetime.datetime.now(datetime.UTC))

    result_response_create_user = Reqres(env).create_user(name="morpheus", job="leader")

    assert result_response_create_user.status_code == HTTPStatus.CREATED
    assert result_response_create_user.json == expected_response_create_user.json


def test_response_create_user(reqresin):
    response = Reqres(env).create_user(name="morpheus", job="leader")
    assert S(response_create_user) == response.json()
