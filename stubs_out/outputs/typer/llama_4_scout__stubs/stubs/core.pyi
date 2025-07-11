import click
from typing import Any, Callable

class TyperArgument(click.core.Argument):
    def __init__(self, *, param_decls: Any, type: Any = ..., required: bool = ..., default: Any = ..., callback: Callable = ..., nargs: Any = ..., metavar: Any = ..., expose_value: bool = ..., is_eager: bool = ..., envvar: Any = ..., shell_complete: Callable = ..., autocompletion: Callable = ..., show_default: bool = ..., show_choices: bool = ..., show_envvar: bool = ..., help: str = ..., hidden: bool = ..., rich_help_panel: str = ...) -> None: ...

class TyperOption(click.core.Option):
    def __init__(self, *, param_decls: Any, type: Any = ..., required: bool = ..., default: Any = ..., callback: Callable = ..., nargs: Any = ..., metavar: Any = ..., expose_value: bool = ..., is_eager: bool = ..., envvar: Any = ..., shell_complete: Callable = ..., autocompletion: Callable = ..., show_default: bool = ..., prompt: bool = ..., confirmation_prompt: bool = ..., prompt_required: bool = ..., hide_input: bool = ..., is_flag: bool = ..., multiple: bool = ..., count: bool = ..., allow_from_autoenv: bool = ..., help: str = ..., hidden: bool = ..., show_choices: bool = ..., show_envvar: bool = ..., rich_help_panel: str = ...) -> None: ...

class TyperCommand(click.core.Command):
    def __init__(self, name: str, *, context_settings: Any = ..., callback: Callable = ..., params: Any = ..., help: str = ..., epilog: str = ..., short_help: str = ..., options_metavar: str = ..., add_help_option: bool = ..., no_args_is_help: bool = ..., hidden: bool = ..., deprecated: bool = ..., rich_markup_mode: str = ..., rich_help_panel: str = ...) -> None: ...

class TyperGroup(click.core.Group):
    def __init__(self, *, name: str = ..., commands: Any = ..., rich_markup_mode: str = ..., rich_help_panel: str = ..., **attrs: Any) -> None: ...
