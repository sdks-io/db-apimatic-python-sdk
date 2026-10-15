from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_response import AccountResponse, AccountResponseDict
from .warning_response import WarningResponse, WarningResponseDict


class AccountGetResponse(SdkBaseModel):
    account: AccountResponse
    warnings: Optional[list[WarningResponse]] = UNSET
    """A list of warnings."""


class AccountGetResponseDict(TypedDict):
    account: AccountResponseDict
    warnings: NotRequired[list[WarningResponseDict]]
