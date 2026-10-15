from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .event import Event, EventDict
from .signature_request_response import SignatureRequestResponse, SignatureRequestResponseDict


class FaxReceivedEvent(SdkBaseModel):
    event: Event
    transmission: Optional[SignatureRequestResponse] = UNSET
    """Contains information about a signature request."""


class FaxReceivedEventDict(TypedDict):
    event: EventDict
    transmission: NotRequired[SignatureRequestResponseDict]
