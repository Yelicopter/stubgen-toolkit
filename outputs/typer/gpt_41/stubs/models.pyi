import inspect
import io
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Dict,
    List,
    Optional,
    Sequence,
    Type,
    TypeVar,
    Union,
)

import click

if TYPE_CHECKING:
    from .core import TyperCommand, TyperGroup
    from .main import Typer

NoneType: type

AnyType: type

Required: Any

class Context(click.Context):
    ...

class FileText(io.TextIOWrapper):
    ...

class FileTextWrite(FileText):
    ...

class FileBinaryRead(io.BufferedReader):
    ...

class FileBinaryWrite(io.BufferedWriter):
    ...

class CallbackParam(click.Parameter):
    ...

class DefaultPlaceholder:
    value: Any
    def __init__(self, value: Any) -> None: ...
    def __bool__(self) -> bool: ...

DefaultType = TypeVar("DefaultType")
CommandFunctionType = TypeVar("CommandFunctionType", bound=Callable[..., Any])

def Default(value: Any) -> DefaultPlaceholder: ...

class CommandInfo:
    name: Any
    cls: Any
    context_settings: Any
    callback: Any
    help: Any
    epilog: Any
    short_help: Any
    options_metavar: Any
    add_help_option: Any
    no_args_is_help: Any
    hidden: Any
    deprecated: Any
    rich_help_panel: Any
    def __init__(
        self,
        name: Any = ...,
        *,
        cls: Any = ...,
        context_settings: Any = ...,
        callback: Any = ...,
        help: Any = ...,
        epilog: Any = ...,
        short_help: Any = ...,
        options_metavar: Any = ...,
        add_help_option: Any = ...,
        no_args_is_help: Any = ...,
        hidden: Any = ...,
        deprecated: Any = ...,
        rich_help_panel: Any = ...,
    ) -> None: ...

class TyperInfo:
    typer_instance: Any
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
        typer_instance: Any = ...,
        *,
        name: Any = ...,
        cls: Any = ...,
        invoke_without_command: Any = ...,
        no_args_is_help: Any = ...,
        subcommand_metavar: Any = ...,
        chain: Any = ...,
        result_callback: Any = ...,
        context_settings: Any = ...,
        callback: Any = ...,
        help: Any = ...,
        epilog: Any = ...,
        short_help: Any = ...,
        options_metavar: Any = ...,
        add_help_option: Any = ...,
        hidden: Any = ...,
        deprecated: Any = ...,
        rich_help_panel: Any = ...,
    ) -> None: ...

class ParameterInfo:
    default: Any
    param_decls: Any
    callback: Any
    metavar: Any
    expose_value: Any
    is_eager: Any
    envvar: Any
    shell_complete: Any
    autocompletion: Any
    default_factory: Any
    parser: Any
    click_type: Any
    show_default: Any
    show_choices: Any
    show_envvar: Any
    help: Any
    hidden: Any
    case_sensitive: Any
    min: Any
    max: Any
    clamp: Any
    formats: Any
    mode: Any
    encoding: Any
    errors: Any
    lazy: Any
    atomic: Any
    exists: Any
    file_okay: Any
    dir_okay: Any
    writable: Any
    readable: Any
    resolve_path: Any
    allow_dash: Any
    path_type: Any
    rich_help_panel: Any
    def __init__(
        self,
        *,
        default: Any = ...,
        param_decls: Any = ...,
        callback: Any = ...,
        metavar: Any = ...,
        expose_value: Any = ...,
        is_eager: Any = ...,
        envvar: Any = ...,
        shell_complete: Any = ...,
        autocompletion: Any = ...,
        default_factory: Any = ...,
        parser: Any = ...,
        click_type: Any = ...,
        show_default: Any = ...,
        show_choices: Any = ...,
        show_envvar: Any = ...,
        help: Any = ...,
        hidden: Any = ...,
        case_sensitive: Any = ...,
        min: Any = ...,
        max: Any = ...,
        clamp: Any = ...,
        formats: Any = ...,
        mode: Any = ...,
        encoding: Any = ...,
        errors: Any = ...,
        lazy: Any = ...,
        atomic: Any = ...,
        exists: Any = ...,
        file_okay: Any = ...,
        dir_okay: Any = ...,
        writable: Any = ...,
        readable: Any = ...,
        resolve_path: Any = ...,
        allow_dash: Any = ...,
        path_type: Any = ...,
        rich_help_panel: Any = ...,
    ) -> None: ...

