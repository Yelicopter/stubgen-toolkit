from collections.abc import Iterator
from llama_index.core.llms import ChatResponse as ChatResponse, CompletionResponse as CompletionResponse
from private_gpt.server.chunks.chunks_service import Chunk as Chunk
from pydantic import BaseModel
from typing import List, Literal, Optional

class OpenAIDelta(BaseModel):
    content: str | None

class OpenAIMessage(BaseModel):
    role: Literal['user', 'assistant', 'system']
    content: str | None

class OpenAIChoice(BaseModel):
    finish_reason: Optional[str]
    delta: Optional[OpenAIDelta]
    message: Optional[OpenAIMessage]
    sources: Optional[List[Chunk]]
    index: int

class OpenAICompletion(BaseModel):
    id: str
    object: Literal['completion', 'completion.chunk']
    created: int
    model: Literal['private-gpt']
    choices: list[OpenAIChoice]
    @classmethod
    def from_text(cls, text: str, finish_reason: Optional[str] = ..., sources: Optional[List[Chunk]] = ...) -> OpenAICompletion: ...
    @classmethod
    def json_from_delta(cls, *, text: str, finish_reason: Optional[str] = ..., sources: Optional[List[Chunk]] = ...) -> str: ...

def to_openai_response(response: ChatResponse | CompletionResponse | str, sources: Optional[List[Chunk]] = ...) -> OpenAICompletion: ...
def to_openai_sse_stream(response_generator: Iterator[ChatResponse | CompletionResponse | str], sources: Optional[List[Chunk]] = ...) -> Iterator[str]: ...
