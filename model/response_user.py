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

    @property
    def json(self):
        return self._json