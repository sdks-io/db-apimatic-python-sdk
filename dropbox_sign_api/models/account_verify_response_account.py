from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AccountVerifyResponseAccount(SdkBaseModel):
    email_address: Optional[str] = UNSET
    """The email address associated with the Account."""


class AccountVerifyResponseAccountDict(TypedDict):
    email_address: NotRequired[str]
