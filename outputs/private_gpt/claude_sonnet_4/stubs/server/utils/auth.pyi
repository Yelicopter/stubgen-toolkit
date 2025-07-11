import logging
import secrets
from typing import Annotated, Optional
from fastapi import Depends, Header, HTTPException
from private_gpt.settings.settings import settings

NOT_AUTHENTICATED: HTTPException
logger: logging.Logger

def _simple_authentication(authorization: Annotated[str, Header()] = "") -> bool: ...

def authenticated() -> bool: ...