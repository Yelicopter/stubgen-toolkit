from __future__ import annotations

import argparse
import logging
import os.path
from typing import Any
from typing import Optional

from flake8.discover_files import expand_paths
from flake8.formatting import base as formatter
from flake8.main import application as app
from flake8.options.parse_args import parse_args

LOG = logging.getLogger(__name__)


__all__ = ("get_style_guide",)


class Report:
    def __init__(self, application: app.Application) -> None:
        ...

    @property
    def total_errors(self) -> int:
        ...

    def get_statistics(self, violation: str) -> list[str]:
        ...


class StyleGuide:
    def __init__(self, application: app.Application) -> None:
        ...

    @property
    def options(self) -> argparse.Namespace:
        ...

    @property
    def paths(self) -> list[str]:
        ...

    def check_files(self, paths: Optional[list[str]] = None) -> Report:
        ...

    def excluded(self, filename: str, parent: Optional[str] = None) -> bool:
        ...

    def init_report(self, reporter: Optional[formatter.BaseFormatter] = None) -> None:
        ...

    def input_file(
        self,
        filename: str,
        lines: Optional[list[str]] = None,
        expected: Optional[str] = None,
        line_offset: int = 0,
    ) -> Report:
        ...

def get_style_guide(**kwargs: Any) -> StyleGuide:
    ...