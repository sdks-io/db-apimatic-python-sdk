from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .template_response_document_field_group import (
    TemplateResponseDocumentFieldGroup,
    TemplateResponseDocumentFieldGroupDict,
)
from .unions.template_response_document_custom_field_base import (
    TemplateResponseDocumentCustomFieldBase,
    TemplateResponseDocumentCustomFieldBaseDict,
)
from .unions.template_response_document_form_field_base import (
    TemplateResponseDocumentFormFieldBase,
    TemplateResponseDocumentFormFieldBaseDict,
)
from .unions.template_response_document_static_field_base import (
    TemplateResponseDocumentStaticFieldBase,
    TemplateResponseDocumentStaticFieldBaseDict,
)


class TemplateResponseDocument(SdkBaseModel):
    name: Optional[str] = UNSET
    """Name of the associated file."""

    index: Optional[int] = UNSET
    """Document ordering, the lowest index is displayed first and the highest last (0-based indexing)."""

    field_groups: Optional[list[TemplateResponseDocumentFieldGroup]] = UNSET
    """An array of Form Field Group objects."""

    form_fields: Optional[list[TemplateResponseDocumentFormFieldBase]] = UNSET
    """An array of Form Field objects containing the name and type of each named field."""

    custom_fields: Optional[list[TemplateResponseDocumentCustomFieldBase]] = UNSET
    """An array of Form Field objects containing the name and type of each named field."""

    static_fields: Optional[list[TemplateResponseDocumentStaticFieldBase]] = UNSET
    """An array describing static overlay fields. **NOTE:** Only available for certain subscriptions."""


class TemplateResponseDocumentDict(TypedDict):
    name: NotRequired[str]
    index: NotRequired[int]
    field_groups: NotRequired[list[TemplateResponseDocumentFieldGroupDict]]
    form_fields: NotRequired[list[TemplateResponseDocumentFormFieldBaseDict]]
    custom_fields: NotRequired[list[TemplateResponseDocumentCustomFieldBaseDict]]
    static_fields: NotRequired[list[TemplateResponseDocumentStaticFieldBaseDict]]
