import logging
from datetime import datetime
from logging import Handler, LogRecord
from pathlib import Path
from types import ModuleType
from typing import ClassVar, Iterable, List, Optional, Type, Union

from rich._null_file import NullFile

from . import get_console
from ._log_render import FormatTimeCallable, LogRender
from .console import Console, ConsoleRenderable
from .highlighter import Highlighter, ReprHighlighter
from .text import Text
from .traceback import Traceback


class RichHandler(Handler):
    ...