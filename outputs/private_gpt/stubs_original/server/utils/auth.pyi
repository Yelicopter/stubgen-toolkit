from _typeshed import Incomplete
from fastapi import Depends as Depends, Header as Header
from private_gpt.settings.settings import settings as settings

NOT_AUTHENTICATED: Incomplete
logger: Incomplete

def authenticated() -> bool: ...
