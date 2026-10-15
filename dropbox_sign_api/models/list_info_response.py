from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class ListInfoResponse(SdkBaseModel):
    """Contains pagination information about the data returned."""

    num_pages: Optional[int] = UNSET
    """Total number of pages available."""

    num_results: OptionalNullable[int] = UNSET
    """Total number of objects available."""

    page: Optional[int] = UNSET
    """Number of the page being returned."""

    page_size: Optional[int] = UNSET
    """Objects returned per page."""


class ListInfoResponseDict(TypedDict):
    num_pages: NotRequired[int]
    num_results: NotRequired[int | None]
    page: NotRequired[int]
    page_size: NotRequired[int]
