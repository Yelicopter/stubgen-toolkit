from pydantic import BaseModel
from typing import Any, Literal

class OpenAIDelta(BaseModel): ...

class OpenAIMessage(BaseModel):
    role: Literal['user']
    content: str | None

class OpenAIChoice(BaseModel):
    finish_reason: Literal['stop']
    delta: OpenAIDelta | None
    message: OpenAIMessage | None
    sources: list[Any] | None
    index: int

class OpenAICompletion(BaseModel):
    id: str
    object: Literal['completion']
    created: int
    model: Literal['private-gpt']
    choices: list[OpenAIChoice]
