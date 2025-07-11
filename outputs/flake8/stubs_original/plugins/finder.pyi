from collections.abc import Iterable as Iterable
from typing import Any, Dict, FrozenSet, List, NamedTuple, Optional, Tuple

class Plugin(NamedTuple):
    package: str
    version: str
    entry_point: Any

class LoadedPlugin(NamedTuple):
    plugin: Plugin
    obj: Any
    parameters: Dict[str, bool]

class Checkers(NamedTuple):
    tree: List[LoadedPlugin]
    logical_line: List[LoadedPlugin]
    physical_line: List[LoadedPlugin]

class Plugins(NamedTuple):
    checkers: Checkers
    reporters: Dict[str, LoadedPlugin]
    disabled: List[LoadedPlugin]

class PluginOptions(NamedTuple):
    local_plugin_paths: Tuple[str, ...]
    enable_extensions: FrozenSet[str]
    require_plugins: FrozenSet[str]

def parse_plugin_options(cfg: Any, cfg_dir: str, *, enable_extensions: Optional[str], require_plugins: Optional[str]) -> PluginOptions: ...
def find_plugins(cfg: Any, opts: PluginOptions) -> List[Plugin]: ...
def load_plugins(plugins: List[Plugin], opts: PluginOptions) -> Plugins: ...
