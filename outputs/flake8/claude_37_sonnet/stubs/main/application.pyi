from __future__ import annotations

import argparse
import logging
import time
from collections.abc import Sequence
from typing import Any, List, Optional, Union

import flake8
from flake8 import checker
from flake8 import defaults
from flake8 import exceptions
from flake8 import style_guide
from flake8.formatting.base import BaseFormatter
from flake8.main import debug
from flake8.options.parse_args import parse_args
from flake8.plugins import finder
from flake8.plugins import reporter

LOG: logging.Logger

class Application:
    start_time: float
    end_time: Optional[float]
    plugins: Optional[finder.Plugins]
    formatter: Optional[BaseFormatter]
    guide: Optional[style_guide.StyleGuideManager]
    file_checker_manager: Optional[checker.Manager]
    options: Optional[argparse.Namespace]
    result_count: int
    total_result_count: int
    catastrophic_failure: bool

    def __init__(self) -> None: ...
    def exit_code(self) -> int: ...
    def make_formatter(self) -> None: ...
    def make_guide(self) -> None: ...
    def make_file_checker_manager(self, argv: Sequence[str]) -> None: ...
    def run_checks(self) -> None: ...
    def report_benchmarks(self) -> None: ...
    def report_errors(self) -> None: ...
    def report_statistics(self) -> None: ...
    def initialize(self, argv: Sequence[str]) -> None: ...
    def report(self) -> None: ...
    def _run(self, argv: Sequence[str]) -> None: ...
    def run(self, argv: Sequence[str]) -> None: ...