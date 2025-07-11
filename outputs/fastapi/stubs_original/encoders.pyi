import datetime
from ._compat import PYDANTIC_V2 as PYDANTIC_V2, UndefinedType as UndefinedType, Url as Url
from _typeshed import Incomplete
from decimal import Decimal
from fastapi.types import IncEx as IncEx
from typing import Any, Callable, Dict, Optional, Tuple, Type, Union
from typing_extensions import Annotated

def isoformat(o: Union[datetime.date, datetime.time]) -> str: ...
def decimal_encoder(dec_value: Decimal) -> Union[int, float]: ...

ENCODERS_BY_TYPE: Dict[Type[Any], Callable[[Any], Any]]

def generate_encoders_by_class_tuples(type_encoder_map: Dict[Any, Callable[[Any], Any]]) -> Dict[Callable[[Any], Any], Tuple[Any, ...]]: ...

encoders_by_class_tuples: Incomplete

def jsonable_encoder(obj: Annotated[Any, None], include: Annotated[Optional[IncEx], None] = ..., exclude: Annotated[Optional[IncEx], None] = ..., by_alias: Annotated[bool, None] = ..., exclude_unset: Annotated[bool, None] = ..., exclude_defaults: Annotated[bool, None] = ..., exclude_none: Annotated[bool, None] = ..., custom_encoder: Annotated[Optional[Dict[Any, Callable[[Any], Any]]], None] = ..., sqlalchemy_safe: Annotated[bool, None] = ...) -> Any: ...
