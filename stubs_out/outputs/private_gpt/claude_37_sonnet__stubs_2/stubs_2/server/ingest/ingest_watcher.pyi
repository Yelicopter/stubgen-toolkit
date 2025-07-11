from collections.abc import Callable as Callable
from pathlib import Path
from typing import Any
from watchdog.events import FileCreatedEvent as FileCreatedEvent, FileModifiedEvent as FileModifiedEvent, FileSystemEvent as FileSystemEvent, FileSystemEventHandler as FileSystemEventHandler
from watchdog.observers import Observer as Observer

class IngestWatcher:
    def __init__(self, watch_path: Path, on_file_changed: Callable[[Path], Any]) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
