from injector import Injector as Injector
from private_gpt.settings.settings import Settings as Settings

def create_application_injector(settings: Settings) -> Injector: ...

global_injector: Injector
