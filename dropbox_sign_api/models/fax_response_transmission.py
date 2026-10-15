from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.status_code import StatusCodeOrStr


class FaxResponseTransmission(SdkBaseModel):
    recipient: str
    """Fax Transmission Recipient"""

    status_code: StatusCodeOrStr
    """Fax Transmission Status Code"""

    sent_at: Optional[int] = UNSET
    """Fax Transmission Sent Timestamp"""


class FaxResponseTransmissionDict(TypedDict):
    recipient: str
    status_code: StatusCodeOrStr
    sent_at: NotRequired[int]
