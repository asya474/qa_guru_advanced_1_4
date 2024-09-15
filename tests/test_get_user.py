from schemas.reqres import response_get_user
from pytest_voluptuous import S
from model.reqres import Reqres, ResponseGetUser, ResponseUser

def test_get_user(env):
    expected_response_get_user = ResponseGetUser(data=ResponseUser(
        id=2,
        email="janet.weaver@reqres.in",
        first_name="Janet",
        last_name="Weaver",
        avatar="https://reqres.in/img/faces/2-image.jpg"
    ))

    result_response_get_user = Reqres(env).get_user(2)

    assert result_response_get_user.support_url == expected_response_get_user.support_url
    assert result_response_get_user.json == expected_response_get_user.json

def test_response_get_user(env, reqresin):
    response = Reqres(env).get_user(2)
    assert S(response_get_user) == response.json