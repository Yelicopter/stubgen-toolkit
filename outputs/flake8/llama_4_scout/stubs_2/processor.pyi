from __future__ import annotations

import argparse
import ast
import functools
import logging
import tokenize
from collections.abc import Generator, Sequence
from typing import Any, Optional

from flake8 import defaults
from flake8 import utils
from flake8._compat import FSTRING_END
from flake8._compat import FSTRING_MIDDLE
from flake8._compat import TSTRING_END
from flake8._compat import TSTRING_MIDDLE
from flake8.plugins.finder import LoadedPlugin

LOG = logging.getLogger(__name__)
NEWLINE = frozenset([tokenize.NL, tokenize.NEWLINE])

SKIP_TOKENS = frozenset(
    [tokenize.NL, tokenize.NEWLINE, tokenize.INDENT, tokenize.DEDENT]
)

_LogicalMapping = list[tuple[int, tuple[int, int]]]
_Logical = tuple[list[str], list[str], _LogicalMapping]


class FileProcessor:
    def __init__(
        self,
        filename: str,
        options: Any,
        lines: Optional[list[str]] = None,
    ) -> None:
        ...

    @functools.cached_property
    def file_tokens(self) -> Any:
        ...

    def fstring_start(self, lineno: int) -> None:
        ...

    def tstring_start(self, lineno: int) -> None:
        ...

    def multiline_string(
        self, token: Any
    ) -> Generator[Optional[tuple[int, int]], None, None]:
        ...

    def reset_blank_before(self) -> None:
        ...

    def delete_first_token(self) -> None:
        ...

    def visited_new_blank_line(self) -> None:
        ...

    def update_state(self, mapping: Any) -> None:
        ...

    def update_checker_state_for(self, plugin: LoadedPlugin) -> None:
        ...

    def next_logical_line(self) -> None:
        ...

    def build_logical_line_tokens(self) -> Any:
        ...

    def build_ast(self) -> Any:
        ...

    def build_logical_line(self) -> Any:
        ...

    def keyword_arguments_for(
        self,
        parameters: Any,
        arguments: Any,
    ) -> dict:
        ...

    def generate_tokens(self) -> Generator[tokenize.TokenInfo, None, None]:
        ...

    def _noqa_line_range(
        self, min_line: int, max_line: int
    ) -> dict:
        ...

    @functools.cached_property
    def _noqa_line_mapping(self) -> dict:
        ...

    def noqa_line_for(self, line_number: int) -> Optional[str]:
        ...

    def next_line(self) -> str:
        ...

    def read_lines(self) -> list[str]:
        ...

    def read_lines_from_filename(self) -> list[str]:
        ...

    def read_lines_from_stdin(self) -> list[str]:
        ...

    def should_ignore_file(self) -> bool:
        ...

    def strip_utf_bom(self) -> None:
        ...


def is_eol_token(token: Any) -> bool:
    ...


def is_multiline_string(token: Any) -> bool:
    ...


def token_is_newline(token: Any) -> bool:
    ...


def count_parentheses(
    current_parentheses_count: int, token_text: str
) -> int:
    ...


def expand_indent(line: str) -> int:
    ...


# NOTE(sigmavirus24): This was taken wholesale from
# https://github.com/PyCQA/pycodestyle. The in-line comments were edited to be
# more descriptive.
def mutate_string(text: str) -> str:
    ...