from typing import IO, Any, Mapping, Optional, Sequence, Union

from click.testing import CliRunner as ClickCliRunner
from click.testing import Result
from typer.main import Typer
from typer.main import get_command as _get_command

class CliRunner(ClickCliRunner):
    def invoke(
        self,
        app: Typer,
        args: Optional[Union[str, Sequence[str]]] = None,
        input: Optional[Union[str, bytes, IO[Any]]] = None,
        env: Optional[Mapping[str, str]] = None,
        catch_exceptions: bool = True,
        color: bool = False,
        **extra: Any,
    ) -> Result: ...