from config import ANTHROPIC_API_KEY as ANTHROPIC_API_KEY
from datetime import datetime as datetime
from llm import Llm as Llm
from models import stream_claude_response_native as stream_claude_response_native
from prompts.claude_prompts import VIDEO_PROMPT as VIDEO_PROMPT
from utils import pprint_prompt as pprint_prompt
from video.utils import assemble_claude_prompt_video as assemble_claude_prompt_video, extract_tag_content as extract_tag_content

STACK: str
VIDEO_DIR: str
SCREENSHOTS_DIR: str
OUTPUTS_DIR: str

async def main() -> None: ...
