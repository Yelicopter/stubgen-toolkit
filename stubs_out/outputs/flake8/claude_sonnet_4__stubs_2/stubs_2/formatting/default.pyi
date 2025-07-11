from flake8.formatting import base
from flake8.violation import Violation as Violation
from typing import Optional

COLORS: dict[str, str]
COLORS_OFF: dict[str, str]

class SimpleFormatter(base.BaseFormatter):
    def format(self, error: Violation) -> Optional[str]: ...

class Default(SimpleFormatter):
    error_format: str
    def after_init(self) -> None: ...

class Pylint(SimpleFormatter):
    error_format: str

class FilenameOnly(SimpleFormatter):
    error_format: str
    def after_init(self) -> None: ...
    def show_source(self, error: Violation) -> Optional[str]: ...
    def format(self, error: Violation) -> Optional[str]: ...

class Nothing(base.BaseFormatter):
    def format(self, error: Violation) -> Optional[str]: ...
    def show_source(self, error: Violation) -> Optional[str]: ...
