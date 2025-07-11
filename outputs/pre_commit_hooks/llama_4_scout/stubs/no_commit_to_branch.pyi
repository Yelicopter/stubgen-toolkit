from __future__ import annotations

import argparse
import re
from collections.abc import Sequence
from typing import AbstractSet

from pre_commit_hooks.util import CalledProcessError
from pre_commit_hooks.util import cmd_output

def is_on_branch(
    protected: AbstractSet[str],
    patterns: AbstractSet[str] = frozenset(),
) -> bool:
    ...

def main(argv: Sequence[str] | None = None) -> int:
    ...