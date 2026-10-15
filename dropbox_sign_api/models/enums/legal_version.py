from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class LegalVersion(str, Enum):
    TERMS1 = "terms1"
    TERMS2 = "terms2"

    __str__ = str.__str__


LegalVersionOrStr: TypeAlias = Annotated[LegalVersion | str, open_enum_validator(LegalVersion)]
