from collections.abc import Iterator
from llama_index.core.llms import ChatResponse, CompletionResponse
from private_gpt.server.chunks.chunks_service import Chunk as Chunk
from pydantic import BaseModel
from typing import Literal

class OpenAIDelta(BaseModel):
    content: str | None

class OpenAIMessage(BaseModel):
    role: Literal['assistant', 'system', 'user']
    content: str | None

class OpenAIChoice(BaseModel):
    finish_reason: str | None
    delta: OpenAIDelta | None
    message: OpenAIMessage | None
    sources: list[Chunk] | None
    index: int

class OpenAICompletion(BaseModel):
    id: str
    object: Literal['completion', 'completion.chunk']
    created: int
    model: Literal['private-gpt']
    choices: list[OpenAIChoice]
    @classmethod
    def from_text(cls, text: str | None, finish_reason: str | None = ..., sources: list[Chunk] | None = ...) -> OpenAICompletion: ...
    @classmethod
    def json_from_delta(cls, *, text: str | None, finish_reason: str | None = ..., sources: list[Chunk] | None = ...) -> str: ...

def to_openai_response(response: str | ChatResponse, sources: list[Chunk] | None = ...) -> OpenAICompletion: ...
def to_openai_sse_stream(response_generator: Iterator[str | CompletionResponse | ChatResponse], sources: list[Chunk] | None = ...) -> Iterator[str]: ...
