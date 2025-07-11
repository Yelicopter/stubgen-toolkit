from typing import Any, Dict
from ghunt.objects.apis import Parser

class PersonGplusExtendedData(Parser):
    contentRestriction: str
    isEntrepriseUser: bool
    def __init__(self) -> None: ...
    def _scrape(self, gplus_data: Any) -> None: ...

class PersonDynamiteExtendedData(Parser):
    presence: str
    entityType: str
    dndState: str
    customerId: str
    def __init__(self) -> None: ...
    def _scrape(self, dynamite_data: Any) -> None: ...

class PersonExtendedData(Parser):
    dynamiteData: PersonDynamiteExtendedData
    gplusData: PersonGplusExtendedData
    def __init__(self) -> None: ...
    def _scrape(self, extended_data: Any) -> None: ...

class PersonPhoto(Parser):
    url: str
    isDefault: bool
    flathash: Any
    def __init__(self) -> None: ...
    async def _scrape(self, as_client: Any, photo_data: Any, photo_type: str) -> None: ...

class PersonEmail(Parser):
    value: str
    def __init__(self) -> None: ...
    def _scrape(self, email_data: Any) -> None: ...

class PersonName(Parser):
    fullname: str
    firstName: str
    lastName: str
    def __init__(self) -> None: ...
    def _scrape(self, name_data: Any) -> None: ...

class PersonProfileInfo(Parser):
    userTypes: list
    def __init__(self) -> None: ...
    def _scrape(self, profile_data: Any) -> None: ...

class PersonSourceIds(Parser):
    lastUpdated: Any
    def __init__(self) -> None: ...
    def _scrape(self, source_ids_data: Any) -> None: ...

class PersonInAppReachability(Parser):
    apps: list
    def __init__(self) -> None: ...
    def _scrape(self, apps_data: Any, container_name: str) -> None: ...

class PersonContainers(Dict[str, Any]):
    ...

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
    async def _scrape(self, as_client: Any, person_data: Any) -> None: ...