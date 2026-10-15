from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ApiAppResponseOwnerAccount(SdkBaseModel):
    """An object describing the app's owner"""

    account_id: Optional[str] = UNSET
    """The owner account's ID"""

    email_address: Optional[str] = UNSET
    """The owner account's email address"""


class ApiAppResponseOwnerAccountDict(TypedDict):
    account_id: NotRequired[str]
    email_address: NotRequired[str]
