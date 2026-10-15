from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ReportType(str, Enum):
    USER_ACTIVITY = "user_activity"
    DOCUMENT_STATUS = "document_status"
    SMS_ACTIVITY = "sms_activity"
    FAX_USAGE = "fax_usage"

    __str__ = str.__str__


ReportTypeOrStr: TypeAlias = Annotated[ReportType | str, open_enum_validator(ReportType)]
