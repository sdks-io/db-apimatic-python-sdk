from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SignatureRequestResponseCustomFieldTypeEnum(str, Enum):
    TEXT = "text"
    CHECKBOX = "checkbox"

    __str__ = str.__str__


SignatureRequestResponseCustomFieldTypeEnumOrStr: TypeAlias = Annotated[
    SignatureRequestResponseCustomFieldTypeEnum | str, open_enum_validator(SignatureRequestResponseCustomFieldTypeEnum)
]
