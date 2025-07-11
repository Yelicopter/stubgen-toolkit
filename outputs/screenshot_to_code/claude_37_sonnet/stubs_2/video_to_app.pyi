import base64
import mimetypes
import time
import subprocess
import os
import asyncio
from datetime import datetime
from typing import Any
from prompts.claude_prompts import VIDEO_PROMPT
from utils import pprint_prompt
from config import ANTHROPIC_API_KEY
from video.utils import extract_tag_content, assemble_claude_prompt_video
from llm import Llm
from models.claude import stream_claude_response_native

STACK: str
VIDEO_DIR: str
SCREENSHOTS_DIR: str
OUTPUTS_DIR: str

async def main() -> None: ...