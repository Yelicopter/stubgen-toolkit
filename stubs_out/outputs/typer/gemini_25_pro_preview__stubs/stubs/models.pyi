import click.shell_completion
import io
from .main import Typer as Typer
from typing import Any, Callable, Dict, List, Optional, Sequence, Type, TypeVar, Union

NoneType: Type[None]
AnyType: Type[Any]
Required: Any

class Context(click.Context): ...
class FileText(io.TextIOWrapper): ...
class FileTextWrite(FileText): ...
class FileBinaryRead(io.BufferedReader): ...
class FileBinaryWrite(io.BufferedWriter): ...
class CallbackParam(click.Parameter): ...
DefaultType = TypeVar('DefaultType')
CommandFunctionType = TypeVar('CommandFunctionType', bound=Callable[..., Any])

class DefaultPlaceholder(Generic[DefaultType]):
    value: DefaultType
    def __init__(self, value: DefaultType) -> None: ...
    def __bool__(self) -> bool: ...

def Default(value: DefaultType) -> DefaultPlaceholder[DefaultType]: ...

class CommandInfo:
    name: Optional[str]
    cls: Optional[Type[TyperCommand]]
    context_settings: Optional[Dict[str, Any]]
    callback: Optional[Callable[..., Any]]
    help: Optional[str]
    epilog: Optional[str]
    short_help: Optional[str]
    options_metavar: str
    add_help_option: bool
    no_args_is_help: bool
    hidden: bool
    deprecated: bool
    rich_help_panel: Optional[str]
    def __init__(self, name: Optional[str] = ..., *, cls: Optional[Type[TyperCommand]] = ..., context_settings: Optional[Dict[str, Any]] = ..., callback: Optional[Callable[..., Any]] = ..., help: Optional[str] = ..., epilog: Optional[str] = ..., short_help: Optional[str] = ..., options_metavar: str = ..., add_help_option: bool = ..., no_args_is_help: bool = ..., hidden: bool = ..., deprecated: bool = ..., rich_help_panel: Optional[str] = ...) -> None: ...

class TyperInfo:
    typer_instance: Optional[Typer]
    name: DefaultPlaceholder[Optional[str]]
    cls: DefaultPlaceholder[Optional[Type[TyperGroup]]]
    invoke_without_command: DefaultPlaceholder[bool]
    no_args_is_help: DefaultPlaceholder[bool]
    subcommand_metavar: DefaultPlaceholder[Optional[str]]
    chain: DefaultPlaceholder[bool]
    result_callback: DefaultPlaceholder[Optional[Callable[..., Any]]]
    context_settings: DefaultPlaceholder[Optional[Dict[str, Any]]]
    callback: DefaultPlaceholder[Optional[Callable[..., Any]]]
    help: DefaultPlaceholder[Optional[str]]
    epilog: DefaultPlaceholder[Optional[str]]
    short_help: DefaultPlaceholder[Optional[str]]
    options_metavar: DefaultPlaceholder[str]
    add_help_option: DefaultPlaceholder[bool]
    hidden: DefaultPlaceholder[bool]
    deprecated: DefaultPlaceholder[bool]
    rich_help_panel: DefaultPlaceholder[Optional[str]]
    def __init__(self, typer_instance: Optional[Typer] = ..., *, name: DefaultPlaceholder[Optional[str]] = ..., cls: DefaultPlaceholder[Optional[Type[TyperGroup]]] = ..., invoke_without_command: DefaultPlaceholder[bool] = ..., no_args_is_help: DefaultPlaceholder[bool] = ..., subcommand_metavar: DefaultPlaceholder[Optional[str]] = ..., chain: DefaultPlaceholder[bool] = ..., result_callback: DefaultPlaceholder[Optional[Callable[..., Any]]] = ..., context_settings: DefaultPlaceholder[Optional[Dict[str, Any]]] = ..., callback: DefaultPlaceholder[Optional[Callable[..., Any]]] = ..., help: DefaultPlaceholder[Optional[str]] = ..., epilog: DefaultPlaceholder[Optional[str]] = ..., short_help: DefaultPlaceholder[Optional[str]] = ..., options_metavar: DefaultPlaceholder[str] = ..., add_help_option: DefaultPlaceholder[bool] = ..., hidden: DefaultPlaceholder[bool] = ..., deprecated: DefaultPlaceholder[bool] = ..., rich_help_panel: DefaultPlaceholder[Optional[str]] = ...) -> None: ...

