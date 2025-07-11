import argparse
import configparser
from collections.abc import Sequence
from flake8.options.manager import OptionManager as OptionManager

def aggregate_options(manager: OptionManager, cfg: configparser.RawConfigParser, cfg_dir: str, argv: Sequence[str]) -> argparse.Namespace: ...
