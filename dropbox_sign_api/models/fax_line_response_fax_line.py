from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_response import AccountResponse, AccountResponseDict


class FaxLineResponseFaxLine(SdkBaseModel):
    number: Optional[str] = UNSET
    """Number"""

    created_at: Optional[int] = UNSET
    """Created at"""

    updated_at: Optional[int] = UNSET
    """Updated at"""

    accounts: Optional[list[AccountResponse]] = UNSET


class FaxLineResponseFaxLineDict(TypedDict):
    number: NotRequired[str]
    created_at: NotRequired[int]
    updated_at: NotRequired[int]
    accounts: NotRequired[list[AccountResponseDict]]
