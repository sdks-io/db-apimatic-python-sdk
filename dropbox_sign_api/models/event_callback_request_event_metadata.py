from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class EventCallbackRequestEventMetadata(SdkBaseModel):
    """Specific metadata about the event."""

    related_signature_id: OptionalNullable[str] = UNSET
    """Signature ID for a specific signer. Applicable to ``signature_request_signed`` and ``signature_request_viewed``
    events."""

    reported_for_account_id: OptionalNullable[str] = UNSET
    """Account ID the event was reported for."""

    reported_for_app_id: OptionalNullable[str] = UNSET
    """App ID the event was reported for."""

    event_message: OptionalNullable[str] = UNSET
    """Message about a declined or failed (due to error) signature flow."""


class EventCallbackRequestEventMetadataDict(TypedDict):
    related_signature_id: NotRequired[str | None]
    reported_for_account_id: NotRequired[str | None]
    reported_for_app_id: NotRequired[str | None]
    event_message: NotRequired[str | None]
