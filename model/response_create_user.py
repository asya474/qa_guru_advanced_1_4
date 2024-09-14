
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

