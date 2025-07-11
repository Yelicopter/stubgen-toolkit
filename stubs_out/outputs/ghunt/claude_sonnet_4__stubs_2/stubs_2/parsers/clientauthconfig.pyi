from typing import *
from ghunt.objects.apis import Parser

class CacBrand(Parser):
    def __init__(self) -> None: ...
    brand_id: str
    project_ids: List[str]
    project_numbers: List[int]
    display_name: str
    icon_url: str
    stored_icon_url: str
    support_email: str
    home_page_url: str
    terms_of_service_urls: List[str]
    privacy_policy_urls: List[str]
    direct_notice_to_parents_url: str
    brand_state: CacBrandState
    clients: List[str]
    review: CacReview
    is_org_internal: bool
    risc_configuration: CacRiscConfiguration
    consistency_token: str
    creation_time: str
    verified_brand: CacVerifiedBrand

class CacBrandState(Parser):
    def __init__(self) -> None: ...
    state: str
    admin_id: str
    reason: str
    limits: CacLimits
    brand_setup: str
    creation_flow: str
    update_timestamp: str

class CacLimits(Parser):
    def __init__(self) -> None: ...
    approval_quota_multiplier: int
    max_domain_count: int
    default_max_client_count: int

class CacReview(Parser):
    def __init__(self) -> None: ...
    has_abuse_verdict: bool
    is_published: bool
    review_state: str
    high_risk_scopes_privilege: str
    low_risk_scopes: List[str]
    pending_scopes: List[str]
    exempt_scopes: List[str]
    approved_scopes: List[str]
    historical_approved_scopes: List[str]
    pending_domains: List[str]
    approved_domains: List[str]
    enforce_request_scopes: bool
    category: List[str]
    decision_timestamp: str

class CacRiscConfiguration(Parser):
    def __init__(self) -> None: ...
    enabled: bool
    delivery_method: str
    receiver_supported_event_type: List[str]
    legal_agreement: List[str]

class CacVerifiedBrand(Parser):
    def __init__(self) -> None: ...
    display_name: CacDisplayName
    stored_icon_url: CacStoredIconUrl
    support_email: CacSupportEmail
    home_page_url: CacHomePageUrl
    privacy_policy_url: CacPrivacyPolicyUrl
    terms_of_service_url: CacTermsOfServiceUrl

class CacDisplayName(Parser):
    def __init__(self) -> None: ...
    value: str
    reason: str

class CacStoredIconUrl(Parser):
    def __init__(self) -> None: ...
    value: str
    reason: str

class CacSupportEmail(Parser):
    def __init__(self) -> None: ...
    value: str
    reason: str

class CacHomePageUrl(Parser):
    def __init__(self) -> None: ...
    value: str
    reason: str

class CacPrivacyPolicyUrl(Parser):
    def __init__(self) -> None: ...
    value: str
    reason: str

class CacTermsOfServiceUrl(Parser):
    def __init__(self) -> None: ...
    value: str
    reason: str
