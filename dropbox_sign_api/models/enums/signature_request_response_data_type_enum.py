from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SignatureRequestResponseDataTypeEnum(str, Enum):
    TEXT = "text"
    CHECKBOX = "checkbox"
    DATE_SIGNED = "date_signed"
    DROPDOWN = "dropdown"
    INITIALS = "initials"
    RADIO = "radio"
    SIGNATURE = "signature"
    TEXT_MERGE = "text-merge"
    CHECKBOX_MERGE = "checkbox-merge"

    __str__ = str.__str__


SignatureRequestResponseDataTypeEnumOrStr: TypeAlias = Annotated[
    SignatureRequestResponseDataTypeEnum | str, open_enum_validator(SignatureRequestResponseDataTypeEnum)
]
