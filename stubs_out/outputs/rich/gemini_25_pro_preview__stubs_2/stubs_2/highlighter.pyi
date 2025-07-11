import abc
from abc import ABC, abstractmethod
from rich.text import Text as Text
from typing import List, Set, Union

class Highlighter(ABC, metaclass=abc.ABCMeta):
    def __call__(self, text: Union[str, Text]) -> Text: ...
    @abstractmethod
    def highlight(self, text: Text) -> None: ...

class NullHighlighter(Highlighter):
    def highlight(self, text: Text) -> None: ...

class RegexHighlighter(Highlighter):
    highlights: List[str]
    base_style: str
    def highlight(self, text: Text) -> None: ...

class ReprHighlighter(RegexHighlighter):
    base_style: str
    highlights: List[str]

class JSONHighlighter(RegexHighlighter):
    JSON_STR: str
    JSON_WHITESPACE: Set[str]
    base_style: str
    highlights: List[str]
    def highlight(self, text: Text) -> None: ...

class ISO8601Highlighter(RegexHighlighter):
    base_style: str
    highlights: List[str]
