from ghunt.objects.apis import Parser
from typing import Any, Dict

class PersonGplusExtendedData(Parser):
    contentRestriction: str
    isEntrepriseUser: bool
    def __init__(self) -> None: ...

class PersonDynamiteExtendedData(Parser):
    presence: str
    entityType: str
    dndState: str
    customerId: str
    def __init__(self) -> None: ...

class PersonExtendedData(Parser):
    dynamiteData: PersonDynamiteExtendedData
    gplusData: PersonGplusExtendedData
    def __init__(self) -> None: ...

class PersonPhoto(Parser):
    url: str
    isDefault: bool
    flathash: Any
    def __init__(self) -> None: ...

class PersonEmail(Parser):
    value: str
    def __init__(self) -> None: ...

class PersonName(Parser):
    fullname: str
    firstName: str
    lastName: str
    def __init__(self) -> None: ...

class PersonProfileInfo(Parser):
    userTypes: list
    def __init__(self) -> None: ...

class PersonSourceIds(Parser):
    lastUpdated: Any
    def __init__(self) -> None: ...

class PersonInAppReachability(Parser):
    apps: list
    def __init__(self) -> None: ...

class PersonContainers(Dict[str, Any]): ...

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
