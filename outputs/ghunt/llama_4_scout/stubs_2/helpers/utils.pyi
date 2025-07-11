from pathlib import Path
from PIL import Image
import hashlib
from typing import Any
from time import time
from datetime import datetime, timezone
from dateutil.parser import isoparse
from copy import deepcopy
import jsonpickle
import json
from packaging.version import parse as parse_version

import httpx
import imagehash
from io import BytesIO

from ghunt import globals as gb
from ghunt import version as current_version
from ghunt.lib.httpx import AsyncClient

def get_httpx_client() -> AsyncClient:
    ...

def oprint(obj: Any) -> None:
    ...

def within_docker() -> bool:
    ...

def gen_sapisidhash(sapisid: str, origin: str, timestamp: str = str(int(time()))) -> str:
    ...

def inject_osid(cookies: Dict[str, str], osids: Dict[str, str], service: str) -> Dict[str, str]:
    ...

def is_headers_syntax_good(headers: Dict[str, str]) -> bool:
    ...

async def get_url_image_flathash(as_client: Any, image_url: str) -> str:
    ...

async def is_default_profile_pic(as_client: Any, image_url: str) -> tuple[bool, str]:
    ...

def get_class_name(obj: Any) -> str:
    ...

def get_datetime_utc(date_str: str) -> datetime:
    ...

def ppnb(nb: float) -> int | float:
    ...

def parse_oauth_flow_response(body: str) -> Dict[str, str]:
    ...

def humanize_list(array: list[str]) -> str:
    ...

def unicode_patch(txt: str) -> str:
    ...

def show_version() -> None:
    ...

def check_new_version() -> tuple[bool, Dict[str, Any]]:
    ...