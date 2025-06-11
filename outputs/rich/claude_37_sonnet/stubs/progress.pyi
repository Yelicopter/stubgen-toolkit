from abc import ABC, abstractmethod
from collections import deque
from dataclasses import dataclass, field
from datetime import timedelta
from io import RawIOBase, UnsupportedOperation
from mmap import mmap
from os import PathLike
from threading import Event, RLock, Thread
from types import TracebackType
from typing import (
    Any,
    BinaryIO,
    Callable,
    ContextManager,
    Deque,
    Dict,
    Generic,
    Iterable,
    List,
    NamedTuple,
    NewType,
    Optional,
    Sequence,
    TextIO,
    Tuple,
    Type,
    TypeVar,
    Union,
    overload,
)
from typing_extensions import Literal, Self

from . import filesize, get_console
from .console import Console, Group, JustifyMethod, RenderableType
from .highlighter import Highlighter
from .jupyter import JupyterMixin
from .live import Live
from .progress_bar import ProgressBar
from .spinner import Spinner
from .style import Style, StyleType
from .table import Column, Table
from .text import Text, TextType

TaskID = NewType("TaskID", int)
ProgressType = TypeVar("ProgressType")
GetTimeCallable = Callable[[], float]
_I = TypeVar("_I", TextIO, BinaryIO)

class _TrackThread(Thread):
    def __init__(self, progress: "Progress", task_id: "TaskID", update_period: float) -> None: ...
    progress: Progress
    task_id: TaskID
    update_period: float
    done: Event
    completed: int
    def run(self) -> None: ...
    def __enter__(self) -> "_TrackThread": ...
    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None: ...

def track(
    sequence: Union[Sequence[ProgressType], Iterable[ProgressType]],
    description: str = ...,
    total: Optional[float] = ...,
    completed: int = ...,
    auto_refresh: bool = ...,
    console: Optional[Console] = ...,
    transient: bool = ...,
    get_time: Optional[Callable[[], float]] = ...,
    refresh_per_second: float = ...,
    style: StyleType = ...,
    complete_style: StyleType = ...,
    finished_style: StyleType = ...,
    pulse_style: StyleType = ...,
    update_period: float = ...,
    disable: bool = ...,
    show_speed: bool = ...,
) -> Iterable[ProgressType]: ...

class _Reader(RawIOBase, BinaryIO):
    def __init__(
        self,
        handle: BinaryIO,
        progress: "Progress",
        task: TaskID,
        close_handle: bool = ...,
    ) -> None: ...
    handle: BinaryIO
    progress: Progress
    task: TaskID
    close_handle: bool
    _closed: bool
    def __enter__(self) -> "_Reader": ...
    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None: ...
    def __iter__(self) -> BinaryIO: ...
    def __next__(self) -> bytes: ...
    @property
    def closed(self) -> bool: ...
    def fileno(self) -> int: ...
    def isatty(self) -> bool: ...
    @property
    def mode(self) -> str: ...
    @property
    def name(self) -> str: ...
    def readable(self) -> bool: ...
    def seekable(self) -> bool: ...
    def writable(self) -> bool: ...
    def read(self, size: int = ...) -> bytes: ...
    def readinto(self, b: Union[bytearray, memoryview, mmap]): ...
    def readline(self, size: int = ...) -> bytes: ...
    def readlines(self, hint: int = ...) -> List[bytes]: ...
    def close(self) -> None: ...
    def seek(self, offset: int, whence: int = ...) -> int: ...
    def tell(self) -> int: ...
    def write(self, s: Any) -> int: ...
    def writelines(self, lines: Iterable[Any]) -> None: ...

class _ReadContext(ContextManager[_I], Generic[_I]):
    def __init__(self, progress: "Progress", reader: _I) -> None: ...
    progress: Progress
    reader: _I
    def __enter__(self) -> _I: ...
    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None: ...

def wrap_file(
    file: BinaryIO,
    total: int,
    *,
    description: str = ...,
    auto_refresh: bool = ...,
    console: Optional[Console] = ...,
    transient: bool = ...,
    get_time: Optional[Callable[[], float]] = ...,
    refresh_per_second: float = ...,
    style: StyleType = ...,
    complete_style: StyleType = ...,
    finished_style: StyleType = ...,
    pulse_style: StyleType = ...,
    disable: bool = ...,
) -> ContextManager[BinaryIO]: ...

@overload
def open(
    file: Union[str, PathLike[str], bytes],
    mode: Union[Literal["rt"], Literal["r"]],
    buffering: int = ...,
    encoding: Optional[str] = ...,
    errors: Optional[str] = ...,
    newline: Optional[str] = ...,
    *,
    total: Optional[int] = ...,
    description: str = ...,
    auto_refresh: bool = ...,
    console: Optional[Console] = ...,
    transient: bool = ...,
    get_time: Optional[Callable[[], float]] = ...,
    refresh_per_second: float = ...,
    style: StyleType = ...,
    complete_style: StyleType = ...,
    finished_style: StyleType = ...,
    pulse_style: StyleType = ...,
    disable: bool = ...,
) -> ContextManager[TextIO]: ...

