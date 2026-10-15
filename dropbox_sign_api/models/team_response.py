from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_response import AccountResponse, AccountResponseDict


class TeamResponse(SdkBaseModel):
    """Contains information about your team and its members"""

    name: Optional[str] = UNSET
    """The name of your Team"""

    accounts: Optional[list[AccountResponse]] = UNSET
    invited_accounts: Optional[list[AccountResponse]] = UNSET
    """A list of all Accounts that have an outstanding invitation to join your Team. Note that this response is a subset
    of the response parameters found in ``GET /account``."""

    invited_emails: Optional[list[str]] = UNSET
    """A list of email addresses that have an outstanding invitation to join your Team and do not yet have a Dropbox
    Sign account."""


class TeamResponseDict(TypedDict):
    name: NotRequired[str]
    accounts: NotRequired[list[AccountResponseDict]]
    invited_accounts: NotRequired[list[AccountResponseDict]]
    invited_emails: NotRequired[list[str]]
