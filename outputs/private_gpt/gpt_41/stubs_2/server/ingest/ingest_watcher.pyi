from collections.abc import Callable
from pathlib import Path
from typing import Any

from watchdog.events import (
    FileCreatedEvent,
    FileModifiedEvent,
    FileSystemEvent,
    FileSystemEventHandler,
)
import watchdog.observers

class IngestWatcher:
    watch_path: Path
    on_file_changed: Callable[[Path], None]
    _observer: "watchdog.observers.Observer"
    def __init__(
        self, watch_path: Path, on_file_changed: Callable[[Path], None]
    ) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...