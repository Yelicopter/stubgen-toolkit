import asyncio
import json
import base64
from typing import Any, Dict

import httpx
from bs4 import BeautifulSoup as bs

from ghunt import globals as gb
from ghunt.objects.base import GHuntCreds
from ghunt.errors import *
from ghunt.helpers.utils import *
from ghunt.helpers import listener
from ghunt.helpers.knowledge import get_domain_of_service, get_package_sig
from ghunt.knowledge.services import services_baseurls

async def android_master_auth(as_client: Any, oauth_token: str) -> tuple[str, list[str], str, str]:
    ...

async def android_oauth_app(as_client: Any, master_token: str, package_name: str, scopes: list[str]) -> tuple[str, list[str], int]:
    ...

async def gen_osid(as_client: Any, cookies: Dict[str, str], generated_osids: Dict[str, str], service: str) -> None:
    ...

async def gen_osids(as_client: Any, cookies: Dict[str, str], osids: Dict[str, str]) -> Dict[str, str]:
    ...

async def check_cookies(as_client: Any, cookies: Dict[str, str]) -> bool:
    ...

async def check_osid(as_client: Any, cookies: Dict[str, str], service: str) -> bool:
    ...

async def check_osids(as_client: Any, cookies: Dict[str, str], osids: Dict[str, str]) -> bool:
    ...

async def check_master_token(as_client: Any, master_token: str) -> bool:
    ...

async def gen_cookies_and_osids(as_client: Any, ghunt_creds: GHuntCreds, osids: list[str] = [*services_baseurls.keys()]) -> None:
    ...

async def check_and_gen(as_client: Any, ghunt_creds: GHuntCreds) -> None:
    ...

def auth_dialog() -> tuple[str, str]:
    ...

async def load_and_auth(as_client: Any, help: bool = True) -> GHuntCreds:
    ...