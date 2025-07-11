import re
from abc import ABC, abstractmethod
from typing import List, Union

from .text import Span, Text


def _combine_regex(*regexes: str) -> str:
    ...

class Highlighter(ABC):
    def __call__(self, text: Union[str, Text]) -> Text:
        ...

    @abstractmethod
    def highlight(self, text: Text) -> None:
        ...

class NullHighlighter(Highlighter):
    def highlight(self, text: Text) -> None:
        ...

class RegexHighlighter(Highlighter):
    def highlight(self, text: Text) -> None:
        ...

class ReprHighlighter(RegexHighlighter):
    ...

class JSONHighlighter(RegexHighlighter):
    ...

class ISO8601Highlighter(RegexHighlighter):
    ...