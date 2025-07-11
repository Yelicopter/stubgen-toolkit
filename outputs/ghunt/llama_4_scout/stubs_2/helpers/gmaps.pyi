from dateutil.relativedelta import relativedelta
from datetime import datetime
import json
from geopy import distance
from geopy.geocoders import Nominatim
from typing import Any, Dict

import httpx
from alive_progress import alive_bar

from ghunt import globals as gb
from ghunt.objects.base import *
from ghunt.helpers.utils import *
from ghunt.objects.utils import *
from ghunt.helpers.knowledge import get_gmaps_type_translation

async def get_reviews(as_client: Any, gaia_id: str) -> tuple[str, Dict[str, Any], list[Any], list[Any]]:
    ...

def avg_location(locs: list[tuple[float, float]]) -> tuple[float, float]:
    ...

def translate_confidence(percents: int) -> str:
    ...

def sanitize_location(location: Dict[str, Any]) -> Dict[str, Any]:
    ...

def calculate_probable_location(geolocator: Any, reviews_and_photos: list[Any], gmaps_radius: int) -> tuple[str, list[Dict[str, Any]]]:
    ...

def output(err: str, stats: Dict[str, Any], reviews: list[Any], photos: list[Any], gaia_id: str) -> None:
    ...