from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .signature_request_response_attachment import (
    SignatureRequestResponseAttachment,
    SignatureRequestResponseAttachmentDict,
)
from .template_response_account import TemplateResponseAccount, TemplateResponseAccountDict
from .template_response_ccrole import TemplateResponseCcrole, TemplateResponseCcroleDict
from .template_response_document import TemplateResponseDocument, TemplateResponseDocumentDict
from .template_response_signer_role import TemplateResponseSignerRole, TemplateResponseSignerRoleDict
from .unions.template_response_document_custom_field_base import (
    TemplateResponseDocumentCustomFieldBase,
    TemplateResponseDocumentCustomFieldBaseDict,
)
from .unions.template_response_document_form_field_base import (
    TemplateResponseDocumentFormFieldBase,
    TemplateResponseDocumentFormFieldBaseDict,
)


class TemplateResponse(SdkBaseModel):
    """Contains information about the templates you and your team have created."""

    template_id: Optional[str] = UNSET
    """The id of the Template."""

    title: Optional[str] = UNSET
    """The title of the Template. This will also be the default subject of the message sent to signers when using this
    Template to send a SignatureRequest. This can be overridden when sending the SignatureRequest."""

    message: Optional[str] = UNSET
    """The default message that will be sent to signers when using this Template to send a SignatureRequest. This can be
    overridden when sending the SignatureRequest."""

    updated_at: Optional[int] = UNSET
    """Time the template was last updated."""

    is_embedded: OptionalNullable[bool] = UNSET
    """``true`` if this template was created using an embedded flow, ``false`` if it was created on our website. Will be
    ``null`` when you are not the creator of the Template."""

    is_creator: Optional[bool] = UNSET
    """``true`` if you are the owner of this template, ``false`` if it's been shared with you by a team member."""

    can_edit: Optional[bool] = UNSET
    """Indicates whether edit rights have been granted to you by the owner (always ``true`` if that's you)."""

    is_locked: Optional[bool] = UNSET
    """Indicates whether the template is locked. If ``true``, then the template was created outside your quota and can
    only be used in ``test_mode``. If ``false``, then the template is within your quota and can be used to create
    signature requests."""

    metadata: Optional[dict[str, Any]] = UNSET
    """The metadata attached to the template."""

    signer_roles: Optional[list[TemplateResponseSignerRole]] = UNSET
    """An array of the designated signer roles that must be specified when sending a SignatureRequest using this
    Template."""

    cc_roles: Optional[list[TemplateResponseCcrole]] = UNSET
    """An array of the designated CC roles that must be specified when sending a SignatureRequest using this
    Template."""

    documents: Optional[list[TemplateResponseDocument]] = UNSET
    """An array describing each document associated with this Template. Includes form field data for each document."""

    custom_fields: OptionalNullable[list[TemplateResponseDocumentCustomFieldBase]] = UNSET
    """Deprecated. Use ``custom_fields`` inside the `documents
    <https://developers.hellosign.com/api/reference/operation/templateGet/#!c=200&path=template/documents&t=response>`__
    array instead."""

    named_form_fields: OptionalNullable[list[TemplateResponseDocumentFormFieldBase]] = UNSET
    """Deprecated. Use ``form_fields`` inside the `documents
    <https://developers.hellosign.com/api/reference/operation/templateGet/#!c=200&path=template/documents&t=response>`__
    array instead."""

    accounts: Optional[list[TemplateResponseAccount]] = UNSET
    """An array of the Accounts that can use this Template."""

    attachments: Optional[list[SignatureRequestResponseAttachment]] = UNSET
    """Signer attachments."""


class TemplateResponseDict(TypedDict):
    template_id: NotRequired[str]
    title: NotRequired[str]
    message: NotRequired[str]
    updated_at: NotRequired[int]
    is_embedded: NotRequired[bool | None]
    is_creator: NotRequired[bool]
    can_edit: NotRequired[bool]
    is_locked: NotRequired[bool]
    metadata: NotRequired[dict[str, Any]]
    signer_roles: NotRequired[list[TemplateResponseSignerRoleDict]]
    cc_roles: NotRequired[list[TemplateResponseCcroleDict]]
    documents: NotRequired[list[TemplateResponseDocumentDict]]
    custom_fields: NotRequired[list[TemplateResponseDocumentCustomFieldBaseDict] | None]
    named_form_fields: NotRequired[list[TemplateResponseDocumentFormFieldBaseDict] | None]
    accounts: NotRequired[list[TemplateResponseAccountDict]]
    attachments: NotRequired[list[SignatureRequestResponseAttachmentDict]]
