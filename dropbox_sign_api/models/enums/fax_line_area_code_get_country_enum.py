from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FaxLineAreaCodeGetCountryEnum(str, Enum):
    CA = "CA"
    US = "US"
    UK = "UK"

    __str__ = str.__str__


FaxLineAreaCodeGetCountryEnumOrStr: TypeAlias = Annotated[
    FaxLineAreaCodeGetCountryEnum | str, open_enum_validator(FaxLineAreaCodeGetCountryEnum)
]
