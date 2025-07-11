import dataclasses
import datetime
from collections import defaultdict, deque
from decimal import Decimal
from enum import Enum
from ipaddress import (
    IPv4Address,
    IPv4Interface,
    IPv4Network,
    IPv6Address,
    IPv6Interface,
    IPv6Network,
)
from pathlib import Path, PurePath
from re import Pattern
from types import GeneratorType
from typing import Any, Callable, Dict, List, Optional, Tuple, Type, Union
from uuid import UUID

from fastapi.types import IncEx
from pydantic import BaseModel
from pydantic.color import Color
from pydantic.networks import AnyUrl, NameEmail
from pydantic.types import SecretBytes, SecretStr
from typing_extensions import Annotated, Doc

from ._compat import PYDANTIC_V2, UndefinedType, Url, _model_dump

def isoformat(o: Union[datetime.date, datetime.datetime, datetime.time]) -> str: ...

def decimal_encoder(dec_value: Decimal) -> Union[int, float]: ...

ENCODERS_BY_TYPE: Dict[Type[Any], Callable[[Any], Any]]

def generate_encoders_by_class_tuples(
    type_encoder_map: Dict[Type[Any], Callable[[Any], Any]],
) -> Dict[Callable[[Any], Any], Tuple[Type[Any], ...]]: ...

encoders_by_class_tuples: Dict[Callable[[Any], Any], Tuple[Type[Any], ...]]

def jsonable_encoder(
    obj: Any,
    include: Optional[Union[Set[str], Dict[str, Any]]] = ...,
    exclude: Optional[Union[Set[str], Dict[str, Any]]] = ...,
    by_alias: bool = ...,
    exclude_unset: bool = ...,
    exclude_defaults: bool = ...,
    exclude_none: bool = ...,
    custom_encoder: Optional[Dict[Type[Any], Callable[[Any], Any]]] = ...,
    sqlalchemy_safe: bool = ...,
) -> Any: ...