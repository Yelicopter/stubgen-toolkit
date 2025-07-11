import argparse
from collections.abc import Sequence
from flake8.plugins.finder import Plugins

def parse_args(
    argv: Sequence[str],
) -> tuple[Plugins, argparse.Namespace]: ...