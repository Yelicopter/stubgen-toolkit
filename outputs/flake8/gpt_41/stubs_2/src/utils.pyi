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

COMMA_SEPARATED_LIST_RE: re.Pattern[str]
LOCAL_PLUGIN_LIST_RE: re.Pattern[str]
NORMALIZE_PACKAGE_NAME_RE: re.Pattern[str]

def parse_comma_separated_list(
    value: str, regexp: re.Pattern[str] = ...
) -> list[str]: ...

class _Token(NamedTuple):
    tp: str
    src: str

def _tokenize_files_to_codes_mapping(value: str) -> list[_Token]: ...

def parse_files_to_codes_mapping(
    value_: str | Sequence[str],
) -> list[tuple[str, list[str]]]: ...

def normalize_paths(
    paths: list[str], parent: str = ...
) -> list[str]: ...

def normalize_path(path: str, parent: str = ...) -> str: ...

@functools.lru_cache(maxsize=1)
def stdin_get_value() -> str: ...

def stdin_get_lines() -> list[str]: ...

def is_using_stdin(paths: Sequence[str]) -> bool: ...

def fnmatch(filename: str, patterns: Sequence[str]) -> bool: ...

def matches_filename(
    path: str,
    patterns: Sequence[str],
    log_message: str,
    logger: logging.Logger,
) -> bool: ...

def get_python_version() -> str: ...

def normalize_pypi_name(s: str) -> str: ...