from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SubFormFieldsPerDocumentTypeEnum(str, Enum):
    CHECKBOX = "checkbox"
    CHECKBOX_MERGE = "checkbox-merge"
    DATE_SIGNED = "date_signed"
    DROPDOWN = "dropdown"
    HYPERLINK = "hyperlink"
    INITIALS = "initials"
    SIGNATURE = "signature"
    RADIO = "radio"
    TEXT = "text"
    TEXT_MERGE = "text-merge"

    __str__ = str.__str__


SubFormFieldsPerDocumentTypeEnumOrStr: TypeAlias = Annotated[
    SubFormFieldsPerDocumentTypeEnum | str, open_enum_validator(SubFormFieldsPerDocumentTypeEnum)
]
