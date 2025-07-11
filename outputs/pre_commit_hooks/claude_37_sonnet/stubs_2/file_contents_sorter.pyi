"""
A very simple pre-commit hook that, when passed one or more filenames
as arguments, will sort the lines in those files.

An example use case for this: you have a deploy-allowlist.txt file
in a repo that contains a list of filenames that is used to specify
files to be included in a docker container. This file has one filename
per line. Various users are adding/removing lines from this file; using
this hook on that file should reduce the instances of git merge
conflicts and keep the file nicely ordered.
"""
from __future__ import annotations

import argparse
from collections.abc import Iterable, Sequence
from typing import Any, Callable, IO, List, Optional, Union

PASS = 0
FAIL = 1


def sort_file_contents(
    f: IO[bytes],
    key: Optional[Callable[[bytes], Any]],
    *,
    unique: bool = False,
) -> int: ...


def main(argv: Optional[Sequence[str]] = None) -> int: ...


if __name__ == '__main__':
    raise SystemExit(main())