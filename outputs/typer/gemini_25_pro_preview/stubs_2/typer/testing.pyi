from typing import IO, Any, Mapping, Optional, Sequence, Union

import click
from click.testing import CliRunner as ClickCliRunner
from click.testing import Result

from .main import Typer

class CliRunner(ClickCliRunner):
    def invoke(
        self,
        app: click.Command,
        args: Optional[Union[str, Sequence[str]]] = ...,
        input: Optional[Union[bytes, str, IO[Any]]] = ...,
        env: Optional[Mapping[str, Optional[str]]] = ...,
        catch_exceptions: Optional[bool] = ...,
        color: bool = ...,
        **extra: Any,
    ) -> Result: ...