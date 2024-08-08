import json
from http import HTTPStatus
from random import randint

from faker import Faker
import pytest
import requests
from app.models.User import User, UserCreate, UserUpdate

fake = Faker()


@pytest.mark.usefixtures("fill_test_data")
def test_users(app_url):
    response = requests.get(f"{app_url}/api/users/")
    assert response.status_code == HTTPStatus.OK

    user_list = response.json()
    for user in user_list:
        User.model_validate(user)


@pytest.mark.usefixtures("fill_test_data")
def test_users_no_duplicates(users):
    users_ids = [user["id"] for user in users]
    assert len(users_ids) == len(set(users_ids))


def test_user(app_url, fill_test_data):
    for user_id in (fill_test_data[0], fill_test_data[-1]):
        response = requests.get(f"{app_url}/api/users/{user_id}")
        assert response.status_code == HTTPStatus.OK
        user = response.json()
        User.model_validate(user)


@pytest.mark.parametrize("user_id", [99])
def test_user_nonexistent_values(app_url, user_id):
    response = requests.get(f"{app_url}/api/users/{user_id}")
    assert response.status_code == HTTPStatus.NOT_FOUND


@pytest.mark.parametrize("user_id", [-1, 0, "fafaf"])
def test_user_invalid_values(app_url, user_id):
    response = requests.get(f"{app_url}/api/users/{user_id}")
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


def test_create_user(app_url):
    data = {"first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.free_email(),
            "avatar": f"https://reqres.in/img/faces/{randint(1, 1000)}-image.jpg"}
    response = requests.post(f"{app_url}/api/users/", data=json.dumps(data))
    assert response.status_code == HTTPStatus.CREATED
    user = response.json()
    UserCreate.model_validate(user)


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


def test_delete_user(app_url, fill_test_data):
    for user_id in (fill_test_data[0], fill_test_data[-1]):
        response = requests.delete(f"{app_url}/api/users/{user_id}")
        assert response.status_code == HTTPStatus.OK
