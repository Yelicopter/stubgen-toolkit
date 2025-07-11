from typing import TYPE_CHECKING, Any, Callable, Dict, List, Optional, Sequence, Type, TypeVar, Union

class Context(click.Context):
    pass

class FileText(io.TextIOWrapper):
    pass

class FileTextWrite(FileText):
    pass

class FileBinaryRead(io.BufferedReader):
    pass

class FileBinaryWrite(io.BufferedWriter):
    pass

class CallbackParam(click.Parameter):
    pass

class DefaultPlaceholder:
    def __init__(self, value: Any) -> None:
        ...

DefaultType = TypeVar("DefaultType")

CommandFunctionType = TypeVar("CommandFunctionType", bound=Callable[..., Any])

def Default(value: Any) -> DefaultPlaceholder:
    ...

class CommandInfo:
    def __init__(
        self,
        name: str = None,
        *,
        cls: Any = None,
        context_settings: Any = None,
        callback: Callable = None,
        help: str = None,
        epilog: str = None,
        short_help: str = None,
        options_metavar: str = "[OPTIONS]",
        add_help_option: bool = True,
        no_args_is_help: bool = False,
        hidden: bool = False,
        deprecated: bool = False,
        rich_help_panel: str = None,
    ) -> None:
        ...

class TyperInfo:
    def __init__(
        self,
        typer_instance: Any = None,
        *,
        name: str = None,
        cls: Any = None,
        invoke_without_command: bool = None,
        no_args_is_help: bool = None,
        subcommand_metavar: str = None,
        chain: bool = None,
        result_callback: Callable = None,
        context_settings: Any = None,
        callback: Callable = None,
        help: str = None,
        epilog: str = None,
        short_help: str = None,
        options_metavar: str = "[OPTIONS]",
        add_help_option: bool = True,
        hidden: bool = None,
        deprecated: bool = None,
        rich_help_panel: str = None,
    ) -> None:
        ...

class ParameterInfo:
    def __init__(
        self,
        *,
        default: Any = None,
        param_decls: Any = None,
        callback: Callable = None,
        metavar: Any = None,
        expose_value: bool = True,
        is_eager: bool = False,
        envvar: Any = None,
        shell_complete: Callable = None,
        autocompletion: Callable = None,
        default_factory: Callable = None,
        parser: Any = None,
        click_type: Any = None,
        show_default: bool = True,
        show_choices: bool = True,
        show_envvar: bool = True,
        help: str = None,
        hidden: bool = False,
        case_sensitive: bool = True,
        min: Any = None,
        max: Any = None,
        clamp: bool = False,
        formats: Any = None,
        mode: Any = None,
        encoding: Any = None,
        errors: Any = None,
        lazy: Any = None,
        atomic: bool = False,
        exists: bool = False,
        file_okay: bool = True,
        dir_okay: bool = True,
        writable: bool = False,
        readable: bool = True,
        resolve_path: bool = False,
        allow_dash: bool = False,
        path_type: Any = None,
        rich_help_panel: str = None,
    ) -> None:
        ...

class OptionInfo(ParameterInfo):
    def __init__(
        self,
        *,
        default: Any = None,
        param_decls: Any = None,
        callback: Callable = None,
        metavar: Any = None,
        expose_value: bool = True,
        is_eager: bool = False,
        envvar: Any = None,
        shell_complete: Callable = None,
        autocompletion: Callable = None,
        default_factory: Callable = None,
        parser: Any = None,
        click_type: Any = None,
        show_default: bool = True,
        prompt: bool = False,
        confirmation_prompt: bool = False,
        prompt_required: bool = True,
        hide_input: bool = False,
        is_flag: bool = None,
        flag_value: Any = None,
        count: bool = False,
        allow_from_autoenv: bool = True,
        help: str = None,
        hidden: bool = False,
        show_choices: bool = True,
        show_envvar: bool = True,
        case_sensitive: bool = True,
        min: Any = None,
        max: Any = None,
        clamp: bool = False,
        formats: Any = None,
        mode: Any = None,
        encoding: Any = None,
        errors: Any = None,
        lazy: Any = None,
        atomic: bool = False,
        exists: bool = False,
        file_okay: bool = True,
        dir_okay: bool = True,
        writable: bool = False,
        readable: bool = True,
        resolve_path: bool = False,
        allow_dash: bool = False,
        path_type: Any = None,
        rich_help_panel: str = None,
    ) -> None:
        ...

class ArgumentInfo(ParameterInfo):
    def __init__(
        self,
        *,
        default: Any = None,
        param_decls: Any = None,
        callback: Callable = None,
        metavar: Any = None,
        expose_value: bool = True,
        is_eager: bool = False,
        envvar: Any = None,
        shell_complete: Callable = None,
        autocompletion: Callable = None,
        default_factory: Callable = None,
        parser: Any = None,
        click_type: Any = None,
        show_default: bool = True,
        show_choices: bool = True,
        show_envvar: bool = True,
        help: str = None,
        hidden: bool = False,
        case_sensitive: bool = True,
        min: Any = None,
        max: Any = None,
        clamp: bool = False,
        formats: Any = None,
        mode: Any = None,
        encoding: Any = None,
        errors: Any = None,
        lazy: Any = None,
        atomic: bool = False,
        exists: bool = False,
        file_okay: bool = True,
        dir_okay: bool = True,
        writable: bool = False,
        readable: bool = True,
        resolve_path: bool = False,
        allow_dash: bool = False,
        path_type: Any = None,
        rich_help_panel: str = None,
    ) -> None:
        ...

class ParamMeta:
    def __init__(
        self,
        *,
        name: str,
        default: Any,
        annotation: Any,
    ) -> None:
        ...

class DeveloperExceptionConfig:
    def __init__(
        self,
        *,
        pretty_exceptions_enable: bool = True,
        pretty_exceptions_show_locals: bool = True,
        pretty_exceptions_short: bool = True,
    ) -> None:
        ...

class TyperPath(click.Path):
    ...