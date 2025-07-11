import click
from enum import Enum as Enum
from typing import Any, Generic, TypeVar

ParamTypeValue = TypeVar('ParamTypeValue')

class TyperChoice(click.Choice, Generic[ParamTypeValue]):
    def normalize_choice(self, choice: Any, ctx: Any) -> str: ...
