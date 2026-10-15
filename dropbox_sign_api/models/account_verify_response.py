from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_verify_response_account import AccountVerifyResponseAccount, AccountVerifyResponseAccountDict
from .warning_response import WarningResponse, WarningResponseDict


class AccountVerifyResponse(SdkBaseModel):
    account: Optional[AccountVerifyResponseAccount] = UNSET
    warnings: Optional[list[WarningResponse]] = UNSET
    """A list of warnings."""


class AccountVerifyResponseDict(TypedDict):
    account: NotRequired[AccountVerifyResponseAccountDict]
    warnings: NotRequired[list[WarningResponseDict]]
