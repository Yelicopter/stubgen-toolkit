from typing import *
from datetime import datetime
from ghunt.errors import *
from ghunt.helpers.utils import is_default_profile_pic, unicode_patch
from ghunt.objects.apis import Parser
import httpx
import imagehash

class PersonGplusExtendedData(Parser):
    def __init__(self) -> None: ...
    contentRestriction: str
    isEntrepriseUser: bool
    
    def _scrape(self, gplus_data: Dict[str, Any]) -> None: ...

class PersonDynamiteExtendedData(Parser):
    def __init__(self) -> None: ...
    presence: str
    entityType: str
    dndState: str
    customerId: str
    
    def _scrape(self, dynamite_data: Dict[str, Any]) -> None: ...

class PersonExtendedData(Parser):
    def __init__(self) -> None: ...
    dynamiteData: PersonDynamiteExtendedData
    gplusData: PersonGplusExtendedData
    
    def _scrape(self, extended_data: Dict[str, Any]) -> None: ...

class PersonPhoto(Parser):
    def __init__(self) -> None: ...
    url: str
    isDefault: bool
    flathash: Optional[str]
    
    async def _scrape(self, as_client: httpx.AsyncClient, photo_data: Dict[str, Any], photo_type: str) -> None: ...

class PersonEmail(Parser):
    def __init__(self) -> None: ...
    value: str
    
    def _scrape(self, email_data: Dict[str, Any]) -> None: ...

class PersonName(Parser):
    def __init__(self) -> None: ...
    fullname: str
    firstName: str
    lastName: str
    
    def _scrape(self, name_data: Dict[str, Any]) -> None: ...

class PersonProfileInfo(Parser):
    def __init__(self) -> None: ...
    userTypes: List[str]
    
    def _scrape(self, profile_data: Dict[str, Any]) -> None: ...

class PersonSourceIds(Parser):
    def __init__(self) -> None: ...
    lastUpdated: Optional[datetime]
    
    def _scrape(self, source_ids_data: Dict[str, Any]) -> None: ...

class PersonInAppReachability(Parser):
    def __init__(self) -> None: ...
    apps: List[str]
    
    def _scrape(self, apps_data: List[Dict[str, Any]], container_name: str) -> None: ...

class PersonContainers(dict): ...

class Person(Parser):
    def __init__(self) -> None: ...
    personId: str
    sourceIds: PersonContainers
    emails: PersonContainers
    names: PersonContainers
    profileInfos: PersonContainers
    profilePhotos: PersonContainers
    coverPhotos: PersonContainers
    inAppReachability: PersonContainers
    extendedData: PersonExtendedData
    
    async def _scrape(self, as_client: httpx.AsyncClient, person_data: Dict[str, Any]) -> None: ...