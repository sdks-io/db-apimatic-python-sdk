from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .report_response import ReportResponse, ReportResponseDict
from .warning_response import WarningResponse, WarningResponseDict


class ReportCreateResponse(SdkBaseModel):
    report: ReportResponse
    """Contains information about the report request."""

    warnings: Optional[list[WarningResponse]] = UNSET
    """A list of warnings."""


class ReportCreateResponseDict(TypedDict):
    report: ReportResponseDict
    warnings: NotRequired[list[WarningResponseDict]]
