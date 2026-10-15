from __future__ import annotations

from typing import Any

from pydantic import EmailStr
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, FileResponse, Optional, OptionalNullable, SdkBaseModel
from .sub_attachment import SubAttachment, SubAttachmentDict
from .sub_custom_field import SubCustomField, SubCustomFieldDict
from .sub_field_options import SubFieldOptions, SubFieldOptionsDict
from .sub_form_field_group import SubFormFieldGroup, SubFormFieldGroupDict
from .sub_form_field_rule import SubFormFieldRule, SubFormFieldRuleDict
from .sub_signature_request_grouped_signers import (
    SubSignatureRequestGroupedSigners,
    SubSignatureRequestGroupedSignersDict,
)
from .sub_signature_request_signer import SubSignatureRequestSigner, SubSignatureRequestSignerDict
from .sub_signing_options import SubSigningOptions, SubSigningOptionsDict
from .unions.sub_form_fields_per_document_base import SubFormFieldsPerDocumentBase, SubFormFieldsPerDocumentBaseDict


class SignatureRequestEditRequest(SdkBaseModel):
    files: Optional[FileResponse] = UNSET
    """Use ``files[]`` to indicate the uploaded file(s) to send for signature.

    This endpoint requires either **files** or **file_urls[]**, but not both."""

    file_urls: Optional[list[str]] = UNSET
    """Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature.

    This endpoint requires either **files** or **file_urls[]**, but not both."""

    signers: Optional[list[SubSignatureRequestSigner]] = UNSET
    """Add Signers to your Signature Request.

    This endpoint requires either **signers** or **grouped_signers**, but not both."""

    grouped_signers: Optional[list[SubSignatureRequestGroupedSigners]] = UNSET
    """Add Grouped Signers to your Signature Request.

    This endpoint requires either **signers** or **grouped_signers**, but not both."""

    allow_decline: bool = False
    """Allows signers to decline to sign a document if ``true``. Defaults to ``false``."""

    allow_reassign: bool = False
    """Allows signers to reassign their signature requests to other signers if set to ``true``. Defaults to ``false``.

    **NOTE:** Only available for Premium plan and higher."""

    attachments: Optional[list[SubAttachment]] = UNSET
    """A list describing the attachments"""

    cc_email_addresses: Optional[list[EmailStr]] = UNSET
    """The email addresses that should be CCed."""

    client_id: Optional[str] = UNSET
    """The client id of the API App you want to associate with this request. Used to apply the branding and callback url
    defined for the app."""

    custom_fields: Optional[list[SubCustomField]] = UNSET
    """When used together with merge fields, ``custom_fields`` allows users to add pre-filled data to their signature
    requests.

    Pre-filled data can be used with "send-once" signature requests by adding merge fields with
    ``form_fields_per_document`` or `Text Tags <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ while
    passing values back with ``custom_fields`` together in one API call.

    For using pre-filled on repeatable signature requests, merge fields are added to templates in the Dropbox Sign UI or
    by calling `/template/create_embedded_draft </api/reference/operation/templateCreateEmbeddedDraft>`__ and then
    passing ``custom_fields`` on subsequent signature requests referencing that template."""

    field_options: Optional[SubFieldOptions] = UNSET
    """This allows the requester to specify field options for a signature request."""

    form_field_groups: Optional[list[SubFormFieldGroup]] = UNSET
    """Group information for fields defined in ``form_fields_per_document``. String-indexed JSON array with
    ``group_label`` and ``requirement`` keys. ``form_fields_per_document`` must contain fields referencing a group
    defined in ``form_field_groups``."""

    form_field_rules: Optional[list[SubFormFieldRule]] = UNSET
    """Conditional Logic rules for fields defined in ``form_fields_per_document``."""

    form_fields_per_document: Optional[list[SubFormFieldsPerDocumentBase]] = UNSET
    """The fields that should appear on the document, expressed as an array of objects. (For more details you can read
    about it here: `Using Form Fields per Document </docs/openapi/form-fields-per-document>`__.)

    **NOTE:** Fields like **text**, **dropdown**, **checkbox**, **radio**, and **hyperlink** have additional required
    and optional parameters. Check out the list of `additional parameters
    </api/reference/constants/#form-fields-per-document>`__ for these field types.

    * Text Field use ``SubFormFieldsPerDocumentText``
    * Dropdown Field use ``SubFormFieldsPerDocumentDropdown``
    * Hyperlink Field use ``SubFormFieldsPerDocumentHyperlink``
    * Checkbox Field use ``SubFormFieldsPerDocumentCheckbox``
    * Radio Field use ``SubFormFieldsPerDocumentRadio``
    * Signature Field use ``SubFormFieldsPerDocumentSignature``
    * Date Signed Field use ``SubFormFieldsPerDocumentDateSigned``
    * Initials Field use ``SubFormFieldsPerDocumentInitials``
    * Text Merge Field use ``SubFormFieldsPerDocumentTextMerge``
    * Checkbox Merge Field use ``SubFormFieldsPerDocumentCheckboxMerge``"""

    hide_text_tags: bool = False
    """Enables automatic Text Tag removal when set to true.

    **NOTE:** Removing text tags this way can cause unwanted clipping. We recommend leaving this setting on ``false``
    and instead hiding your text tags using white text or a similar approach. See the `Text Tags Walkthrough
    <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ for more information."""

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

    use_text_tags: bool = False
    """Send with a value of ``true`` if you wish to enable `Text Tags
    <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ parsing in your document. Defaults to disabled,
    or ``false``."""

    ignore_text_tags_extraction_errors: bool = False
    """Sent with a value of ``true`` to ignore the validation errors from text tags extraction. Defaults to
    ``false``."""

    expires_at: OptionalNullable[int] = UNSET
    """When the signature request will expire. Unsigned signatures will be moved to the expired status, and no longer
    signable. See `Signature Request Expiration Date
    <https://developers.hellosign.com/docs/signature-request/expiration/>`__ for details."""


class SignatureRequestEditRequestDict(TypedDict):
    files: NotRequired[FileResponse]
    file_urls: NotRequired[list[str]]
    signers: NotRequired[list[SubSignatureRequestSignerDict]]
    grouped_signers: NotRequired[list[SubSignatureRequestGroupedSignersDict]]
    allow_decline: NotRequired[bool]
    allow_reassign: NotRequired[bool]
    attachments: NotRequired[list[SubAttachmentDict]]
    cc_email_addresses: NotRequired[list[EmailStr]]
    client_id: NotRequired[str]
    custom_fields: NotRequired[list[SubCustomFieldDict]]
    field_options: NotRequired[SubFieldOptionsDict]
    form_field_groups: NotRequired[list[SubFormFieldGroupDict]]
    form_field_rules: NotRequired[list[SubFormFieldRuleDict]]
    form_fields_per_document: NotRequired[list[SubFormFieldsPerDocumentBaseDict]]
    hide_text_tags: NotRequired[bool]
    is_eid: NotRequired[bool]
    message: NotRequired[str]
    metadata: NotRequired[dict[str, Any]]
    signing_options: NotRequired[SubSigningOptionsDict]
    signing_redirect_url: NotRequired[str]
    subject: NotRequired[str]
    test_mode: NotRequired[bool]
    title: NotRequired[str]
    use_text_tags: NotRequired[bool]
    ignore_text_tags_extraction_errors: NotRequired[bool]
    expires_at: NotRequired[int | None]
