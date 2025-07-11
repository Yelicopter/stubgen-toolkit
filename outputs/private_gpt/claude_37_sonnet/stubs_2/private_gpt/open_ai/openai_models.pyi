import time
import uuid
from collections.abc import Iterator
from typing import List, Literal, Optional

from llama_index.core.llms import ChatResponse, CompletionResponse
from pydantic import BaseModel, Field

from private_gpt.server.chunks.chunks_service import Chunk

class OpenAIDelta(BaseModel):
    content: str | None

class OpenAIMessage(BaseModel):
    role: Literal["user", "assistant", "system"] = Field(default="user")
    content: str | None

class OpenAIChoice(BaseModel):
    finish_reason: Optional[str] = Field(examples=["stop"])
    delta: Optional[OpenAIDelta] = None
    message: Optional[OpenAIMessage] = None
    sources: Optional[List[Chunk]] = None
    index: int = 0

class OpenAICompletion(BaseModel):
    id: str
    object: Literal["completion", "completion.chunk"] = Field(default="completion")
    created: int = Field(..., examples=[1623340000])
    model: Literal["private-gpt"]
    choices: list[OpenAIChoice]

    @classmethod
    def from_text(
        cls,
        text: str,
        finish_reason: Optional[str] = None,
        sources: Optional[List[Chunk]] = None,
    ) -> OpenAICompletion: ...

    @classmethod
    def json_from_delta(
        cls,
        *,
        text: str,
        finish_reason: Optional[str] = None,
        sources: Optional[List[Chunk]] = None,
    ) -> str: ...

def to_openai_response(
    response: ChatResponse | CompletionResponse | str, sources: Optional[List[Chunk]] = None
) -> OpenAICompletion: ...

def to_openai_sse_stream(
    response_generator: Iterator[ChatResponse | CompletionResponse | str],
    sources: Optional[List[Chunk]] = None,
) -> Iterator[str]: ...