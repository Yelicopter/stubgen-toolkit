from __future__ import annotations

import argparse
import os
from collections.abc import Sequence
from typing import Optional

from pre_commit_hooks.util import cmd_output


def main(argv: Optional[Sequence[str]] = None) -> int: ...


if __name__ == '__main__':
    raise SystemExit(main())