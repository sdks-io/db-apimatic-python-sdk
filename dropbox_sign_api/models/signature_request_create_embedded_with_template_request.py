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


class SignatureRequestCreateEmbeddedWithTemplateRequest(SdkBaseModel):
    template_ids: list[str]
    """Use ``template_ids`` to create a SignatureRequest from one or more templates, in the order in which the template
    will be used."""

    allow_decline: bool = False
    """Allows signers to decline to sign a document if ``true``. Defaults to ``false``."""

    ccs: Optional[list[SubCc]] = UNSET
    """Add CC email recipients. Required when a CC role exists for the Template."""

    client_id: str
    """Client id of the app you're using to create this embedded signature request. Used for security purposes."""

    custom_fields: Optional[list[SubCustomField]] = UNSET
    """An array defining values and options for custom fields. Required when a custom field exists in the Template."""

    files: Optional[FileResponse] = UNSET
    """Use ``files[]`` to indicate the uploaded file(s) to send for signature.

    This endpoint requires either **files** or **file_urls[]**, but not both."""

    file_urls: Optional[list[str]] = UNSET
    """Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature.

    This endpoint requires either **files** or **file_urls[]**, but not both."""

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

    subject: Optional[str] = UNSET
    """The subject in the email that will be sent to the signers."""

    test_mode: bool = False
    """Whether this is a test, the signature request will not be legally binding if set to ``true``. Defaults to
    ``false``."""

    title: Optional[str] = UNSET
    """The title you want to assign to the SignatureRequest."""

    populate_auto_fill_fields: bool = False
    """Controls whether `auto fill fields <https://faq.hellosign.com/hc/en-us/articles/360051467511-Auto-Fill-Fields>`__
    can automatically populate a signer's information during signing.

    **NOTE:** Keep your signer's information safe by ensuring that the _signer on your signature request is the intended
    party_ before using this feature."""

    expires_at: OptionalNullable[int] = UNSET
    """When the signature request will expire. Unsigned signatures will be moved to the expired status, and no longer
    signable. See `Signature Request Expiration Date
    <https://developers.hellosign.com/docs/signature-request/expiration/>`__ for details."""


class SignatureRequestCreateEmbeddedWithTemplateRequestDict(TypedDict):
    template_ids: list[str]
    allow_decline: NotRequired[bool]
    ccs: NotRequired[list[SubCcDict]]
    client_id: str
    custom_fields: NotRequired[list[SubCustomFieldDict]]
    files: NotRequired[FileResponse]
    file_urls: NotRequired[list[str]]
    message: NotRequired[str]
    metadata: NotRequired[dict[str, Any]]
    signers: list[SubSignatureRequestTemplateSignerDict]
    signing_options: NotRequired[SubSigningOptionsDict]
    subject: NotRequired[str]
    test_mode: NotRequired[bool]
    title: NotRequired[str]
    populate_auto_fill_fields: NotRequired[bool]
    expires_at: NotRequired[int | None]
