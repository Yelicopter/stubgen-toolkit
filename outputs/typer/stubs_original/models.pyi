import click.shell_completion
import io
from .core import TyperCommand as TyperCommand, TyperGroup as TyperGroup
from .main import Typer as Typer
from _typeshed import Incomplete
from typing import Any, Callable, Dict, List, Optional, Sequence, Type, TypeVar, Union

NoneType: Incomplete
AnyType = Type[Any]
Required: Incomplete

class Context(click.Context): ...
class FileText(io.TextIOWrapper): ...
class FileTextWrite(FileText): ...
class FileBinaryRead(io.BufferedReader): ...
class FileBinaryWrite(io.BufferedWriter): ...
class CallbackParam(click.Parameter): ...

class DefaultPlaceholder:
    value: Incomplete
    def __init__(self, value: Any) -> None: ...
    def __bool__(self) -> bool: ...
DefaultType = TypeVar('DefaultType')
CommandFunctionType = TypeVar('CommandFunctionType', bound=Callable[..., Any])

def Default(value: DefaultType) -> DefaultType: ...

class CommandInfo:
    name: Incomplete
    cls: Incomplete
    context_settings: Incomplete
    callback: Incomplete
    help: Incomplete
    epilog: Incomplete
    short_help: Incomplete
    options_metavar: Incomplete
    add_help_option: Incomplete
    no_args_is_help: Incomplete
    hidden: Incomplete
    deprecated: Incomplete
    rich_help_panel: Incomplete
    def __init__(self, name: Optional[str] = ..., *, cls: Optional[Type['TyperCommand']] = ..., context_settings: Optional[Dict[Any, Any]] = ..., callback: Optional[Callable[..., Any]] = ..., help: Optional[str] = ..., epilog: Optional[str] = ..., short_help: Optional[str] = ..., options_metavar: str = ..., add_help_option: bool = ..., no_args_is_help: bool = ..., hidden: bool = ..., deprecated: bool = ..., rich_help_panel: Union[str, None] = ...) -> None: ...

class TyperInfo:
    typer_instance: Incomplete
    name: Incomplete
    cls: Incomplete
    invoke_without_command: Incomplete
    no_args_is_help: Incomplete
    subcommand_metavar: Incomplete
    chain: Incomplete
    result_callback: Incomplete
    context_settings: Incomplete
    callback: Incomplete
    help: Incomplete
    epilog: Incomplete
    short_help: Incomplete
    options_metavar: Incomplete
    add_help_option: Incomplete
    hidden: Incomplete
    deprecated: Incomplete
    rich_help_panel: Incomplete
    def __init__(self, typer_instance: Optional['Typer'] = ..., *, name: Optional[str] = ..., cls: Optional[Type['TyperGroup']] = ..., invoke_without_command: bool = ..., no_args_is_help: bool = ..., subcommand_metavar: Optional[str] = ..., chain: bool = ..., result_callback: Optional[Callable[..., Any]] = ..., context_settings: Optional[Dict[Any, Any]] = ..., callback: Optional[Callable[..., Any]] = ..., help: Optional[str] = ..., epilog: Optional[str] = ..., short_help: Optional[str] = ..., options_metavar: str = ..., add_help_option: bool = ..., hidden: bool = ..., deprecated: bool = ..., rich_help_panel: Union[str, None] = ...) -> None: ...

class ParameterInfo:
    default: Incomplete
    param_decls: Incomplete
    callback: Incomplete
    metavar: Incomplete
    expose_value: Incomplete
    is_eager: Incomplete
    envvar: Incomplete
    shell_complete: Incomplete
    autocompletion: Incomplete
    default_factory: Incomplete
    parser: Incomplete
    click_type: Incomplete
    show_default: Incomplete
    show_choices: Incomplete
    show_envvar: Incomplete
    help: Incomplete
    hidden: Incomplete
    case_sensitive: Incomplete
    min: Incomplete
    max: Incomplete
    clamp: Incomplete
    formats: Incomplete
    mode: Incomplete
    encoding: Incomplete
    errors: Incomplete
    lazy: Incomplete
    atomic: Incomplete
    exists: Incomplete
    file_okay: Incomplete
    dir_okay: Incomplete
    writable: Incomplete
    readable: Incomplete
    resolve_path: Incomplete
    allow_dash: Incomplete
    path_type: Incomplete
    rich_help_panel: Incomplete
    def __init__(self, *, default: Optional[Any] = ..., param_decls: Optional[Sequence[str]] = ..., callback: Optional[Callable[..., Any]] = ..., metavar: Optional[str] = ..., expose_value: bool = ..., is_eager: bool = ..., envvar: Optional[Union[str, List[str]]] = ..., shell_complete: Optional[Callable[[click.Context, click.Parameter, str], Union[List['click.shell_completion.CompletionItem'], List[str]]]] = ..., autocompletion: Optional[Callable[..., Any]] = ..., default_factory: Optional[Callable[[], Any]] = ..., parser: Optional[Callable[[str], Any]] = ..., click_type: Optional[click.ParamType] = ..., show_default: Union[bool, str] = ..., show_choices: bool = ..., show_envvar: bool = ..., help: Optional[str] = ..., hidden: bool = ..., case_sensitive: bool = ..., min: Optional[Union[int, float]] = ..., max: Optional[Union[int, float]] = ..., clamp: bool = ..., formats: Optional[List[str]] = ..., mode: Optional[str] = ..., encoding: Optional[str] = ..., errors: Optional[str] = ..., lazy: Optional[bool] = ..., atomic: bool = ..., exists: bool = ..., file_okay: bool = ..., dir_okay: bool = ..., writable: bool = ..., readable: bool = ..., resolve_path: bool = ..., allow_dash: bool = ..., path_type: Union[None, Type[str], Type[bytes]] = ..., rich_help_panel: Union[str, None] = ...) -> None: ...

