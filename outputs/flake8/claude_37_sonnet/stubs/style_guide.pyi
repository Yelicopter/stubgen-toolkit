from __future__ import annotations

import argparse
import contextlib
import copy
import enum
import functools
import logging
from collections.abc import Generator
from collections.abc import Sequence
from typing import Callable, Dict, List, Optional, Tuple, Union

from flake8 import defaults
from flake8 import statistics
from flake8 import utils
from flake8.formatting import base as base_formatter
from flake8.violation import Violation

__all__: tuple[str, ...]

LOG: logging.Logger

class Selected(enum.Enum):
    Explicitly = "explicitly selected"
    Implicitly = "implicitly selected"

class Ignored(enum.Enum):
    Explicitly = "explicitly ignored"
    Implicitly = "implicitly ignored"

class Decision(enum.Enum):
    Ignored = "ignored error"
    Selected = "selected error"

def _explicitly_chosen(
    *,
    option: Optional[Sequence[str]],
    extend: Optional[Sequence[str]],
) -> tuple[str, ...]: ...

def _select_ignore(
    *,
    option: Optional[Sequence[str]],
    default: tuple[str, ...],
    extended_default: Sequence[str],
    extend: Optional[Sequence[str]],
) -> tuple[str, ...]: ...

class DecisionEngine:
    cache: dict[str, Decision]
    selected_explicitly: tuple[str, ...]
    ignored_explicitly: tuple[str, ...]
    selected: tuple[str, ...]
    ignored: tuple[str, ...]

    def __init__(self, options: argparse.Namespace) -> None: ...
    def was_selected(self, code: str) -> Union[Selected, Ignored]: ...
    def was_ignored(self, code: str) -> Union[Selected, Ignored]: ...
    def make_decision(self, code: str) -> Decision: ...
    def decision_for(self, code: str) -> Decision: ...

class StyleGuideManager:
    options: argparse.Namespace
    formatter: base_formatter.BaseFormatter
    stats: statistics.Statistics
    decider: DecisionEngine
    style_guides: list[StyleGuide]
    default_style_guide: StyleGuide
    style_guide_for: Callable[[str], StyleGuide]

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
    options: argparse.Namespace
    formatter: base_formatter.BaseFormatter
    stats: statistics.Statistics
    decider: DecisionEngine
    filename: Optional[str]

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