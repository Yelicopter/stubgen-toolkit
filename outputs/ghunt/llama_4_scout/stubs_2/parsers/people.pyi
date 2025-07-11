from typing import Dict, List
from datetime import datetime

class PersonGplusExtendedData:
    def __init__(self) -> None:
        self.contentRestriction: str = ""
        self.isEntrepriseUser: bool = False

    def _scrape(self, gplus_data: Dict) -> None:
        ...

class PersonDynamiteExtendedData:
    def __init__(self) -> None:
        self.presence: str = ""
        self.entityType: str = ""
        self.dndState: str = ""
        self.customerId: str = ""

    def _scrape(self, dynamite_data: Dict) -> None:
        ...

class PersonExtendedData:
    def __init__(self) -> None:
        self.dynamiteData: PersonDynamiteExtendedData = PersonDynamiteExtendedData()
        self.gplusData: PersonGplusExtendedData = PersonGplusExtendedData()

    def _scrape(self, extended_data: Dict) -> None:
        ...

class PersonPhoto:
    def __init__(self) -> None:
        self.url: str = ""
        self.isDefault: bool = False
        self.flathash: str = None

    async def _scrape(self, as_client: object, photo_data: Dict, photo_type: str) -> None:
        ...

class PersonEmail:
    def __init__(self) -> None:
        self.value: str = ""

    def _scrape(self, email_data: Dict) -> None:
        ...

class PersonName:
    def __init__(self) -> None:
        self.fullname: str = ""
        self.firstName: str = ""
        self.lastName: str = ""

    def _scrape(self, name_data: Dict) -> None:
        ...

class PersonProfileInfo:
    def __init__(self) -> None:
        self.userTypes: List[str] = []

    def _scrape(self, profile_data: Dict) -> None:
        ...

class PersonSourceIds:
    def __init__(self) -> None:
        self.lastUpdated: datetime = None

    def _scrape(self, source_ids_data: Dict) -> None:
        ...

class PersonInAppReachability:
    def __init__(self) -> None:
        self.apps: List[str] = []

    def _scrape(self, apps_data: List[Dict], container_name: str) -> None:
        ...

class Person:
    def __init__(self) -> None:
        self.personId: str = ""
        self.sourceIds: Dict[str, PersonSourceIds] = {}
        self.emails: Dict[str, PersonEmail] = {}
        self.names: Dict[str, PersonName] = {}
        self.profileInfos: Dict[str, PersonProfileInfo] = {}
        self.profilePhotos: Dict[str, PersonPhoto] = {}
        self.coverPhotos: Dict[str, PersonPhoto] = {}
        self.inAppReachability: Dict[str, PersonInAppReachability] = {}
        self.extendedData: PersonExtendedData = PersonExtendedData()

    async def _scrape(self, as_client: object, person_data: Dict) -> None:
        ...