from typing import Any, MutableMapping, Tuple
import click

def get_completion_inspect_parameters() -> Tuple[Any, Any]:
    ...
def install_callback(ctx: Any, param: Any, value: Any) -> Any:
    ...
def show_callback(ctx: Any, param: Any, value: Any) -> Any:
    ...
def _install_completion_placeholder_function(
    install_completion: Any = None,
    show_completion: Any = None,
) -> None:
    ...
def _install_completion_no_auto_placeholder_function(
    install_completion: Any = None,
    show_completion: Any = None,
) -> None:
    ...
def shell_complete(
    cli: Any,
    ctx_args: Any,
    prog_name: str,
    complete_var: str,
    instruction: str,
) -> int:
    ...