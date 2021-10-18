from typing import Dict, Any
from enum import Enum


class StringEnum(str, Enum):
    pass


class CurrencyEndpoint:
    codes = "Codes"
    convert = "Convert"
    history = "History"
    rates = "Rates"


class M3oCurrency:
    def __init__(self):
        self.m3o_currency = "currency"
        self.m3o_currency_enum = CurrencyEndpoint

    def currency_codes(self, data: Dict[str, Any] = None):
        return self._general_func(data, self.m3o_currency, self.m3o_currency_enum.codes, self.version)

    def currency_convert(self, data: Dict[str, Any] = None):
        return self._general_func(data, self.m3o_currency, self.m3o_currency_enum.convert, self.version)

    def currency_history(self, data: Dict[str, Any] = None):
        return self._general_func(data, self.m3o_currency, self.m3o_currency_enum.history, self.version)

    def currency_rates(self, data: Dict[str, Any] = None):
        return self._general_func(data, self.m3o_currency, self.m3o_currency_enum.rates, self.version)
