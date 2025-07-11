from typing import *
from ghunt.errors import *
from datetime import datetime
from ghunt.helpers.utils import is_default_profile_pic as is_default_profile_pic, unicode_patch as unicode_patch
from ghunt.objects.apis import Parser

class PersonGplusExtendedData(Parser):
    def __init__(self) -> None: ...
    contentRestriction: str
    isEntrepriseUser: bool

class PersonDynamiteExtendedData(Parser):
    def __init__(self) -> None: ...
    presence: str
    entityType: str
    dndState: str
    customerId: str

class PersonExtendedData(Parser):
    def __init__(self) -> None: ...
    dynamiteData: PersonDynamiteExtendedData
    gplusData: PersonGplusExtendedData

class PersonPhoto(Parser):
    def __init__(self) -> None: ...
    url: str
    isDefault: bool
    flathash: Optional[str]

class PersonEmail(Parser):
    def __init__(self) -> None: ...
    value: str

class PersonName(Parser):
    def __init__(self) -> None: ...
    fullname: str
    firstName: str
    lastName: str

class PersonProfileInfo(Parser):
    def __init__(self) -> None: ...
    userTypes: List[str]

class PersonSourceIds(Parser):
    def __init__(self) -> None: ...
    lastUpdated: Optional[datetime]

class PersonInAppReachability(Parser):
    def __init__(self) -> None: ...
    apps: List[str]

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
