from __future__ import annotations

import argparse
from collections.abc import Sequence

import flake8
from flake8.main import options
from flake8.options import aggregator
from flake8.options import config
from flake8.options import manager
from flake8.plugins import finder


def parse_args(
    argv: Sequence[str],
) -> tuple[finder.Plugins, argparse.Namespace]:
    ...