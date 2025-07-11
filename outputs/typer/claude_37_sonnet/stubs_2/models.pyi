import inspect
import io
import os
from typing import Any, Callable, Dict, List, Optional, Sequence, Type, TypeVar, Union

import click
import click.shell_completion

NoneType: Type[None]
AnyType: Type[Any]
Required: Any

class Context(click.Context): ...
class FileText(io.TextIOWrapper): ...
class FileTextWrite(FileText): ...
class FileBinaryRead(io.BufferedReader): ...
class FileBinaryWrite(io.BufferedWriter): ...
class CallbackParam(click.Parameter): ...

class DefaultPlaceholder:
    value: Any
    def __init__(self, value: Any) -> None: ...
    def __bool__(self) -> bool: ...

DefaultType = TypeVar("DefaultType")
CommandFunctionType = TypeVar("CommandFunctionType", bound=Callable[..., Any])

def Default(value: DefaultType) -> DefaultType: ...

class CommandInfo:
    name: Optional[str]
    cls: Optional[Type[click.Command]]
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

    def __init__(
        self,
        name: Optional[str] = None,
        *,
        cls: Optional[Type[click.Command]] = None,
        context_settings: Optional[Dict[str, Any]] = None,
        callback: Optional[Callable[..., Any]] = None,
        help: Optional[str] = None,
        epilog: Optional[str] = None,
        short_help: Optional[str] = None,
        options_metavar: str = "[OPTIONS]",
        add_help_option: bool = True,
        no_args_is_help: bool = False,
        hidden: bool = False,
        deprecated: bool = False,
        rich_help_panel: Optional[str] = None,
    ) -> None: ...

class TyperInfo:
    typer_instance: Optional[Any]
    name: Any
    cls: Any
    invoke_without_command: Any
    no_args_is_help: Any
    subcommand_metavar: Any
    chain: Any
    result_callback: Any
    context_settings: Any
    callback: Any
    help: Any
    epilog: Any
    short_help: Any
    options_metavar: Any
    add_help_option: Any
    hidden: Any
    deprecated: Any
    rich_help_panel: Any

    def __init__(
        self,
        typer_instance: Any = Default(None),
        *,
        name: Any = Default(None),
        cls: Any = Default(None),
        invoke_without_command: bool = Default(False),
        no_args_is_help: bool = Default(False),
        subcommand_metavar: Any = Default(None),
        chain: bool = Default(False),
        result_callback: Any = Default(None),
        context_settings: Any = Default(None),
        callback: Any = Default(None),
        help: Any = Default(None),
        epilog: Any = Default(None),
        short_help: Any = Default(None),
        options_metavar: Any = Default("[OPTIONS]"),
        add_help_option: bool = Default(True),
        hidden: bool = Default(False),
        deprecated: bool = Default(False),
        rich_help_panel: Any = Default(None),
    ) -> None: ...

class ParameterInfo:
    default: Any
    param_decls: Optional[Sequence[str]]
    callback: Optional[Callable[..., Any]]
    metavar: Optional[str]
    expose_value: bool
    is_eager: bool
    envvar: Optional[Union[str, List[str]]]
    shell_complete: Optional[Callable[..., Any]]
    autocompletion: Optional[Callable[..., Any]]
    default_factory: Optional[Callable[[], Any]]
    parser: Optional[Callable[[str], Any]]
    click_type: Optional[click.types.ParamType]
    show_default: Union[bool, str]
    show_choices: bool
    show_envvar: bool
    help: Optional[str]
    hidden: bool
    case_sensitive: bool
    min: Optional[Union[int, float]]
    max: Optional[Union[int, float]]
    clamp: bool
    formats: Optional[List[str]]
    mode: Optional[str]
    encoding: Optional[str]
    errors: str
    lazy: Optional[bool]
    atomic: bool
    exists: bool
    file_okay: bool
    dir_okay: bool
    writable: bool
    readable: bool
    resolve_path: bool
    allow_dash: bool
    path_type: Optional[Type[os.PathLike]]
    rich_help_panel: Optional[str]

    def __init__(
        self,
        *,
        default: Any = None,
        param_decls: Optional[Sequence[str]] = None,
        callback: Optional[Callable[..., Any]] = None,
        metavar: Optional[str] = None,
        expose_value: bool = True,
        is_eager: bool = False,
        envvar: Optional[Union[str, List[str]]] = None,
        shell_complete: Optional[Callable[..., Any]] = None,
        autocompletion: Optional[Callable[..., Any]] = None,
        default_factory: Optional[Callable[[], Any]] = None,
        parser: Optional[Callable[[str], Any]] = None,
        click_type: Optional[click.types.ParamType] = None,
        show_default: Union[bool, str] = True,
        show_choices: bool = True,
        show_envvar: bool = True,
        help: Optional[str] = None,
        hidden: bool = False,
        case_sensitive: bool = True,
        min: Optional[Union[int, float]] = None,
        max: Optional[Union[int, float]] = None,
        clamp: bool = False,
        formats: Optional[List[str]] = None,
        mode: Optional[str] = None,
        encoding: Optional[str] = None,
        errors: str = "strict",
        lazy: Optional[bool] = None,
        atomic: bool = False,
        exists: bool = False,
        file_okay: bool = True,
        dir_okay: bool = True,
        writable: bool = False,
        readable: bool = True,
        resolve_path: bool = False,
        allow_dash: bool = False,
        path_type: Optional[Type[os.PathLike]] = None,
        rich_help_panel: Optional[str] = None,
    ) -> None: ...

