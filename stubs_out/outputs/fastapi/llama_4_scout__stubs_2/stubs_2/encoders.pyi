from collections import defaultdict as defaultdict, deque as deque
from decimal import Decimal as Decimal
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
from typing import Any, Callable, Dict, Optional
from uuid import UUID as UUID

def jsonable_encoder(obj: Any, *, include: Any = ..., exclude: Any = ..., by_alias: bool = ..., exclude_unset: bool = ..., exclude_defaults: bool = ..., exclude_none: bool = ..., custom_encoder: Optional[Dict[Any, Callable[[Any], Any]]] = ..., sqlalchemy_safe: bool = ...) -> Any: ...
