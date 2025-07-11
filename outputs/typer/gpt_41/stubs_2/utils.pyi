import inspect
import sys
from copy import copy
from typing import Any, Callable, Dict, List, Tuple, Type, cast

if sys.version_info >= (3, 9):
    from typing import Annotated, get_args, get_origin, get_type_hints
else:
    from typing_extensions import Annotated, get_args, get_origin, get_type_hints

from .models import ArgumentInfo, OptionInfo, ParameterInfo, ParamMeta

def _param_type_to_user_string(param_type: type) -> str: ...

class AnnotatedParamWithDefaultValueError(Exception):
    argument_name: str
    param_type: type[ParameterInfo]
    def __init__(self, argument_name: str, param_type: type[ParameterInfo]) -> None: ...
    def __str__(self) -> str: ...

class MixedAnnotatedAndDefaultStyleError(Exception):
    argument_name: str
    annotated_param_type: type[ParameterInfo]
    default_param_type: type[ParameterInfo]
    def __init__(
        self,
        argument_name: str,
        annotated_param_type: type[ParameterInfo],
        default_param_type: type[ParameterInfo],
    ) -> None: ...
    def __str__(self) -> str: ...

class MultipleTyperAnnotationsError(Exception):
    argument_name: str
    def __init__(self, argument_name: str) -> None: ...
    def __str__(self) -> str: ...

class DefaultFactoryAndDefaultValueError(Exception):
    argument_name: str
    param_type: type[ParameterInfo]
    def __init__(self, argument_name: str, param_type: type[ParameterInfo]) -> None: ...
    def __str__(self) -> str: ...

def _split_annotation_from_typer_annotations(
    base_annotation: Any,
) -> tuple[Any, list[ParameterInfo]]: ...
def get_params_from_function(func: Callable[..., Any]) -> dict[str, ParamMeta]: ...