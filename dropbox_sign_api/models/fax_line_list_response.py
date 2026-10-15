from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .fax_line_response_fax_line import FaxLineResponseFaxLine, FaxLineResponseFaxLineDict
from .list_info_response import ListInfoResponse, ListInfoResponseDict
from .warning_response import WarningResponse, WarningResponseDict


class FaxLineListResponse(SdkBaseModel):
    list_info: ListInfoResponse
    """Contains pagination information about the data returned."""

    fax_lines: list[FaxLineResponseFaxLine]
    warnings: Optional[WarningResponse] = UNSET
    """A list of warnings."""


class FaxLineListResponseDict(TypedDict):
    list_info: ListInfoResponseDict
    fax_lines: list[FaxLineResponseFaxLineDict]
    warnings: NotRequired[WarningResponseDict]
