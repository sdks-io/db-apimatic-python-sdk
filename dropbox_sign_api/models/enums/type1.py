from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type1(str, Enum):
    CHANGE_FIELD_VISIBILITY = "change-field-visibility"
    CHANGE_GROUP_VISIBILITY = "change-group-visibility"

    __str__ = str.__str__


Type1OrStr: TypeAlias = Annotated[Type1 | str, open_enum_validator(Type1)]
