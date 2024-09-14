from datetime import datetime

from response_user import ResponseUser
class ResponseUpdateUser:
    def __init__(self, **kwargs):
        json_ = kwargs.pop("json", {})

        self._json = json_ if json_ else {
        "name": "morpheus",
        "job": "zion resident",
        "updatedAt": datetime.datetime.now(datetime.UTC)
        }

    @property
    def json(self):
        return self._json