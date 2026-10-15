from __future__ import annotations

from typing import Annotated, TypeAlias

from pydantic import Tag

from ...core import WireDiscriminator
from ..template_response_document_form_field_checkbox import (
    TemplateResponseDocumentFormFieldCheckbox,
    TemplateResponseDocumentFormFieldCheckboxDict,
)
from ..template_response_document_form_field_date_signed import (
    TemplateResponseDocumentFormFieldDateSigned,
    TemplateResponseDocumentFormFieldDateSignedDict,
)
from ..template_response_document_form_field_dropdown import (
    TemplateResponseDocumentFormFieldDropdown,
    TemplateResponseDocumentFormFieldDropdownDict,
)
from ..template_response_document_form_field_hyperlink import (
    TemplateResponseDocumentFormFieldHyperlink,
    TemplateResponseDocumentFormFieldHyperlinkDict,
)
from ..template_response_document_form_field_initials import (
    TemplateResponseDocumentFormFieldInitials,
    TemplateResponseDocumentFormFieldInitialsDict,
)
from ..template_response_document_form_field_radio import (
    TemplateResponseDocumentFormFieldRadio,
    TemplateResponseDocumentFormFieldRadioDict,
)
from ..template_response_document_form_field_signature import (
    TemplateResponseDocumentFormFieldSignature,
    TemplateResponseDocumentFormFieldSignatureDict,
)
from ..template_response_document_form_field_text import (
    TemplateResponseDocumentFormFieldText,
    TemplateResponseDocumentFormFieldTextDict,
)

TemplateResponseDocumentFormFieldBase: TypeAlias = Annotated[
    (
        Annotated[TemplateResponseDocumentFormFieldCheckbox, Tag("checkbox")]
        | Annotated[TemplateResponseDocumentFormFieldDateSigned, Tag("date_signed")]
        | Annotated[TemplateResponseDocumentFormFieldDropdown, Tag("dropdown")]
        | Annotated[TemplateResponseDocumentFormFieldHyperlink, Tag("hyperlink")]
        | Annotated[TemplateResponseDocumentFormFieldInitials, Tag("initials")]
        | Annotated[TemplateResponseDocumentFormFieldRadio, Tag("radio")]
        | Annotated[TemplateResponseDocumentFormFieldSignature, Tag("signature")]
        | Annotated[TemplateResponseDocumentFormFieldText, Tag("text")]
    ),
    WireDiscriminator("type"),
]
"""An array of Form Field objects containing the name and type of each named field."""

TemplateResponseDocumentFormFieldBaseDict: TypeAlias = (
    TemplateResponseDocumentFormFieldCheckboxDict
    | TemplateResponseDocumentFormFieldDateSignedDict
    | TemplateResponseDocumentFormFieldDropdownDict
    | TemplateResponseDocumentFormFieldHyperlinkDict
    | TemplateResponseDocumentFormFieldInitialsDict
    | TemplateResponseDocumentFormFieldRadioDict
    | TemplateResponseDocumentFormFieldSignatureDict
    | TemplateResponseDocumentFormFieldTextDict
)
