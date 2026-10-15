from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .account_response_quotas import AccountResponseQuotas, AccountResponseQuotasDict
from .account_response_settings import AccountResponseSettings, AccountResponseSettingsDict
from .account_response_usage import AccountResponseUsage, AccountResponseUsageDict


class AccountResponse(SdkBaseModel):
    account_id: Optional[str] = UNSET
    """The ID of the Account"""

    email_address: Optional[str] = UNSET
    """The email address associated with the Account."""

    is_locked: Optional[bool] = UNSET
    """Returns ``true`` if the user has been locked out of their account by a team admin."""

    is_paid_hs: Optional[bool] = UNSET
    """Returns ``true`` if the user has a paid Dropbox Sign account."""

    is_paid_hf: Optional[bool] = UNSET
    """Returns ``true`` if the user has a paid HelloFax account."""

    quotas: Optional[AccountResponseQuotas] = UNSET
    """Details concerning remaining monthly quotas."""

    callback_url: OptionalNullable[str] = UNSET
    """The URL that Dropbox Sign events will ``POST`` to."""

    role_code: OptionalNullable[str] = UNSET
    """The membership role for the team."""

    team_id: OptionalNullable[str] = UNSET
    """The id of the team account belongs to."""

    locale: OptionalNullable[str] = UNSET
    """The locale used in this Account. Check out the list of `supported locales
    </api/reference/constants/#supported-locales>`__ to learn more about the possible values."""

    usage: Optional[AccountResponseUsage] = UNSET
    """Details concerning monthly usage"""

    settings: Optional[AccountResponseSettings] = UNSET
    """Subset of configured settings"""


class AccountResponseDict(TypedDict):
    account_id: NotRequired[str]
    email_address: NotRequired[str]
    is_locked: NotRequired[bool]
    is_paid_hs: NotRequired[bool]
    is_paid_hf: NotRequired[bool]
    quotas: NotRequired[AccountResponseQuotasDict]
    callback_url: NotRequired[str | None]
    role_code: NotRequired[str | None]
    team_id: NotRequired[str | None]
    locale: NotRequired[str | None]
    usage: NotRequired[AccountResponseUsageDict]
    settings: NotRequired[AccountResponseSettingsDict]
