import argparse
import configparser
import logging
from collections.abc import Sequence
from flake8.options.manager import OptionManager

LOG: ...

def aggregate_options(
    manager: OptionManager,
    cfg: configparser.RawConfigParser,
    cfg_dir: str,
    argv: Sequence[str],
) -> argparse.Namespace: ...