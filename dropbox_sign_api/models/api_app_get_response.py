from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .api_app_response import ApiAppResponse, ApiAppResponseDict
from .warning_response import WarningResponse, WarningResponseDict


class ApiAppGetResponse(SdkBaseModel):
    api_app: ApiAppResponse
    """Contains information about an API App."""

    warnings: Optional[list[WarningResponse]] = UNSET
    """A list of warnings."""


class ApiAppGetResponseDict(TypedDict):
    api_app: ApiAppResponseDict
    warnings: NotRequired[list[WarningResponseDict]]
