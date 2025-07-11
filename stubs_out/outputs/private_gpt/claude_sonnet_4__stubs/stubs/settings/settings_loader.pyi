import logging
from collections.abc import Iterable
from pathlib import Path as Path
from private_gpt.constants import PROJECT_ROOT_PATH as PROJECT_ROOT_PATH
from private_gpt.settings.yaml import load_yaml_with_envvars as load_yaml_with_envvars
from pydantic.v1.utils import deep_update as deep_update, unique_list as unique_list
from typing import Any, Dict, List

logger: logging.Logger
active_profiles: List[str]

def merge_settings(settings: Iterable[Dict[str, Any]]) -> Dict[str, Any]: ...
def load_settings_from_profile(profile: str) -> Dict[str, Any]: ...
def load_active_settings() -> Dict[str, Any]: ...
