from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class WarningResponse(SdkBaseModel):
    """A list of warnings."""

    warning_msg: str
    """Warning message"""

    warning_name: str
    """Warning name"""


class WarningResponseDict(TypedDict):
    warning_msg: str
    warning_name: str
