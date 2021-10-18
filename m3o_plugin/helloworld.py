from typing import Dict, Any
from enum import Enum


class StringEnum(str, Enum):
    pass


class HelloWorldEndpoint:
    call = "Call"


class M3oHelloWorld:
    def __init__(self):
        self.m3o_hello_world = "helloworld"
        self.m3o_hello_world_enum = HelloWorldEndpoint

    def hello_world_call(self, data: Dict[str, Any] = None):
        return self._general_func(data, self.m3o_hello_world, self.m3o_hello_world_enum.call, self.version)
