from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DefaultType(str, Enum):
    """The default type shown (limited to the listed types)"""

    DRAW = "draw"
    PHONE = "phone"
    TYPE = "type"
    UPLOAD = "upload"

    __str__ = str.__str__


DefaultTypeOrStr: TypeAlias = Annotated[DefaultType | str, open_enum_validator(DefaultType)]
