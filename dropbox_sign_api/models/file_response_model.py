from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class FileResponseModel(SdkBaseModel):
    file_url: str
    """URL to the file."""

    expires_at: int
    """When the link expires."""


class FileResponseModelDict(TypedDict):
    file_url: str
    expires_at: int
