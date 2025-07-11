from ._typing import Annotated as Annotated, get_args as get_args, get_origin as get_origin, get_type_hints as get_type_hints
from .models import ArgumentInfo as ArgumentInfo, OptionInfo as OptionInfo, ParamMeta as ParamMeta, ParameterInfo as ParameterInfo
from copy import copy as copy
from typing import Any, Callable

class AnnotatedParamWithDefaultValueError(Exception):
    argument_name: str
    param_type: type[ParameterInfo]
    def __init__(self, argument_name: str, param_type: type[ParameterInfo]) -> None: ...

class MixedAnnotatedAndDefaultStyleError(Exception):
    argument_name: str
    annotated_param_type: type[ParameterInfo]
    default_param_type: type[ParameterInfo]
    def __init__(self, argument_name: str, annotated_param_type: type[ParameterInfo], default_param_type: type[ParameterInfo]) -> None: ...

class MultipleTyperAnnotationsError(Exception):
    argument_name: str
    def __init__(self, argument_name: str) -> None: ...

class DefaultFactoryAndDefaultValueError(Exception):
    argument_name: str
    param_type: type[ParameterInfo]
    def __init__(self, argument_name: str, param_type: type[ParameterInfo]) -> None: ...

def get_params_from_function(func: Callable[..., Any]) -> dict[str, ParamMeta]: ...
