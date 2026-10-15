from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class AccountUpdateRequest(SdkBaseModel):
    account_id: OptionalNullable[str] = UNSET
    """The ID of the Account"""

    callback_url: Optional[str] = UNSET
    """The URL that Dropbox Sign should POST events to."""

    locale: Optional[str] = UNSET
    """The locale used in this Account. Check out the list of `supported locales
    </api/reference/constants/#supported-locales>`__ to learn more about the possible values."""


class AccountUpdateRequestDict(TypedDict):
    account_id: NotRequired[str | None]
    callback_url: NotRequired[str]
    locale: NotRequired[str]
