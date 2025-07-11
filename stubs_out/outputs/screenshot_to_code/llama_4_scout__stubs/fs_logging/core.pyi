from datetime import datetime as datetime
from openai.types.chat import ChatCompletionMessageParam as ChatCompletionMessageParam

def write_logs(prompt_messages: list[ChatCompletionMessageParam], completion: str) -> None: ...
