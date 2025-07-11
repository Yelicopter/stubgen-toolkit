import argparse
import configparser
from _typeshed import Incomplete
from collections.abc import Sequence
from flake8.options import config as config
from flake8.options.manager import OptionManager as OptionManager

LOG: Incomplete

def aggregate_options(manager: OptionManager, cfg: configparser.RawConfigParser, cfg_dir: str, argv: Sequence[str]) -> argparse.Namespace: ...
