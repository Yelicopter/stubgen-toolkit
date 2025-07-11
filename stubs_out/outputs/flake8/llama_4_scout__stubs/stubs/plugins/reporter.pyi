from _typeshed import Incomplete
from flake8.formatting.base import BaseFormatter as BaseFormatter
from flake8.plugins.finder import LoadedPlugin as LoadedPlugin
from typing import Any

LOG: Incomplete

def make(reporters: dict[str, LoadedPlugin], options: Any) -> BaseFormatter: ...
