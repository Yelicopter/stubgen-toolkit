import os
import platform

from rich import inspect
from rich.console import Console, get_windows_console_features
from rich.panel import Panel
from rich.pretty import Pretty


def report() -> None:
    ...