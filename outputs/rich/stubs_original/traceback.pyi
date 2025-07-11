from types import ModuleType, TracebackType
from typing import Any, Callable, Dict, Iterable, List, Optional, Sequence, Tuple, Type, Union

def install(*, console: Optional[Any] = ..., width: Optional[int] = ..., code_width: Optional[int] = ..., extra_lines: int = ..., theme: Optional[str] = ..., word_wrap: bool = ..., show_locals: bool = ..., locals_max_length: int = ..., locals_max_string: int = ..., locals_hide_dunder: bool = ..., locals_hide_sunder: Optional[bool] = ..., indent_guides: bool = ..., suppress: Iterable[Union[str, ModuleType]] = ..., max_frames: int = ...) -> Callable[[Type[BaseException], BaseException, Optional[TracebackType]], Any]: ...

class Frame:
    filename: str
    lineno: int
    name: str
    line: str
    locals: Optional[Dict[str, Any]]
    last_instruction: Optional[Tuple[Tuple[int, int], Tuple[int, int]]]
    def __init__(self, filename, lineno, name, line, locals, last_instruction) -> None: ...

class _SyntaxError:
    offset: int
    filename: str
    line: str
    lineno: int
    msg: str
    notes: List[str]
    def __init__(self, offset, filename, line, lineno, msg, notes) -> None: ...

class Stack:
    exc_type: str
    exc_value: str
    syntax_error: Optional[_SyntaxError]
    is_cause: bool
    frames: List[Frame]
    notes: List[str]
    is_group: bool
    exceptions: List['Trace']
    def __init__(self, exc_type, exc_value, syntax_error, is_cause, frames, notes, is_group, exceptions) -> None: ...

class Trace:
    stacks: List[Stack]
    def __init__(self, stacks) -> None: ...

class PathHighlighter:
    highlights: List[str]

class Traceback:
    LEXERS: Dict[str, str]
    trace: Trace
    width: Optional[int]
    code_width: Optional[int]
    extra_lines: int
    theme: Any
    word_wrap: bool
    show_locals: bool
    indent_guides: bool
    locals_max_length: int
    locals_max_string: int
    locals_hide_dunder: bool
    locals_hide_sunder: bool
    suppress: Sequence[str]
    max_frames: int
    def __init__(self, trace: Optional[Trace] = ..., *, width: Optional[int] = ..., code_width: Optional[int] = ..., extra_lines: int = ..., theme: Optional[str] = ..., word_wrap: bool = ..., show_locals: bool = ..., locals_max_length: int = ..., locals_max_string: int = ..., locals_hide_dunder: bool = ..., locals_hide_sunder: bool = ..., indent_guides: bool = ..., suppress: Iterable[Union[str, ModuleType]] = ..., max_frames: int = ...) -> None: ...
    @classmethod
    def from_exception(cls, exc_type: Type[Any], exc_value: BaseException, traceback: Optional[TracebackType], *, width: Optional[int] = ..., code_width: Optional[int] = ..., extra_lines: int = ..., theme: Optional[str] = ..., word_wrap: bool = ..., show_locals: bool = ..., locals_max_length: int = ..., locals_max_string: int = ..., locals_hide_dunder: bool = ..., locals_hide_sunder: bool = ..., indent_guides: bool = ..., suppress: Iterable[Union[str, ModuleType]] = ..., max_frames: int = ...) -> Traceback: ...
    @classmethod
    def extract(cls, exc_type: Type[BaseException], exc_value: BaseException, traceback: Optional[TracebackType], *, show_locals: bool = ..., locals_max_length: int = ..., locals_max_string: int = ..., locals_hide_dunder: bool = ..., locals_hide_sunder: bool = ...) -> Trace: ...
    def __rich_console__(self, console: Any, options: Any) -> Iterable[Any]: ...
