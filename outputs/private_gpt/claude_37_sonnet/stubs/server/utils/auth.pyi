import logging
from typing import Annotated, Callable, Optional

from fastapi import Depends, Header, HTTPException

from private_gpt.settings.settings import settings

NOT_AUTHENTICATED: HTTPException
logger: logging.Logger

def _simple_authentication(authorization: Optional[str] = "") -> bool: ...
def authenticated() -> bool: ...