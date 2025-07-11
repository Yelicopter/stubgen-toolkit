from _typeshed import Incomplete
from ghunt.errors import GHuntAPIResponseParsingError as GHuntAPIResponseParsingError
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
    dynamiteData: Incomplete
    gplusData: Incomplete
    def __init__(self) -> None: ...

class PersonPhoto(Parser):
    url: str
    isDefault: bool
    flathash: Incomplete
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
    userTypes: Incomplete
    def __init__(self) -> None: ...

class PersonSourceIds(Parser):
    lastUpdated: Incomplete
    def __init__(self) -> None: ...

class PersonInAppReachability(Parser):
    apps: Incomplete
    def __init__(self) -> None: ...

class Person(Parser):
    personId: str
    sourceIds: Incomplete
    emails: Incomplete
    names: Incomplete
    profileInfos: Incomplete
    profilePhotos: Incomplete
    coverPhotos: Incomplete
    inAppReachability: Incomplete
    extendedData: Incomplete
    def __init__(self) -> None: ...
