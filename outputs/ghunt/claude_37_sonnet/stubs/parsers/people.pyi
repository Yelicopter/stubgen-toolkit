from typing import *
from datetime import datetime
from ghunt.errors import *
from ghunt.helpers.utils import is_default_profile_pic, unicode_patch
from ghunt.objects.apis import Parser
import httpx
import imagehash

class PersonGplusExtendedData(Parser):
    contentRestriction: str
    isEntrepriseUser: bool
    
    def __init__(self) -> None: ...
    def _scrape(self, gplus_data: Dict[str, Any]) -> None: ...

class PersonDynamiteExtendedData(Parser):
    presence: str
    entityType: str
    dndState: str
    customerId: str
    
    def __init__(self) -> None: ...
    def _scrape(self, dynamite_data: Dict[str, Any]) -> None: ...

class PersonExtendedData(Parser):
    dynamiteData: PersonDynamiteExtendedData
    gplusData: PersonGplusExtendedData
    
    def __init__(self) -> None: ...
    def _scrape(self, extended_data: Dict[str, Any]) -> None: ...

class PersonPhoto(Parser):
    url: str
    isDefault: bool
    flathash: Optional[str]
    
    def __init__(self) -> None: ...
    async def _scrape(self, as_client: httpx.AsyncClient, photo_data: Dict[str, Any], photo_type: str) -> None: ...

class PersonEmail(Parser):
    value: str
    
    def __init__(self) -> None: ...
    def _scrape(self, email_data: Dict[str, Any]) -> None: ...

class PersonName(Parser):
    fullname: str
    firstName: str
    lastName: str
    
    def __init__(self) -> None: ...
    def _scrape(self, name_data: Dict[str, Any]) -> None: ...

class PersonProfileInfo(Parser):
    userTypes: List[str]
    
    def __init__(self) -> None: ...
    def _scrape(self, profile_data: Dict[str, Any]) -> None: ...

class PersonSourceIds(Parser):
    lastUpdated: Optional[datetime]
    
    def __init__(self) -> None: ...
    def _scrape(self, source_ids_data: Dict[str, Any]) -> None: ...

class PersonInAppReachability(Parser):
    apps: List[str]
    
    def __init__(self) -> None: ...
    def _scrape(self, apps_data: List[Dict[str, Any]], container_name: str) -> None: ...

class PersonContainers(dict):
    pass

class Person(Parser):
    personId: str
    sourceIds: PersonContainers
    emails: PersonContainers
    names: PersonContainers
    profileInfos: PersonContainers
    profilePhotos: PersonContainers
    coverPhotos: PersonContainers
    inAppReachability: PersonContainers
    extendedData: PersonExtendedData
    
    def __init__(self) -> None: ...
    async def _scrape(self, as_client: httpx.AsyncClient, person_data: Dict[str, Any]) -> None: ...