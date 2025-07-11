from __future__ import annotations

import sys
import tokenize

if sys.version_info >= (3, 12):  
    FSTRING_START = tokenize.FSTRING_START
    FSTRING_MIDDLE = tokenize.FSTRING_MIDDLE
    FSTRING_END = tokenize.FSTRING_END
else:  
    FSTRING_START = FSTRING_MIDDLE = FSTRING_END = -1

if sys.version_info >= (3, 14):  
    TSTRING_START = tokenize.TSTRING_START
    TSTRING_MIDDLE = tokenize.TSTRING_MIDDLE
    TSTRING_END = tokenize.TSTRING_END
else:  
    TSTRING_START = TSTRING_MIDDLE = TSTRING_END = -1