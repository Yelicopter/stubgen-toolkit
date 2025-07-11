from _typeshed import Incomplete

class PersonGplusExtendedData:
    contentRestriction: str
    isEntrepriseUser: bool
    def __init__(self) -> None: ...

class PersonDynamiteExtendedData:
    presence: str
    entityType: str
    dndState: str
    customerId: str
    def __init__(self) -> None: ...

class PersonExtendedData:
    dynamiteData: Incomplete
    gplusData: Incomplete
    def __init__(self) -> None: ...

class PersonPhoto:
    url: str
    isDefault: bool
    flathash: Incomplete
    def __init__(self) -> None: ...

class PersonEmail:
    value: str
    def __init__(self) -> None: ...

class PersonName:
    fullname: str
    firstName: str
    lastName: str
    def __init__(self) -> None: ...

class PersonProfileInfo:
    userTypes: Incomplete
    def __init__(self) -> None: ...

class PersonSourceIds:
    lastUpdated: Incomplete
    def __init__(self) -> None: ...

class PersonInAppReachability:
    apps: Incomplete
    def __init__(self) -> None: ...

class Person:
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
