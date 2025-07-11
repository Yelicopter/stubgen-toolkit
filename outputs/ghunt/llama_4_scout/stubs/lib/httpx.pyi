import httpx

class AsyncClient(httpx.AsyncClient):
    ...

    def _merge_cookies(self, cookies: Dict[str, str]) -> Dict[str, str]:
        ...