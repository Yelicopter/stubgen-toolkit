import click
from enum import Enum
from typing import Generic, Optional, TypeVar, Union

ParamTypeValue = TypeVar('ParamTypeValue')

class TyperChoice(click.Choice[str], Generic[ParamTypeValue]):
    def normalize_choice(self, choice: Union[ParamTypeValue, Enum], ctx: Optional[click.Context]) -> str: ...
