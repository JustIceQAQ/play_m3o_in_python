from typing import Dict, Any
from enum import Enum


class StringEnum(str, Enum):
    pass


class EmojiEndpoint:
    find = "Find"
    flag = "Flag"
    print = "Print"
    send = "Send"


class M3oEmoji:
    def __init__(self):
        self.m3o_emoji = "emoji"
        self.m3o_emoji_enum = EmojiEndpoint

    def emoji_find(self, data: Dict[str, Any] = None):
        return self._general_func(data, self.m3o_emoji, self.m3o_emoji_enum.find, self.version)

    def emoji_flag(self, data: Dict[str, Any] = None):
        return self._general_func(data, self.m3o_emoji, self.m3o_emoji_enum.flag, self.version)

    def emoji_print(self, data: Dict[str, Any] = None):
        return self._general_func(data, self.m3o_emoji, self.m3o_emoji_enum.print, self.version)

    def emoji_send(self, data: Dict[str, Any] = None):
        return self._general_func(data, self.m3o_emoji, self.m3o_emoji_enum.send, self.version)
