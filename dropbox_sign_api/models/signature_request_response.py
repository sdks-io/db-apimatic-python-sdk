from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .signature_request_response_attachment import (
    SignatureRequestResponseAttachment,
    SignatureRequestResponseAttachmentDict,
)
from .signature_request_response_signatures import (
    SignatureRequestResponseSignatures,
    SignatureRequestResponseSignaturesDict,
)
from .unions.signature_request_response_custom_field_base import (
    SignatureRequestResponseCustomFieldBase,
    SignatureRequestResponseCustomFieldBaseDict,
)
from .unions.signature_request_response_data_base import (
    SignatureRequestResponseDataBase,
    SignatureRequestResponseDataBaseDict,
)


class SignatureRequestResponse(SdkBaseModel):
    """Contains information about a signature request."""

    test_mode: bool = False
    """Whether this is a test signature request. Test requests have no legal value. Defaults to ``false``."""

    signature_request_id: Optional[str] = UNSET
    """The id of the SignatureRequest."""

    requester_email_address: OptionalNullable[str] = UNSET
    """The email address of the initiator of the SignatureRequest."""

    title: Optional[str] = UNSET
    """The title the specified Account uses for the SignatureRequest."""

    original_title: Optional[str] = UNSET
    """Default Label for account."""

    subject: OptionalNullable[str] = UNSET
    """The subject in the email that was initially sent to the signers."""

    message: OptionalNullable[str] = UNSET
    """The custom message in the email that was initially sent to the signers."""

    metadata: Optional[dict[str, Any]] = UNSET
    """The metadata attached to the signature request."""

    created_at: Optional[int] = UNSET
    """Time the signature request was created."""

    expires_at: OptionalNullable[int] = UNSET
    """The time when the signature request will expire unsigned signatures. See `Signature Request Expiration Date
    <https://developers.hellosign.com/docs/signature-request/expiration/>`__ for details."""

    is_complete: Optional[bool] = UNSET
    """Whether or not the SignatureRequest has been fully executed by all signers."""

    is_declined: Optional[bool] = UNSET
    """Whether or not the SignatureRequest has been declined by a signer."""

    has_error: Optional[bool] = UNSET
    """Whether or not an error occurred (either during the creation of the SignatureRequest or during one of the
    signings)."""

    files_url: Optional[str] = UNSET
    """The URL where a copy of the request's documents can be downloaded."""

    signing_url: OptionalNullable[str] = UNSET
    """The URL where a signer, after authenticating, can sign the documents. This should only be used by users with
    existing Dropbox Sign accounts as they will be required to log in before signing."""

    details_url: Optional[str] = UNSET
    """The URL where the requester and the signers can view the current status of the SignatureRequest."""

    cc_email_addresses: Optional[list[str]] = UNSET
    """A list of email addresses that were CCed on the SignatureRequest. They will receive a copy of the final PDF once
    all the signers have signed."""

    signing_redirect_url: OptionalNullable[str] = UNSET
    """The URL you want the signer redirected to after they successfully sign."""

    final_copy_uri: OptionalNullable[str] = UNSET
    """The path where the completed document can be downloaded"""

    template_ids: OptionalNullable[list[str]] = UNSET
    """Templates IDs used in this SignatureRequest (if any)."""

    custom_fields: OptionalNullable[list[SignatureRequestResponseCustomFieldBase]] = UNSET
    """An array of Custom Field objects containing the name and type of each custom field.

    * Text Field uses ``SignatureRequestResponseCustomFieldText``
    * Checkbox Field uses ``SignatureRequestResponseCustomFieldCheckbox``"""

    attachments: OptionalNullable[list[SignatureRequestResponseAttachment]] = UNSET
    """Signer attachments."""

    response_data: OptionalNullable[list[SignatureRequestResponseDataBase]] = UNSET
    """An array of form field objects containing the name, value, and type of each textbox or checkmark field filled in
    by the signers."""

    signatures: Optional[list[SignatureRequestResponseSignatures]] = UNSET
    """An array of signature objects, 1 for each signer."""

    bulk_send_job_id: OptionalNullable[str] = UNSET
    """The ID of the Bulk Send job which sent the signature request, if applicable."""


class SignatureRequestResponseDict(TypedDict):
    test_mode: NotRequired[bool]
    signature_request_id: NotRequired[str]
    requester_email_address: NotRequired[str | None]
    title: NotRequired[str]
    original_title: NotRequired[str]
    subject: NotRequired[str | None]
    message: NotRequired[str | None]
    metadata: NotRequired[dict[str, Any]]
    created_at: NotRequired[int]
    expires_at: NotRequired[int | None]
    is_complete: NotRequired[bool]
    is_declined: NotRequired[bool]
    has_error: NotRequired[bool]
    files_url: NotRequired[str]
    signing_url: NotRequired[str | None]
    details_url: NotRequired[str]
    cc_email_addresses: NotRequired[list[str]]
    signing_redirect_url: NotRequired[str | None]
    final_copy_uri: NotRequired[str | None]
    template_ids: NotRequired[list[str] | None]
    custom_fields: NotRequired[list[SignatureRequestResponseCustomFieldBaseDict] | None]
    attachments: NotRequired[list[SignatureRequestResponseAttachmentDict] | None]
    response_data: NotRequired[list[SignatureRequestResponseDataBaseDict] | None]
    signatures: NotRequired[list[SignatureRequestResponseSignaturesDict]]
    bulk_send_job_id: NotRequired[str | None]
