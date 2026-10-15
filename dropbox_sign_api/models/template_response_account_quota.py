from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TemplateResponseAccountQuota(SdkBaseModel):
    """An array of the designated CC roles that must be specified when sending a SignatureRequest using this
    Template."""

    templates_left: Optional[int] = UNSET
    """API templates remaining."""

    api_signature_requests_left: Optional[int] = UNSET
    """API signature requests remaining."""

    documents_left: Optional[int] = UNSET
    """Signature requests remaining."""

    sms_verifications_left: Optional[int] = UNSET
    """SMS verifications remaining."""


class TemplateResponseAccountQuotaDict(TypedDict):
    templates_left: NotRequired[int]
    api_signature_requests_left: NotRequired[int]
    documents_left: NotRequired[int]
    sms_verifications_left: NotRequired[int]
