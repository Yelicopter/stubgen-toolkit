from __future__ import annotations

class Flake8Exception(Exception): ...

class EarlyQuit(Flake8Exception): ...

class ExecutionError(Flake8Exception): ...

class FailedToLoadPlugin(Flake8Exception):
    FORMAT: str
    plugin_name: str
    original_exception: Exception

    def __init__(self, plugin_name: str, exception: Exception) -> None: ...
    def __str__(self) -> str: ...

class PluginRequestedUnknownParameters(Flake8Exception):
    FORMAT: str
    plugin_name: str
    original_exception: Exception

    def __init__(self, plugin_name: str, exception: Exception) -> None: ...
    def __str__(self) -> str: ...

class PluginExecutionFailed(Flake8Exception):
    FORMAT: str
    filename: str
    plugin_name: str
    original_exception: Exception

    def __init__(
        self,
        filename: str,
        plugin_name: str,
        exception: Exception,
    ) -> None: ...
    def __str__(self) -> str: ...