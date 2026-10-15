from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_response import AccountResponse, AccountResponseDict
from .event import Event, EventDict


class AccountConfirmedEvent(SdkBaseModel):
    event: Event
    account: Optional[AccountResponse] = UNSET


class AccountConfirmedEventDict(TypedDict):
    event: EventDict
    account: NotRequired[AccountResponseDict]
