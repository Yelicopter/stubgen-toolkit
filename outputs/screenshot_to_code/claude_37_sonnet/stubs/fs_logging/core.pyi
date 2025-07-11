from datetime import datetime
import json
import os
from typing import Dict, Any, List
from openai.types.chat import ChatCompletionMessageParam

def write_logs(prompt_messages: List[ChatCompletionMessageParam], completion: str) -> None: ...