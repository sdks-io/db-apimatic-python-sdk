from __future__ import annotations

from pydantic import EmailStr
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class SignatureRequestUpdateRequest(SdkBaseModel):
    email_address: Optional[EmailStr] = UNSET
    """The new email address for the recipient.

    This will generate a new ``signature_id`` value.

    **NOTE:** Optional if ``name`` is provided."""

    name: Optional[str] = UNSET
    """The new name for the recipient.

    **NOTE:** Optional if ``email_address`` is provided."""

    signature_id: str
    """The signature ID for the recipient."""

    expires_at: OptionalNullable[int] = UNSET
    """The new time when the signature request will expire. Unsigned signatures will be moved to the expired status, and
    no longer signable. See `Signature Request Expiration Date
    <https://developers.hellosign.com/docs/signature-request/expiration/>`__ for details."""


class SignatureRequestUpdateRequestDict(TypedDict):
    email_address: NotRequired[EmailStr]
    name: NotRequired[str]
    signature_id: str
    expires_at: NotRequired[int | None]
