import re
from abc import ABC, abstractmethod
from typing import List, Union

from .text import Span, Text

class Highlighter(ABC):
    def __call__(self, text: Union[str, Text]) -> Text: ...
    
    @abstractmethod
    def highlight(self, text: Text) -> None: ...

class NullHighlighter(Highlighter):
    def highlight(self, text: Text) -> None: ...

class RegexHighlighter(Highlighter):
    highlights: List[str] = []
    base_style: str = ""
    
    def highlight(self, text: Text) -> None: ...

class ReprHighlighter(RegexHighlighter):
    base_style: str = "repr."
    highlights: List[str] = ...

class JSONHighlighter(RegexHighlighter):
    base_style: str = "json."
    highlights: List[str] = ...
    
    def highlight(self, text: Text) -> None: ...

class ISO8601Highlighter(RegexHighlighter):
    base_style: str = "iso8601."
    highlights: List[str] = ...