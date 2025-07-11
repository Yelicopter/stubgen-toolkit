from enum import Enum
from typing import Generic, TypeVar, Union
import click

ParamTypeValue = TypeVar("ParamTypeValue")

class TyperChoice(click.Choice, Generic[ParamTypeValue]):
    ...