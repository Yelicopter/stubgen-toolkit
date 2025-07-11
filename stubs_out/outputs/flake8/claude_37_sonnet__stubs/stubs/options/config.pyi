import configparser
import logging
from flake8 import exceptions as exceptions
from flake8.defaults import VALID_CODE_PREFIX as VALID_CODE_PREFIX
from flake8.options.manager import OptionManager as OptionManager
from typing import Any, Dict, Optional, Tuple

LOG: logging.Logger

def load_config(config: Optional[str], extra: list[str], *, isolated: bool = ...) -> Tuple[configparser.RawConfigParser, str]: ...
def parse_config(option_manager: OptionManager, cfg: configparser.RawConfigParser, cfg_dir: str) -> Dict[str, Any]: ...
