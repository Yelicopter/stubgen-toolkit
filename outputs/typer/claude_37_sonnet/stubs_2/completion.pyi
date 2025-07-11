import os
import sys
from typing import Any, MutableMapping, Tuple

import click

from ._completion_classes import completion_init
from ._completion_shared import Shells, get_completion_script, install
from .models import ParamMeta
from .params import Option
from .utils import get_params_from_function

def get_completion_inspect_parameters() -> Tuple[ParamMeta, ParamMeta]: ...
def install_callback(ctx: click.Context, param: click.Parameter, value: Any) -> Any: ...
def show_callback(ctx: click.Context, param: click.Parameter, value: Any) -> Any: ...
def _install_completion_placeholder_function(
    install_completion: bool = ...,
    show_completion: bool = ...,
) -> None: ...
def _install_completion_no_auto_placeholder_function(
    install_completion: str = ...,
    show_completion: str = ...,
) -> None: ...
def shell_complete(
    cli: click.Command,
    ctx_args: MutableMapping[str, Any],
    prog_name: str,
    complete_var: str,
    instruction: str,
) -> int: ...