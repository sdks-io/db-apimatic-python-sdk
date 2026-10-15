from __future__ import annotations

from typing import Any

from pydantic import EmailStr, Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, FileResponse, Optional, OptionalNullable, SdkBaseModel
from .enums.type3 import Type3, Type3OrStr
from .sub_attachment import SubAttachment, SubAttachmentDict
from .sub_custom_field import SubCustomField, SubCustomFieldDict
from .sub_editor_options import SubEditorOptions, SubEditorOptionsDict
from .sub_field_options import SubFieldOptions, SubFieldOptionsDict
from .sub_form_field_group import SubFormFieldGroup, SubFormFieldGroupDict
from .sub_form_field_rule import SubFormFieldRule, SubFormFieldRuleDict
from .sub_signing_options import SubSigningOptions, SubSigningOptionsDict
from .sub_unclaimed_draft_signer import SubUnclaimedDraftSigner, SubUnclaimedDraftSignerDict
from .unions.sub_form_fields_per_document_base import SubFormFieldsPerDocumentBase, SubFormFieldsPerDocumentBaseDict


class UnclaimedDraftCreateEmbeddedRequest(SdkBaseModel):
    files: Optional[FileResponse] = UNSET
    """Use ``files[]`` to indicate the uploaded file(s) to send for signature.

    This endpoint requires either **files** or **file_urls[]**, but not both."""

    file_urls: Optional[list[str]] = UNSET
    """Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature.

    This endpoint requires either **files** or **file_urls[]**, but not both."""

    allow_ccs: bool = True
    """This allows the requester to specify whether the user is allowed to provide email addresses to CC when claiming
    the draft."""

    allow_decline: bool = False
    """Allows signers to decline to sign a document if ``true``. Defaults to ``false``."""

    allow_reassign: bool = False
    """Allows signers to reassign their signature requests to other signers if set to ``true``. Defaults to ``false``.

    **NOTE:** Only available for Premium plan and higher."""

    attachments: Optional[list[SubAttachment]] = UNSET
    """A list describing the attachments"""

    cc_email_addresses: Optional[list[EmailStr]] = UNSET
    """The email addresses that should be CCed."""

    client_id: str
    """Client id of the app used to create the draft. Used to apply the branding and callback url defined for the
    app."""

    custom_fields: Optional[list[SubCustomField]] = UNSET
    """When used together with merge fields, ``custom_fields`` allows users to add pre-filled data to their signature
    requests.

    Pre-filled data can be used with "send-once" signature requests by adding merge fields with
    ``form_fields_per_document`` or `Text Tags <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ while
    passing values back with ``custom_fields`` together in one API call.

    For using pre-filled on repeatable signature requests, merge fields are added to templates in the Dropbox Sign UI or
    by calling `/template/create_embedded_draft </api/reference/operation/templateCreateEmbeddedDraft>`__ and then
    passing ``custom_fields`` on subsequent signature requests referencing that template."""

    editor_options: Optional[SubEditorOptions] = UNSET
    """This allows the requester to specify editor options when a preparing a document"""

    field_options: Optional[SubFieldOptions] = UNSET
    """This allows the requester to specify field options for a signature request."""

    force_signer_page: bool = False
    """Provide users the ability to review/edit the signers."""

    force_subject_message: bool = False
    """Provide users the ability to review/edit the subject and message."""

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
    """Send with a value of ``true`` if you wish to enable automatic Text Tag removal. Defaults to ``false``. When using
    Text Tags it is preferred that you set this to ``false`` and hide your tags with white text or something similar
    because the automatic removal system can cause unwanted clipping. See the `Text Tags
    <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ walkthrough for more details."""

    hold_request: bool = False
    """The request from this draft will not automatically send to signers post-claim if set to ``true``. Requester must
    `release </api/reference/operation/signatureRequestReleaseHold/>`__ the request from hold when ready to send.
    Defaults to ``false``."""

    is_for_embedded_signing: bool = False
    """The request created from this draft will also be signable in embedded mode if set to ``true``. Defaults to
    ``false``."""

    message: Optional[str] = UNSET
    """The custom message in the email that will be sent to the signers."""

    metadata: Optional[dict[str, Any]] = UNSET
    """Key-value data that should be attached to the signature request. This metadata is included in all API responses
    and events involving the signature request. For example, use the metadata field to store a signer's order number for
    look up when receiving events for the signature request.

    Each request can include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters
    long and values up to 1000 characters long."""

    requester_email_address: EmailStr
    """The email address of the user that should be designated as the requester of this draft, if the draft type is
    ``request_signature``."""

    requesting_redirect_url: Optional[str] = UNSET
    """The URL you want signers redirected to after they successfully request a signature."""

    show_preview: Optional[bool] = UNSET
    """This allows the requester to enable the editor/preview experience.

    - ``show_preview=true``: Allows requesters to enable the editor/preview experience.
    - ``show_preview=false``: Allows requesters to disable the editor/preview experience."""

    show_progress_stepper: bool = True
    """When only one step remains in the signature request process and this parameter is set to ``false`` then the
    progress stepper will be hidden."""

    signers: Optional[list[SubUnclaimedDraftSigner]] = UNSET
    """Add Signers to your Unclaimed Draft Signature Request."""

    signing_options: Optional[SubSigningOptions] = UNSET
    """This allows the requester to specify the types allowed for creating a signature and specify another signing
    options.

    **NOTE:** If ``signing_options`` are not defined in the request, the allowed types will default to those specified
    in the account settings.

    **NOTE:** If ``force_advanced_signature_details`` is set, allowed types has to be defined too."""

    signing_redirect_url: Optional[str] = UNSET
    """The URL you want signers redirected to after they successfully sign."""

    skip_me_now: bool = False
    """Disables the "Me (Now)" option for the person preparing the document. Does not work with type ``send_document``.
    Defaults to ``false``."""

    subject: Optional[str] = UNSET
    """The subject in the email that will be sent to the signers."""

    test_mode: bool = False
    """Whether this is a test, the signature request created from this draft will not be legally binding if set to
    ``true``. Defaults to ``false``."""

    type_: Type3OrStr = Field(default=Type3.REQUEST_SIGNATURE, alias="type")
    """The type of the draft. By default this is ``request_signature``, but you can set it to ``send_document`` if you
    want to self sign a document and download it."""

    use_preexisting_fields: bool = False
    """Set ``use_text_tags`` to ``true`` to enable `Text Tags
    <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ parsing in your document (defaults to disabled,
    or ``false``). Alternatively, if your PDF contains pre-defined fields, enable the detection of these fields by
    setting the ``use_preexisting_fields`` to ``true`` (defaults to disabled, or ``false``). Currently we only support
    use of either ``use_text_tags`` or ``use_preexisting_fields`` parameter, not both."""

    use_text_tags: bool = False
    """Set ``use_text_tags`` to ``true`` to enable `Text Tags
    <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ parsing in your document (defaults to disabled,
    or ``false``). Alternatively, if your PDF contains pre-defined fields, enable the detection of these fields by
    setting the ``use_preexisting_fields`` to ``true`` (defaults to disabled, or ``false``). Currently we only support
    use of either ``use_text_tags`` or ``use_preexisting_fields`` parameter, not both."""

    ignore_text_tags_extraction_errors: bool = False
    """Sent with a value of ``true`` to ignore the validation errors from text tags extraction. Defaults to
    ``false``."""

    populate_auto_fill_fields: bool = False
    """Controls whether `auto fill fields <https://faq.hellosign.com/hc/en-us/articles/360051467511-Auto-Fill-Fields>`__
    can automatically populate a signer's information during signing.

    **NOTE:** Keep your signer's information safe by ensuring that the _signer on your signature request is the intended
    party_ before using this feature."""

    expires_at: OptionalNullable[int] = UNSET
    """When the signature request will expire. Unsigned signatures will be moved to the expired status, and no longer
    signable. See `Signature Request Expiration Date
    <https://developers.hellosign.com/docs/signature-request/expiration/>`__ for details.

    **NOTE:** This does not correspond to the **expires_at** returned in the response."""


