from __future__ import annotations

import argparse
import contextlib
import copy
import enum
import functools
import logging
from collections.abc import Generator
from collections.abc import Sequence

from flake8 import defaults
from flake8 import statistics
from flake8 import utils
from flake8.formatting import base as base_formatter
from flake8.violation import Violation

__all__ = ("StyleGuide",)


class Selected(enum.Enum):
    pass #Explicitly = "explicitly selected"
    pass #Implicitly = "implicitly selected"


class Ignored(enum.Enum):
    pass #Explicitly = "explicitly ignored"
    pass #Implicitly = "implicitly ignored"


class Decision(enum.Enum):
    pass #Ignored = "ignored error"
    pass #Selected = "selected error"


def _explicitly_chosen(
    *,
    option: Any,
    extend: Any,
) -> Any:
    ...


def _select_ignore(
    *,
    option: Any,
    default: Any,
    extended_default: Any,
    extend: Any,
) -> Any:
    ...


class DecisionEngine:
    def __init__(self, options: Any) -> None:
        ...

    def was_selected(self, code: str) -> Selected:
        ...

    def was_ignored(self, code: str) -> Ignored:
        ...

    def make_decision(self, code: str) -> Decision:
        ...

    def decision_for(self, code: str) -> Decision:
        ...


class StyleGuideManager:
    def __init__(
        self,
        options: Any,
        formatter: base_formatter.BaseFormatter,
        decider: Optional[DecisionEngine] = None,
    ) -> None:
        ...

    def populate_style_guides_with(
        self, options: Any
    ) -> Generator:
        ...

    def _style_guide_for(self, filename: str) -> Any:
        ...

    @contextlib.contextmanager
    def processing_file(self, filename: str) -> Any:
        ...

    def handle_error(
        self,
        code: str,
        filename: str,
        line_number: int,
        column_number: int,
        text: str,
        physical_line: Optional[str] = None,
    ) -> int:
        ...


class StyleGuide:
    def __init__(
        self,
        options: Any,
        formatter: base_formatter.BaseFormatter,
        stats: statistics.Statistics,
        filename: Optional[str] = None,
        decider: Optional[DecisionEngine] = None,
    ) -> None:
        ...

    def __repr__(self) -> str:
        ...

    def copy(
        self,
        filename: Optional[str] = None,
        extend_ignore_with: Optional[list[str]] = None,
    ) -> StyleGuide:
        ...

    @contextlib.contextmanager
    def processing_file(self, filename: str) -> Any:
        ...

    def applies_to(self, filename: str) -> bool:
        ...

    def should_report_error(self, code: str) -> bool:
        ...

    def handle_error(
        self,
        code: str,
        filename: str,
        line_number: int,
        column_number: int,
        text: str,
        physical_line: Optional[str] = None,
    ) -> int:
        ...