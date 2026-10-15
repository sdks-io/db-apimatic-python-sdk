from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class StatusCode(str, Enum):
    """Fax Transmission Status Code"""

    SUCCESS = "success"
    TRANSMITTING = "transmitting"
    ERROR_COULD_NOT_FAX = "error_could_not_fax"
    ERROR_UNKNOWN = "error_unknown"
    ERROR_BUSY = "error_busy"
    ERROR_NO_ANSWER = "error_no_answer"
    ERROR_DISCONNECTED = "error_disconnected"
    ERROR_BAD_DESTINATION = "error_bad_destination"

    __str__ = str.__str__


StatusCodeOrStr: TypeAlias = Annotated[StatusCode | str, open_enum_validator(StatusCode)]
