from fastapi import FastAPI as FastAPI
from injector import Injector as Injector
from private_gpt.settings.settings import Settings as Settings

def create_app(root_injector: Injector) -> FastAPI: ...
