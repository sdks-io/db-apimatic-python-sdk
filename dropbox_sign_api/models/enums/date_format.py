from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DateFormat(str, Enum):
    """Allows requester to specify the date format (see list of allowed `formats
    </api/reference/constants/#date-formats>`__)

    **NOTE:** Only available for Premium and higher."""

    MM_DD_YYYY = "MM / DD / YYYY"
    MM_DD_YYYY2 = "MM - DD - YYYY"
    DD_MM_YYYY = "DD / MM / YYYY"
    DD_MM_YYYY2 = "DD - MM - YYYY"
    YYYY_MM_DD = "YYYY / MM / DD"
    YYYY_MM_DD2 = "YYYY - MM - DD"

    __str__ = str.__str__


DateFormatOrStr: TypeAlias = Annotated[DateFormat | str, open_enum_validator(DateFormat)]
