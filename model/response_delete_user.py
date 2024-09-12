from response_user import ResponseUser
class ResponseDeleteUser:
    def __init__(self, **kwargs):
        response = kwargs.pop("response", None)
        json_ = kwargs.pop("json", response.json() if response else None)
        self._data = kwargs.pop("data", ResponseUser()).json
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