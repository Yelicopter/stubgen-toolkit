import importlib.util
import os
import re
import sys
from typing import Any, Dict, List, Tuple
import click
import click.parser
import click.shell_completion
from ._completion_shared import (
    COMPLETION_SCRIPT_BASH,
    COMPLETION_SCRIPT_FISH,
    COMPLETION_SCRIPT_POWER_SHELL,
    COMPLETION_SCRIPT_ZSH,
    Shells,
)

try:
    from click.shell_completion import split_arg_string as click_split_arg_string
except ImportError:
    from click.parser import split_arg_string as click_split_arg_string

try:
    import shellingham
except ImportError:
    shellingham = None

def _sanitize_help_text(text: str) -> str: ...

class BashComplete(click.shell_completion.BashComplete):
    name: str
    source_template: str
    def source_vars(self) -> Dict[str, str]: ...
    def get_completion_args(self) -> Tuple[List[str], str]: ...
    def format_completion(self, item: click.shell_completion.CompletionItem) -> str: ...
    def complete(self) -> str: ...

class ZshComplete(click.shell_completion.ZshComplete):
    name: str
    source_template: str
    def source_vars(self) -> Dict[str, str]: ...
    def get_completion_args(self) -> Tuple[List[str], str]: ...
    def format_completion(self, item: click.shell_completion.CompletionItem) -> str: ...
    def complete(self) -> str: ...

class FishComplete(click.shell_completion.FishComplete):
    name: str
    source_template: str
    def source_vars(self) -> Dict[str, str]: ...
    def get_completion_args(self) -> Tuple[List[str], str]: ...
    def format_completion(self, item: click.shell_completion.CompletionItem) -> str: ...
    def complete(self) -> str: ...

class PowerShellComplete(click.shell_completion.ShellComplete):
    name: str
    source_template: str
    def source_vars(self) -> Dict[str, str]: ...
    def get_completion_args(self) -> Tuple[List[str], str]: ...
    def format_completion(self, item: click.shell_completion.CompletionItem) -> str: ...

def completion_init() -> None: ...