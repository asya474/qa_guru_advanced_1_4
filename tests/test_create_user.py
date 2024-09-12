
from http import HTTPStatus

from model.reqres import Reqres
from model.response_create_user import ResponseCreateUser


def test_create_user(env):
    expected_response_create_user = ResponseCreateUser(
    name="morpheus", job="leader", id="506", created_at="2024-09-12T17:27:35.495Z")

    result_response_create_user = Reqres(env).create_user(name="morpheus", job="leader")

    assert result_response_create_user.status_code == HTTPStatus.CREATED

    assert result_response_create_user.json == expected_response_create_user.json