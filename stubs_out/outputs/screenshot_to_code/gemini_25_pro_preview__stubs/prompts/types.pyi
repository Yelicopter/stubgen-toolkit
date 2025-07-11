from _typeshed import Incomplete
from typing import List, TypedDict

class SystemPrompts(TypedDict):
    html_css: str
    html_tailwind: str
    react_tailwind: str
    bootstrap: str
    ionic_tailwind: str
    vue_tailwind: str
    svg: str

class PromptContent(TypedDict):
    text: str
    images: List[str]

Stack: Incomplete
