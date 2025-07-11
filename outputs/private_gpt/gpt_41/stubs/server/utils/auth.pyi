import logging
import secrets
from typing import Annotated

from fastapi import Depends, Header, HTTPException

from private_gpt.settings.settings import settings

NOT_AUTHENTICATED: HTTPException

def _simple_authentication(authorization: str = "") -> bool: ...
def authenticated() -> bool: ...