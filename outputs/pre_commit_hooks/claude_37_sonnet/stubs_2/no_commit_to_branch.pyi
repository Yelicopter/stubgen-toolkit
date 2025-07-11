from __future__ import annotations

import argparse
import re
from collections.abc import Sequence
from typing import AbstractSet, List, Optional, Pattern, Set

from pre_commit_hooks.util import CalledProcessError
from pre_commit_hooks.util import cmd_output


def is_on_branch(
        protected: AbstractSet[str],
        patterns: AbstractSet[str] = frozenset(),
) -> bool: ...


def main(argv: Optional[Sequence[str]] = None) -> int: ...


if __name__ == '__main__':
    raise SystemExit(main())