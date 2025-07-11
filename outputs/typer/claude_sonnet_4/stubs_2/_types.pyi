from enum import Enum
from typing import Generic, Optional, TypeVar, Union
import click

ParamTypeValue = TypeVar("ParamTypeValue")

class TyperChoice(click.Choice[str], Generic[ParamTypeValue]):
    def normalize_choice(
        self, choice: Union[str, Enum], ctx: Optional[click.Context]
    ) -> str: ...