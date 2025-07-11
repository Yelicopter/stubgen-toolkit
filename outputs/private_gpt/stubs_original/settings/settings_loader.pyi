from _typeshed import Incomplete
from collections.abc import Iterable
from private_gpt.constants import PROJECT_ROOT_PATH as PROJECT_ROOT_PATH
from private_gpt.settings.yaml import load_yaml_with_envvars as load_yaml_with_envvars
from typing import Any

logger: Incomplete
active_profiles: list[str]

def merge_settings(settings: Iterable[dict[str, Any]]) -> dict[str, Any]: ...
def load_settings_from_profile(profile: str) -> dict[str, Any]: ...
def load_active_settings() -> dict[str, Any]: ...
