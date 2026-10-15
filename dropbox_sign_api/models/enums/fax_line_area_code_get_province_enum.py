from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FaxLineAreaCodeGetProvinceEnum(str, Enum):
    AB = "AB"
    BC = "BC"
    MB = "MB"
    NB = "NB"
    NL = "NL"
    NT = "NT"
    NS = "NS"
    NU = "NU"
    ON = "ON"
    PE = "PE"
    QC = "QC"
    SK = "SK"
    YT = "YT"

    __str__ = str.__str__


FaxLineAreaCodeGetProvinceEnumOrStr: TypeAlias = Annotated[
    FaxLineAreaCodeGetProvinceEnum | str, open_enum_validator(FaxLineAreaCodeGetProvinceEnum)
]
