import os
import logging
import uuid

from config import DEBUG_DIR, IS_DEBUG_ENABLED

class DebugFileWriter:
    def __init__(self) -> None:
        ...

    def write_to_file(self, filename: str, content: str) -> None:
        ...

    def extract_html_content(self, text: str) -> str:
        ...