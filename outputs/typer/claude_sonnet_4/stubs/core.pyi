import errno
import inspect
import os
import sys
from enum import Enum
from gettext import gettext as _
from typing import (
    Any,
    Callable,
    Dict,
    List,
    MutableMapping,
    Optional,
    Sequence,
    TextIO,
    Tuple,
    Union,
    cast,
)
import click
import click.core
import click.formatting
import click.parser
import click.shell_completion
import click.types
import click.utils
from ._typing import Literal

MarkupMode = Literal["markdown", "rich", None]

try:
    import rich
    from . import rich_utils
    DEFAULT_MARKUP_MODE: MarkupMode
except ImportError:
    rich = None
    DEFAULT_MARKUP_MODE: MarkupMode

def _split_opt(opt: str) -> Tuple[str, str]: ...

def _typer_param_setup_autocompletion_compat(
    self: click.Parameter,
    *,
    autocompletion: Optional[Callable[..., Any]] = None,
) -> None: ...

def _get_default_string(
    obj: Union["TyperOption", "TyperArgument"],
    *,
    ctx: click.Context,
    show_default_is_str: bool,
    default_value: Any,
) -> str: ...

def _extract_default_help_str(
    obj: Union["TyperOption", "TyperArgument"], *, ctx: click.Context
) -> Any: ...

def _main(
    self: click.Command,
    *,
    args: Optional[Sequence[str]] = None,
    prog_name: Optional[str] = None,
    complete_var: Optional[str] = None,
    standalone_mode: bool = True,
    windows_expand_args: bool = True,
    rich_markup_mode: MarkupMode = DEFAULT_MARKUP_MODE,
    **extra: Any,
) -> Any: ...

class TyperArgument(click.core.Argument):
    help: Optional[str]
    show_default: Union[bool, str]
    show_choices: bool
    show_envvar: bool
    hidden: bool
    rich_help_panel: Optional[str]
    
    def __init__(
        self,
        *,
        param_decls: Sequence[str],
        type: Optional[click.types.ParamType] = None,
        required: Optional[bool] = None,
        default: Any = None,
        callback: Optional[Callable[..., Any]] = None,
        nargs: Optional[int] = None,
        metavar: Optional[str] = None,
        expose_value: bool = True,
        is_eager: bool = False,
        envvar: Optional[Union[str, Sequence[str]]] = None,
        shell_complete: Optional[Callable[..., Any]] = None,
        autocompletion: Optional[Callable[..., Any]] = None,
        show_default: Union[bool, str] = True,
        show_choices: bool = True,
        show_envvar: bool = True,
        help: Optional[str] = None,
        hidden: bool = False,
        rich_help_panel: Optional[str] = None,
    ) -> None: ...
    
    def _get_default_string(
        self,
        *,
        ctx: click.Context,
        show_default_is_str: bool,
        default_value: Any,
    ) -> str: ...
    
    def _extract_default_help_str(
        self, *, ctx: click.Context
    ) -> Any: ...
    
    def get_help_record(self, ctx: click.Context) -> Optional[Tuple[str, str]]: ...
    def make_metavar(self, ctx: Optional[click.Context] = None) -> str: ...

