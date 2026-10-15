from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.country import CountryOrStr


class FaxLineCreateRequest(SdkBaseModel):
    area_code: int
    """Area code of the new Fax Line"""

    country: CountryOrStr
    """Country of the area code"""

    city: Optional[str] = UNSET
    """City of the area code"""

    account_id: Optional[str] = UNSET
    """Account ID of the account that will be assigned this new Fax Line"""


class FaxLineCreateRequestDict(TypedDict):
    area_code: int
    country: CountryOrStr
    city: NotRequired[str]
    account_id: NotRequired[str]
