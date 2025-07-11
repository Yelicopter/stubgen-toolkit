from typing import *
from ghunt.errors import *
from datetime import datetime
from ghunt.helpers.utils import is_default_profile_pic as is_default_profile_pic, unicode_patch as unicode_patch
from ghunt.objects.apis import Parser

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
    flathash: Optional[str]
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
    userTypes: List[str]
    def __init__(self) -> None: ...

class PersonSourceIds(Parser):
    lastUpdated: Optional[datetime]
    def __init__(self) -> None: ...

class PersonInAppReachability(Parser):
    apps: List[str]
    def __init__(self) -> None: ...

class PersonContainers(dict): ...

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
