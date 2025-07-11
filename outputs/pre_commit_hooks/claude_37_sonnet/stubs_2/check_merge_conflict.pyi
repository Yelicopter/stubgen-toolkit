from __future__ import annotations

import argparse
import os.path
from collections.abc import Sequence
from typing import List, Optional

from pre_commit_hooks.util import cmd_output


CONFLICT_PATTERNS = [
    b'<<<<<<< ',
    b'======= ',
    b'=======\r\n',
    b'=======\n',
    b'>>>>>>> ',
]


def is_in_merge() -> bool: ...


def main(argv: Optional[Sequence[str]] = None) -> int: ...


if __name__ == '__main__':
    raise SystemExit(main())