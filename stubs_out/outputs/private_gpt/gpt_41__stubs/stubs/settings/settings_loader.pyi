from collections.abc import Iterable as Iterable
from pathlib import Path as Path
from private_gpt.constants import PROJECT_ROOT_PATH as PROJECT_ROOT_PATH
from private_gpt.settings.yaml import load_yaml_with_envvars as load_yaml_with_envvars
from pydantic.v1.utils import deep_update as deep_update, unique_list as unique_list

active_profiles: list[str]

def merge_settings(settings: list[dict]) -> dict: ...
def load_settings_from_profile(profile: str) -> dict: ...
def load_active_settings() -> dict: ...
