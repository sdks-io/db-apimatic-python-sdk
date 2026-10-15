from __future__ import annotations

from typing import Annotated, TypeAlias

from pydantic import Tag

from ...core import WireDiscriminator
from ..template_response_document_static_field_checkbox import (
    TemplateResponseDocumentStaticFieldCheckbox,
    TemplateResponseDocumentStaticFieldCheckboxDict,
)
from ..template_response_document_static_field_date_signed import (
    TemplateResponseDocumentStaticFieldDateSigned,
    TemplateResponseDocumentStaticFieldDateSignedDict,
)
from ..template_response_document_static_field_dropdown import (
    TemplateResponseDocumentStaticFieldDropdown,
    TemplateResponseDocumentStaticFieldDropdownDict,
)
from ..template_response_document_static_field_hyperlink import (
    TemplateResponseDocumentStaticFieldHyperlink,
    TemplateResponseDocumentStaticFieldHyperlinkDict,
)
from ..template_response_document_static_field_initials import (
    TemplateResponseDocumentStaticFieldInitials,
    TemplateResponseDocumentStaticFieldInitialsDict,
)
from ..template_response_document_static_field_radio import (
    TemplateResponseDocumentStaticFieldRadio,
    TemplateResponseDocumentStaticFieldRadioDict,
)
from ..template_response_document_static_field_signature import (
    TemplateResponseDocumentStaticFieldSignature,
    TemplateResponseDocumentStaticFieldSignatureDict,
)
from ..template_response_document_static_field_text import (
    TemplateResponseDocumentStaticFieldText,
    TemplateResponseDocumentStaticFieldTextDict,
)

TemplateResponseDocumentStaticFieldBase: TypeAlias = Annotated[
    (
        Annotated[TemplateResponseDocumentStaticFieldCheckbox, Tag("checkbox")]
        | Annotated[TemplateResponseDocumentStaticFieldDateSigned, Tag("date_signed")]
        | Annotated[TemplateResponseDocumentStaticFieldDropdown, Tag("dropdown")]
        | Annotated[TemplateResponseDocumentStaticFieldHyperlink, Tag("hyperlink")]
        | Annotated[TemplateResponseDocumentStaticFieldInitials, Tag("initials")]
        | Annotated[TemplateResponseDocumentStaticFieldRadio, Tag("radio")]
        | Annotated[TemplateResponseDocumentStaticFieldSignature, Tag("signature")]
        | Annotated[TemplateResponseDocumentStaticFieldText, Tag("text")]
    ),
    WireDiscriminator("type"),
]
"""An array describing static overlay fields. **NOTE:** Only available for certain subscriptions."""

TemplateResponseDocumentStaticFieldBaseDict: TypeAlias = (
    TemplateResponseDocumentStaticFieldCheckboxDict
    | TemplateResponseDocumentStaticFieldDateSignedDict
    | TemplateResponseDocumentStaticFieldDropdownDict
    | TemplateResponseDocumentStaticFieldHyperlinkDict
    | TemplateResponseDocumentStaticFieldInitialsDict
    | TemplateResponseDocumentStaticFieldRadioDict
    | TemplateResponseDocumentStaticFieldSignatureDict
    | TemplateResponseDocumentStaticFieldTextDict
)
