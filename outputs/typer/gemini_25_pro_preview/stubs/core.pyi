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
)

import click
import click.core
import click.formatting
import click.shell_completion
import click.types
import click.utils
from typing_extensions import Literal

MarkupMode = Literal["markdown", "rich", None]
DEFAULT_MARKUP_MODE: MarkupMode

def _split_opt(opt: str) -> Tuple[str, str]: ...
def _typer_param_setup_autocompletion_compat(
    self: click.Parameter, *, autocompletion: Optional[Callable[..., Any]] = ...
) -> None: ...
def _get_default_string(
    obj: click.Option,
    *,
    ctx: click.Context,
    show_default_is_str: bool,
    default_value: Any,
) -> str: ...
def _extract_default_help_str(obj: click.Option, *, ctx: click.Context) -> Any: ...
def _main(
    self: click.Command,
    *,
    args: Optional[Sequence[str]] = ...,
    prog_name: Optional[str] = ...,
    complete_var: Optional[str] = ...,
    standalone_mode: bool = ...,
    windows_expand_args: bool = ...,
    rich_markup_mode: MarkupMode = ...,
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
        type: Optional[Any] = ...,
        required: Optional[bool] = ...,
        default: Optional[Any] = ...,
        callback: Optional[Callable[..., Any]] = ...,
        nargs: Optional[int] = ...,
        metavar: Optional[str] = ...,
        expose_value: bool = ...,
        is_eager: bool = ...,
        envvar: Optional[Union[str, List[str]]] = ...,
        shell_complete: Optional[
            Callable[
                [click.Context, click.Parameter, str],
                Union[List[click.shell_completion.CompletionItem], List[str]],
            ]
        ] = ...,
        autocompletion: Optional[Callable[..., Any]] = ...,
        show_default: Union[bool, str] = ...,
        show_choices: bool = ...,
        show_envvar: bool = ...,
        help: Optional[str] = ...,
        hidden: bool = ...,
        rich_help_panel: Optional[str] = ...,
    ) -> None: ...
    def _get_default_string(
        self, *, ctx: click.Context, show_default_is_str: bool, default_value: Any
    ) -> str: ...
    def _extract_default_help_str(self, *, ctx: click.Context) -> Any: ...
    def get_help_record(self, ctx: click.Context) -> Optional[Tuple[str, str]]: ...
    def make_metavar(self, ctx: Optional[click.Context] = ...) -> str: ...

class TyperOption(click.core.Option):
    rich_help_panel: Optional[str]
    def __init__(
        self,
        *,
        param_decls: Sequence[str],
        type: Optional[Any] = ...,
        required: Optional[bool] = ...,
        default: Optional[Any] = ...,
        callback: Optional[Callable[..., Any]] = ...,
        nargs: Optional[int] = ...,
        metavar: Optional[str] = ...,
        expose_value: bool = ...,
        is_eager: bool = ...,
        envvar: Optional[Union[str, List[str]]] = ...,
        shell_complete: Optional[
            Callable[
                [click.Context, click.Parameter, str],
                Union[List[click.shell_completion.CompletionItem], List[str]],
            ]
        ] = ...,
        autocompletion: Optional[Callable[..., Any]] = ...,
        show_default: Union[bool, str] = ...,
        prompt: Union[bool, str] = ...,
        confirmation_prompt: bool = ...,
        prompt_required: bool = ...,
        hide_input: bool = ...,
        is_flag: Optional[bool] = ...,
        multiple: bool = ...,
        count: bool = ...,
        allow_from_autoenv: bool = ...,
        help: Optional[str] = ...,
        hidden: bool = ...,
        show_choices: bool = ...,
        show_envvar: bool = ...,
        rich_help_panel: Optional[str] = ...,
    ) -> None: ...
    def _get_default_string(
        self, *, ctx: click.Context, show_default_is_str: bool, default_value: Any
    ) -> str: ...
    def _extract_default_help_str(self, *, ctx: click.Context) -> Any: ...
    def make_metavar(self, ctx: Optional[click.Context] = ...) -> str: ...
    def get_help_record(self, ctx: click.Context) -> Optional[Tuple[str, str]]: ...

def _typer_format_options(
    self: click.Command, *, ctx: click.Context, formatter: click.formatting.HelpFormatter
) -> None: ...
def _typer_main_shell_completion(
    self: click.Command,
    *,
    ctx_args: MutableMapping[str, Any],
    prog_name: str,
    complete_var: Optional[str] = ...,
) -> None: ...

class TyperCommand(click.core.Command):
    rich_markup_mode: MarkupMode
    rich_help_panel: Optional[str]
    def __init__(
        self,
        name: Optional[str],
        *,
        context_settings: Optional[Dict[str, Any]] = ...,
        callback: Optional[Callable[..., Any]] = ...,
        params: Optional[List[click.Parameter]] = ...,
        help: Optional[str] = ...,
        epilog: Optional[str] = ...,
        short_help: Optional[str] = ...,
        options_metavar: str = ...,
        add_help_option: bool = ...,
        no_args_is_help: bool = ...,
        hidden: bool = ...,
        deprecated: bool = ...,
        rich_markup_mode: MarkupMode = ...,
        rich_help_panel: Optional[str] = ...,
    ) -> None: ...
    def format_options(
        self, ctx: click.Context, formatter: click.formatting.HelpFormatter
    ) -> None: ...
    def _main_shell_completion(
        self,
        ctx_args: MutableMapping[str, Any],
        prog_name: str,
        complete_var: Optional[str] = ...,
    ) -> None: ...
    def main(
        self,
        args: Optional[Sequence[str]] = ...,
        prog_name: Optional[str] = ...,
        complete_var: Optional[str] = ...,
        standalone_mode: bool = ...,
        windows_expand_args: bool = ...,
        **extra: Any,
    ) -> Any: ...
    def format_help(
        self, ctx: click.Context, formatter: click.formatting.HelpFormatter
    ) -> None: ...

class TyperGroup(click.core.Group):
    rich_markup_mode: MarkupMode
    rich_help_panel: Optional[str]
    def __init__(
        self,
        *,
        name: Optional[str] = ...,
        commands: Optional[Union[Dict[str, click.Command], Sequence[click.Command]]] = ...,
        rich_markup_mode: MarkupMode = ...,
        rich_help_panel: Optional[str] = ...,
        **attrs: Any,
    ) -> None: ...
    def format_options(
        self, ctx: click.Context, formatter: click.formatting.HelpFormatter
    ) -> None: ...
    def _main_shell_completion(
        self,
        ctx_args: MutableMapping[str, Any],
        prog_name: str,
        complete_var: Optional[str] = ...,
    ) -> None: ...
    def main(
        self,
        args: Optional[Sequence[str]] = ...,
        prog_name: Optional[str] = ...,
        complete_var: Optional[str] = ...,
        standalone_mode: bool = ...,
        windows_expand_args: bool = ...,
        **extra: Any,
    ) -> Any: ...
    def format_help(
        self, ctx: click.Context, formatter: click.formatting.HelpFormatter
    ) -> None: ...
    def list_commands(self, ctx: click.Context) -> List[str]: ...