from ghunt.objects.utils import TMPrinter
from rich.console import Console
from typing import Any

config: Any
tmprinter: TMPrinter
rc: Console

def init_globals() -> None: ...