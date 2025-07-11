from typing import Any, Dict, List
from openai.types.chat import ChatCompletionMessageParam

def write_logs(prompt_messages: List[ChatCompletionMessageParam], completion: str) -> None: ...
