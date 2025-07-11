from private_gpt.launcher import create_app
from private_gpt.di import global_injector

app = create_app(global_injector)