class OptionInfo(ParameterInfo):
    prompt: Any
    confirmation_prompt: Any
    prompt_required: Any
    hide_input: Any
    count: Any
    allow_from_autoenv: Any
    def __init__(
        self,
        *,
        default: Any = ...,
        param_decls: Any = ...,
        callback: Any = ...,
        metavar: Any = ...,
        expose_value: Any = ...,
        is_eager: Any = ...,
        envvar: Any = ...,
        shell_complete: Any = ...,
        autocompletion: Any = ...,
        default_factory: Any = ...,
        parser: Any = ...,
        click_type: Any = ...,
        show_default: Any = ...,
        prompt: Any = ...,
        confirmation_prompt: Any = ...,
        prompt_required: Any = ...,
        hide_input: Any = ...,
        is_flag: Any = ...,
        flag_value: Any = ...,
        count: Any = ...,
        allow_from_autoenv: Any = ...,
        help: Any = ...,
        hidden: Any = ...,
        show_choices: Any = ...,
        show_envvar: Any = ...,
        case_sensitive: Any = ...,
        min: Any = ...,
        max: Any = ...,
        clamp: Any = ...,
        formats: Any = ...,
        mode: Any = ...,
        encoding: Any = ...,
        errors: Any = ...,
        lazy: Any = ...,
        atomic: Any = ...,
        exists: Any = ...,
        file_okay: Any = ...,
        dir_okay: Any = ...,
        writable: Any = ...,
        readable: Any = ...,
        resolve_path: Any = ...,
        allow_dash: Any = ...,
        path_type: Any = ...,
        rich_help_panel: Any = ...,
    ) -> None: ...

class ArgumentInfo(ParameterInfo):
    def __init__(
        self,
        *,
        default: Any = ...,
        param_decls: Any = ...,
        callback: Any = ...,
        metavar: Any = ...,
        expose_value: Any = ...,
        is_eager: Any = ...,
        envvar: Any = ...,
        shell_complete: Any = ...,
        autocompletion: Any = ...,
        default_factory: Any = ...,
        parser: Any = ...,
        click_type: Any = ...,
        show_default: Any = ...,
        show_choices: Any = ...,
        show_envvar: Any = ...,
        help: Any = ...,
        hidden: Any = ...,
        case_sensitive: Any = ...,
        min: Any = ...,
        max: Any = ...,
        clamp: Any = ...,
        formats: Any = ...,
        mode: Any = ...,
        encoding: Any = ...,
        errors: Any = ...,
        lazy: Any = ...,
        atomic: Any = ...,
        exists: Any = ...,
        file_okay: Any = ...,
        dir_okay: Any = ...,
        writable: Any = ...,
        readable: Any = ...,
        resolve_path: Any = ...,
        allow_dash: Any = ...,
        path_type: Any = ...,
        rich_help_panel: Any = ...,
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
        default: Any = ...,
        annotation: Any = ...,
    ) -> None: ...

class DeveloperExceptionConfig:
    pretty_exceptions_enable: bool
    pretty_exceptions_show_locals: bool
    pretty_exceptions_short: bool
    def __init__(
        self,
        *,
        pretty_exceptions_enable: bool = ...,
        pretty_exceptions_show_locals: bool = ...,
        pretty_exceptions_short: bool = ...,
    ) -> None: ...

class TyperPath(click.Path):
    def shell_complete(
        self, ctx: Any, param: Any, incomplete: str
    ) -> list[Any]: ...