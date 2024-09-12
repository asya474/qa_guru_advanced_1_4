import json
import pytest
import requests
from jsonschema import validate
from http import HTTPStatus
from random import randint
from model.reqres import ResponseGetUser, User, ResponseUser, Reqres, UserCreate, UserUpdate
from faker import Faker

fake = Faker()
def test_delete_user(app_url, fill_test_data):
    for user_id in (fill_test_data[0], fill_test_data[-1]):
        response = requests.delete(f"{app_url}/api/users/{user_id}")
        assert response.status_code == HTTPStatus.OK