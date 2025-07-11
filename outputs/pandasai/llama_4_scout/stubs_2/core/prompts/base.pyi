import os
import re
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Optional

from jinja2 import Environment, FileSystemLoader


class BasePrompt:
    template: str | None = None
    template_path: str | None = None

    def __init__(self, **kwargs) -> None:
        ...

    def render(self) -> str:
        ...


    def to_string(self) -> str:
        ...

    def __str__(self) -> str:
        ...

    def validate(self, output: str) -> bool:
        ...

    def to_json(self) -> dict:
        ...


class AbstractPrompt(ABC):
    @abstractmethod
    def get_prompt(self) -> None:
        pass


# Make sure to export AbstractPrompt if using __all__
__all__ = ["AbstractPrompt"]