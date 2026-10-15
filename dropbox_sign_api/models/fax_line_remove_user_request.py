from __future__ import annotations

from pydantic import EmailStr
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class FaxLineRemoveUserRequest(SdkBaseModel):
    number: str
    """The Fax Line number"""

    account_id: Optional[str] = UNSET
    """Account ID of the user to remove access"""

    email_address: Optional[EmailStr] = UNSET
    """Email address of the user to remove access"""


class FaxLineRemoveUserRequestDict(TypedDict):
    number: str
    account_id: NotRequired[str]
    email_address: NotRequired[EmailStr]
