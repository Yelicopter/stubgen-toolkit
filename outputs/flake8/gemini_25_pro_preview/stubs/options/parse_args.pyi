from __future__ import annotations

import argparse
from collections.abc import Sequence

from flake8.plugins import finder

def parse_args(argv: list[str]) -> tuple[finder.Plugins, argparse.Namespace]: ...