@overload
def open(
    file: Union[str, PathLike[str], bytes],
    mode: Literal["rb"],
    buffering: int = ...,
    encoding: Optional[str] = ...,
    errors: Optional[str] = ...,
    newline: Optional[str] = ...,
    *,
    total: Optional[int] = ...,
    description: str = ...,
    auto_refresh: bool = ...,
    console: Optional[Console] = ...,
    transient: bool = ...,
    get_time: Optional[Callable[[], float]] = ...,
    refresh_per_second: float = ...,
    style: StyleType = ...,
    complete_style: StyleType = ...,
    finished_style: StyleType = ...,
    pulse_style: StyleType = ...,
    disable: bool = ...,
) -> ContextManager[BinaryIO]: ...

class ProgressColumn(ABC):
    max_refresh: Optional[float]
    def __init__(self, table_column: Optional[Column] = ...) -> None: ...
    _table_column: Optional[Column]
    _renderable_cache: Dict[TaskID, Tuple[float, RenderableType]]
    _update_time: Optional[float]
    def get_table_column(self) -> Column: ...
    def __call__(self, task: "Task") -> RenderableType: ...
    @abstractmethod
    def render(self, task: "Task") -> RenderableType: ...

class RenderableColumn(ProgressColumn):
    def __init__(
        self, renderable: RenderableType = ..., *, table_column: Optional[Column] = ...
    ) -> None: ...
    renderable: RenderableType
    def render(self, task: "Task") -> RenderableType: ...

class SpinnerColumn(ProgressColumn):
    def __init__(
        self,
        spinner_name: str = ...,
        style: Optional[StyleType] = ...,
        speed: float = ...,
        finished_text: TextType = ...,
        table_column: Optional[Column] = ...,
    ) -> None: ...
    spinner: Spinner
    finished_text: Text
    def set_spinner(
        self,
        spinner_name: str,
        spinner_style: Optional[StyleType] = ...,
        speed: float = ...,
    ) -> None: ...
    def render(self, task: "Task") -> RenderableType: ...

class TextColumn(ProgressColumn):
    def __init__(
        self,
        text_format: str,
        style: StyleType = ...,
        justify: JustifyMethod = ...,
        markup: bool = ...,
        highlighter: Optional[Highlighter] = ...,
        table_column: Optional[Column] = ...,
    ) -> None: ...
    text_format: str
    justify: JustifyMethod
    style: StyleType
    markup: bool
    highlighter: Optional[Highlighter]
    def render(self, task: "Task") -> Text: ...

class BarColumn(ProgressColumn):
    def __init__(
        self,
        bar_width: Optional[int] = ...,
        style: StyleType = ...,
        complete_style: StyleType = ...,
        finished_style: StyleType = ...,
        pulse_style: StyleType = ...,
        table_column: Optional[Column] = ...,
    ) -> None: ...
    bar_width: Optional[int]
    style: StyleType
    complete_style: StyleType
    finished_style: StyleType
    pulse_style: StyleType
    def render(self, task: "Task") -> ProgressBar: ...

class TimeElapsedColumn(ProgressColumn):
    def render(self, task: "Task") -> Text: ...

class TaskProgressColumn(TextColumn):
    def __init__(
        self,
        text_format: str = ...,
        text_format_no_percentage: str = ...,
        style: StyleType = ...,
        justify: JustifyMethod = ...,
        markup: bool = ...,
        highlighter: Optional[Highlighter] = ...,
        table_column: Optional[Column] = ...,
        show_speed: bool = ...,
    ) -> None: ...
    text_format_no_percentage: str
    show_speed: bool
    @classmethod
    def render_speed(cls, speed: Optional[float]) -> Text: ...
    def render(self, task: "Task") -> Text: ...

class TimeRemainingColumn(ProgressColumn):
    max_refresh: float
    def __init__(
        self,
        compact: bool = ...,
        elapsed_when_finished: bool = ...,
        table_column: Optional[Column] = ...,
    ) -> None: ...
    compact: bool
    elapsed_when_finished: bool
    def render(self, task: "Task") -> Text: ...

class FileSizeColumn(ProgressColumn):
    def render(self, task: "Task") -> Text: ...

class TotalFileSizeColumn(ProgressColumn):
    def render(self, task: "Task") -> Text: ...

class MofNCompleteColumn(ProgressColumn):
    def __init__(self, separator: str = ..., table_column: Optional[Column] = ...) -> None: ...
    separator: str
    def render(self, task: "Task") -> Text: ...

class DownloadColumn(ProgressColumn):
    def __init__(
        self, binary_units: bool = ..., table_column: Optional[Column] = ...
    ) -> None: ...
    binary_units: bool
    def render(self, task: "Task") -> Text: ...

class TransferSpeedColumn(ProgressColumn):
    def render(self, task: "Task") -> Text: ...

class ProgressSample(NamedTuple):
    timestamp: float
    completed: float

