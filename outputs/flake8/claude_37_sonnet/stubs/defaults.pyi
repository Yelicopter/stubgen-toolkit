from __future__ import annotations

import re
from typing import FrozenSet, Pattern, Tuple

EXCLUDE: Tuple[str, ...]
IGNORE: Tuple[str, ...]
MAX_LINE_LENGTH: int
INDENT_SIZE: int

WHITESPACE: FrozenSet[str]

STATISTIC_NAMES: Tuple[str, ...]

NOQA_INLINE_REGEXP: Pattern[str]

NOQA_FILE: Pattern[str]

VALID_CODE_PREFIX: Pattern[str]