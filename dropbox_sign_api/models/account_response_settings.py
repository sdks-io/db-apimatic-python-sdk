from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AccountResponseSettings(SdkBaseModel):
    """Subset of configured settings"""

    signer_access_codes: Optional[bool] = UNSET
    """Returns ``true`` if _Custom access codes_ is enabled in Admin Console. `Read more
    <https://developers.hellosign.com/docs/sms-tools/walkthrough>`__."""

    sms_delivery: Optional[bool] = UNSET
    """Returns ``true`` if _Text message_ is enabled in Admin Console. `Read more
    <https://developers.hellosign.com/docs/sms-tools/walkthrough>`__."""

    sms_authentication: Optional[bool] = UNSET
    """Returns ``true`` if _Signer authentication_ is enabled in Admin Console. `Read more
    <https://developers.hellosign.com/docs/sms-tools/walkthrough>`__."""


class AccountResponseSettingsDict(TypedDict):
    signer_access_codes: NotRequired[bool]
    sms_delivery: NotRequired[bool]
    sms_authentication: NotRequired[bool]
