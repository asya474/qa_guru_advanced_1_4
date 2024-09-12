import json
import pytest
import requests
from jsonschema import validate
from http import HTTPStatus
from random import randint
from model.reqres import ResponseGetUser, User, ResponseUser, Reqres, UserCreate, UserUpdate
from faker import Faker

fake = Faker()
def test_create_user(env):
    data = {"first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.free_email(),
            "avatar": f"https://reqres.in/img/faces/{randint(1, 1000)}-image.jpg"}

    result_response_create_user = requests.post(f"{app_url}/api/users/", data=json.dumps(data))

    assert result_response_create_user.status_code == HTTPStatus.CREATED

    user = result_response_create_user.json()
    UserCreate.model_validate(user)