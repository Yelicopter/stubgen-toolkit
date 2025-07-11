import os
import logging
import uuid
from typing import Optional

from config import DEBUG_DIR, IS_DEBUG_ENABLED

class DebugFileWriter:
    debug_artifacts_path: str
    
    def __init__(self) -> None: ...
    def write_to_file(self, filename: str, content: str) -> None: ...
    def extract_html_content(self, text: str) -> str: ...