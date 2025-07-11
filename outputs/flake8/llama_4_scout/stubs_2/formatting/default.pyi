from __future__ import annotations

from flake8.formatting import base
from flake8.violation import Violation

COLORS = {
    "bold": "\033[1m",
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "reset": "\033[m",
}
COLORS_OFF = {k: "" for k in COLORS}


class SimpleFormatter(base.BaseFormatter):
    error_format: str

    def format(self, error: Violation) -> str:
        ...


class Default(SimpleFormatter):
    error_format = (
        "%(bold)s%(path)s%(reset)s"
        "%(cyan)s:%(reset)s%(row)d%(cyan)s:%(reset)s%(col)d%(cyan)s:%(reset)s "
        "%(bold)s%(red)s%(code)s%(reset)s %(text)s"
    )

    def after_init(self) -> None:
        ...


class Pylint(SimpleFormatter):
    error_format = "%(path)s:%(row)d: %(code)s %(text)s"


class FilenameOnly(SimpleFormatter):
    error_format = "%(path)s"

    def after_init(self) -> None:
        ...

    def show_source(self, error: Violation) -> None:
        ...

    def format(self, error: Violation) -> str:
        ...


class Nothing(base.BaseFormatter):
    def format(self, error: Violation) -> None:
        ...

    def show_source(self, error: Violation) -> None:
        ...