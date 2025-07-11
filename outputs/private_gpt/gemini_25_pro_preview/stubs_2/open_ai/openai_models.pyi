from __future__ import annotations

from collections.abc import Iterator
from typing import Literal, Optional

from llama_index.core.llms import ChatResponse, CompletionResponse
from pydantic import BaseModel, Field

from private_gpt.server.chunks.chunks_service import Chunk

class OpenAIDelta(BaseModel):
    content: str | None

class OpenAIMessage(BaseModel):
    role: Literal["user", "assistant", "system"] = Field(default="user")
    content: str | None

class OpenAIChoice(BaseModel):
    finish_reason: str | None = Field(examples=["stop"])
    delta: OpenAIDelta | None
    message: OpenAIMessage | None
    sources: list[Chunk] | None
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
        text: str | None,
        finish_reason: str | None = ...,
        sources: list[Chunk] | None = ...,
    ) -> OpenAICompletion: ...
    @classmethod
    def json_from_delta(
        cls,
        *,
        text: str | None,
        finish_reason: str | None = ...,
        sources: list[Chunk] | None = ...,
    ) -> str: ...

def to_openai_response(
    response: ChatResponse | str, sources: list[Chunk] | None = ...
) -> OpenAICompletion: ...
def to_openai_sse_stream(
    response_generator: Iterator[CompletionResponse | ChatResponse | str],
    sources: list[Chunk] | None = ...,
) -> Iterator[str]: ...