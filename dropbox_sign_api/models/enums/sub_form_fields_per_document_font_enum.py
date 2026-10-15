from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SubFormFieldsPerDocumentFontEnum(str, Enum):
    HELVETICA = "helvetica"
    ARIAL = "arial"
    COURIER = "courier"
    CALIBRI = "calibri"
    CAMBRIA = "cambria"
    GEORGIA = "georgia"
    TIMES = "times"
    TREBUCHET = "trebuchet"
    VERDANA = "verdana"
    ROBOTO = "roboto"
    ROBOTO_MONO = "robotoMono"
    NOTO_SANS = "notoSans"
    NOTO_SERIF = "notoSerif"
    NOTO_CJK_JP_REGULAR = "notoCJK-JP-Regular"
    NOTO_HEBREW_REGULAR = "notoHebrew-Regular"
    NOTO_SAN_THAI_MERGED = "notoSanThaiMerged"

    __str__ = str.__str__


SubFormFieldsPerDocumentFontEnumOrStr: TypeAlias = Annotated[
    SubFormFieldsPerDocumentFontEnum | str, open_enum_validator(SubFormFieldsPerDocumentFontEnum)
]
