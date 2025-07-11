from typing import *
from _typeshed import Incomplete
from ghunt.objects.apis import Parser as Parser

class CacBrand(Parser):
    brand_id: str
    project_ids: Incomplete
    project_numbers: Incomplete
    display_name: str
    icon_url: str
    stored_icon_url: str
    support_email: str
    home_page_url: str
    terms_of_service_urls: Incomplete
    privacy_policy_urls: Incomplete
    direct_notice_to_parents_url: str
    brand_state: Incomplete
    clients: Incomplete
    review: Incomplete
    is_org_internal: bool
    risc_configuration: Incomplete
    consistency_token: str
    creation_time: str
    verified_brand: Incomplete
    def __init__(self) -> None: ...

class CacBrandState(Parser):
    state: str
    admin_id: str
    reason: str
    limits: Incomplete
    brand_setup: str
    creation_flow: str
    update_timestamp: str
    def __init__(self) -> None: ...

class CacLimits(Parser):
    approval_quota_multiplier: int
    max_domain_count: int
    default_max_client_count: int
    def __init__(self) -> None: ...

class CacReview(Parser):
    has_abuse_verdict: bool
    is_published: bool
    review_state: str
    high_risk_scopes_privilege: str
    low_risk_scopes: Incomplete
    pending_scopes: Incomplete
    exempt_scopes: Incomplete
    approved_scopes: Incomplete
    historical_approved_scopes: Incomplete
    pending_domains: Incomplete
    approved_domains: Incomplete
    enforce_request_scopes: bool
    category: Incomplete
    decision_timestamp: str
    def __init__(self) -> None: ...

class CacRiscConfiguration(Parser):
    enabled: bool
    delivery_method: str
    receiver_supported_event_type: Incomplete
    legal_agreement: Incomplete
    def __init__(self) -> None: ...

class CacVerifiedBrand(Parser):
    display_name: Incomplete
    stored_icon_url: Incomplete
    support_email: Incomplete
    home_page_url: Incomplete
    privacy_policy_url: Incomplete
    terms_of_service_url: Incomplete
    def __init__(self) -> None: ...

class CacDisplayName(Parser):
    value: str
    reason: str
    def __init__(self) -> None: ...

class CacStoredIconUrl(Parser):
    value: str
    reason: str
    def __init__(self) -> None: ...

class CacSupportEmail(Parser):
    value: str
    reason: str
    def __init__(self) -> None: ...

class CacHomePageUrl(Parser):
    value: str
    reason: str
    def __init__(self) -> None: ...

class CacPrivacyPolicyUrl(Parser):
    value: str
    reason: str
    def __init__(self) -> None: ...

class CacTermsOfServiceUrl(Parser):
    value: str
    reason: str
    def __init__(self) -> None: ...
