import click
from enum import Enum as Enum
from typing import Any, Generic, TypeVar

ParamTypeValue = TypeVar('ParamTypeValue')

class TyperChoice(click.Choice[ParamTypeValue], Generic[ParamTypeValue]):
    def normalize_choice(self, choice: Any, ctx: Any) -> str: ...
