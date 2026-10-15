from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class SignatureRequestResponseAttachment(SdkBaseModel):
    """Signer attachments."""

    id: str
    """The unique ID for this attachment."""

    signer: str
    """The Signer this attachment is assigned to."""

    name: str
    """The name of this attachment."""

    required: bool
    """A boolean value denoting if this attachment is required."""

    instructions: OptionalNullable[str] = UNSET
    """Instructions for Signer."""

    uploaded_at: OptionalNullable[int] = UNSET
    """Timestamp when attachment was uploaded by Signer."""


class SignatureRequestResponseAttachmentDict(TypedDict):
    id: str
    signer: str
    name: str
    required: bool
    instructions: NotRequired[str | None]
    uploaded_at: NotRequired[int | None]
