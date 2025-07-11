from pydantic import BaseModel, Field
from typing import Literal

class OpenAIDelta(BaseModel):
    pass 

class OpenAIMessage(BaseModel):
    role: Literal["user"] = Field(default="user")
    content: str | None = None

class OpenAIChoice(BaseModel):
    finish_reason: Literal["stop"]
    delta: OpenAIDelta | None
    message: OpenAIMessage | None
    sources: list[Any] | None
    index: int

class OpenAICompletion(BaseModel):
    id: str
    object: Literal["completion"]
    created: int
    model: Literal["private-gpt"]
    choices: list[OpenAIChoice]