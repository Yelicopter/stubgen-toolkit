import logging
from fastapi import Depends as Depends, FastAPI as FastAPI, Request as Request
from fastapi.middleware.cors import CORSMiddleware as CORSMiddleware
from injector import Injector as Injector
from llama_index.core.callbacks import CallbackManager as CallbackManager
from llama_index.core.callbacks.global_handlers import create_global_handler as create_global_handler
from private_gpt.server.chat.chat_router import chat_router as chat_router
from private_gpt.server.chunks.chunks_router import chunks_router as chunks_router
from private_gpt.server.completions.completions_router import completions_router as completions_router
from private_gpt.server.embeddings.embeddings_router import embeddings_router as embeddings_router
from private_gpt.server.health.health_router import health_router as health_router
from private_gpt.server.ingest.ingest_router import ingest_router as ingest_router
from private_gpt.server.recipes.summarize.summarize_router import summarize_router as summarize_router
from private_gpt.settings.settings import Settings as Settings

logger: logging.Logger

def create_app(root_injector: Injector) -> FastAPI: ...
async def bind_injector_to_request(request: Request) -> None: ...
