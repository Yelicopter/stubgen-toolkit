from enum import Enum
from typing import Generic, TypeVar, Any

import click

ParamTypeValue = TypeVar("ParamTypeValue")

class TyperChoice(click.Choice[ParamTypeValue], Generic[ParamTypeValue]):
    def normalize_choice(
        self, choice: Any, ctx: Any
    ) -> str: ...