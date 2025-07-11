from .console import Group as Group, RenderableType as RenderableType
from .control import escape_control_codes as escape_control_codes
from .highlighter import ReprHighlighter as ReprHighlighter
from .jupyter import JupyterMixin as JupyterMixin
from .panel import Panel as Panel
from .pretty import Pretty as Pretty
from .table import Table as Table
from .text import Text as Text, TextType as TextType
from inspect import cleandoc as cleandoc, getdoc as getdoc, getfile as getfile, isclass as isclass, ismodule as ismodule, signature as signature
from typing import Any, Optional

class Inspect(JupyterMixin):
    def __init__(self, obj: Any, *, title: Optional[str] = ..., help: bool = ..., methods: bool = ..., docs: bool = ..., private: bool = ..., dunder: bool = ..., sort: bool = ..., all: bool = ..., value: bool = ...) -> None: ...
    def __rich__(self) -> Panel: ...
