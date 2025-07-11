import click
from enum import Enum
from typing import Generic, TypeVar, Union

ParamTypeValue = TypeVar('ParamTypeValue')

class TyperChoice(click.Choice, Generic[ParamTypeValue]):
    def normalize_choice(self, choice: Union[str, Enum], ctx: Optional[click.Context]) -> str: ...
