from __future__ import annotations

import functools
import linecache
import logging
from re import Match
from typing import NamedTuple, Optional

from flake8 import defaults
from flake8 import utils


LOG = logging.getLogger(__name__)


@functools.lru_cache(maxsize=512)
def _find_noqa(physical_line: str) -> Optional[Match]:
    ...


class Violation(NamedTuple):
    code: str
    filename: str
    line_number: int
    column_number: int
    text: str
    physical_line: Optional[str]

    def is_inline_ignored(self, disable_noqa: bool) -> bool:
        ...