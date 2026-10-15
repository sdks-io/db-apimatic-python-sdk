from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SubAttachment(SdkBaseModel):
    instructions: Optional[str] = UNSET
    """The instructions for uploading the attachment."""

    name: str
    """The name of attachment."""

    required: bool = False
    """Determines if the attachment must be uploaded."""

    signer_index: int
    """The signer's index in the ``signers`` parameter (0-based indexing).

    **NOTE:** Only one signer can be assigned per attachment."""


class SubAttachmentDict(TypedDict):
    instructions: NotRequired[str]
    name: str
    required: NotRequired[bool]
    signer_index: int
