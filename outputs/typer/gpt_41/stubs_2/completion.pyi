from typing import Any, MutableMapping, Tuple

import click

from ._completion_classes import completion_init
from ._completion_shared import Shells, get_completion_script, install
from .models import ParamMeta

def get_completion_inspect_parameters() -> tuple[Any, Any]: ...
def install_callback(ctx: Any, param: Any, value: Any) -> Any: ...
def show_callback(ctx: Any, param: Any, value: Any) -> Any: ...
def _install_completion_placeholder_function(
    install_completion: Any = ...,
    show_completion: Any = ...,
) -> None: ...
def _install_completion_no_auto_placeholder_function(
    install_completion: Any = ...,
    show_completion: Any = ...,
) -> None: ...
def shell_complete(
    cli: Any,
    ctx_args: Any,
    prog_name: str,
    complete_var: str,
    instruction: str,
) -> int: ...