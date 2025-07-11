import inspect
from inspect import cleandoc, getdoc, getfile, isclass, ismodule, signature
from typing import Any, Collection, Iterable, Optional, Tuple, Type, Union

from .console import Group, RenderableType
from .control import escape_control_codes
from .highlighter import ReprHighlighter
from .jupyter import JupyterMixin
from .panel import Panel
from .pretty import Pretty
from .table import Table
from .text import Text, TextType


class Inspect(JupyterMixin):
    """A renderable to inspect any Python Object.

    Args:
        obj (Any): An object to inspect.
        title (str, optional): Title to display over inspect result, or None use type. Defaults to None.
        help (bool, optional): Show full help text rather than just first paragraph. Defaults to False.
        methods (bool, optional): Enable inspection of callables. Defaults to False.
        docs (bool, optional): Also render doc strings. Defaults to True.
        private (bool, optional): Show private attributes (beginning with underscore). Defaults to False.
        dunder (bool, optional): Show attributes starting with double underscore. Defaults to False.
        sort (bool, optional): Sort attributes alphabetically. Defaults to True.
        all (bool, optional): Show all attributes. Defaults to False.
        value (bool, optional): Pretty print value. Defaults to True.
    """

    def __init__(
        self,
        obj: Any,
        *,
        title: Optional[str] = None,
        help: bool = False,
        methods: bool = False,
        docs: bool = True,
        private: bool = False,
        dunder: bool = False,
        sort: bool = True,
        all: bool = True,
        value: bool = True,
    ) -> None:
        ...

    def __rich__(self) -> Panel:
        ...