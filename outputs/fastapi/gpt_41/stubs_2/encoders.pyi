from typing import Any, Callable, Dict, List, Optional, Tuple, Type, Union

def isoformat(o: Any) -> str: ...
def decimal_encoder(dec_value: Any) -> Union[int, float]: ...
ENCODERS_BY_TYPE: Dict[Any, Callable[[Any], Any]]
def generate_encoders_by_class_tuples(
    type_encoder_map: Dict[Any, Callable[[Any], Any]],
) -> Dict[Callable[[Any], Any], Tuple[Any, ...]]: ...
encoders_by_class_tuples: Dict[Callable[[Any], Any], Tuple[Any, ...]]
def jsonable_encoder(
    obj: Any,
    include: Any = ...,
    exclude: Any = ...,
    by_alias: bool = ...,
    exclude_unset: bool = ...,
    exclude_defaults: bool = ...,
    exclude_none: bool = ...,
    custom_encoder: Optional[Dict[Any, Callable[[Any], Any]]] = ...,
    sqlalchemy_safe: bool = ...,
) -> Any: ...