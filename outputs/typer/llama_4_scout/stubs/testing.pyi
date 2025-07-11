from typing import IO, Any, Mapping, Optional, Sequence, Union

class CliRunner:
    def invoke(
        self,
        app: Any,
        args: Any = None,
        input: Any = None,
        env: Any = None,
        catch_exceptions: bool = True,
        color: bool = False,
        **extra: Any,
    ) -> Any:
        ...