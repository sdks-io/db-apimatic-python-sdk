from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SmsPhoneNumberType(str, Enum):
    """Specifies the feature used with the ``sms_phone_number``. Default ``authentication``.

    If ``authentication``, signer is sent a verification code via SMS that is required to access the document.

    If ``delivery``, a link to complete the signature request is delivered via SMS (_and_ email)."""

    AUTHENTICATION = "authentication"
    DELIVERY = "delivery"

    __str__ = str.__str__


SmsPhoneNumberTypeOrStr: TypeAlias = Annotated[SmsPhoneNumberType | str, open_enum_validator(SmsPhoneNumberType)]
