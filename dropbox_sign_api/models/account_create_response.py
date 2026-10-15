from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_response import AccountResponse, AccountResponseDict
from .oauth_token_response import OauthTokenResponse, OauthTokenResponseDict
from .warning_response import WarningResponse, WarningResponseDict


class AccountCreateResponse(SdkBaseModel):
    account: AccountResponse
    oauth_data: Optional[OauthTokenResponse] = UNSET
    warnings: Optional[list[WarningResponse]] = UNSET
    """A list of warnings."""


class AccountCreateResponseDict(TypedDict):
    account: AccountResponseDict
    oauth_data: NotRequired[OauthTokenResponseDict]
    warnings: NotRequired[list[WarningResponseDict]]
