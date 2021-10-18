from typing import Dict, Any
from enum import Enum


class StringEnum(str, Enum):
    pass


class EmailEndpoint:
    send = "Send"


class M3oEmail:
    def __init__(self):
        self.m3o_email = "email"
        self.m3o_email_enum = EmailEndpoint

    def email_send(self, data: Dict[str, Any] = None):
        return self._general_func(data, self.m3o_email, self.m3o_email_enum.send, self.version)
