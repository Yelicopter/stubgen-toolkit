from typing import Any, List, Union

class Highlighter:
    def __call__(self, text: Union[str, Any]) -> Any: ...
    def highlight(self, text: Any) -> None: ...

class NullHighlighter(Highlighter):
    def highlight(self, text: Any) -> None: ...

class RegexHighlighter(Highlighter):
    highlights: List[str]
    base_style: str
    def highlight(self, text: Any) -> None: ...

class ReprHighlighter(RegexHighlighter): ...

class JSONHighlighter(RegexHighlighter):
    JSON_STR: str
    JSON_WHITESPACE: set[str]
    base_style: str
    highlights: List[str]
    def highlight(self, text: Any) -> None: ...

class ISO8601Highlighter(RegexHighlighter):
    base_style: str
    highlights: List[str]
