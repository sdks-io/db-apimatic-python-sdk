from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .list_info_response import ListInfoResponse, ListInfoResponseDict
from .template_response import TemplateResponse, TemplateResponseDict
from .warning_response import WarningResponse, WarningResponseDict


class TemplateListResponse(SdkBaseModel):
    templates: list[TemplateResponse]
    """List of templates that the API caller has access to."""

    list_info: ListInfoResponse
    """Contains pagination information about the data returned."""

    warnings: Optional[list[WarningResponse]] = UNSET
    """A list of warnings."""


class TemplateListResponseDict(TypedDict):
    templates: list[TemplateResponseDict]
    list_info: ListInfoResponseDict
    warnings: NotRequired[list[WarningResponseDict]]
