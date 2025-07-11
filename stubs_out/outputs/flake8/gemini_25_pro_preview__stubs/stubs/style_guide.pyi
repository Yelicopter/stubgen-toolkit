import argparse
import enum
from collections.abc import Generator
from flake8 import statistics as statistics
from flake8.formatting import base as base_formatter
from flake8.violation import Violation as Violation
from typing import Optional, Union

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
    def was_selected(self, code: str) -> Union[Selected, Ignored]: ...
    def was_ignored(self, code: str) -> Union[Ignored, Selected]: ...
    def make_decision(self, code: str) -> Decision: ...
    def decision_for(self, code: str) -> Decision: ...

class StyleGuideManager:
    options: argparse.Namespace
    formatter: base_formatter.BaseFormatter
    stats: statistics.Statistics
    decider: DecisionEngine
    style_guides: list[StyleGuide]
    default_style_guide: StyleGuide
    def __init__(self, options: argparse.Namespace, formatter: base_formatter.BaseFormatter, decider: Optional[DecisionEngine] = ...) -> None: ...
    def populate_style_guides_with(self, options: argparse.Namespace) -> Generator[StyleGuide, None, None]: ...
    def processing_file(self, filename: str) -> Generator[StyleGuide, None, None]: ...
    def handle_error(self, code: str, filename: str, line_number: int, column_number: int, text: str, physical_line: Optional[str] = ...) -> int: ...

class StyleGuide:
    options: argparse.Namespace
    formatter: base_formatter.BaseFormatter
    stats: statistics.Statistics
    decider: DecisionEngine
    filename: Optional[str]
    def __init__(self, options: argparse.Namespace, formatter: base_formatter.BaseFormatter, stats: statistics.Statistics, filename: Optional[str] = ..., decider: Optional[DecisionEngine] = ...) -> None: ...
    def copy(self, filename: Optional[str] = ..., extend_ignore_with: Optional[list[str]] = ...) -> StyleGuide: ...
    def processing_file(self, filename: str) -> Generator[StyleGuide, None, None]: ...
    def applies_to(self, filename: str) -> bool: ...
    def should_report_error(self, code: str) -> Decision: ...
    def handle_error(self, code: str, filename: str, line_number: int, column_number: int, text: str, physical_line: Optional[str] = ...) -> int: ...
