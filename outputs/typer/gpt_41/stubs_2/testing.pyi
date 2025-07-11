from typing import IO, Any, Mapping, Optional, Sequence, Union

from click.testing import CliRunner as ClickCliRunner
from click.testing import Result
from typer.main import Typer

class CliRunner(ClickCliRunner):
    def invoke(
        self,
        app: Any,
        args: Any = ...,
        input: Any = ...,
        env: Any = ...,
        catch_exceptions: Optional[bool] = ...,
        color: bool = ...,
        **extra: Any,
    ) -> Result: ...