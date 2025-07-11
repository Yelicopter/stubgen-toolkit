from click.testing import CliRunner as ClickCliRunner, Result as Result
from typer.main import Typer as Typer
from typing import Any

class CliRunner(ClickCliRunner):
    def invoke(self, app: Any, args: Any = ..., input: Any = ..., env: Any = ..., catch_exceptions: bool = ..., color: bool = ..., **extra: Any) -> Result: ...
