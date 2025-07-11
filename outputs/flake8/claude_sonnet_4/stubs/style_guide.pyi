import argparse
import contextlib
import copy
import enum
import functools
import logging
from collections.abc import Generator, Sequence
from typing import Optional
from flake8 import statistics
from flake8.formatting import base as base_formatter
from flake8.violation import Violation

__all__: tuple[str, ...]
LOG: ...

class Selected(enum.Enum):
    Explicitly: str
    Implicitly: str

class Ignored(enum.Enum):
    Explicitly: str
    Implicitly: str

class Decision(enum.Enum):
    Ignored: str
    Selected: str

def _explicitly_chosen(
    *,
    option: Optional[Sequence[str]],
    extend: Optional[Sequence[str]],
) -> tuple[str, ...]: ...

def _select_ignore(
    *,
    option: Optional[Sequence[str]],
    default: Sequence[str],
    extended_default: list[str],
    extend: Optional[Sequence[str]],
) -> tuple[str, ...]: ...

class DecisionEngine:
    def __init__(self, options: argparse.Namespace) -> None: ...
    def was_selected(self, code: str) -> Selected | Ignored: ...
    def was_ignored(self, code: str) -> Ignored | Selected: ...
    def make_decision(self, code: str) -> Decision: ...
    def decision_for(self, code: str) -> Decision: ...

class StyleGuideManager:
    def __init__(
        self,
        options: argparse.Namespace,
        formatter: base_formatter.BaseFormatter,
        decider: Optional[DecisionEngine] = None,
    ) -> None: ...
    def populate_style_guides_with(
        self, options: argparse.Namespace
    ) -> Generator[StyleGuide, None, None]: ...
    def _style_guide_for(self, filename: str) -> StyleGuide: ...
    @contextlib.contextmanager
    def processing_file(self, filename: str) -> Generator[StyleGuide, None, None]: ...
    def handle_error(
        self,
        code: str,
        filename: str,
        line_number: int,
        column_number: int,
        text: str,
        physical_line: Optional[str] = None,
    ) -> int: ...

class StyleGuide:
    def __init__(
        self,
        options: argparse.Namespace,
        formatter: base_formatter.BaseFormatter,
        stats: statistics.Statistics,
        filename: Optional[str] = None,
        decider: Optional[DecisionEngine] = None,
    ) -> None: ...
    def __repr__(self) -> str: ...
    def copy(
        self,
        filename: Optional[str] = None,
        extend_ignore_with: Optional[Sequence[str]] = None,
    ) -> StyleGuide: ...
    @contextlib.contextmanager
    def processing_file(self, filename: str) -> Generator[StyleGuide, None, None]: ...
    def applies_to(self, filename: str) -> bool: ...
    def should_report_error(self, code: str) -> Decision: ...
    def handle_error(
        self,
        code: str,
        filename: str,
        line_number: int,
        column_number: int,
        text: str,
        physical_line: Optional[str] = None,
    ) -> int: ...