import logging
from fastapi import Depends as Depends, HTTPException as HTTPException, Header as Header
from private_gpt.settings.settings import settings as settings

NOT_AUTHENTICATED: HTTPException
logger: logging.Logger

def authenticated() -> bool: ...
