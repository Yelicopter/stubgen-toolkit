from typing import Any, Callable, Dict, List, MutableMapping, Optional, Sequence, TextIO, Tuple, Union
import click

class TyperArgument(click.Argument):
    def __init__(
        self,
        *,
        param_decls: Any,
        type: Any = None,
        required: bool = None,
        default: Any = None,
        callback: Callable[..., Any] = None,
        nargs: Any = None,
        metavar: Any = None,
        expose_value: bool = True,
        is_eager: bool = False,
        envvar: Any = None,
        shell_complete: Callable[..., Any] = None,
        autocompletion: Callable[..., Any] = None,
        show_default: bool = True,
        show_choices: bool = True,
        show_envvar: bool = True,
        help: str = None,
        hidden: bool = False,
        rich_help_panel: str = None,
    ) -> None:
        ...

class TyperOption(click.Option):
    def __init__(
        self,
        *,
        param_decls: Any,
        type: Any = None,
        required: bool = None,
        default: Any = None,
        callback: Callable[..., Any] = None,
        nargs: Any = None,
        metavar: Any = None,
        expose_value: bool = True,
        is_eager: bool = False,
        envvar: Any = None,
        shell_complete: Callable[..., Any] = None,
        autocompletion: Callable[..., Any] = None,
        show_default: bool = False,
        prompt: bool = False,
        confirmation_prompt: bool = False,
        prompt_required: bool = True,
        hide_input: bool = False,
        is_flag: bool = None,
        multiple: bool = False,
        count: bool = False,
        allow_from_autoenv: bool = True,
        help: str = None,
        hidden: bool = False,
        show_choices: bool = True,
        show_envvar: bool = False,
        rich_help_panel: str = None,
    ) -> None:
        ...

class TyperCommand(click.Command):
    def __init__(
        self,
        name: str,
        *,
        context_settings: Any = None,
        callback: Callable[..., Any] = None,
        params: Any = None,
        help: str = None,
        epilog: str = None,
        short_help: str = None,
        options_metavar: str = "[OPTIONS]",
        add_help_option: bool = True,
        no_args_is_help: bool = False,
        hidden: bool = False,
        deprecated: bool = False,
        rich_markup_mode: str = None,
        rich_help_panel: str = None,
    ) -> None:
        ...

class TyperGroup(click.Group):
    def __init__(
        self,
        *,
        name: str = None,
        commands: Any = None,
        rich_markup_mode: str = None,
        rich_help_panel: str = None,
        **attrs: Any,
    ) -> None:
        ...