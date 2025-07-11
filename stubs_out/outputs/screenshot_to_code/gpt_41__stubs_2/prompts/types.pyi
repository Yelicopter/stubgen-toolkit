from _typeshed import Incomplete
from typing import List, TypedDict

class SystemPrompts(TypedDict, total=False):
    html_css: str
    html_tailwind: str
    react_tailwind: str
    bootstrap: str
    ionic_tailwind: str
    vue_tailwind: str
    svg: str

class PromptContent(TypedDict, total=False):
    text: str
    images: List[str]

Stack: Incomplete
