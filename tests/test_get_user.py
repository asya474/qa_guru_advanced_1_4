import json
import pytest
import requests
from jsonschema import validate
from http import HTTPStatus
from random import randint
from model.reqres import ResponseGetUser, User, ResponseUser, Reqres, UserCreate, UserUpdate
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