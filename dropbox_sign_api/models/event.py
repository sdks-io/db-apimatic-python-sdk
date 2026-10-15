from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.event_type import EventTypeOrStr
from .event_callback_request_event_metadata import (
    EventCallbackRequestEventMetadata,
    EventCallbackRequestEventMetadataDict,
)


class Event(SdkBaseModel):
    event_time: str
    """Time the event was created (using Unix time)."""

    event_type: EventTypeOrStr
    """Type of callback event that was triggered."""

    event_hash: str
    """Generated hash used to verify source of event data."""

    event_metadata: Optional[EventCallbackRequestEventMetadata] = UNSET
    """Specific metadata about the event."""


class EventDict(TypedDict):
    event_time: str
    event_type: EventTypeOrStr
    event_hash: str
    event_metadata: NotRequired[EventCallbackRequestEventMetadataDict]
