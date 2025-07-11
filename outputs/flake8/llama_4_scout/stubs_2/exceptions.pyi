from __future__ import annotations

class Flake8Exception(Exception):
    """Plain Flake8 exception."""


class EarlyQuit(Flake8Exception):
    """Except raised when encountering a KeyboardInterrupt."""


class ExecutionError(Flake8Exception):
    """Exception raised during execution of Flake8."""


class FailedToLoadPlugin(Flake8Exception):
    """Exception raised when a plugin fails to load."""

    def __init__(self, plugin_name: str, exception: Exception) -> None:
        ...

    def __str__(self) -> str:
        ...


class PluginRequestedUnknownParameters(Flake8Exception):
    """The plugin requested unknown parameters."""

    def __init__(self, plugin_name: str, exception: Exception) -> None:
        ...

    def __str__(self) -> str:
        ...


class PluginExecutionFailed(Flake8Exception):
    """The plugin failed during execution."""

    def __init__(
        self,
        filename: str,
        plugin_name: str,
        exception: Exception,
    ) -> None:
        ...

    def __str__(self) -> str:
        ...