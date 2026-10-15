from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, FileResponse, Optional, SdkBaseModel
from .sub_attachment import SubAttachment, SubAttachmentDict
from .sub_field_options import SubFieldOptions, SubFieldOptionsDict
from .sub_form_field_group import SubFormFieldGroup, SubFormFieldGroupDict
from .sub_form_field_rule import SubFormFieldRule, SubFormFieldRuleDict
from .sub_merge_field import SubMergeField, SubMergeFieldDict
from .sub_template_role import SubTemplateRole, SubTemplateRoleDict
from .unions.sub_form_fields_per_document_base import SubFormFieldsPerDocumentBase, SubFormFieldsPerDocumentBaseDict


class TemplateCreateRequest(SdkBaseModel):
    files: Optional[FileResponse] = UNSET
    """Use ``files[]`` to indicate the uploaded file(s) to send for signature.

    This endpoint requires either **files** or **file_urls[]**, but not both."""

    file_urls: Optional[list[str]] = UNSET
    """Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature.

    This endpoint requires either **files** or **file_urls[]**, but not both."""

    allow_reassign: bool = False
    """Allows signers to reassign their signature requests to other signers if set to ``true``. Defaults to ``false``.

    **NOTE:** Only available for Premium plan and higher."""

    attachments: Optional[list[SubAttachment]] = UNSET
    """A list describing the attachments"""

    cc_roles: Optional[list[str]] = UNSET
    """The CC roles that must be assigned when using the template to send a signature request"""

    client_id: Optional[str] = UNSET
    """Client id of the app you're using to create this draft. Used to apply the branding and callback url defined for
    the app."""

    field_options: Optional[SubFieldOptions] = UNSET
    """This allows the requester to specify field options for a signature request."""

    form_field_groups: Optional[list[SubFormFieldGroup]] = UNSET
    """Group information for fields defined in ``form_fields_per_document``. String-indexed JSON array with
    ``group_label`` and ``requirement`` keys. ``form_fields_per_document`` must contain fields referencing a group
    defined in ``form_field_groups``."""

    form_field_rules: Optional[list[SubFormFieldRule]] = UNSET
    """Conditional Logic rules for fields defined in ``form_fields_per_document``."""

    form_fields_per_document: list[SubFormFieldsPerDocumentBase]
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

    merge_fields: Optional[list[SubMergeField]] = UNSET
    """Add merge fields to the template. Merge fields are placed by the user creating the template and used to pre-fill
    data by passing values into signature requests with the ``custom_fields`` parameter. If the signature request using
    that template *does not* pass a value into a merge field, then an empty field remains in the document."""

    message: Optional[str] = UNSET
    """The default template email message."""

    metadata: Optional[dict[str, Any]] = UNSET
    """Key-value data that should be attached to the signature request. This metadata is included in all API responses
    and events involving the signature request. For example, use the metadata field to store a signer's order number for
    look up when receiving events for the signature request.

    Each request can include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters
    long and values up to 1000 characters long."""

    signer_roles: list[SubTemplateRole]
    """An array of the designated signer roles that must be specified when sending a SignatureRequest using this
    Template."""

    subject: Optional[str] = UNSET
    """The template title (alias)."""

    test_mode: bool = False
    """Whether this is a test, the signature request created from this draft will not be legally binding if set to
    ``true``. Defaults to ``false``."""

    title: Optional[str] = UNSET
    """The title you want to assign to the SignatureRequest."""

    use_preexisting_fields: bool = False
    """Enable the detection of predefined PDF fields by setting the ``use_preexisting_fields`` to ``true`` (defaults to
    disabled, or ``false``)."""

    ignore_text_tags_extraction_errors: bool = False
    """Sent with a value of ``true`` to ignore the validation errors from text tags extraction. Defaults to
    ``false``."""


class TemplateCreateRequestDict(TypedDict):
    files: NotRequired[FileResponse]
    file_urls: NotRequired[list[str]]
    allow_reassign: NotRequired[bool]
    attachments: NotRequired[list[SubAttachmentDict]]
    cc_roles: NotRequired[list[str]]
    client_id: NotRequired[str]
    field_options: NotRequired[SubFieldOptionsDict]
    form_field_groups: NotRequired[list[SubFormFieldGroupDict]]
    form_field_rules: NotRequired[list[SubFormFieldRuleDict]]
    form_fields_per_document: list[SubFormFieldsPerDocumentBaseDict]
    merge_fields: NotRequired[list[SubMergeFieldDict]]
    message: NotRequired[str]
    metadata: NotRequired[dict[str, Any]]
    signer_roles: list[SubTemplateRoleDict]
    subject: NotRequired[str]
    test_mode: NotRequired[bool]
    title: NotRequired[str]
    use_preexisting_fields: NotRequired[bool]
    ignore_text_tags_extraction_errors: NotRequired[bool]
