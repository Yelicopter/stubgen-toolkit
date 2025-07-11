import abc
from abc import ABC, abstractmethod
from jinja2 import Environment as Environment, FileSystemLoader as FileSystemLoader
from pathlib import Path as Path
from typing import Any, Dict, Optional

class BasePrompt:
    template: Optional[str]
    template_path: Optional[str]
    props: Dict[str, Any]
    prompt: Any
    def __init__(self, **kwargs) -> None: ...
    def render(self) -> str: ...
    def to_string(self) -> str: ...
    def validate(self, output: str) -> bool: ...
    def to_json(self) -> Dict[str, Any]: ...

class AbstractPrompt(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def get_prompt(self) -> str: ...
