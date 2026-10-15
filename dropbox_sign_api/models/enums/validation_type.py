from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ValidationType(str, Enum):
    """Each text field may contain a ``validation_type`` parameter. Check out the list of `validation types
    <https://faq.hellosign.com/hc/en-us/articles/217115577>`__ to learn more about the possible values.

    **NOTE:** When using ``custom_regex`` you are required to pass a second parameter ``validation_custom_regex`` and
    you can optionally provide ``validation_custom_regex_format_label`` for the error message the user will see in case
    of an invalid value."""

    NUMBERS_ONLY = "numbers_only"
    LETTERS_ONLY = "letters_only"
    PHONE_NUMBER = "phone_number"
    BANK_ROUTING_NUMBER = "bank_routing_number"
    BANK_ACCOUNT_NUMBER = "bank_account_number"
    EMAIL_ADDRESS = "email_address"
    ZIP_CODE = "zip_code"
    SOCIAL_SECURITY_NUMBER = "social_security_number"
    EMPLOYER_IDENTIFICATION_NUMBER = "employer_identification_number"
    CUSTOM_REGEX = "custom_regex"

    __str__ = str.__str__


ValidationTypeOrStr: TypeAlias = Annotated[ValidationType | str, open_enum_validator(ValidationType)]
