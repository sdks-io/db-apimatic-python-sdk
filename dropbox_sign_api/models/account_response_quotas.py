from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class AccountResponseQuotas(SdkBaseModel):
    """Details concerning remaining monthly quotas."""

    api_signature_requests_left: OptionalNullable[int] = UNSET
    """API signature requests remaining."""

    documents_left: OptionalNullable[int] = UNSET
    """Signature requests remaining."""

    templates_total: OptionalNullable[int] = UNSET
    """Total API templates allowed."""

    templates_left: OptionalNullable[int] = UNSET
    """API templates remaining."""

    sms_verifications_left: OptionalNullable[int] = UNSET
    """SMS verifications remaining."""

    num_fax_pages_left: OptionalNullable[int] = UNSET
    """Number of fax pages left"""


class AccountResponseQuotasDict(TypedDict):
    api_signature_requests_left: NotRequired[int | None]
    documents_left: NotRequired[int | None]
    templates_total: NotRequired[int | None]
    templates_left: NotRequired[int | None]
    sms_verifications_left: NotRequired[int | None]
    num_fax_pages_left: NotRequired[int | None]
