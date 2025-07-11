import argparse
import enum
import logging
from collections.abc import Generator
from flake8.formatting.base import BaseFormatter as BaseFormatter
from flake8.statistics import Statistics as Statistics
from flake8.violation import Violation as Violation

LOG: logging.Logger

class Selected(enum.Enum):
    Explicitly: str
    Implicitly: str

class Ignored(enum.Enum):
    Explicitly: str
    Implicitly: str

class Decision(enum.Enum):
    Ignored: str
    Selected: str

class DecisionEngine:
    cache: dict[str, Decision]
    selected_explicitly: tuple[str, ...]
    ignored_explicitly: tuple[str, ...]
    selected: tuple[str, ...]
    ignored: tuple[str, ...]
    def __init__(self, options: argparse.Namespace) -> None: ...
    def was_selected(self, code: str) -> Selected | Ignored: ...
    def was_ignored(self, code: str) -> Selected | Ignored: ...
    def make_decision(self, code: str) -> Decision: ...
    def decision_for(self, code: str) -> Decision: ...

class StyleGuideManager:
    options: argparse.Namespace
    formatter: BaseFormatter
    stats: Statistics
    decider: DecisionEngine
    style_guides: list['StyleGuide']
    default_style_guide: StyleGuide
    style_guide_for: Callable[[str], 'StyleGuide']
    def __init__(self, options: argparse.Namespace, formatter: BaseFormatter, decider: DecisionEngine | None = ...) -> None: ...
    def populate_style_guides_with(self, options: argparse.Namespace) -> Generator['StyleGuide', None, None]: ...
    def processing_file(self, filename: str) -> Generator['StyleGuide', None, None]: ...
    def handle_error(self, code: str, filename: str, line_number: int, column_number: int, text: str, physical_line: str | None = ...) -> int: ...

class StyleGuide:
    options: argparse.Namespace
    formatter: BaseFormatter
    stats: Statistics
    decider: DecisionEngine
    filename: str | None
    def __init__(self, options: argparse.Namespace, formatter: BaseFormatter, stats: Statistics, filename: str | None = ..., decider: DecisionEngine | None = ...) -> None: ...
    def copy(self, filename: str | None = ..., extend_ignore_with: list[str] | None = ...) -> StyleGuide: ...
    def processing_file(self, filename: str) -> Generator['StyleGuide', None, None]: ...
    def applies_to(self, filename: str) -> bool: ...
    def should_report_error(self, code: str) -> Decision: ...
    def handle_error(self, code: str, filename: str, line_number: int, column_number: int, text: str, physical_line: str | None = ...) -> int: ...
