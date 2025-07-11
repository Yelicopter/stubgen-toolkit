from typing import Any, Dict
from openai.types.chat import ChatCompletionMessageParam

def write_logs(prompt_messages: List[ChatCompletionMessageParam], completion: str) -> None: ...