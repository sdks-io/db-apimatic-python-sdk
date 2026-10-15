from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .signature_request_response import SignatureRequestResponse, SignatureRequestResponseDict
from .warning_response import WarningResponse, WarningResponseDict


class SignatureRequestGetResponse(SdkBaseModel):
    signature_request: SignatureRequestResponse
    """Contains information about a signature request."""

    warnings: Optional[list[WarningResponse]] = UNSET
    """A list of warnings."""


class SignatureRequestGetResponseDict(TypedDict):
    signature_request: SignatureRequestResponseDict
    warnings: NotRequired[list[WarningResponseDict]]
