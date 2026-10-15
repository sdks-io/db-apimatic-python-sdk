from __future__ import annotations

from typing import Annotated, TypeAlias

from pydantic import Tag

from ...core import WireDiscriminator
from ..signature_request_response_data_value_checkbox import (
    SignatureRequestResponseDataValueCheckbox,
    SignatureRequestResponseDataValueCheckboxDict,
)
from ..signature_request_response_data_value_checkbox_merge import (
    SignatureRequestResponseDataValueCheckboxMerge,
    SignatureRequestResponseDataValueCheckboxMergeDict,
)
from ..signature_request_response_data_value_date_signed import (
    SignatureRequestResponseDataValueDateSigned,
    SignatureRequestResponseDataValueDateSignedDict,
)
from ..signature_request_response_data_value_dropdown import (
    SignatureRequestResponseDataValueDropdown,
    SignatureRequestResponseDataValueDropdownDict,
)
from ..signature_request_response_data_value_initials import (
    SignatureRequestResponseDataValueInitials,
    SignatureRequestResponseDataValueInitialsDict,
)
from ..signature_request_response_data_value_radio import (
    SignatureRequestResponseDataValueRadio,
    SignatureRequestResponseDataValueRadioDict,
)
from ..signature_request_response_data_value_signature import (
    SignatureRequestResponseDataValueSignature,
    SignatureRequestResponseDataValueSignatureDict,
)
from ..signature_request_response_data_value_text import (
    SignatureRequestResponseDataValueText,
    SignatureRequestResponseDataValueTextDict,
)
from ..signature_request_response_data_value_text_merge import (
    SignatureRequestResponseDataValueTextMerge,
    SignatureRequestResponseDataValueTextMergeDict,
)

SignatureRequestResponseDataBase: TypeAlias = Annotated[
    (
        Annotated[SignatureRequestResponseDataValueCheckbox, Tag("checkbox")]
        | Annotated[SignatureRequestResponseDataValueCheckboxMerge, Tag("checkbox-merge")]
        | Annotated[SignatureRequestResponseDataValueDateSigned, Tag("date_signed")]
        | Annotated[SignatureRequestResponseDataValueDropdown, Tag("dropdown")]
        | Annotated[SignatureRequestResponseDataValueInitials, Tag("initials")]
        | Annotated[SignatureRequestResponseDataValueRadio, Tag("radio")]
        | Annotated[SignatureRequestResponseDataValueSignature, Tag("signature")]
        | Annotated[SignatureRequestResponseDataValueText, Tag("text")]
        | Annotated[SignatureRequestResponseDataValueTextMerge, Tag("text-merge")]
    ),
    WireDiscriminator("type"),
]
"""An array of form field objects containing the name, value, and type of each textbox or checkmark field filled in by
the signers."""

SignatureRequestResponseDataBaseDict: TypeAlias = (
    SignatureRequestResponseDataValueCheckboxDict
    | SignatureRequestResponseDataValueCheckboxMergeDict
    | SignatureRequestResponseDataValueDateSignedDict
    | SignatureRequestResponseDataValueDropdownDict
    | SignatureRequestResponseDataValueInitialsDict
    | SignatureRequestResponseDataValueRadioDict
    | SignatureRequestResponseDataValueSignatureDict
    | SignatureRequestResponseDataValueTextDict
    | SignatureRequestResponseDataValueTextMergeDict
)
