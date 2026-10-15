from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .fax_response import FaxResponse, FaxResponseDict
from .list_info_response import ListInfoResponse, ListInfoResponseDict


class FaxListResponse(SdkBaseModel):
    faxes: list[FaxResponse]
    list_info: ListInfoResponse
    """Contains pagination information about the data returned."""


class FaxListResponseDict(TypedDict):
    faxes: list[FaxResponseDict]
    list_info: ListInfoResponseDict