class ParameterInfo:
    def __init__(self, *, default: Any = ..., param_decls: Optional[Sequence[str]] = ..., callback: Optional[Callable[..., Any]] = ..., metavar: Optional[str] = ..., expose_value: bool = ..., is_eager: bool = ..., envvar: Optional[Union[str, List[str]]] = ..., shell_complete: Optional[Callable[[click.Context, click.Parameter, str], Union[List[click.shell_completion.CompletionItem], List[str]]]] = ..., autocompletion: Optional[Callable[..., Any]] = ..., default_factory: Optional[Callable[[], Any]] = ..., parser: Optional[Callable[[Any], Any]] = ..., click_type: Optional[click.ParamType] = ..., show_default: Union[bool, str] = ..., show_choices: bool = ..., show_envvar: bool = ..., help: Optional[str] = ..., hidden: bool = ..., case_sensitive: bool = ..., min: Optional[Union[int, float]] = ..., max: Optional[Union[int, float]] = ..., clamp: bool = ..., formats: Optional[List[str]] = ..., mode: Optional[str] = ..., encoding: Optional[str] = ..., errors: str = ..., lazy: Optional[bool] = ..., atomic: bool = ..., exists: bool = ..., file_okay: bool = ..., dir_okay: bool = ..., writable: bool = ..., readable: bool = ..., resolve_path: bool = ..., allow_dash: bool = ..., path_type: Optional[Type[Any]] = ..., rich_help_panel: Optional[str] = ...) -> None: ...

class OptionInfo(ParameterInfo):
    def __init__(self, *, default: Any = ..., param_decls: Optional[Sequence[str]] = ..., callback: Optional[Callable[..., Any]] = ..., metavar: Optional[str] = ..., expose_value: bool = ..., is_eager: bool = ..., envvar: Optional[Union[str, List[str]]] = ..., shell_complete: Optional[Callable[[click.Context, click.Parameter, str], Union[List[click.shell_completion.CompletionItem], List[str]]]] = ..., autocompletion: Optional[Callable[..., Any]] = ..., default_factory: Optional[Callable[[], Any]] = ..., parser: Optional[Callable[[Any], Any]] = ..., click_type: Optional[click.ParamType] = ..., show_default: Union[bool, str] = ..., prompt: Union[bool, str] = ..., confirmation_prompt: bool = ..., prompt_required: bool = ..., hide_input: bool = ..., is_flag: Optional[bool] = ..., flag_value: Optional[Any] = ..., count: bool = ..., allow_from_autoenv: bool = ..., help: Optional[str] = ..., hidden: bool = ..., show_choices: bool = ..., show_envvar: bool = ..., case_sensitive: bool = ..., min: Optional[Union[int, float]] = ..., max: Optional[Union[int, float]] = ..., clamp: bool = ..., formats: Optional[List[str]] = ..., mode: Optional[str] = ..., encoding: Optional[str] = ..., errors: str = ..., lazy: Optional[bool] = ..., atomic: bool = ..., exists: bool = ..., file_okay: bool = ..., dir_okay: bool = ..., writable: bool = ..., readable: bool = ..., resolve_path: bool = ..., allow_dash: bool = ..., path_type: Optional[Type[Any]] = ..., rich_help_panel: Optional[str] = ...) -> None: ...

class ArgumentInfo(ParameterInfo):
    def __init__(self, *, default: Any = ..., param_decls: Optional[Sequence[str]] = ..., callback: Optional[Callable[..., Any]] = ..., metavar: Optional[str] = ..., expose_value: bool = ..., is_eager: bool = ..., envvar: Optional[Union[str, List[str]]] = ..., shell_complete: Optional[Callable[[click.Context, click.Parameter, str], Union[List[click.shell_completion.CompletionItem], List[str]]]] = ..., autocompletion: Optional[Callable[..., Any]] = ..., default_factory: Optional[Callable[[], Any]] = ..., parser: Optional[Callable[[Any], Any]] = ..., click_type: Optional[click.ParamType] = ..., show_default: Union[bool, str] = ..., show_choices: bool = ..., show_envvar: bool = ..., help: Optional[str] = ..., hidden: bool = ..., case_sensitive: bool = ..., min: Optional[Union[int, float]] = ..., max: Optional[Union[int, float]] = ..., clamp: bool = ..., formats: Optional[List[str]] = ..., mode: Optional[str] = ..., encoding: Optional[str] = ..., errors: str = ..., lazy: Optional[bool] = ..., atomic: bool = ..., exists: bool = ..., file_okay: bool = ..., dir_okay: bool = ..., writable: bool = ..., readable: bool = ..., resolve_path: bool = ..., allow_dash: bool = ..., path_type: Optional[Type[Any]] = ..., rich_help_panel: Optional[str] = ...) -> None: ...

class ParamMeta:
    empty: Any
    name: str
    default: Any
    annotation: Any
    def __init__(self, *, name: str, default: Any = ..., annotation: Any = ...) -> None: ...

class DeveloperExceptionConfig:
    pretty_exceptions_enable: bool
    pretty_exceptions_show_locals: bool
    pretty_exceptions_short: bool
    def __init__(self, *, pretty_exceptions_enable: bool = ..., pretty_exceptions_show_locals: bool = ..., pretty_exceptions_short: bool = ...) -> None: ...

class TyperPath(click.Path):
    def shell_complete(self, ctx: click.Context, param: click.Parameter, incomplete: str) -> List[click.shell_completion.CompletionItem]: ...
