from typing import Dict, Any
from enum import Enum


class StringEnum(str, Enum):
    pass


class CryptoEndpoint:
    history = "History"
    news = "News"
    price = "Price"
    quote = "Quote"


class M3oCrypto:
    def __init__(self):
        self.m3o_crypto = "crypto"
        self.m3o_crypto_enum = CryptoEndpoint

    def crypto_history(self, data: Dict[str, Any] = None):
        return self._general_func(data, self.m3o_crypto, self.m3o_crypto_enum.history, self.version)

    def crypto_news(self, data: Dict[str, Any] = None):
        return self._general_func(data, self.m3o_crypto, self.m3o_crypto_enum.news, self.version)

    def crypto_price(self, data: Dict[str, Any] = None):
        return self._general_func(data, self.m3o_crypto, self.m3o_crypto_enum.price, self.version)

    def crypto_quote(self, data: Dict[str, Any] = None):
        return self._general_func(data, self.m3o_crypto, self.m3o_crypto_enum.quote, self.version)
