from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .fax_line_response_fax_line import FaxLineResponseFaxLine, FaxLineResponseFaxLineDict
from .warning_response import WarningResponse, WarningResponseDict


class FaxLineResponse(SdkBaseModel):
    fax_line: FaxLineResponseFaxLine
    warnings: Optional[WarningResponse] = UNSET
    """A list of warnings."""


class FaxLineResponseDict(TypedDict):
    fax_line: FaxLineResponseFaxLineDict
    warnings: NotRequired[WarningResponseDict]
