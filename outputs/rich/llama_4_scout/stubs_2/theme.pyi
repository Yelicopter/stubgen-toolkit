import configparser
from typing import IO, Dict, List, Mapping, Optional

from .default_styles import DEFAULT_STYLES
from .style import Style, StyleType

class Theme:
    ...

class ThemeStackError(Exception):
    ...

class ThemeStack:
    ...