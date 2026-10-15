from __future__ import annotations

from pydantic import EmailStr
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.sms_phone_number_type import SmsPhoneNumberTypeOrStr


class SubSignatureRequestSigner(SdkBaseModel):
    name: str
    """The name of the signer."""

    email_address: EmailStr
    """The email address of the signer."""

    order: OptionalNullable[int] = UNSET
    """The order the signer is required to sign in."""

    pin: Optional[str] = UNSET
    """The 4- to 12-character access code that will secure this signer's signature page."""

    sms_phone_number: Optional[str] = UNSET
    """An E.164 formatted phone number.

    By using the feature, you agree you are responsible for obtaining a signer's consent to receive text messages from
    Dropbox Sign related to this signature request and confirm you have obtained such consent from all signers prior to
    enabling SMS delivery for this signature request. `Learn more
    <https://faq.hellosign.com/hc/en-us/articles/15815316468877-Dropbox-Sign-SMS-tools-add-on>`__.

    **NOTE:** Not available in test mode and requires a Standard plan or higher."""

    sms_phone_number_type: Optional[SmsPhoneNumberTypeOrStr] = UNSET
    """Specifies the feature used with the ``sms_phone_number``. Default ``authentication``.

    If ``authentication``, signer is sent a verification code via SMS that is required to access the document.

    If ``delivery``, a link to complete the signature request is delivered via SMS (_and_ email)."""


class SubSignatureRequestSignerDict(TypedDict):
    name: str
    email_address: EmailStr
    order: NotRequired[int | None]
    pin: NotRequired[str]
    sms_phone_number: NotRequired[str]
    sms_phone_number_type: NotRequired[SmsPhoneNumberTypeOrStr]