@dataclass
class Task:
    id: TaskID
    description: str
    total: Optional[float]
    completed: float
    _get_time: GetTimeCallable
    finished_time: Optional[float] = ...
    visible: bool = ...
    fields: Dict[str, Any] = ...
    start_time: Optional[float] = field(default=None, init=False, repr=False)
    stop_time: Optional[float] = field(default=None, init=False, repr=False)
    finished_speed: Optional[float] = ...
    _progress: Deque[ProgressSample] = field(
        default_factory=lambda: deque(maxlen=1000), init=False, repr=False
    )
    _lock: RLock = field(repr=False, default_factory=RLock)
    def get_time(self) -> float: ...
    @property
    def started(self) -> bool: ...
    @property
    def remaining(self) -> Optional[float]: ...
    @property
    def elapsed(self) -> Optional[float]: ...
    @property
    def finished(self) -> bool: ...
    @property
    def percentage(self) -> float: ...
    @property
    def speed(self) -> Optional[float]: ...
    @property
    def time_remaining(self) -> Optional[float]: ...
    def _reset(self) -> None: ...

class Progress(JupyterMixin):
    def __init__(
        self,
        *columns: Union[str, ProgressColumn],
        console: Optional[Console] = ...,
        auto_refresh: bool = ...,
        refresh_per_second: float = ...,
        speed_estimate_period: float = ...,
        transient: bool = ...,
        redirect_stdout: bool = ...,
        redirect_stderr: bool = ...,
        get_time: Optional[GetTimeCallable] = ...,
        disable: bool = ...,
        expand: bool = ...,
    ) -> None: ...
    columns: Tuple[Union[str, ProgressColumn], ...]
    speed_estimate_period: float
    disable: bool
    expand: bool
    _tasks: Dict[TaskID, Task]
    _task_index: TaskID
    live: Live
    get_time: GetTimeCallable
    print: Callable[..., None]
    log: Callable[..., None]
    @classmethod
    def get_default_columns(cls) -> Tuple[ProgressColumn, ...]: ...
    @property
    def console(self) -> Console: ...
    @property
    def tasks(self) -> List[Task]: ...
    @property
    def task_ids(self) -> List[TaskID]: ...
    @property
    def finished(self) -> bool: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None: ...
    def track(
        self,
        sequence: Union[Iterable[ProgressType], Sequence[ProgressType]],
        total: Optional[float] = ...,
        completed: int = ...,
        task_id: Optional[TaskID] = ...,
        description: str = ...,
        update_period: float = ...,
    ) -> Iterable[ProgressType]: ...
    def wrap_file(
        self,
        file: BinaryIO,
        total: Optional[int] = ...,
        *,
        task_id: Optional[TaskID] = ...,
        description: str = ...,
    ) -> BinaryIO: ...
    @overload
    def open(
        self,
        file: Union[str, PathLike[str], bytes],
        mode: Literal["rb"],
        buffering: int = ...,
        encoding: Optional[str] = ...,
        errors: Optional[str] = ...,
        newline: Optional[str] = ...,
        *,
        total: Optional[int] = ...,
        task_id: Optional[TaskID] = ...,
        description: str = ...,
    ) -> BinaryIO: ...
    @overload
    def open(
        self,
        file: Union[str, PathLike[str], bytes],
        mode: Union[Literal["r"], Literal["rt"]],
        buffering: int = ...,
        encoding: Optional[str] = ...,
        errors: Optional[str] = ...,
        newline: Optional[str] = ...,
        *,
        total: Optional[int] = ...,
        task_id: Optional[TaskID] = ...,
        description: str = ...,
    ) -> TextIO: ...
    def start_task(self, task_id: TaskID) -> None: ...
    def stop_task(self, task_id: TaskID) -> None: ...
    def update(
        self,
        task_id: TaskID,
        *,
        total: Optional[float] = ...,
        completed: Optional[float] = ...,
        advance: Optional[float] = ...,
        description: Optional[str] = ...,
        visible: Optional[bool] = ...,
        refresh: bool = ...,
        **fields: Any,
    ) -> None: ...
    def reset(
        self,
        task_id: TaskID,
        *,
        start: bool = ...,
        total: Optional[float] = ...,
        completed: int = ...,
        visible: Optional[bool] = ...,
        description: Optional[str] = ...,
        **fields: Any,
    ) -> None: ...
    def advance(self, task_id: TaskID, advance: float = ...) -> None: ...
    def refresh(self) -> None: ...
    def get_renderable(self) -> RenderableType: ...
    def get_renderables(self) -> Iterable[RenderableType]: ...
    def make_tasks_table(self, tasks: Iterable[Task]) -> Table: ...
    def __rich__(self) -> RenderableType: ...
    def add_task(
        self,
        description: str,
        start: bool = ...,
        total: Optional[float] = ...,
        completed: int = ...,
        visible: bool = ...,
        **fields: Any,
    ) -> TaskID: ...
    def remove_task(self, task_id: TaskID) -> None: ...