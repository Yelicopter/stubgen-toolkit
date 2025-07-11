from enum import Enum
from typing import Optional, Tuple
import click

class Shells(str, Enum):
    bash = "bash"
    zsh = "zsh"
    fish = "fish"
    powershell = "powershell"
    pwsh = "pwsh"

def get_completion_script(*, prog_name: str, complete_var: str, shell: str) -> str:
    ...
def install_bash(*, prog_name: str, complete_var: str, shell: str) -> Path:
    ...
def install_zsh(*, prog_name: str, complete_var: str, shell: str) -> Path:
    ...
def install_fish(*, prog_name: str, complete_var: str, shell: str) -> Path:
    ...
def install_powershell(*, prog_name: str, complete_var: str, shell: str) -> Path:
    ...
def install(
    shell: Optional[str] = None,
    prog_name: Optional[str] = None,
    complete_var: Optional[str] = None,
) -> Tuple[str, Path]:
    ...