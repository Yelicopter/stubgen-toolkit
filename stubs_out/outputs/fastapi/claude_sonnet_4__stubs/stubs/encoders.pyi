import datetime
from ._compat import PYDANTIC_V2 as PYDANTIC_V2, UndefinedType as UndefinedType, Url as Url
from collections import defaultdict as defaultdict, deque as deque
from decimal import Decimal
from enum import Enum as Enum
from fastapi.types import IncEx as IncEx
from ipaddress import IPv4Address as IPv4Address, IPv4Interface as IPv4Interface, IPv4Network as IPv4Network, IPv6Address as IPv6Address, IPv6Interface as IPv6Interface, IPv6Network as IPv6Network
from pathlib import Path as Path, PurePath as PurePath
from pydantic import BaseModel as BaseModel
from pydantic.color import Color as Color
from pydantic.networks import AnyUrl as AnyUrl, NameEmail as NameEmail
from pydantic.types import SecretBytes as SecretBytes, SecretStr as SecretStr
from re import Pattern as Pattern
from types import GeneratorType as GeneratorType
from typing import Any, Callable, Dict, Optional, Tuple, Type, Union
from uuid import UUID as UUID

def isoformat(o: Union[datetime.date, datetime.time, datetime.datetime]) -> str: ...
def decimal_encoder(dec_value: Decimal) -> Union[int, float]: ...

ENCODERS_BY_TYPE: Dict[Type[Any], Callable[[Any], Any]]

def generate_encoders_by_class_tuples(type_encoder_map: Dict[Type[Any], Callable[[Any], Any]]) -> Dict[Callable[[Any], Any], Tuple[Type[Any], ...]]: ...

encoders_by_class_tuples: Dict[Callable[[Any], Any], Tuple[Type[Any], ...]]

def jsonable_encoder(obj: Any, include: Optional[IncEx] = ..., exclude: Optional[IncEx] = ..., by_alias: bool = ..., exclude_unset: bool = ..., exclude_defaults: bool = ..., exclude_none: bool = ..., custom_encoder: Optional[Dict[Any, Callable[[Any], Any]]] = ..., sqlalchemy_safe: bool = ...) -> Any: ...
