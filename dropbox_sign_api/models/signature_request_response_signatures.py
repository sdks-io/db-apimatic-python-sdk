from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class SignatureRequestResponseSignatures(SdkBaseModel):
    """An array of signature objects, 1 for each signer."""

    signature_id: Optional[str] = UNSET
    """Signature identifier."""

    signer_group_guid: OptionalNullable[str] = UNSET
    """Signer Group GUID"""

    signer_email_address: Optional[str] = UNSET
    """The email address of the signer."""

    signer_name: OptionalNullable[str] = UNSET
    """The name of the signer."""

    signer_role: OptionalNullable[str] = UNSET
    """The role of the signer."""

    order: OptionalNullable[int] = UNSET
    """If signer order is assigned this is the 0-based index for this signer."""

    status_code: Optional[str] = UNSET
    """The current status of the signature. eg: awaiting_signature, signed, declined."""

    decline_reason: OptionalNullable[str] = UNSET
    """The reason provided by the signer for declining the request."""

    signed_at: OptionalNullable[int] = UNSET
    """Time that the document was signed or null."""

    last_viewed_at: OptionalNullable[int] = UNSET
    """The time that the document was last viewed by this signer or null."""

    last_reminded_at: OptionalNullable[int] = UNSET
    """The time the last reminder email was sent to the signer or null."""

    has_pin: Optional[bool] = UNSET
    """Boolean to indicate whether this signature requires a PIN to access."""

    has_sms_auth: OptionalNullable[bool] = UNSET
    """Boolean to indicate whether this signature has SMS authentication enabled."""

    has_sms_delivery: OptionalNullable[bool] = UNSET
    """Boolean to indicate whether this signature has SMS delivery enabled."""

    sms_phone_number: OptionalNullable[str] = UNSET
    """The SMS phone number used for authentication or signature request delivery."""

    reassigned_by: OptionalNullable[str] = UNSET
    """Email address of original signer who reassigned to this signer."""

    reassignment_reason: OptionalNullable[str] = UNSET
    """Reason provided by original signer who reassigned to this signer."""

    reassigned_from: OptionalNullable[str] = UNSET
    """Previous signature identifier."""

    error: OptionalNullable[str] = UNSET
    """Error message pertaining to this signer, or null."""


class SignatureRequestResponseSignaturesDict(TypedDict):
    signature_id: NotRequired[str]
    signer_group_guid: NotRequired[str | None]
    signer_email_address: NotRequired[str]
    signer_name: NotRequired[str | None]
    signer_role: NotRequired[str | None]
    order: NotRequired[int | None]
    status_code: NotRequired[str]
    decline_reason: NotRequired[str | None]
    signed_at: NotRequired[int | None]
    last_viewed_at: NotRequired[int | None]
    last_reminded_at: NotRequired[int | None]
    has_pin: NotRequired[bool]
    has_sms_auth: NotRequired[bool | None]
    has_sms_delivery: NotRequired[bool | None]
    sms_phone_number: NotRequired[str | None]
    reassigned_by: NotRequired[str | None]
    reassignment_reason: NotRequired[str | None]
    reassigned_from: NotRequired[str | None]
    error: NotRequired[str | None]
