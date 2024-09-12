import json
import pytest
import requests
from jsonschema import validate
from http import HTTPStatus
from random import randint
from model.reqres import ResponseGetUser, User, ResponseUser, Reqres, UserCreate, UserUpdate
from faker import Faker

fake = Faker()
def test_update_user(app_url):
    data = {"first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.free_email(),
            "avatar": f"https://reqres.in/img/faces/{randint(1, 1000)}-image.jpg"}
    response = requests.post(url=f"{app_url}/api/users/", data=json.dumps(data))
    user_id = response.json()["id"]
    data_update = {"first_name": fake.first_name(),
                   "last_name": fake.last_name(),
                   "email": fake.free_email(),
                   "avatar": f"https://reqres.in/img/faces/{randint(1, 1000)}-image.jpg"}
    response = requests.patch(url=f"{app_url}/api/users/{user_id}", data=json.dumps(data_update))
    assert response.status_code == HTTPStatus.OK
    user = response.json()
    UserUpdate.model_validate(user)