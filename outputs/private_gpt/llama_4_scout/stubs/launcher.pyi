from fastapi import FastAPI
from injector import Injector
from private_gpt.settings.settings import Settings

def create_app(root_injector: Injector) -> FastAPI:
    ...