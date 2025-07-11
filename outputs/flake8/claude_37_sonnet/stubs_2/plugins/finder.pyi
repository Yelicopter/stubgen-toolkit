from __future__ import annotations

import configparser
import importlib.metadata
import inspect
import itertools
import logging
import sys
from collections.abc import Generator, Iterable
from typing import Any, Dict, FrozenSet, List, NamedTuple, Optional, Tuple, Union

from flake8 import utils
from flake8.defaults import VALID_CODE_PREFIX
from flake8.exceptions import ExecutionError
from flake8.exceptions import FailedToLoadPlugin

LOG: logging.Logger

FLAKE8_GROUPS: frozenset[str]

BANNED_PLUGINS: dict[str, str]

class Plugin(NamedTuple):
    package: str
    version: str
    entry_point: importlib.metadata.EntryPoint

class LoadedPlugin(NamedTuple):
    plugin: Plugin
    obj: Any
    parameters: dict[str, bool]

    @property
    def entry_name(self) -> str: ...
    @property
    def display_name(self) -> str: ...

class Checkers(NamedTuple):
    tree: list[LoadedPlugin]
    logical_line: list[LoadedPlugin]
    physical_line: list[LoadedPlugin]

class Plugins(NamedTuple):
    checkers: Checkers
    reporters: dict[str, LoadedPlugin]
    disabled: list[LoadedPlugin]

    def all_plugins(self) -> Generator[LoadedPlugin, None, None]: ...
    def versions_str(self) -> str: ...

class PluginOptions(NamedTuple):
    local_plugin_paths: tuple[str, ...]
    enable_extensions: frozenset[str]
    require_plugins: frozenset[str]

    @classmethod
    def blank(cls) -> PluginOptions: ...

def _parse_option(
    cfg: configparser.RawConfigParser,
    cfg_opt_name: str,
    opt: Optional[str],
) -> list[str]: ...

def parse_plugin_options(
    cfg: configparser.RawConfigParser,
    cfg_dir: str,
    *,
    enable_extensions: Optional[str],
    require_plugins: Optional[str],
) -> PluginOptions: ...

def _flake8_plugins(
    eps: Iterable[importlib.metadata.EntryPoint],
    name: str,
    version: str,
) -> Generator[Plugin, None, None]: ...

def _find_importlib_plugins() -> Generator[Plugin, None, None]: ...

def _find_local_plugins(
    cfg: configparser.RawConfigParser,
) -> Generator[Plugin, None, None]: ...

def _check_required_plugins(
    plugins: list[Plugin],
    expected: FrozenSet[str],
) -> None: ...

def find_plugins(
    cfg: configparser.RawConfigParser,
    opts: PluginOptions,
) -> list[Plugin]: ...

def _parameters_for(func: Any) -> dict[str, bool]: ...

def _load_plugin(plugin: Plugin) -> LoadedPlugin: ...

def _import_plugins(
    plugins: list[Plugin],
    opts: PluginOptions,
) -> list[LoadedPlugin]: ...

def _classify_plugins(
    plugins: list[LoadedPlugin],
    opts: PluginOptions,
) -> Plugins: ...

def load_plugins(
    plugins: list[Plugin],
    opts: PluginOptions,
) -> Plugins: ...