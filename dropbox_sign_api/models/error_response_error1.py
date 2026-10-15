from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .error_response_error import ErrorResponseError, ErrorResponseErrorDict


class ErrorResponseError1(SdkBaseModel):
    error: ErrorResponseError
    """Contains information about an error that occurred."""


class ErrorResponseError1Dict(TypedDict):
    error: ErrorResponseErrorDict
