from _typeshed import Incomplete
from flake8.formatting import base
from flake8.violation import Violation as Violation

COLORS: Incomplete
COLORS_OFF: Incomplete

class SimpleFormatter(base.BaseFormatter):
    error_format: str
    def format(self, error: Violation) -> str: ...

class Default(SimpleFormatter):
    error_format: str
    def after_init(self) -> None: ...

class Pylint(SimpleFormatter):
    error_format: str

class FilenameOnly(SimpleFormatter):
    error_format: str
    def after_init(self) -> None: ...
    def show_source(self, error: Violation) -> None: ...
    def format(self, error: Violation) -> str: ...

class Nothing(base.BaseFormatter):
    def format(self, error: Violation) -> None: ...
    def show_source(self, error: Violation) -> None: ...
