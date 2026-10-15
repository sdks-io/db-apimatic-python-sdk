from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .event import Event, EventDict
from .signature_request_response import SignatureRequestResponse, SignatureRequestResponseDict


class SignUrlInvalidEvent(SdkBaseModel):
    event: Event
    signature_request: Optional[SignatureRequestResponse] = UNSET
    """Contains information about a signature request."""


class SignUrlInvalidEventDict(TypedDict):
    event: EventDict
    signature_request: NotRequired[SignatureRequestResponseDict]
