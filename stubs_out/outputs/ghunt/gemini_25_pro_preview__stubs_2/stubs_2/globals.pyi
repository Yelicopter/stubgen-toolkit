from ghunt.objects.utils import TMPrinter as TMPrinter
from rich.console import Console as Console
from typing import Any

config: Any
tmprinter: TMPrinter
rc: Console

def init_globals() -> None: ...
