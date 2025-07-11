from .main import Typer as Typer
from click.testing import CliRunner as ClickCliRunner, Result as Result
from typing import Any, IO, Mapping, Optional, Sequence, Union

class CliRunner(ClickCliRunner):
    def invoke(self, app: Typer, args: Optional[Union[str, Sequence[str]]] = ..., input: Optional[Union[bytes, str, IO[Any]]] = ..., env: Optional[Mapping[str, Optional[str]]] = ..., catch_exceptions: bool = ..., color: bool = ..., **extra: Any) -> Result: ...
