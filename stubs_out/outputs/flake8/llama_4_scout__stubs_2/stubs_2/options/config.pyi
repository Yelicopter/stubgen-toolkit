import configparser
from _typeshed import Incomplete
from flake8 import exceptions as exceptions
from flake8.defaults import VALID_CODE_PREFIX as VALID_CODE_PREFIX
from flake8.options.manager import OptionManager as OptionManager
from typing import Optional, Sequence

LOG: Incomplete

def load_config(config: Optional[str], extra: Sequence[str], *, isolated: bool = ...) -> tuple[configparser.RawConfigParser, str]: ...
def parse_config(option_manager: OptionManager, cfg: configparser.RawConfigParser, cfg_dir: str) -> dict: ...
