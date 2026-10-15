from __future__ import annotations

from typing import Any

from pydantic import EmailStr
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, FileResponse, Optional, SdkBaseModel
from .sub_cc import SubCc, SubCcDict
from .sub_custom_field import SubCustomField, SubCustomFieldDict
from .sub_editor_options import SubEditorOptions, SubEditorOptionsDict
from .sub_field_options import SubFieldOptions, SubFieldOptionsDict
from .sub_signing_options import SubSigningOptions, SubSigningOptionsDict
from .sub_unclaimed_draft_template_signer import SubUnclaimedDraftTemplateSigner, SubUnclaimedDraftTemplateSignerDict


class UnclaimedDraftCreateEmbeddedWithTemplateRequest(SdkBaseModel):
    allow_decline: bool = False
    """Allows signers to decline to sign a document if ``true``. Defaults to ``false``."""

    allow_reassign: bool = False
    """Allows signers to reassign their signature requests to other signers if set to ``true``. Defaults to ``false``.

    **NOTE:** Only available for Premium plan and higher."""

    ccs: Optional[list[SubCc]] = UNSET
    """Add CC email recipients. Required when a CC role exists for the Template."""

    client_id: str
    """Client id of the app used to create the draft. Used to apply the branding and callback url defined for the
    app."""

    custom_fields: Optional[list[SubCustomField]] = UNSET
    """An array defining values and options for custom fields. Required when a custom field exists in the Template."""

    editor_options: Optional[SubEditorOptions] = UNSET
    """This allows the requester to specify editor options when a preparing a document"""

    field_options: Optional[SubFieldOptions] = UNSET
    """This allows the requester to specify field options for a signature request."""

    files: Optional[FileResponse] = UNSET
    """Use ``files[]`` to append additional files to the signature request being created from the template. Dropbox Sign
    will parse the files for `text tags <https://app.hellosign.com/api/textTagsWalkthrough>`__ and append it to the
    signature request. Text tags for signers not on the template(s) will be ignored.

    **files** or **file_urls[]** is required, but not both."""

    file_urls: Optional[list[str]] = UNSET
    """Use file_urls[] to append additional files to the signature request being created from the template. Dropbox Sign
    will download the file, then parse it for `text tags <https://app.hellosign.com/api/textTagsWalkthrough>`__, and
    append to the signature request. Text tags for signers not on the template(s) will be ignored.

    **files** or **file_urls[]** is required, but not both."""

    force_signer_roles: bool = False
    """Provide users the ability to review/edit the template signer roles."""

    force_subject_message: bool = False
    """Provide users the ability to review/edit the template subject and message."""

    hold_request: bool = False
    """The request from this draft will not automatically send to signers post-claim if set to 1. Requester must
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

    preview_only: bool = False
    """This allows the requester to enable the preview experience (i.e. does not allow the requester's end user to add
    any additional fields via the editor).

    - ``preview_only=true``: Allows requesters to enable the preview only experience.
    - ``preview_only=false``: Allows requesters to disable the preview only experience.

    **NOTE:** This parameter overwrites ``show_preview=1`` (if set)."""

    requester_email_address: EmailStr
    """The email address of the user that should be designated as the requester of this draft."""

    requesting_redirect_url: Optional[str] = UNSET
    """The URL you want signers redirected to after they successfully request a signature."""

    show_preview: bool = False
    """This allows the requester to enable the editor/preview experience.

    - ``show_preview=true``: Allows requesters to enable the editor/preview experience.
    - ``show_preview=false``: Allows requesters to disable the editor/preview experience."""

    show_progress_stepper: bool = True
    """When only one step remains in the signature request process and this parameter is set to ``false`` then the
    progress stepper will be hidden."""

    signers: Optional[list[SubUnclaimedDraftTemplateSigner]] = UNSET
    """Add Signers to your Templated-based Signature Request."""

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

    template_ids: list[str]
    """Use ``template_ids`` to create a SignatureRequest from one or more templates, in the order in which the templates
    will be used."""

    test_mode: bool = False
    """Whether this is a test, the signature request created from this draft will not be legally binding if set to
    ``true``. Defaults to ``false``."""

    title: Optional[str] = UNSET
    """The title you want to assign to the SignatureRequest."""

    populate_auto_fill_fields: bool = False
    """Controls whether `auto fill fields <https://faq.hellosign.com/hc/en-us/articles/360051467511-Auto-Fill-Fields>`__
    can automatically populate a signer's information during signing.

    **NOTE:** Keep your signer's information safe by ensuring that the _signer on your signature request is the intended
    party_ before using this feature."""

    allow_ccs: bool = False
    """This allows the requester to specify whether the user is allowed to provide email addresses to CC when claiming
    the draft."""


class UnclaimedDraftCreateEmbeddedWithTemplateRequestDict(TypedDict):
    allow_decline: NotRequired[bool]
    allow_reassign: NotRequired[bool]
    ccs: NotRequired[list[SubCcDict]]
    client_id: str
    custom_fields: NotRequired[list[SubCustomFieldDict]]
    editor_options: NotRequired[SubEditorOptionsDict]
    field_options: NotRequired[SubFieldOptionsDict]
    files: NotRequired[FileResponse]
    file_urls: NotRequired[list[str]]
    force_signer_roles: NotRequired[bool]
    force_subject_message: NotRequired[bool]
    hold_request: NotRequired[bool]
    is_for_embedded_signing: NotRequired[bool]
    message: NotRequired[str]
    metadata: NotRequired[dict[str, Any]]
    preview_only: NotRequired[bool]
    requester_email_address: EmailStr
    requesting_redirect_url: NotRequired[str]
    show_preview: NotRequired[bool]
    show_progress_stepper: NotRequired[bool]
    signers: NotRequired[list[SubUnclaimedDraftTemplateSignerDict]]
    signing_options: NotRequired[SubSigningOptionsDict]
    signing_redirect_url: NotRequired[str]
    skip_me_now: NotRequired[bool]
    subject: NotRequired[str]
    template_ids: list[str]
    test_mode: NotRequired[bool]
    title: NotRequired[str]
    populate_auto_fill_fields: NotRequired[bool]
    allow_ccs: NotRequired[bool]
