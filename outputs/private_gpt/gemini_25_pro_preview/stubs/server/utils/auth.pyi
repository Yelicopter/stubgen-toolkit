from typing import Annotated

from fastapi import Header, HTTPException

NOT_AUTHENTICATED: HTTPException

def _simple_authentication(authorization: Annotated[str | None, Header()] = ...) -> bool: ...
def authenticated(_simple_authentication: bool) -> bool: ...