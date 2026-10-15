from __future__ import annotations

from pydantic import EmailStr
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class FaxLineAddUserRequest(SdkBaseModel):
    number: str
    """The Fax Line number"""

    account_id: Optional[str] = UNSET
    """Account ID"""

    email_address: Optional[EmailStr] = UNSET
    """Email address"""


class FaxLineAddUserRequestDict(TypedDict):
    number: str
    account_id: NotRequired[str]
    email_address: NotRequired[EmailStr]