class TyperOption(click.core.Option):
    rich_help_panel: Optional[str]
    
    def __init__(
        self,
        *,
        param_decls: Sequence[str],
        type: Optional[click.types.ParamType] = None,
        required: Optional[bool] = None,
        default: Any = None,
        callback: Optional[Callable[..., Any]] = None,
        nargs: Optional[int] = None,
        metavar: Optional[str] = None,
        expose_value: bool = True,
        is_eager: bool = False,
        envvar: Optional[Union[str, Sequence[str]]] = None,
        shell_complete: Optional[Callable[..., Any]] = None,
        autocompletion: Optional[Callable[..., Any]] = None,
        show_default: Union[bool, str] = False,
        prompt: Union[bool, str] = False,
        confirmation_prompt: Union[bool, str] = False,
        prompt_required: bool = True,
        hide_input: bool = False,
        is_flag: Optional[bool] = None,
        multiple: bool = False,
        count: bool = False,
        allow_from_autoenv: bool = True,
        help: Optional[str] = None,
        hidden: bool = False,
        show_choices: bool = True,
        show_envvar: bool = False,
        rich_help_panel: Optional[str] = None,
    ) -> None: ...
    
    def _get_default_string(
        self,
        *,
        ctx: click.Context,
        show_default_is_str: bool,
        default_value: Any,
    ) -> str: ...
    
    def _extract_default_help_str(
        self, *, ctx: click.Context
    ) -> Any: ...
    
    def make_metavar(self, ctx: Optional[click.Context] = None) -> str: ...
    def get_help_record(self, ctx: click.Context) -> Optional[Tuple[str, str]]: ...

def _typer_format_options(
    self: click.Command, *, ctx: click.Context, formatter: click.formatting.HelpFormatter
) -> None: ...

def _typer_main_shell_completion(
    self: click.Command,
    *,
    ctx_args: MutableMapping[str, Any],
    prog_name: str,
    complete_var: Optional[str] = None,
) -> None: ...

class TyperCommand(click.core.Command):
    rich_markup_mode: MarkupMode
    rich_help_panel: Optional[str]
    
    def __init__(
        self,
        name: Optional[str],
        *,
        context_settings: Optional[Dict[str, Any]] = None,
        callback: Optional[Callable[..., Any]] = None,
        params: Optional[List[click.Parameter]] = None,
        help: Optional[str] = None,
        epilog: Optional[str] = None,
        short_help: Optional[str] = None,
        options_metavar: Optional[str] = "[OPTIONS]",
        add_help_option: bool = True,
        no_args_is_help: bool = False,
        hidden: bool = False,
        deprecated: bool = False,
        rich_markup_mode: MarkupMode = DEFAULT_MARKUP_MODE,
        rich_help_panel: Optional[str] = None,
    ) -> None: ...
    
    def format_options(
        self, ctx: click.Context, formatter: click.formatting.HelpFormatter
    ) -> None: ...
    
    def _main_shell_completion(
        self,
        ctx_args: MutableMapping[str, Any],
        prog_name: str,
        complete_var: Optional[str] = None,
    ) -> None: ...
    
    def main(
        self,
        args: Optional[Sequence[str]] = None,
        prog_name: Optional[str] = None,
        complete_var: Optional[str] = None,
        standalone_mode: bool = True,
        windows_expand_args: bool = True,
        **extra: Any,
    ) -> Any: ...
    
    def format_help(self, ctx: click.Context, formatter: click.formatting.HelpFormatter) -> None: ...

class TyperGroup(click.core.Group):
    rich_markup_mode: MarkupMode
    rich_help_panel: Optional[str]
    
    def __init__(
        self,
        *,
        name: Optional[str] = None,
        commands: Optional[Dict[str, click.Command]] = None,
        rich_markup_mode: MarkupMode = DEFAULT_MARKUP_MODE,
        rich_help_panel: Optional[str] = None,
        **attrs: Any,
    ) -> None: ...
    
    def format_options(
        self, ctx: click.Context, formatter: click.formatting.HelpFormatter
    ) -> None: ...
    
    def _main_shell_completion(
        self,
        ctx_args: MutableMapping[str, Any],
        prog_name: str,
        complete_var: Optional[str] = None,
    ) -> None: ...
    
    def main(
        self,
        args: Optional[Sequence[str]] = None,
        prog_name: Optional[str] = None,
        complete_var: Optional[str] = None,
        standalone_mode: bool = True,
        windows_expand_args: bool = True,
        **extra: Any,
    ) -> Any: ...
    
    def format_help(self, ctx: click.Context, formatter: click.formatting.HelpFormatter) -> None: ...
    def list_commands(self, ctx: click.Context) -> List[str]: ...