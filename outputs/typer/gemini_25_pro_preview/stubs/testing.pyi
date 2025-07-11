from typing import IO, Any, Mapping, Optional, Sequence, Union

from click.testing import CliRunner as ClickCliRunner
from click.testing import Result

from .main import Typer

class CliRunner(ClickCliRunner):
    def invoke(
        self,
        app: Typer,
        args: Optional[Union[str, Sequence[str]]] = ...,
        input: Optional[Union[bytes, str, IO[Any]]] = ...,
        env: Optional[Mapping[str, Optional[str]]] = ...,
        catch_exceptions: bool = ...,
        color: bool = ...,
        **extra: Any,
    ) -> Result: ...