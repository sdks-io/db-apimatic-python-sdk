from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_response import AccountResponse, AccountResponseDict
from .event_callback_request_event import EventCallbackRequestEvent, EventCallbackRequestEventDict
from .signature_request_response import SignatureRequestResponse, SignatureRequestResponseDict
from .template_response import TemplateResponse, TemplateResponseDict


class EventCallbackRequest(SdkBaseModel):
    event: EventCallbackRequestEvent
    """Basic information about the event that occurred."""

    account: Optional[AccountResponse] = UNSET
    signature_request: Optional[SignatureRequestResponse] = UNSET
    """Contains information about a signature request."""

    template: Optional[TemplateResponse] = UNSET
    """Contains information about the templates you and your team have created."""


class EventCallbackRequestDict(TypedDict):
    event: EventCallbackRequestEventDict
    account: NotRequired[AccountResponseDict]
    signature_request: NotRequired[SignatureRequestResponseDict]
    template: NotRequired[TemplateResponseDict]
