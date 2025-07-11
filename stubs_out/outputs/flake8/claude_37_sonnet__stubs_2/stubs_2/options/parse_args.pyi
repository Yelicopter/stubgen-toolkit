import argparse
from collections.abc import Sequence
from flake8.main import options as options
from flake8.options import aggregator as aggregator, config as config, manager as manager
from flake8.plugins import finder as finder
from typing import Tuple

def parse_args(argv: Sequence[str]) -> Tuple[finder.Plugins, argparse.Namespace]: ...
