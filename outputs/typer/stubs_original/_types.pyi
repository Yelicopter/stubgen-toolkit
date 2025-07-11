import click
from typing import Generic, TypeVar, Union

ParamTypeValue = TypeVar('ParamTypeValue')

class TyperChoice(click.Choice, Generic[ParamTypeValue]):
    def normalize_choice(self, choice: ParamTypeValue, ctx: Union[click.Context, None]) -> str: ...
