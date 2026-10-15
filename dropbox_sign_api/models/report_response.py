from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.report_type import ReportTypeOrStr


class ReportResponse(SdkBaseModel):
    """Contains information about the report request."""

    success: Optional[str] = UNSET
    """A message indicating the requested operation's success"""

    start_date: Optional[str] = UNSET
    """The (inclusive) start date for the report data in MM/DD/YYYY format."""

    end_date: Optional[str] = UNSET
    """The (inclusive) end date for the report data in MM/DD/YYYY format."""

    report_type: Optional[list[ReportTypeOrStr]] = UNSET
    """The type(s) of the report you are requesting. Allowed values are "user_activity" and "document_status". User
    activity reports contain list of all users and their activity during the specified date range. Document status
    report contain a list of signature requests created in the specified time range (and their status)."""


class ReportResponseDict(TypedDict):
    success: NotRequired[str]
    start_date: NotRequired[str]
    end_date: NotRequired[str]
    report_type: NotRequired[list[ReportTypeOrStr]]
