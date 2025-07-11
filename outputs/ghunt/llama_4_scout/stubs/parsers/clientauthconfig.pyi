from typing import List, Dict

from ghunt.objects.apis import Parser

class CacBrand(Parser):
    def __init__(self) -> None:
        self.brand_id: str = ""
        self.project_ids: List[str] = []
        self.project_numbers: List[str] = []
        self.display_name: str = ""
        self.icon_url: str = ""
        self.stored_icon_url: str = ""
        self.support_email: str = ""
        self.home_page_url: str = ""
        self.terms_of_service_urls: List[str] = []
        self.privacy_policy_urls: List[str] = []
        self.direct_notice_to_parents_url: str = ""
        self.brand_state: CacBrandState = CacBrandState()
        self.clients: List[str] = []
        self.review: CacReview = CacReview()
        self.is_org_internal: bool = False
        self.risc_configuration: CacRiscConfiguration = CacRiscConfiguration()
        self.consistency_token: str = ""
        self.creation_time: str = ""
        self.verified_brand: CacVerifiedBrand = CacVerifiedBrand()

    def _scrape(self, base_model_data: Dict) -> None:
        ...

class CacBrandState(Parser):
    def __init__(self) -> None:
        self.state: str = ""
        self.admin_id: str = ""
        self.reason: str = ""
        self.limits: CacLimits = CacLimits()
        self.brand_setup: str = ""
        self.creation_flow: str = ""
        self.update_timestamp: str = ""

    def _scrape(self, brand_state_data: Dict) -> None:
        ...

class CacLimits(Parser):
    def __init__(self) -> None:
        self.approval_quota_multiplier: int = 0
        self.max_domain_count: int = 0
        self.default_max_client_count: int = 0

    def _scrape(self, limits_data: Dict) -> None:
        ...

class CacReview(Parser):
    def __init__(self) -> None:
        self.has_abuse_verdict: bool = False
        self.is_published: bool = False
        self.review_state: str = ""
        self.high_risk_scopes_privilege: str = ""
        self.low_risk_scopes: List[str] = []
        self.pending_scopes: List[str] = []
        self.exempt_scopes: List[str] = []
        self.approved_scopes: List[str] = []
        self.historical_approved_scopes: List[str] = []
        self.pending_domains: List[str] = []
        self.approved_domains: List[str] = []
        self.enforce_request_scopes: bool = False
        self.category: List[str] = []
        self.decision_timestamp: str = ""

    def _scrape(self, review_data: Dict) -> None:
        ...

class CacRiscConfiguration(Parser):
    def __init__(self) -> None:
        self.enabled: bool = False
        self.delivery_method: str = ""
        self.receiver_supported_event_type: List[str] = []
        self.legal_agreement: List[str] = []

    def _scrape(self, risc_configuration_data: Dict) -> None:
        ...

class CacVerifiedBrand(Parser):
    def __init__(self) -> None:
        self.display_name: CacDisplayName = CacDisplayName()
        self.stored_icon_url: CacStoredIconUrl = CacStoredIconUrl()
        self.support_email: CacSupportEmail = CacSupportEmail()
        self.home_page_url: CacHomePageUrl = CacHomePageUrl()
        self.privacy_policy_url: CacPrivacyPolicyUrl = CacPrivacyPolicyUrl()
        self.terms_of_service_url: CacTermsOfServiceUrl = CacTermsOfServiceUrl()

    def _scrape(self, verified_brand_data: Dict) -> None:
        ...

class CacDisplayName(Parser):
    def __init__(self) -> None:
        self.value: str = ""
        self.reason: str = ""

    def _scrape(self, display_name_data: Dict) -> None:
        ...

class CacStoredIconUrl(Parser):
    def __init__(self) -> None:
        self.value: str = ""
        self.reason: str = ""

    def _scrape(self, stored_icon_url_data: Dict) -> None:
        ...

class CacSupportEmail(Parser):
    def __init__(self) -> None:
        self.value: str = ""
        self.reason: str = ""

    def _scrape(self, support_email_data: Dict) -> None:
        ...

class CacHomePageUrl(Parser):
    def __init__(self) -> None:
        self.value: str = ""
        self.reason: str = ""

    def _scrape(self, home_page_url_data: Dict) -> None:
        ...

class CacPrivacyPolicyUrl(Parser):
    def __init__(self) -> None:
        self.value: str = ""
        self.reason: str = ""

    def _scrape(self, privacy_policy_url_data: Dict) -> None:
        ...

class CacTermsOfServiceUrl(Parser):
    def __init__(self) -> None:
        self.value: str = ""
        self.reason: str = ""

    def _scrape(self, terms_of_service_url_data: Dict) -> None:
        ...