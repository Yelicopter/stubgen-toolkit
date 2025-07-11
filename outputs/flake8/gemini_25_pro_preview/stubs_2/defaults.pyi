from __future__ import annotations

import re

EXCLUDE: tuple[str, ...]
IGNORE: tuple[str, ...]
MAX_LINE_LENGTH: int
INDENT_SIZE: int
WHITESPACE: frozenset[str]
STATISTIC_NAMES: tuple[str, ...]
NOQA_INLINE_REGEXP: re.Pattern[str]
NOQA_FILE: re.Pattern[str]
VALID_CODE_PREFIX: re.Pattern[str]