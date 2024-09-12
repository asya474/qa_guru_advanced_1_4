from model.response_user import ResponseUser


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
