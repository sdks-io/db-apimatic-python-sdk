from __future__ import annotations

from typing import Annotated, TypeAlias

from pydantic import Tag

from ...core import WireDiscriminator
from ..sub_form_fields_per_document_checkbox import (
    SubFormFieldsPerDocumentCheckbox,
    SubFormFieldsPerDocumentCheckboxDict,
)
from ..sub_form_fields_per_document_checkbox_merge import (
    SubFormFieldsPerDocumentCheckboxMerge,
    SubFormFieldsPerDocumentCheckboxMergeDict,
)
from ..sub_form_fields_per_document_date_signed import (
    SubFormFieldsPerDocumentDateSigned,
    SubFormFieldsPerDocumentDateSignedDict,
)
from ..sub_form_fields_per_document_dropdown import (
    SubFormFieldsPerDocumentDropdown,
    SubFormFieldsPerDocumentDropdownDict,
)
from ..sub_form_fields_per_document_hyperlink import (
    SubFormFieldsPerDocumentHyperlink,
    SubFormFieldsPerDocumentHyperlinkDict,
)
from ..sub_form_fields_per_document_initials import (
    SubFormFieldsPerDocumentInitials,
    SubFormFieldsPerDocumentInitialsDict,
)
from ..sub_form_fields_per_document_radio import SubFormFieldsPerDocumentRadio, SubFormFieldsPerDocumentRadioDict
from ..sub_form_fields_per_document_signature import (
    SubFormFieldsPerDocumentSignature,
    SubFormFieldsPerDocumentSignatureDict,
)
from ..sub_form_fields_per_document_text import SubFormFieldsPerDocumentText, SubFormFieldsPerDocumentTextDict
from ..sub_form_fields_per_document_text_merge import (
    SubFormFieldsPerDocumentTextMerge,
    SubFormFieldsPerDocumentTextMergeDict,
)

SubFormFieldsPerDocumentBase: TypeAlias = Annotated[
    (
        Annotated[SubFormFieldsPerDocumentCheckbox, Tag("checkbox")]
        | Annotated[SubFormFieldsPerDocumentCheckboxMerge, Tag("checkbox-merge")]
        | Annotated[SubFormFieldsPerDocumentDateSigned, Tag("date_signed")]
        | Annotated[SubFormFieldsPerDocumentDropdown, Tag("dropdown")]
        | Annotated[SubFormFieldsPerDocumentHyperlink, Tag("hyperlink")]
        | Annotated[SubFormFieldsPerDocumentInitials, Tag("initials")]
        | Annotated[SubFormFieldsPerDocumentRadio, Tag("radio")]
        | Annotated[SubFormFieldsPerDocumentSignature, Tag("signature")]
        | Annotated[SubFormFieldsPerDocumentText, Tag("text")]
        | Annotated[SubFormFieldsPerDocumentTextMerge, Tag("text-merge")]
    ),
    WireDiscriminator("type"),
]
"""The fields that should appear on the document, expressed as an array of objects. (For more details you can read about
it here: `Using Form Fields per Document </docs/openapi/form-fields-per-document>`__.)

**NOTE:** Fields like **text**, **dropdown**, **checkbox**, **radio**, and **hyperlink** have additional required and
optional parameters. Check out the list of `additional parameters
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

SubFormFieldsPerDocumentBaseDict: TypeAlias = (
    SubFormFieldsPerDocumentCheckboxDict
    | SubFormFieldsPerDocumentCheckboxMergeDict
    | SubFormFieldsPerDocumentDateSignedDict
    | SubFormFieldsPerDocumentDropdownDict
    | SubFormFieldsPerDocumentHyperlinkDict
    | SubFormFieldsPerDocumentInitialsDict
    | SubFormFieldsPerDocumentRadioDict
    | SubFormFieldsPerDocumentSignatureDict
    | SubFormFieldsPerDocumentTextDict
    | SubFormFieldsPerDocumentTextMergeDict
)
