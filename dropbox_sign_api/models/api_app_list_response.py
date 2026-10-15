from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .api_app_response import ApiAppResponse, ApiAppResponseDict
from .list_info_response import ListInfoResponse, ListInfoResponseDict
from .warning_response import WarningResponse, WarningResponseDict


class ApiAppListResponse(SdkBaseModel):
    api_apps: list[ApiAppResponse]
    """Contains information about API Apps."""

    list_info: ListInfoResponse
    """Contains pagination information about the data returned."""

    warnings: Optional[list[WarningResponse]] = UNSET
    """A list of warnings."""


class ApiAppListResponseDict(TypedDict):
    api_apps: list[ApiAppResponseDict]
    list_info: ListInfoResponseDict
    warnings: NotRequired[list[WarningResponseDict]]
