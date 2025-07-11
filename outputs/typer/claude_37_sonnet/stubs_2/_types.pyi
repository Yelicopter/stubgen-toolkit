from enum import Enum
from typing import Generic, TypeVar, Union, Optional

import click

ParamTypeValue = TypeVar("ParamTypeValue")

class TyperChoice(click.Choice[ParamTypeValue], Generic[ParamTypeValue]):
    def normalize_choice(
        self, choice: Union[str, Enum], ctx: Optional[click.Context]
    ) -> str: ...