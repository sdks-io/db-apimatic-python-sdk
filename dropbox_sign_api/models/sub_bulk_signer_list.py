from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .sub_bulk_signer_list_custom_field import SubBulkSignerListCustomField, SubBulkSignerListCustomFieldDict
from .sub_signature_request_template_signer import (
    SubSignatureRequestTemplateSigner,
    SubSignatureRequestTemplateSignerDict,
)


class SubBulkSignerList(SdkBaseModel):
    custom_fields: Optional[list[SubBulkSignerListCustomField]] = UNSET
    """An array of custom field values."""

    signers: Optional[list[SubSignatureRequestTemplateSigner]] = UNSET
    """Add Signers to your Templated-based Signature Request. Allows the requester to specify editor options when a
    preparing a document.

    Currently only templates with a single role are supported. All signers must have the same ``role`` value."""


class SubBulkSignerListDict(TypedDict):
    custom_fields: NotRequired[list[SubBulkSignerListCustomFieldDict]]
    signers: NotRequired[list[SubSignatureRequestTemplateSignerDict]]
