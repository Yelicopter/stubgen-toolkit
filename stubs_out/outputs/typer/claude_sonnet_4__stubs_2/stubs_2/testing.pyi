from click.testing import CliRunner as ClickCliRunner, Result as Result
from typer.main import Typer
from typing import Any, IO, Mapping, Optional, Sequence, Union

class CliRunner(ClickCliRunner):
    def invoke(self, app: Typer, args: Optional[Union[str, Sequence[str]]] = ..., input: Optional[Union[str, bytes, IO[Any]]] = ..., env: Optional[Mapping[str, Optional[str]]] = ..., catch_exceptions: Optional[bool] = ..., color: bool = ..., **extra: Any) -> Result: ...
