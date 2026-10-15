from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, FileResponse, Optional, OptionalNullable, SdkBaseModel
from .sub_cc import SubCc, SubCcDict
from .sub_custom_field import SubCustomField, SubCustomFieldDict
from .sub_signature_request_template_signer import (
    SubSignatureRequestTemplateSigner,
    SubSignatureRequestTemplateSignerDict,
)
from .sub_signing_options import SubSigningOptions, SubSigningOptionsDict


class SignatureRequestSendWithTemplateRequest(SdkBaseModel):
    template_ids: list[str]
    """Use ``template_ids`` to create a SignatureRequest from one or more templates, in the order in which the template
    will be used."""

    allow_decline: bool = False
    """Allows signers to decline to sign a document if ``true``. Defaults to ``false``."""

    ccs: Optional[list[SubCc]] = UNSET
    """Add CC email recipients. Required when a CC role exists for the Template."""

    client_id: Optional[str] = UNSET
    """Client id of the app to associate with the signature request. Used to apply the branding and callback url defined
    for the app."""

    custom_fields: Optional[list[SubCustomField]] = UNSET
    """An array defining values and options for custom fields. Required when a custom field exists in the Template."""

    files: Optional[FileResponse] = UNSET
    """Use ``files[]`` to indicate the uploaded file(s) to send for signature.

    This endpoint requires either **files** or **file_urls[]**, but not both."""

    file_urls: Optional[list[str]] = UNSET
    """Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature.

    This endpoint requires either **files** or **file_urls[]**, but not both."""

    is_eid: bool = False
    """Send with a value of ``true`` if you wish to enable `electronic identification (eID)
    <https://www.hellosign.com/features/electronic-id>`__, which requires the signer to verify their identity with an
    eID provider to sign a document.<br> **NOTE:** You need the eID add-on to use this feature. Please `contact sales
    <https://sign.dropbox.com/form/contact-sales>`__ for more information. Cannot be used in ``test_mode``. Only works
    on requests with one signer."""

    message: Optional[str] = UNSET
    """The custom message in the email that will be sent to the signers."""

    metadata: Optional[dict[str, Any]] = UNSET
    """Key-value data that should be attached to the signature request. This metadata is included in all API responses
    and events involving the signature request. For example, use the metadata field to store a signer's order number for
    look up when receiving events for the signature request.

    Each request can include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters
    long and values up to 1000 characters long."""

    signers: list[SubSignatureRequestTemplateSigner]
    """Add Signers to your Templated-based Signature Request."""

    signing_options: Optional[SubSigningOptions] = UNSET
    """This allows the requester to specify the types allowed for creating a signature and specify another signing
    options.

    **NOTE:** If ``signing_options`` are not defined in the request, the allowed types will default to those specified
    in the account settings.

    **NOTE:** If ``force_advanced_signature_details`` is set, allowed types has to be defined too."""

    signing_redirect_url: Optional[str] = UNSET
    """The URL you want signers redirected to after they successfully sign."""

    subject: Optional[str] = UNSET
    """The subject in the email that will be sent to the signers."""

    test_mode: bool = False
    """Whether this is a test, the signature request will not be legally binding if set to ``true``. Defaults to
    ``false``."""

    title: Optional[str] = UNSET
    """The title you want to assign to the SignatureRequest."""

    expires_at: OptionalNullable[int] = UNSET
    """When the signature request will expire. Unsigned signatures will be moved to the expired status, and no longer
    signable. See `Signature Request Expiration Date
    <https://developers.hellosign.com/docs/signature-request/expiration/>`__ for details."""


class SignatureRequestSendWithTemplateRequestDict(TypedDict):
    template_ids: list[str]
    allow_decline: NotRequired[bool]
    ccs: NotRequired[list[SubCcDict]]
    client_id: NotRequired[str]
    custom_fields: NotRequired[list[SubCustomFieldDict]]
    files: NotRequired[FileResponse]
    file_urls: NotRequired[list[str]]
    is_eid: NotRequired[bool]
    message: NotRequired[str]
    metadata: NotRequired[dict[str, Any]]
    signers: list[SubSignatureRequestTemplateSignerDict]
    signing_options: NotRequired[SubSigningOptionsDict]
    signing_redirect_url: NotRequired[str]
    subject: NotRequired[str]
    test_mode: NotRequired[bool]
    title: NotRequired[str]
    expires_at: NotRequired[int | None]
