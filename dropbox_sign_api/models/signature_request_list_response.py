from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .list_info_response import ListInfoResponse, ListInfoResponseDict
from .signature_request_response import SignatureRequestResponse, SignatureRequestResponseDict
from .warning_response import WarningResponse, WarningResponseDict


class SignatureRequestListResponse(SdkBaseModel):
    signature_requests: list[SignatureRequestResponse]
    """Contains information about signature requests."""

    list_info: ListInfoResponse
    """Contains pagination information about the data returned."""

    warnings: Optional[list[WarningResponse]] = UNSET
    """A list of warnings."""


class SignatureRequestListResponseDict(TypedDict):
    signature_requests: list[SignatureRequestResponseDict]
    list_info: ListInfoResponseDict
    warnings: NotRequired[list[WarningResponseDict]]
