from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class EventType(str, Enum):
    """Type of callback event that was triggered."""

    ACCOUNT_CONFIRMED = "account_confirmed"
    UNKNOWN_ERROR = "unknown_error"
    FILE_ERROR = "file_error"
    SIGN_URL_INVALID = "sign_url_invalid"
    SIGNATURE_REQUEST_VIEWED = "signature_request_viewed"
    SIGNATURE_REQUEST_SIGNED = "signature_request_signed"
    SIGNATURE_REQUEST_SENT = "signature_request_sent"
    SIGNATURE_REQUEST_ALL_SIGNED = "signature_request_all_signed"
    SIGNATURE_REQUEST_EMAIL_BOUNCE = "signature_request_email_bounce"
    SIGNATURE_REQUEST_REMIND = "signature_request_remind"
    SIGNATURE_REQUEST_INCOMPLETE_QES = "signature_request_incomplete_qes"
    SIGNATURE_REQUEST_DESTROYED = "signature_request_destroyed"
    SIGNATURE_REQUEST_CANCELED = "signature_request_canceled"
    SIGNATURE_REQUEST_DOWNLOADABLE = "signature_request_downloadable"
    SIGNATURE_REQUEST_DECLINED = "signature_request_declined"
    SIGNATURE_REQUEST_REASSIGNED = "signature_request_reassigned"
    SIGNATURE_REQUEST_INVALID = "signature_request_invalid"
    SIGNATURE_REQUEST_PREPARED = "signature_request_prepared"
    SIGNATURE_REQUEST_EXPIRED = "signature_request_expired"
    TEMPLATE_CREATED = "template_created"
    TEMPLATE_ERROR = "template_error"
    CALLBACK_TEST = "callback_test"
    SIGNATURE_REQUEST_SIGNER_REMOVED = "signature_request_signer_removed"
    FAX_RECEIVED = "fax_received"
    FAX_SENT = "fax_sent"
    FAX_ON_HOLD = "fax_on_hold"
    FAX_BUSY = "fax_busy"
    FAX_NO_ANSWER = "fax_no_answer"
    FAX_DISCONNECTED = "fax_disconnected"
    FAX_BLACKLISTED = "fax_blacklisted"

    __str__ = str.__str__


EventTypeOrStr: TypeAlias = Annotated[EventType | str, open_enum_validator(EventType)]
