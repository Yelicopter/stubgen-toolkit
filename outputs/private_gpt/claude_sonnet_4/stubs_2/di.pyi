from injector import Injector
from private_gpt.settings.settings import Settings, unsafe_typed_settings

def create_application_injector() -> Injector: ...

global_injector: Injector