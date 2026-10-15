from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .bulk_send_job_response import BulkSendJobResponse, BulkSendJobResponseDict
from .list_info_response import ListInfoResponse, ListInfoResponseDict
from .warning_response import WarningResponse, WarningResponseDict


class BulkSendJobListResponse(SdkBaseModel):
    bulk_send_jobs: list[BulkSendJobResponse]
    """Contains a list of BulkSendJobs that the API caller has access to."""

    list_info: ListInfoResponse
    """Contains pagination information about the data returned."""

    warnings: Optional[list[WarningResponse]] = UNSET
    """A list of warnings."""


class BulkSendJobListResponseDict(TypedDict):
    bulk_send_jobs: list[BulkSendJobResponseDict]
    list_info: ListInfoResponseDict
    warnings: NotRequired[list[WarningResponseDict]]
