from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.report_type import ReportTypeOrStr


class ReportCreateRequest(SdkBaseModel):
    end_date: str
    """The (inclusive) end date for the report data in ``MM/DD/YYYY`` format."""

    report_type: list[ReportTypeOrStr]
    """The type(s) of the report you are requesting. Allowed values are ``user_activity`` and ``document_status``. User
    activity reports contain list of all users and their activity during the specified date range. Document status
    report contain a list of signature requests created in the specified time range (and their status)."""

    start_date: str
    """The (inclusive) start date for the report data in ``MM/DD/YYYY`` format."""


class ReportCreateRequestDict(TypedDict):
    end_date: str
    report_type: list[ReportTypeOrStr]
    start_date: str
