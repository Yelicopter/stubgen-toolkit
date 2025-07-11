from typing import Optional, Tuple

def get_authorization_scheme_param(
    authorization_header_value: Optional[str],
) -> Tuple[str, str]:
    ...
