from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .bulk_send_job_response import BulkSendJobResponse, BulkSendJobResponseDict
from .warning_response import WarningResponse, WarningResponseDict


class BulkSendJobSendResponse(SdkBaseModel):
    bulk_send_job: BulkSendJobResponse
    """Contains information about the BulkSendJob such as when it was created and how many signature requests are
    queued."""

    warnings: Optional[list[WarningResponse]] = UNSET
    """A list of warnings."""


class BulkSendJobSendResponseDict(TypedDict):
    bulk_send_job: BulkSendJobResponseDict
    warnings: NotRequired[list[WarningResponseDict]]
