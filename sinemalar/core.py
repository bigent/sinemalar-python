import requests, json

class APIConfig(object):
    def __init__(self, api_domain="api.sinemalar.com", api_protocol="http", api_version="v1"):

        if api_protocol not in ('http', 'https'):
            raise ValueError("The protocol must be 'http' or 'https'.")

        self.api_domain = api_domain
        self._api_protocol = api_protocol
        self._api_version = api_version

    def get_url(self):
        if self.api_domain == "www.sinemalar.com":
            return "{protocol}://{domain}/json/mobile".format(
                protocol=self._api_protocol,
                domain=self.api_domain,
            )
        else:
            return "{protocol}://{domain}/ajax/json/ios/{version}".format(
                protocol=self._api_protocol,
                domain=self.api_domain,
                version=self._api_version,
            )


class Method(APIConfig):
    def __init__(self, method="get"):
        self._method = method
        APIConfig.__init__(self)
        self._splitter_char = "/"

    def add_to_url(self, path, *continue_urls):
        for i in continue_urls:
            path = "{}{splitter}{}".format(path, i, splitter=self._splitter_char)
        return path

    def GET(self, *continue_urls):
        method = "get"

        if self.api_domain == "www.sinemalar.com" or continue_urls[0] == "gallery" or continue_urls[0] == "gps":
            return json.loads(requests.get(self.add_to_url(self.get_url(), *continue_urls)).content)
        else:
            return json.loads(requests.get(self.add_to_url(self.get_url(), 'get', *continue_urls)).content)

    def POST(self, *continue_urls):
        method = "post"
        return json.loads(requests.post(self.add_to_url(self.get_url(), 'get', *continue_urls)).content)


class CallObject(Method):
    def __init__(self):
        Method.__init__(self)

    @staticmethod
    def is_True(boolean):
        if boolean:
            return "1"
        else:
            return "0"


