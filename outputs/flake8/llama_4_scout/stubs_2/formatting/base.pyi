from __future__ import annotations

import argparse
import os
import sys
from typing import IO, Any, Optional

from flake8.formatting import _windows_color
from flake8.statistics import Statistics
from flake8.violation import Violation


class BaseFormatter:
    def __init__(self, options: Any) -> None:
        ...

    def after_init(self) -> None:
        ...

    def beginning(self, filename: str) -> None:
        ...

    def finished(self, filename: str) -> None:
        ...

    def start(self) -> None:
        ...

    def handle(self, error: Violation) -> None:
        ...

    def format(self, error: Violation) -> str:
        ...

    def show_statistics(self, statistics: Statistics) -> None:
        ...

    def show_benchmarks(self, benchmarks: Any) -> None:
        ...

    def show_source(self, error: Violation) -> Optional[str]:
        ...

    def _write(self, output: str) -> None:
        ...

    def write(self, line: str, source: Optional[str]) -> None:
        ...

    def stop(self) -> None:
        ...