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
from typing_extensions import Annotated

def jsonable_encoder(
    obj: Any,
    *,
    include: Any = None,
    exclude: Any = None,
    by_alias: bool = True,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    exclude_none: bool = False,
    custom_encoder: Optional[Dict[Any, Callable[[Any], Any]]] = None,
    sqlalchemy_safe: bool = True,
) -> Any:
    ...