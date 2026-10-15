from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .fax_response import FaxResponse, FaxResponseDict
from .warning_response import WarningResponse, WarningResponseDict


class FaxGetResponse(SdkBaseModel):
    fax: FaxResponse
    warnings: Optional[list[WarningResponse]] = UNSET
    """A list of warnings."""


class FaxGetResponseDict(TypedDict):
    fax: FaxResponseDict
    warnings: NotRequired[list[WarningResponseDict]]
