from __future__ import annotations

import argparse
import contextlib
import errno
import logging
import multiprocessing.pool
import operator
import signal
import tokenize
from collections.abc import Generator, Sequence
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

from flake8 import defaults
from flake8 import exceptions
from flake8 import processor
from flake8 import utils
from flake8._compat import FSTRING_START
from flake8._compat import TSTRING_START
from flake8.discover_files import expand_paths
from flake8.options.parse_args import parse_args
from flake8.plugins.finder import Checkers
from flake8.plugins.finder import LoadedPlugin
from flake8.style_guide import StyleGuideManager

Results = list[tuple[str, int, int, str, Optional[str]]]

LOG: logging.Logger

SERIAL_RETRY_ERRNOS: set[int]

_mp: Optional[tuple[Checkers, argparse.Namespace]]

@contextlib.contextmanager
def _mp_prefork(
    plugins: Checkers, options: argparse.Namespace
) -> Generator[None, None, None]: ...

def _mp_init(argv: Sequence[str]) -> None: ...

def _mp_run(filename: str) -> tuple[str, Results, dict[str, int]]: ...

class Manager:
    style_guide: StyleGuideManager
    options: argparse.Namespace
    plugins: Checkers
    jobs: int
    statistics: dict[str, int]
    exclude: tuple[str, ...]
    argv: Sequence[str]
    results: list[tuple[str, Results, dict[str, int]]]
    filenames: tuple[str, ...]

    def __init__(
        self,
        style_guide: StyleGuideManager,
        plugins: Checkers,
        argv: Sequence[str],
    ) -> None: ...
    def _process_statistics(self) -> None: ...
    def _job_count(self) -> int: ...
    def _handle_results(self, filename: str, results: Results) -> int: ...
    def report(self) -> tuple[int, int]: ...
    def run_parallel(self) -> None: ...
    def run_serial(self) -> None: ...
    def run(self) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...

class FileChecker:
    options: argparse.Namespace
    filename: str
    plugins: Checkers
    results: Results
    statistics: dict[str, int]
    processor: Optional[processor.FileProcessor]
    display_name: str
    should_process: bool

    def __init__(
        self,
        *,
        filename: str,
        plugins: Checkers,
        options: argparse.Namespace,
    ) -> None: ...
    def __repr__(self) -> str: ...
    def _make_processor(self) -> Optional[processor.FileProcessor]: ...
    def report(
        self,
        error_code: Union[str, None],
        line_number: int,
        column: int,
        text: str,
    ) -> str: ...
    def run_check(self, plugin: LoadedPlugin, **arguments: Any) -> Any: ...
    @staticmethod
    def _extract_syntax_information(exception: Exception) -> tuple[int, int]: ...
    def run_ast_checks(self) -> None: ...
    def run_logical_checks(self) -> None: ...
    def run_physical_checks(self, physical_line: str) -> None: ...
    def process_tokens(self) -> None: ...
    def run_checks(self) -> tuple[str, Results, dict[str, int]]: ...
    def handle_newline(self, token_type: int) -> None: ...
    def check_physical_eol(
        self, token: tokenize.TokenInfo, prev_physical: str
    ) -> None: ...

def _try_initialize_processpool(
    job_count: int,
    argv: Sequence[str],
) -> Optional[multiprocessing.pool.Pool]: ...

def find_offset(
    offset: Union[int, tuple[int, int]], mapping: list[tuple[int, tuple[int, int]]]
) -> tuple[int, int]: ...