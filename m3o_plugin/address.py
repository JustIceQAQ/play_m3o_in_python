from typing import Dict, Any
from enum import Enum


class StringEnum(str, Enum):
    pass


class AddressEndpoint:
    lookup_postcode = "LookupPostcode"


class M3oAddress:
    def __init__(self):
        self.m3o_address = "address"
        self.m3o_address_enum = AddressEndpoint

    def address_lookup_postcode(self, data: Dict[str, Any] = None):
        return self._general_func(data, self.m3o_address, self.m3o_address_enum.lookup_postcode, self.version)
