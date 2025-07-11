import sys
import os
import errno
import inspect
from enum import Enum
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

from ._typing import Literal

MarkupMode = Literal["markdown", "rich", None]

def _split_opt(opt: str) -> tuple[str, str]: ...
def _typer_param_setup_autocompletion_compat(
    self: Any,
    *,
    autocompletion: Any = ...,
) -> None: ...
def _get_default_string(
    obj: Any,
    *,
    ctx: Any,
    show_default_is_str: bool,
    default_value: Any,
) -> str: ...
def _extract_default_help_str(
    obj: Any, *, ctx: Any
) -> Any: ...
def _main(
    self: Any,
    *,
    args: Optional[Sequence[str]] = ...,
    prog_name: Optional[str] = ...,
    complete_var: Optional[str] = ...,
    standalone_mode: bool = ...,
    windows_expand_args: bool = ...,
    rich_markup_mode: Any = ...,
    **extra: Any,
) -> Any: ...

class TyperArgument(click.core.Argument):
    help: Any
    show_default: Any
    show_choices: Any
    show_envvar: Any
    hidden: Any
    rich_help_panel: Any
    def __init__(
        self,
        *,
        param_decls: Any,
        type: Any = ...,
        required: Any = ...,
        default: Any = ...,
        callback: Any = ...,
        nargs: Any = ...,
        metavar: Any = ...,
        expose_value: Any = ...,
        is_eager: Any = ...,
        envvar: Any = ...,
        shell_complete: Any = ...,
        autocompletion: Any = ...,
        show_default: Any = ...,
        show_choices: Any = ...,
        show_envvar: Any = ...,
        help: Any = ...,
        hidden: Any = ...,
        rich_help_panel: Any = ...,
    ) -> None: ...
    def _get_default_string(
        self,
        *,
        ctx: Any,
        show_default_is_str: bool,
        default_value: Any,
    ) -> str: ...
    def _extract_default_help_str(
        self, *, ctx: Any
    ) -> Any: ...
    def get_help_record(self, ctx: Any) -> Optional[tuple[str, str]]: ...
    def make_metavar(self, ctx: Any = ...) -> str: ...

class TyperOption(click.core.Option):
    rich_help_panel: Any
    def __init__(
        self,
        *,
        param_decls: Any,
        type: Any = ...,
        required: Any = ...,
        default: Any = ...,
        callback: Any = ...,
        nargs: Any = ...,
        metavar: Any = ...,
        expose_value: Any = ...,
        is_eager: Any = ...,
        envvar: Any = ...,
        shell_complete: Any = ...,
        autocompletion: Any = ...,
        show_default: Any = ...,
        prompt: Any = ...,
        confirmation_prompt: Any = ...,
        prompt_required: Any = ...,
        hide_input: Any = ...,
        is_flag: Any = ...,
        multiple: Any = ...,
        count: Any = ...,
        allow_from_autoenv: Any = ...,
        help: Any = ...,
        hidden: Any = ...,
        show_choices: Any = ...,
        show_envvar: Any = ...,
        rich_help_panel: Any = ...,
    ) -> None: ...
    def _get_default_string(
        self,
        *,
        ctx: Any,
        show_default_is_str: bool,
        default_value: Any,
    ) -> str: ...
    def _extract_default_help_str(
        self, *, ctx: Any
    ) -> Any: ...
    def make_metavar(self, ctx: Any = ...) -> str: ...
    def get_help_record(self, ctx: Any) -> Optional[tuple[str, str]]: ...

def _typer_format_options(
    self: Any, *, ctx: Any, formatter: Any
) -> None: ...
def _typer_main_shell_completion(
    self: Any,
    *,
    ctx_args: Any,
    prog_name: str,
    complete_var: Any = ...,
) -> None: ...

class TyperCommand(click.core.Command):
    rich_markup_mode: Any
    rich_help_panel: Any
    def __init__(
        self,
        name: str,
        *,
        context_settings: Any = ...,
        callback: Any = ...,
        params: Any = ...,
        help: Any = ...,
        epilog: Any = ...,
        short_help: Any = ...,
        options_metavar: Any = ...,
        add_help_option: Any = ...,
        no_args_is_help: Any = ...,
        hidden: Any = ...,
        deprecated: Any = ...,
        rich_markup_mode: Any = ...,
        rich_help_panel: Any = ...,
    ) -> None: ...
    def format_options(
        self, ctx: Any, formatter: Any
    ) -> None: ...
    def _main_shell_completion(
        self,
        ctx_args: Any,
        prog_name: str,
        complete_var: Any = ...,
    ) -> None: ...
    def main(
        self,
        args: Any = ...,
        prog_name: Any = ...,
        complete_var: Any = ...,
        standalone_mode: Any = ...,
        windows_expand_args: Any = ...,
        **extra: Any,
    ) -> Any: ...
    def format_help(self, ctx: Any, formatter: Any) -> Any: ...

class TyperGroup(click.core.Group):
    rich_markup_mode: Any
    rich_help_panel: Any
    def __init__(
        self,
        *,
        name: Any = ...,
        commands: Any = ...,
        rich_markup_mode: Any = ...,
        rich_help_panel: Any = ...,
        **attrs: Any,
    ) -> None: ...
    def format_options(
        self, ctx: Any, formatter: Any
    ) -> None: ...
    def _main_shell_completion(
        self,
        ctx_args: Any,
        prog_name: str,
        complete_var: Any = ...,
    ) -> None: ...
    def main(
        self,
        args: Any = ...,
        prog_name: Any = ...,
        complete_var: Any = ...,
        standalone_mode: Any = ...,
        windows_expand_args: Any = ...,
        **extra: Any,
    ) -> Any: ...
    def format_help(self, ctx: Any, formatter: Any) -> Any: ...
    def list_commands(self, ctx: Any) -> list[str]: ...