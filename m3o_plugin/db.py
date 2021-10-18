from typing import Dict, Any
import json
from enum import Enum


class StringEnum(str, Enum):
    pass


class DbEndpoint:
    create = "create"
    delete = "delete"
    read = "read"
    truncate = "truncate"
    update = "update"


class M3oDb:
    def __init__(self):
        self.m3o_db = "db"
        self.m3o_db_enum = DbEndpoint

    def db_create(self, data: Dict[str, Any] = None):
        return self._general_func(data, self.m3o_db, self.m3o_db_enum.create, self.version)

    def db_delete(self, data: Dict[str, Any] = None):
        return self._general_func(data, self.m3o_db, self.m3o_db_enum.delete, self.version)

    def db_read(self, data: Dict[str, Any] = None):
        return self._general_func(data, self.m3o_db, self.m3o_db_enum.read, self.version)

    def db_truncate(self, data: Dict[str, Any] = None):
        return self._general_func(data, self.m3o_db, self.m3o_db_enum.truncate, self.version)

    def db_update(self, data: Dict[str, Any] = None):
        return self._general_func(data, self.m3o_db, self.m3o_db_enum.update, self.version)
