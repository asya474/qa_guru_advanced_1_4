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

