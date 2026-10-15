from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.date_format import DateFormatOrStr


class SubFieldOptions(SdkBaseModel):
    """This allows the requester to specify field options for a signature request."""

    date_format: DateFormatOrStr
    """Allows requester to specify the date format (see list of allowed `formats
    </api/reference/constants/#date-formats>`__)

    **NOTE:** Only available for Premium and higher."""


class SubFieldOptionsDict(TypedDict):
    date_format: DateFormatOrStr
