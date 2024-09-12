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
