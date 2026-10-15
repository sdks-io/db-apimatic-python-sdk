from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, FileResponse, Optional, OptionalNullable, SdkBaseModel
from .sub_bulk_signer_list import SubBulkSignerList, SubBulkSignerListDict
from .sub_cc import SubCc, SubCcDict
from .sub_custom_field import SubCustomField, SubCustomFieldDict


class SignatureRequestBulkCreateEmbeddedWithTemplateRequest(SdkBaseModel):
    template_ids: list[str]
    """Use ``template_ids`` to create a SignatureRequest from one or more templates, in the order in which the template
    will be used."""

    signer_file: Optional[FileResponse] = UNSET
    """``signer_file`` is a CSV file defining values and options for signer fields. Required unless a ``signer_list`` is
    used, you may not use both. The CSV can have the following columns:

    - ``name``: the name of the signer filling the role of RoleName
    - ``email_address``: email address of the signer filling the role of RoleName
    - ``pin``: the 4- to 12-character access code that will secure this signer's signature page (optional)
    - ``sms_phone_number``: An E.164 formatted phone number that will receive a code via SMS to access this signer's
        signature page. (optional)

        By using the feature, you agree you are responsible for obtaining a signer's consent to receive text messages
        from Dropbox Sign related to this signature request and confirm you have obtained such consent from all signers
        prior to enabling SMS delivery for this signature request. `Learn more
        <https://faq.hellosign.com/hc/en-us/articles/15815316468877-Dropbox-Sign-SMS-tools-add-on>`__.

        **NOTE:** Not available in test mode and requires a Standard plan or higher.
    - ``*_field``: any column with a _field" suffix will be treated as a custom field (optional)

        You may only specify field values here, any other options should be set in the custom_fields request parameter.

    Example CSV:

    ```
    name, email_address, pin, company_field George, george@example.com, d79a3td, ABC Corp Mary, mary@example.com,
    gd9as5b, 123 LLC
    ```"""

    signer_list: Optional[list[SubBulkSignerList]] = UNSET
    """``signer_list`` is an array defining values and options for signer fields. Required unless a ``signer_file`` is
    used, you may not use both."""

    allow_decline: bool = False
    """Allows signers to decline to sign a document if ``true``. Defaults to ``false``."""

    ccs: Optional[list[SubCc]] = UNSET
    """Add CC email recipients. Required when a CC role exists for the Template."""

    client_id: str
    """Client id of the app you're using to create this embedded signature request. Used for security purposes."""

    custom_fields: Optional[list[SubCustomField]] = UNSET
    """When used together with merge fields, ``custom_fields`` allows users to add pre-filled data to their signature
    requests.

    Pre-filled data can be used with "send-once" signature requests by adding merge fields with
    ``form_fields_per_document`` or `Text Tags <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ while
    passing values back with ``custom_fields`` together in one API call.

    For using pre-filled on repeatable signature requests, merge fields are added to templates in the Dropbox Sign UI or
    by calling `/template/create_embedded_draft </api/reference/operation/templateCreateEmbeddedDraft>`__ and then
    passing ``custom_fields`` on subsequent signature requests referencing that template."""

    message: Optional[str] = UNSET
    """The custom message in the email that will be sent to the signers."""

    metadata: Optional[dict[str, Any]] = UNSET
    """Key-value data that should be attached to the signature request. This metadata is included in all API responses
    and events involving the signature request. For example, use the metadata field to store a signer's order number for
    look up when receiving events for the signature request.

    Each request can include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters
    long and values up to 1000 characters long."""

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


class SignatureRequestBulkCreateEmbeddedWithTemplateRequestDict(TypedDict):
    template_ids: list[str]
    signer_file: NotRequired[FileResponse]
    signer_list: NotRequired[list[SubBulkSignerListDict]]
    allow_decline: NotRequired[bool]
    ccs: NotRequired[list[SubCcDict]]
    client_id: str
    custom_fields: NotRequired[list[SubCustomFieldDict]]
    message: NotRequired[str]
    metadata: NotRequired[dict[str, Any]]
    signing_redirect_url: NotRequired[str]
    subject: NotRequired[str]
    test_mode: NotRequired[bool]
    title: NotRequired[str]
    expires_at: NotRequired[int | None]
