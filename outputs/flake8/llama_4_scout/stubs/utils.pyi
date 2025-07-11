from __future__ import annotations

import fnmatch as _fnmatch
import functools
import io
import logging
import os
import platform
import re
import sys
import textwrap
import tokenize
from collections.abc import Sequence
from re import Pattern
from typing import NamedTuple

from flake8 import exceptions

COMMA_SEPARATED_LIST_RE = re.compile(r"[,\s]")
LOCAL_PLUGIN_LIST_RE = re.compile(r"[,\t\n\r\f\v]")
NORMALIZE_PACKAGE_NAME_RE = re.compile(r"[-_.]+")


def parse_comma_separated_list(
    value: str,
    regexp: Pattern = COMMA_SEPARATED_LIST_RE,
) -> list[str]:
    ...


class _Token(NamedTuple):
    pass #tp: str
    pass #src: str


_CODE, _FILE, _COLON, _COMMA, _WS = "code", "file", "colon", "comma", "ws"
_EOF = "eof"
_FILE_LIST_TOKEN_TYPES = [
    (re.compile(r"[A-Z]+[0-9]*(?=$|\s|,)"), _CODE),
    (re.compile(r"[^\s:,]+"), _FILE),
    (re.compile(r"\s*:\s*"), _COLON),
    (re.compile(r"\s*,\s*"), _COMMA),
    (re.compile(r"\s+"), _WS),
]


def _tokenize_files_to_codes_mapping(value: str) -> Any:
    ...


def parse_files_to_codes_mapping(value: str) -> Any:
    ...


def normalize_paths(
    paths: list[str],
    parent: str = os.curdir,
) -> list[str]:
    ...


def normalize_path(path: str, parent: str = os.curdir) -> str:
    ...


@functools.lru_cache(maxsize=1)
def stdin_get_value() -> str:
    ...


def stdin_get_lines() -> list[str]:
    ...


def is_using_stdin(paths: Sequence[str]) -> bool:
    ...


def fnmatch(filename: str, patterns: Sequence[str]) -> bool:
    ...


def matches_filename(
    path: str,
    patterns: Sequence[str],
    log_message: str,
    logger: logging.Logger,
) -> bool:
    ...


def get_python_version() -> str:
    ...


def normalize_pypi_name(s: str) -> str:
    ...