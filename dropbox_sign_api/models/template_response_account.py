from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .template_response_account_quota import TemplateResponseAccountQuota, TemplateResponseAccountQuotaDict


class TemplateResponseAccount(SdkBaseModel):
    account_id: Optional[str] = UNSET
    """The id of the Account."""

    email_address: Optional[str] = UNSET
    """The email address associated with the Account."""

    is_locked: Optional[bool] = UNSET
    """Returns ``true`` if the user has been locked out of their account by a team admin."""

    is_paid_hs: Optional[bool] = UNSET
    """Returns ``true`` if the user has a paid Dropbox Sign account."""

    is_paid_hf: Optional[bool] = UNSET
    """Returns ``true`` if the user has a paid HelloFax account."""

    quotas: Optional[TemplateResponseAccountQuota] = UNSET
    """An array of the designated CC roles that must be specified when sending a SignatureRequest using this
    Template."""


class TemplateResponseAccountDict(TypedDict):
    account_id: NotRequired[str]
    email_address: NotRequired[str]
    is_locked: NotRequired[bool]
    is_paid_hs: NotRequired[bool]
    is_paid_hf: NotRequired[bool]
    quotas: NotRequired[TemplateResponseAccountQuotaDict]
