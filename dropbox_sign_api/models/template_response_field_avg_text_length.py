from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TemplateResponseFieldAvgTextLength(SdkBaseModel):
    """Average text length in this field."""

    num_lines: Optional[int] = UNSET
    """Number of lines."""

    num_chars_per_line: Optional[int] = UNSET
    """Number of characters per line."""


class TemplateResponseFieldAvgTextLengthDict(TypedDict):
    num_lines: NotRequired[int]
    num_chars_per_line: NotRequired[int]