class OptionInfo(ParameterInfo):
    prompt: Incomplete
    confirmation_prompt: Incomplete
    prompt_required: Incomplete
    hide_input: Incomplete
    count: Incomplete
    allow_from_autoenv: Incomplete
    def __init__(self, *, default: Optional[Any] = ..., param_decls: Optional[Sequence[str]] = ..., callback: Optional[Callable[..., Any]] = ..., metavar: Optional[str] = ..., expose_value: bool = ..., is_eager: bool = ..., envvar: Optional[Union[str, List[str]]] = ..., shell_complete: Optional[Callable[[click.Context, click.Parameter, str], Union[List['click.shell_completion.CompletionItem'], List[str]]]] = ..., autocompletion: Optional[Callable[..., Any]] = ..., default_factory: Optional[Callable[[], Any]] = ..., parser: Optional[Callable[[str], Any]] = ..., click_type: Optional[click.ParamType] = ..., show_default: Union[bool, str] = ..., prompt: Union[bool, str] = ..., confirmation_prompt: bool = ..., prompt_required: bool = ..., hide_input: bool = ..., is_flag: Optional[bool] = ..., flag_value: Optional[Any] = ..., count: bool = ..., allow_from_autoenv: bool = ..., help: Optional[str] = ..., hidden: bool = ..., show_choices: bool = ..., show_envvar: bool = ..., case_sensitive: bool = ..., min: Optional[Union[int, float]] = ..., max: Optional[Union[int, float]] = ..., clamp: bool = ..., formats: Optional[List[str]] = ..., mode: Optional[str] = ..., encoding: Optional[str] = ..., errors: Optional[str] = ..., lazy: Optional[bool] = ..., atomic: bool = ..., exists: bool = ..., file_okay: bool = ..., dir_okay: bool = ..., writable: bool = ..., readable: bool = ..., resolve_path: bool = ..., allow_dash: bool = ..., path_type: Union[None, Type[str], Type[bytes]] = ..., rich_help_panel: Union[str, None] = ...) -> None: ...

class ArgumentInfo(ParameterInfo):
    def __init__(self, *, default: Optional[Any] = ..., param_decls: Optional[Sequence[str]] = ..., callback: Optional[Callable[..., Any]] = ..., metavar: Optional[str] = ..., expose_value: bool = ..., is_eager: bool = ..., envvar: Optional[Union[str, List[str]]] = ..., shell_complete: Optional[Callable[[click.Context, click.Parameter, str], Union[List['click.shell_completion.CompletionItem'], List[str]]]] = ..., autocompletion: Optional[Callable[..., Any]] = ..., default_factory: Optional[Callable[[], Any]] = ..., parser: Optional[Callable[[str], Any]] = ..., click_type: Optional[click.ParamType] = ..., show_default: Union[bool, str] = ..., show_choices: bool = ..., show_envvar: bool = ..., help: Optional[str] = ..., hidden: bool = ..., case_sensitive: bool = ..., min: Optional[Union[int, float]] = ..., max: Optional[Union[int, float]] = ..., clamp: bool = ..., formats: Optional[List[str]] = ..., mode: Optional[str] = ..., encoding: Optional[str] = ..., errors: Optional[str] = ..., lazy: Optional[bool] = ..., atomic: bool = ..., exists: bool = ..., file_okay: bool = ..., dir_okay: bool = ..., writable: bool = ..., readable: bool = ..., resolve_path: bool = ..., allow_dash: bool = ..., path_type: Union[None, Type[str], Type[bytes]] = ..., rich_help_panel: Union[str, None] = ...) -> None: ...

class ParamMeta:
    empty: Incomplete
    name: Incomplete
    default: Incomplete
    annotation: Incomplete
    def __init__(self, *, name: str, default: Any = ..., annotation: Any = ...) -> None: ...

class DeveloperExceptionConfig:
    pretty_exceptions_enable: Incomplete
    pretty_exceptions_show_locals: Incomplete
    pretty_exceptions_short: Incomplete
    def __init__(self, *, pretty_exceptions_enable: bool = ..., pretty_exceptions_show_locals: bool = ..., pretty_exceptions_short: bool = ...) -> None: ...

class TyperPath(click.Path):
    def shell_complete(self, ctx: click.Context, param: click.Parameter, incomplete: str) -> List[click.shell_completion.CompletionItem]: ...
