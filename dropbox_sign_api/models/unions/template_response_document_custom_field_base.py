from __future__ import annotations

from typing import Annotated, TypeAlias

from pydantic import Tag

from ...core import WireDiscriminator
from ..template_response_document_custom_field_checkbox import (
    TemplateResponseDocumentCustomFieldCheckbox,
    TemplateResponseDocumentCustomFieldCheckboxDict,
)
from ..template_response_document_custom_field_text import (
    TemplateResponseDocumentCustomFieldText,
    TemplateResponseDocumentCustomFieldTextDict,
)

TemplateResponseDocumentCustomFieldBase: TypeAlias = Annotated[
    (
        Annotated[TemplateResponseDocumentCustomFieldCheckbox, Tag("checkbox")]
        | Annotated[TemplateResponseDocumentCustomFieldText, Tag("text")]
    ),
    WireDiscriminator("type"),
]
"""An array of Form Field objects containing the name and type of each named field."""

TemplateResponseDocumentCustomFieldBaseDict: TypeAlias = (
    TemplateResponseDocumentCustomFieldCheckboxDict | TemplateResponseDocumentCustomFieldTextDict
)
