from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type3(str, Enum):
    """The type of the draft. By default this is ``request_signature``, but you can set it to ``send_document`` if you
    want to self sign a document and download it."""

    SEND_DOCUMENT = "send_document"
    REQUEST_SIGNATURE = "request_signature"

    __str__ = str.__str__


Type3OrStr: TypeAlias = Annotated[Type3 | str, open_enum_validator(Type3)]
