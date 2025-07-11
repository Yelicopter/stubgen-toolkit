import configparser
from typing import Any
from flake8.options.manager import OptionManager

def _stat_key(s: str) -> tuple[int, int]: ...
def _find_config_file(path: str) -> str | None: ...
def load_config(
    config: str | None,
    extra: list[str],
    *,
    isolated: bool = ...,
) -> tuple[configparser.RawConfigParser, str] | tuple[configparser.RawConfigParser, str]: ...
def parse_config(
    option_manager: OptionManager,
    cfg: configparser.RawConfigParser,
    cfg_dir: str,
) -> dict[str, Any]: ...