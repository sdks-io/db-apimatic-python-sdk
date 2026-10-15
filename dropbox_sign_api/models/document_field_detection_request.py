from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, FileResponse, Optional, SdkBaseModel
from .unions.detection_mode import DetectionMode, DetectionModeDict


class DocumentFieldDetectionRequest(SdkBaseModel):
    file: Optional[FileResponse] = UNSET
    """The PDF file to analyze.

    This endpoint requires either ``file`` or ``file_url``, but not both."""

    file_url: Optional[str] = UNSET
    """The URL of the PDF file to analyze.

    This endpoint requires either ``file`` or ``file_url``, but not both."""

    detection_mode: DetectionMode
    """The field detection method to use. Set to ``annotations`` to detect PDF form annotations or ``text_tags`` to
    detect Dropbox Sign text tags."""

    page_range: Optional[str] = UNSET
    """The zero-based page indexes to analyze. Accepts ``all``, individual pages, inclusive ranges, or comma-separated
    combinations, such as ``0-2,5,7-9``. Defaults to ``all``."""


class DocumentFieldDetectionRequestDict(TypedDict):
    file: NotRequired[FileResponse]
    file_url: NotRequired[str]
    detection_mode: DetectionModeDict
    page_range: NotRequired[str]
