from _typeshed import Incomplete
from flake8 import defaults as defaults, utils as utils
from re import Match as Match
from typing import NamedTuple

LOG: Incomplete

class Violation(NamedTuple):
    def is_inline_ignored(self, disable_noqa: bool) -> bool: ...