class UnclaimedDraftCreateEmbeddedRequestDict(TypedDict):
    files: NotRequired[FileResponse]
    file_urls: NotRequired[list[str]]
    allow_ccs: NotRequired[bool]
    allow_decline: NotRequired[bool]
    allow_reassign: NotRequired[bool]
    attachments: NotRequired[list[SubAttachmentDict]]
    cc_email_addresses: NotRequired[list[EmailStr]]
    client_id: str
    custom_fields: NotRequired[list[SubCustomFieldDict]]
    editor_options: NotRequired[SubEditorOptionsDict]
    field_options: NotRequired[SubFieldOptionsDict]
    force_signer_page: NotRequired[bool]
    force_subject_message: NotRequired[bool]
    form_field_groups: NotRequired[list[SubFormFieldGroupDict]]
    form_field_rules: NotRequired[list[SubFormFieldRuleDict]]
    form_fields_per_document: NotRequired[list[SubFormFieldsPerDocumentBaseDict]]
    hide_text_tags: NotRequired[bool]
    hold_request: NotRequired[bool]
    is_for_embedded_signing: NotRequired[bool]
    message: NotRequired[str]
    metadata: NotRequired[dict[str, Any]]
    requester_email_address: EmailStr
    requesting_redirect_url: NotRequired[str]
    show_preview: NotRequired[bool]
    show_progress_stepper: NotRequired[bool]
    signers: NotRequired[list[SubUnclaimedDraftSignerDict]]
    signing_options: NotRequired[SubSigningOptionsDict]
    signing_redirect_url: NotRequired[str]
    skip_me_now: NotRequired[bool]
    subject: NotRequired[str]
    test_mode: NotRequired[bool]
    type_: NotRequired[Type3OrStr]
    use_preexisting_fields: NotRequired[bool]
    use_text_tags: NotRequired[bool]
    ignore_text_tags_extraction_errors: NotRequired[bool]
    populate_auto_fill_fields: NotRequired[bool]
    expires_at: NotRequired[int | None]
