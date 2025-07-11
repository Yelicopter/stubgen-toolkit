from os import terminal_size
from typing import IO, Any, Callable, Iterable, List, Optional, TextIO, Tuple, Type, Union

from click.exceptions import Abort as Abort
from click.exceptions import BadParameter as BadParameter
from click.exceptions import Exit as Exit

from . import colors as colors
from .main import Typer as Typer
from .main import launch as launch
from .main import run as run
from .models import CallbackParam as CallbackParam
from .models import Context as Context
from .models import FileBinaryRead as FileBinaryRead
from .models import FileBinaryWrite as FileBinaryWrite
from .models import FileText as FileText
from .models import FileTextWrite as FileTextWrite
from .params import Argument as Argument
from .params import Option as Option

__version__: str

def get_terminal_size() -> terminal_size: ...
def clear() -> None: ...
def confirm(
    text: str,
    default: bool = ...,
    abort: bool = ...,
    prompt_suffix: str = ...,
    show_default: bool = ...,
    err: bool = ...,
) -> bool: ...
def echo_via_pager(
    text_or_generator: Union[str, Iterable[str], Callable[[], Union[str, Iterable[str]]]],
    color: Optional[bool] = ...,
) -> None: ...
def edit(
    text: Optional[str] = ...,
    editor: Optional[str] = ...,
    env: Optional[Any] = ...,
    require_save: bool = ...,
    extension: str = ...,
    filename: Optional[str] = ...,
) -> Optional[str]: ...
def getchar(echo: bool = ...) -> str: ...
def pause(info: Optional[str] = ..., err: bool = ...) -> None: ...
def progressbar(
    iterable: Optional[Iterable[Any]] = ...,
    length: Optional[int] = ...,
    label: Optional[str] = ...,
    show_eta: bool = ...,
    show_percent: Optional[bool] = ...,
    show_pos: bool = ...,
    item_show_func: Optional[Callable[[Optional[Any]], Optional[str]]] = ...,
    fill_char: str = ...,
    empty_char: str = ...,
    bar_template: str = ...,
    info_sep: str = ...,
    width: int = ...,
    file: Optional[TextIO] = ...,
    color: Optional[bool] = ...,
    update_min_steps: int = ...,
) -> Any: ...
def prompt(
    text: str,
    default: Optional[Any] = ...,
    hide_input: bool = ...,
    confirmation_prompt: bool = ...,
    type: Optional[Union[Type[Any], Any]] = ...,
    value_proc: Optional[Callable[[Optional[str]], Any]] = ...,
    prompt_suffix: str = ...,
    show_default: bool = ...,
    err: bool = ...,
) -> Any: ...
def secho(
    message: Optional[Any] = ...,
    file: Optional[IO[Any]] = ...,
    nl: bool = ...,
    err: bool = ...,
    color: Optional[bool] = ...,
    **styles: Any,
) -> None: ...
def style(
    text: str,
    fg: Optional[str] = ...,
    bg: Optional[str] = ...,
    bold: Optional[bool] = ...,
    dim: Optional[bool] = ...,
    underline: Optional[bool] = ...,
    blink: Optional[bool] = ...,
    reverse: Optional[bool] = ...,
    reset: bool = ...,
) -> str: ...
def unstyle(text: str) -> str: ...
def echo(
    message: Optional[Any] = ...,
    file: Optional[IO[Any]] = ...,
    nl: bool = ...,
    err: bool = ...,
    color: Optional[bool] = ...,
) -> None: ...
def format_filename(filename: str, shorten: bool = ...) -> str: ...
def get_app_dir(app_name: str, roaming: bool = ..., force_posix: bool = ...) -> str: ...
def get_binary_stream(name: str) -> IO[bytes]: ...
def get_text_stream(name: str, encoding: Optional[str] = ..., errors: str = ...) -> TextIO: ...
def open_file(
    filename: str,
    mode: str = ...,
    encoding: Optional[str] = ...,
    errors: str = ...,
    lazy: bool = ...,
    atomic: bool = ...,
) -> Tuple[TextIO, bool]: ...