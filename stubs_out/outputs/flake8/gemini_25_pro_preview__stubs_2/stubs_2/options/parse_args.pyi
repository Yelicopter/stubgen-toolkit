import argparse
from collections.abc import Sequence as Sequence
from flake8.plugins import finder as finder

def parse_args(argv: list[str]) -> tuple[finder.Plugins, argparse.Namespace]: ...
