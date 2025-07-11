import click
from enum import Enum as Enum
from typing import Generic, TypeVar

ParamTypeValue = TypeVar('ParamTypeValue')

class TyperChoice(click.Choice, Generic[ParamTypeValue]): ...
