from typing import *
from ghunt.objects.apis import Parser

class CacBrand(Parser):
    brand_id: str
    project_ids: List[str]
    project_numbers: List[str]
    display_name: str
    icon_url: str
    stored_icon_url: str
    support_email: str
    home_page_url: str
    terms_of_service_urls: List[str]
    privacy_policy_urls: List[str]
    direct_notice_to_parents_url: str
    brand_state: 'CacBrandState'
    clients: List[Any]
    review: 'CacReview'
    is_org_internal: bool
    risc_configuration: 'CacRiscConfiguration'
    consistency_token: str
    creation_time: str
    verified_brand: 'CacVerifiedBrand'
    def __init__(self) -> None: ...
    def _scrape(self, base_model_data: Dict[str, Any]) -> None: ...

class CacBrandState(Parser):
    state: str
    admin_id: str
    reason: str
    limits: 'CacLimits'
    brand_setup: str
    creation_flow: str
    update_timestamp: str
    def __init__(self) -> None: ...
    def _scrape(self, brand_state_data: Dict[str, Any]) -> None: ...

class CacLimits(Parser):
    approval_quota_multiplier: int
    max_domain_count: int
    default_max_client_count: int
    def __init__(self) -> None: ...
    def _scrape(self, limits_data: Dict[str, Any]) -> None: ...

class CacReview(Parser):
    has_abuse_verdict: bool
    is_published: bool
    review_state: str
    high_risk_scopes_privilege: str
    low_risk_scopes: List[str]
    pending_scopes: List[str]
    exempt_scopes: List[str]
    approved_scopes: List[str]
    historical_approved_scopes: List[str]
    pending_domains: List[Any]
    approved_domains: List[str]
    enforce_request_scopes: bool
    category: List[str]
    decision_timestamp: str
    def __init__(self) -> None: ...
    def _scrape(self, review_data: Dict[str, Any]) -> None: ...

class CacRiscConfiguration(Parser):
    enabled: bool
    delivery_method: str
    receiver_supported_event_type: List[str]
    legal_agreement: List[Any]
    def __init__(self) -> None: ...
    def _scrape(self, risc_configuration_data: Dict[str, Any]) -> None: ...

class CacVerifiedBrand(Parser):
    display_name: 'CacDisplayName'
    stored_icon_url: 'CacStoredIconUrl'
    support_email: 'CacSupportEmail'
    home_page_url: 'CacHomePageUrl'
    privacy_policy_url: 'CacPrivacyPolicyUrl'
    terms_of_service_url: 'CacTermsOfServiceUrl'
    def __init__(self) -> None: ...
    def _scrape(self, verified_brand_data: Dict[str, Any]) -> None: ...

class CacDisplayName(Parser):
    value: str
    reason: str
    def __init__(self) -> None: ...
    def _scrape(self, display_name_data: Dict[str, Any]) -> None: ...

class CacStoredIconUrl(Parser):
    value: str
    reason: str
    def __init__(self) -> None: ...
    def _scrape(self, stored_icon_url_data: Dict[str, Any]) -> None: ...

class CacSupportEmail(Parser):
    value: str
    reason: str
    def __init__(self) -> None: ...
    def _scrape(self, support_email_data: Dict[str, Any]) -> None: ...

class CacHomePageUrl(Parser):
    value: str
    reason: str
    def __init__(self) -> None: ...
    def _scrape(self, home_page_url_data: Dict[str, Any]) -> None: ...

class CacPrivacyPolicyUrl(Parser):
    value: str
    reason: str
    def __init__(self) -> None: ...
    def _scrape(self, privacy_policy_url_data: Dict[str, Any]) -> None: ...

class CacTermsOfServiceUrl(Parser):
    value: str
    reason: str
    def __init__(self) -> None: ...
    def _scrape(self, terms_of_service_url_data: Dict[str, Any]) -> None: ...