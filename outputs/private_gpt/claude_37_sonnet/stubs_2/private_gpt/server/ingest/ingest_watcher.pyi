from collections.abc import Callable
from pathlib import Path
from typing import Any

from watchdog.events import (
    FileCreatedEvent,
    FileModifiedEvent,
    FileSystemEvent,
    FileSystemEventHandler,
)
from watchdog.observers import Observer

class IngestWatcher:
    def __init__(
        self, watch_path: Path, on_file_changed: Callable[[Path], Any]
    ) -> None: ...
    
    def start(self) -> None: ...
    def stop(self) -> None: ...