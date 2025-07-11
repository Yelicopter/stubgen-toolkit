from fastapi import HTTPException as HTTPException, Header as Header

NOT_AUTHENTICATED: HTTPException

def authenticated(_simple_authentication: bool) -> bool: ...
