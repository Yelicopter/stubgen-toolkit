from _typeshed import Incomplete
from collections.abc import Callable as Callable
from pathlib import Path
from watchdog.events import FileSystemEvent as FileSystemEvent

class IngestWatcher:
    watch_path: Incomplete
    on_file_changed: Incomplete
    def __init__(self, watch_path: Path, on_file_changed: Callable[[Path], None]) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
