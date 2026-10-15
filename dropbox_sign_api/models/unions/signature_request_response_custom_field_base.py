from __future__ import annotations

from typing import Annotated, TypeAlias

from pydantic import Tag

from ...core import WireDiscriminator
from ..signature_request_response_custom_field_checkbox import (
    SignatureRequestResponseCustomFieldCheckbox,
    SignatureRequestResponseCustomFieldCheckboxDict,
)
from ..signature_request_response_custom_field_text import (
    SignatureRequestResponseCustomFieldText,
    SignatureRequestResponseCustomFieldTextDict,
)

SignatureRequestResponseCustomFieldBase: TypeAlias = Annotated[
    (
        Annotated[SignatureRequestResponseCustomFieldCheckbox, Tag("checkbox")]
        | Annotated[SignatureRequestResponseCustomFieldText, Tag("text")]
    ),
    WireDiscriminator("type"),
]
"""An array of Custom Field objects containing the name and type of each custom field.

* Text Field uses ``SignatureRequestResponseCustomFieldText``
* Checkbox Field uses ``SignatureRequestResponseCustomFieldCheckbox``"""

SignatureRequestResponseCustomFieldBaseDict: TypeAlias = (
    SignatureRequestResponseCustomFieldCheckboxDict | SignatureRequestResponseCustomFieldTextDict
)
