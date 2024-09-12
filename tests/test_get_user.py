from model.response_get_user import ResponseGetUser
from model.response_user import ResponseUser
from model.reqres import Reqres
from faker import Faker

fake = Faker()

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