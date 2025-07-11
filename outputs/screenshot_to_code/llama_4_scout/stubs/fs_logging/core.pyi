from datetime import datetime
import json
import os
from openai.types.chat import ChatCompletionMessageParam

def write_logs(prompt_messages: list[ChatCompletionMessageParam], completion: str) -> None:
    ...