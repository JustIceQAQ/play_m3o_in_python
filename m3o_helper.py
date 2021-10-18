import requests
import json

from m3o_plugin.db import M3oDb
from m3o_plugin.cache import M3oCache
from m3o_plugin.answer import M3oAnswer
from m3o_plugin.address import M3oAddress
from m3o_plugin.crypto import M3oCrypto
from m3o_plugin.currency import M3oCurrency
from m3o_plugin.email import M3oEmail
from m3o_plugin.helloworld import M3oHelloWorld


class M3o(
    M3oDb,
    M3oCache,
    M3oAnswer,
    M3oAddress,
    M3oCrypto,
    M3oCurrency,
    M3oEmail,
    M3oHelloWorld,

):
    def __init__(self, token, version="v1"):
        self.hostname = "https://api.m3o.com/{version}/{service}/{endpoint}"
        self.requests = requests.session()
        self.version = version
        self.requests.headers.update({
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        })
        M3oDb.__init__(self)
        M3oCache.__init__(self)
        M3oAnswer.__init__(self)
        M3oAddress.__init__(self)
        M3oCrypto.__init__(self)
        M3oCurrency.__init__(self)
        M3oEmail.__init__(self)
        M3oHelloWorld.__init__(self)

    def _general_func(self, data, service, endpoint, version, status_code=200):
        service_endpoint = {"service": service, "endpoint": endpoint, "version": version}
        hostname = self.hostname.format(**service_endpoint)
        data = data if data is not None else {}
        payload = json.dumps(data)
        response = self.requests.post(hostname, data=payload)
        return response.json() if response.status_code == status_code else response.text
