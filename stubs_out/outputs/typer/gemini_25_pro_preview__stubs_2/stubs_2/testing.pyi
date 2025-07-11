import click
from .main import Typer as Typer
from click.testing import CliRunner as ClickCliRunner, Result as Result
from typing import Any, IO, Mapping, Optional, Sequence, Union

class CliRunner(ClickCliRunner):
    def invoke(self, app: click.Command, args: Optional[Union[str, Sequence[str]]] = ..., input: Optional[Union[bytes, str, IO[Any]]] = ..., env: Optional[Mapping[str, Optional[str]]] = ..., catch_exceptions: Optional[bool] = ..., color: bool = ..., **extra: Any) -> Result: ...
