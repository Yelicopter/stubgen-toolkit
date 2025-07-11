from openai.types.chat import ChatCompletionMessageParam as ChatCompletionMessageParam
from typing import List

def write_logs(prompt_messages: List[ChatCompletionMessageParam], completion: str) -> None: ...
