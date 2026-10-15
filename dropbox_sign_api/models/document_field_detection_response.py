from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .document_field_detection_response_detection_result import (
    DocumentFieldDetectionResponseDetectionResult,
    DocumentFieldDetectionResponseDetectionResultDict,
)
from .warning_response import WarningResponse, WarningResponseDict


class DocumentFieldDetectionResponse(SdkBaseModel):
    detection_result: DocumentFieldDetectionResponseDetectionResult
    warnings: Optional[list[WarningResponse]] = UNSET
    """A list of warnings."""


class DocumentFieldDetectionResponseDict(TypedDict):
    detection_result: DocumentFieldDetectionResponseDetectionResultDict
    warnings: NotRequired[list[WarningResponseDict]]
