from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class FileResponseDataUri(SdkBaseModel):
    data_uri: str
    """File as base64 encoded string."""


class FileResponseDataUriDict(TypedDict):
    data_uri: str
