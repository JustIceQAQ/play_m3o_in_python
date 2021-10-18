from typing import Dict, Any
from enum import Enum


class StringEnum(str, Enum):
    pass


class CacheEndpoint:
    decrement = "decrement"
    delete = "delete"
    get = "get"
    increment = "increment"
    set = "set"


class M3oCache:
    def __init__(self):
        self.m3o_cache = "cache"
        self.m3o_cache_enum = CacheEndpoint

    def cache_decrement(self, data: Dict[str, Any] = None):
        return self._general_func(data, self.m3o_cache, self.m3o_cache_enum.decrement, self.version)

    def cache_delete(self, data: Dict[str, Any] = None):
        return self._general_func(data, self.m3o_cache, self.m3o_cache_enum.delete, self.version)

    def cache_get(self, data: Dict[str, Any] = None):
        return self._general_func(data, self.m3o_cache, self.m3o_cache_enum.get, self.version)

    def cache_increment(self, data: Dict[str, Any] = None):
        return self._general_func(data, self.m3o_cache, self.m3o_cache_enum.increment, self.version)

    def cache_set(self, data: Dict[str, Any] = None):
        return self._general_func(data, self.m3o_cache, self.m3o_cache_enum.set, self.version)
