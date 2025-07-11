from __future__ import annotations

import configparser
import importlib.metadata
import inspect
import itertools
import logging
import sys
from collections.abc import Generator
from collections.abc import Iterable
from typing import Any
from typing import NamedTuple

from flake8 import utils
from flake8.defaults import VALID_CODE_PREFIX
from flake8.exceptions import ExecutionError
from flake8.exceptions import FailedToLoadPlugin

LOG = logging.getLogger(__name__)


class Plugin(NamedTuple):
    pass #package: str
    pass #version: str
    pass #entry_point: importlib.metadata.EntryPoint


class LoadedPlugin(NamedTuple):
    pass #plugin: Plugin
    pass #obj: Any
    pass #parameters: dict[str, bool]

    @property
    def entry_name(self) -> str:
        ...

    @property
    def display_name(self) -> str:
        ...


class Checkers(NamedTuple):
    pass #tree: list[LoadedPlugin]
    pass #logical_line: list[LoadedPlugin]
    pass #physical_line: list[LoadedPlugin]


class Plugins(NamedTuple):
    pass #checkers: Checkers
    pass #reporters: dict[str, LoadedPlugin]
    pass #disabled: list[LoadedPlugin]

    def all_plugins(self) -> Generator:
        ...

    def versions_str(self) -> str:
        ...


class PluginOptions(NamedTuple):
    pass #local_plugin_paths: tuple[str, ...]
    pass #enable_extensions: frozenset[str]
    pass #require_plugins: frozenset[str]

    @classmethod
    def blank(cls) -> PluginOptions:
        ...


def _parse_option(
    cfg: configparser.RawConfigParser,
    cfg_opt_name: str,
    opt: Optional[str],
) -> list[str]:
    ...


def parse_plugin_options(
    cfg: configparser.RawConfigParser,
    cfg_dir: str,
    *,
    enable_extensions: Optional[str],
    require_plugins: Optional[str],
) -> PluginOptions:
    ...


def _flake8_plugins(
    eps: Any,
    name: str,
    version: str,
) -> Generator:
    ...


def _find_importlib_plugins() -> Generator:
    ...


def _find_local_plugins(
    cfg: configparser.RawConfigParser,
) -> Generator:
    ...


def _check_required_plugins(
    plugins: list[Plugin],
    expected: frozenset[str],
) -> None:
    ...


def find_plugins(
    cfg: configparser.RawConfigParser,
    opts: PluginOptions,
) -> list[Plugin]:
    ...


def _parameters_for(func: Any) -> dict:
    ...


def _load_plugin(plugin: Plugin) -> LoadedPlugin:
    ...


def _import_plugins(
    plugins: list[Plugin],
    opts: PluginOptions,
) -> list[LoadedPlugin]:
    ...


def _classify_plugins(
    plugins: list[LoadedPlugin],
    opts: PluginOptions,
) -> Plugins:
    ...


def load_plugins(
    plugins: list[Plugin],
    opts: PluginOptions,
) -> Plugins:
    ...