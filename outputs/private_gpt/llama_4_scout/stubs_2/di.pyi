from injector import Injector
from private_gpt.settings.settings import Settings

def create_application_injector(settings: Settings) -> Injector:
    ...

global_injector: Injector