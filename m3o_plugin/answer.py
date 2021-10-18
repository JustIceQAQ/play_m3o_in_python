from typing import Dict, Any
from enum import Enum


class StringEnum(str, Enum):
    pass


class AnswerEndpoint:
    question = "Question"


class M3oAnswer:
    def __init__(self):
        self.m3o_answer = "answer"
        self.m3o_answer_enum = AnswerEndpoint

    def answer_question(self, data: Dict[str, Any] = None):
        return self._general_func(data, self.m3o_answer, self.m3o_answer_enum.question, self.version)