class OptionInfo(ParameterInfo):
    prompt: Union[bool, str]
    confirmation_prompt: bool
    prompt_required: bool
    hide_input: bool
    count: bool
    allow_from_autoenv: bool

    def __init__(
        self,
        *,
        default: Any = None,
        param_decls: Optional[Sequence[str]] = None,
        callback: Optional[Callable[..., Any]] = None,
        metavar: Optional[str] = None,
        expose_value: bool = True,
        is_eager: bool = False,
        envvar: Optional[Union[str, List[str]]] = None,
        shell_complete: Optional[Callable[..., Any]] = None,
        autocompletion: Optional[Callable[..., Any]] = None,
        default_factory: Optional[Callable[[], Any]] = None,
        parser: Optional[Callable[[str], Any]] = None,
        click_type: Optional[click.types.ParamType] = None,
        show_default: Union[bool, str] = True,
        prompt: Union[bool, str] = False,
        confirmation_prompt: bool = False,
        prompt_required: bool = True,
        hide_input: bool = False,
        is_flag: Optional[bool] = None,
        flag_value: Any = None,
        count: bool = False,
        allow_from_autoenv: bool = True,
        help: Optional[str] = None,
        hidden: bool = False,
        show_choices: bool = True,
        show_envvar: bool = True,
        case_sensitive: bool = True,
        min: Optional[Union[int, float]] = None,
        max: Optional[Union[int, float]] = None,
        clamp: bool = False,
        formats: Optional[List[str]] = None,
        mode: Optional[str] = None,
        encoding: Optional[str] = None,
        errors: str = "strict",
        lazy: Optional[bool] = None,
        atomic: bool = False,
        exists: bool = False,
        file_okay: bool = True,
        dir_okay: bool = True,
        writable: bool = False,
        readable: bool = True,
        resolve_path: bool = False,
        allow_dash: bool = False,
        path_type: Optional[Type[os.PathLike]] = None,
        rich_help_panel: Optional[str] = None,
    ) -> None: ...

class ArgumentInfo(ParameterInfo):
    def __init__(
        self,
        *,
        default: Any = None,
        param_decls: Optional[Sequence[str]] = None,
        callback: Optional[Callable[..., Any]] = None,
        metavar: Optional[str] = None,
        expose_value: bool = True,
        is_eager: bool = False,
        envvar: Optional[Union[str, List[str]]] = None,
        shell_complete: Optional[Callable[..., Any]] = None,
        autocompletion: Optional[Callable[..., Any]] = None,
        default_factory: Optional[Callable[[], Any]] = None,
        parser: Optional[Callable[[str], Any]] = None,
        click_type: Optional[click.types.ParamType] = None,
        show_default: Union[bool, str] = True,
        show_choices: bool = True,
        show_envvar: bool = True,
        help: Optional[str] = None,
        hidden: bool = False,
        case_sensitive: bool = True,
        min: Optional[Union[int, float]] = None,
        max: Optional[Union[int, float]] = None,
        clamp: bool = False,
        formats: Optional[List[str]] = None,
        mode: Optional[str] = None,
        encoding: Optional[str] = None,
        errors: str = "strict",
        lazy: Optional[bool] = None,
        atomic: bool = False,
        exists: bool = False,
        file_okay: bool = True,
        dir_okay: bool = True,
        writable: bool = False,
        readable: bool = True,
        resolve_path: bool = False,
        allow_dash: bool = False,
        path_type: Optional[Type[os.PathLike]] = None,
        rich_help_panel: Optional[str] = None,
    ) -> None: ...

class ParamMeta:
    empty: Any
    name: str
    default: Any
    annotation: Any

    def __init__(
        self,
        *,
        name: str,
        default: Any = inspect.Parameter.empty,
        annotation: Any = inspect.Parameter.empty,
    ) -> None: ...

class DeveloperExceptionConfig:
    pretty_exceptions_enable: bool
    pretty_exceptions_show_locals: bool
    pretty_exceptions_short: bool

    def __init__(
        self,
        *,
        pretty_exceptions_enable: bool = True,
        pretty_exceptions_show_locals: bool = True,
        pretty_exceptions_short: bool = True,
    ) -> None: ...

class TyperPath(click.Path):
    def shell_complete(
        self, ctx: click.Context, param: click.Parameter, incomplete: str
    ) -> List[click.shell_completion.CompletionItem]: ...