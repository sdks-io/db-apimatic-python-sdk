from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Scope(str, Enum):
    REQUEST_SIGNATURE = "request_signature"
    BASIC_ACCOUNT_INFO = "basic_account_info"
    ACCOUNT_ACCESS = "account_access"
    SIGNATURE_REQUEST_ACCESS = "signature_request_access"
    TEMPLATE_ACCESS = "template_access"
    TEAM_ACCESS = "team_access"
    API_APP_ACCESS = "api_app_access"

    __str__ = str.__str__


ScopeOrStr: TypeAlias = Annotated[Scope | str, open_enum_validator(Scope)]
