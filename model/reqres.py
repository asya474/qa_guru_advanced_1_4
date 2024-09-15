from datetime import datetime, timezone

from utils.base_session import BaseSession
from config import Server


class User:
    def __init__(self, **kwargs):
        json_ = kwargs.pop("json", {})
        self._name = kwargs.pop("name", None)
        self._job = kwargs.pop("job", None)
        self._json = json_ if json_ else {
            "name": self._name,
            "job": self._job,
        }

    @property
    def name(self):
        return self._json['name']

    @property
    def job(self):
        return self._json['job']

    @property
    def json(self):
        return self._json


class Support:
    def __init__(self, **kwargs):
        self._url = kwargs.pop("url", "https://reqres.in/#support-heading")
        self._text = kwargs.pop("text", "To keep ReqRes free, contributions towards server costs are appreciated!")
        self._json = {
            "url": self._url,
            "text": self._text,

        }

    @property
    def url(self):
        return self._json['url']

    @property
    def text(self):
        return self._json['text']

    @property
    def json(self):
        return self._json


class ResponseUser:
    def __init__(self, **kwargs):
        json_ = kwargs.pop("json", {})
        self._id = kwargs.pop("id", 2)
        self._email = kwargs.pop("email", "janet.weaver@reqres.in")
        self._first_name = kwargs.pop("first_name", "Janet")
        self._last_name = kwargs.pop("last_name", "Weaver")
        self._avatar = kwargs.pop("avatar", "https://reqres.in/img/faces/2-image.jpg")
        self._json = json_ if json_ else {
            "id": self._id,
            "email": self._email,
            "first_name": self._first_name,
            "last_name": self._last_name,
            "avatar": self._avatar,
        }


class ResponseGetUser:
    def __init__(self, **kwargs):
        response = kwargs.pop("response", None)
        json_ = kwargs.pop("json", response.json() if response else None)
        self._data = kwargs.pop("data", ResponseUser())._json
        self._json = json_ if json_ else {
            "data": self._data,
            "support": {
                "url": "https://reqres.in/#support-heading",
                "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
            }
        }

    @property
    def json(self):
        return self._json

    @property
    def support_url(self):
        return self._json['support']['url']

    @property
    def support_text(self):
        return self._json['support']['text']


class ResponseGetUsers:
    def __init__(self, **kwargs):
        json_ = kwargs.pop("json", {})

        self._json = json_ if json_ else {
            "page": 2,
            "per_page": 6,
            "total": 12,
            "total_pages": 2,
            "data": []
        }

    def add_user(self, user: ResponseUser):
        self._json['data'].append(user.json)
        return self

    @property
    def json(self):
        return self._json


class ResponseCreateUser:
    def __init__(self, **kwargs):
        json_ = kwargs.pop("json", {})
        self._json = json_ if json_ else {
            "name": "morpheus",
            "job": "leader"
        }

    @property
    def json(self):
        return self._json


class ResponseUpdateUser:
    def __init__(self, **kwargs):
        json_ = kwargs.pop("json", {})

        self._json = json_ if json_ else {
            "name": "morpheus",
            "job": "zion resident",
            "updatedAt": str(datetime.now(timezone.utc))
        }

    @property
    def json(self):
        return self._json


class ResponseDeleteUser:
    def __init__(self, **kwargs):
        response = kwargs.pop("response", None)


class Reqres:
    def __init__(self, env):
        self.session = BaseSession(base_url=Server(env).reqres)

    def get_user(self, user_id: int):
        return ResponseGetUser(response=self.session.get(f"/api/users/{user_id}"))

    def get_users(self):
        return ResponseGetUsers(response=self.session.get(f"/api/users/"))

    def create_user(self, user_id: int):
        return ResponseCreateUser(response=self.session.post(f"/api/users/{user_id}"))

    def update_user(self, user_id: int):
        return ResponseUpdateUser(response=self.session.patch(f"/api/users/{user_id}"))

    def delete_user(self, user_id: int):
        return ResponseDeleteUser(response=self.session.delete(f"/api/users/{user_id}"))
