from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .bulk_send_job_get_response_signature_requests import (
    BulkSendJobGetResponseSignatureRequests,
    BulkSendJobGetResponseSignatureRequestsDict,
)
from .bulk_send_job_response import BulkSendJobResponse, BulkSendJobResponseDict
from .list_info_response import ListInfoResponse, ListInfoResponseDict
from .warning_response import WarningResponse, WarningResponseDict


class BulkSendJobGetResponse(SdkBaseModel):
    bulk_send_job: BulkSendJobResponse
    """Contains information about the BulkSendJob such as when it was created and how many signature requests are
    queued."""

    list_info: ListInfoResponse
    """Contains pagination information about the data returned."""

    signature_requests: list[BulkSendJobGetResponseSignatureRequests]
    """Contains information about the Signature Requests sent in bulk."""

    warnings: Optional[list[WarningResponse]] = UNSET
    """A list of warnings."""


class BulkSendJobGetResponseDict(TypedDict):
    bulk_send_job: BulkSendJobResponseDict
    list_info: ListInfoResponseDict
    signature_requests: list[BulkSendJobGetResponseSignatureRequestsDict]
    warnings: NotRequired[list[WarningResponseDict]]
