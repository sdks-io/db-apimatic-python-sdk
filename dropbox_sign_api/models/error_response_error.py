from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ErrorResponseError(SdkBaseModel):
    """Contains information about an error that occurred."""

    error_msg: str
    """Message describing an error."""

    error_path: Optional[str] = UNSET
    """Path at which an error occurred."""

    error_name: str
    """Name of the error. See the ``x-error-codes`` catalog in openapi file for a complete list of possible error codes
    with detailed information including HTTP status codes, causes, remediation steps, and retry guidance."""


class ErrorResponseErrorDict(TypedDict):
    error_msg: str
    error_path: NotRequired[str]
    error_name: str
