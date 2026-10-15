from __future__ import annotations

from typing import TypeAlias

from ..account_confirmed_event import AccountConfirmedEvent, AccountConfirmedEventDict
from ..callback_test_event import CallbackTestEvent, CallbackTestEventDict
from ..fax_blacklisted_event import FaxBlacklistedEvent, FaxBlacklistedEventDict
from ..fax_busy_event import FaxBusyEvent, FaxBusyEventDict
from ..fax_disconnected_event import FaxDisconnectedEvent, FaxDisconnectedEventDict
from ..fax_no_answer_event import FaxNoAnswerEvent, FaxNoAnswerEventDict
from ..fax_on_hold_event import FaxOnHoldEvent, FaxOnHoldEventDict
from ..fax_received_event import FaxReceivedEvent, FaxReceivedEventDict
from ..fax_sent_event import FaxSentEvent, FaxSentEventDict
from ..file_error_event import FileErrorEvent, FileErrorEventDict
from ..sign_url_invalid_event import SignUrlInvalidEvent, SignUrlInvalidEventDict
from ..signature_request_all_signed_event import SignatureRequestAllSignedEvent, SignatureRequestAllSignedEventDict
from ..signature_request_canceled_event import SignatureRequestCanceledEvent, SignatureRequestCanceledEventDict
from ..signature_request_declined_event import SignatureRequestDeclinedEvent, SignatureRequestDeclinedEventDict
from ..signature_request_destroyed_event import SignatureRequestDestroyedEvent, SignatureRequestDestroyedEventDict
from ..signature_request_downloadable_event import (
    SignatureRequestDownloadableEvent,
    SignatureRequestDownloadableEventDict,
)
from ..signature_request_email_bounce_event import (
    SignatureRequestEmailBounceEvent,
    SignatureRequestEmailBounceEventDict,
)
from ..signature_request_expired_event import SignatureRequestExpiredEvent, SignatureRequestExpiredEventDict
from ..signature_request_incomplete_qes_event import (
    SignatureRequestIncompleteQesEvent,
    SignatureRequestIncompleteQesEventDict,
)
from ..signature_request_invalid_event import SignatureRequestInvalidEvent, SignatureRequestInvalidEventDict
from ..signature_request_prepared_event import SignatureRequestPreparedEvent, SignatureRequestPreparedEventDict
from ..signature_request_reassigned_event import SignatureRequestReassignedEvent, SignatureRequestReassignedEventDict
from ..signature_request_remind_event import SignatureRequestRemindEvent, SignatureRequestRemindEventDict
from ..signature_request_sent_event import SignatureRequestSentEvent, SignatureRequestSentEventDict
from ..signature_request_signed_event import SignatureRequestSignedEvent, SignatureRequestSignedEventDict
from ..signature_request_signer_removed_event import (
    SignatureRequestSignerRemovedEvent,
    SignatureRequestSignerRemovedEventDict,
)
from ..signature_request_viewed_event import SignatureRequestViewedEvent, SignatureRequestViewedEventDict
from ..template_created_event import TemplateCreatedEvent, TemplateCreatedEventDict
from ..template_error_event import TemplateErrorEvent, TemplateErrorEventDict
from ..unknown_error_event import UnknownErrorEvent, UnknownErrorEventDict

EventCallbackPayload: TypeAlias = (
    SignatureRequestViewedEvent
    | SignatureRequestSignedEvent
    | SignatureRequestSignerRemovedEvent
    | SignatureRequestDownloadableEvent
    | SignatureRequestSentEvent
    | SignatureRequestAllSignedEvent
    | SignatureRequestInvalidEvent
    | SignatureRequestEmailBounceEvent
    | SignatureRequestRemindEvent
    | SignatureRequestIncompleteQesEvent
    | SignatureRequestDestroyedEvent
    | SignatureRequestCanceledEvent
    | SignatureRequestDeclinedEvent
    | SignatureRequestExpiredEvent
    | SignatureRequestReassignedEvent
    | SignatureRequestPreparedEvent
    | AccountConfirmedEvent
    | UnknownErrorEvent
    | FileErrorEvent
    | TemplateCreatedEvent
    | TemplateErrorEvent
    | SignUrlInvalidEvent
    | CallbackTestEvent
    | FaxReceivedEvent
    | FaxSentEvent
    | FaxOnHoldEvent
    | FaxBusyEvent
    | FaxNoAnswerEvent
    | FaxDisconnectedEvent
    | FaxBlacklistedEvent
)
"""JSON payload delivered for a webhook event. The concrete shape is selected by ``event.event_type``."""

EventCallbackPayloadDict: TypeAlias = (
    SignatureRequestViewedEventDict
    | SignatureRequestSignedEventDict
    | SignatureRequestSignerRemovedEventDict
    | SignatureRequestDownloadableEventDict
    | SignatureRequestSentEventDict
    | SignatureRequestAllSignedEventDict
    | SignatureRequestInvalidEventDict
    | SignatureRequestEmailBounceEventDict
    | SignatureRequestRemindEventDict
    | SignatureRequestIncompleteQesEventDict
    | SignatureRequestDestroyedEventDict
    | SignatureRequestCanceledEventDict
    | SignatureRequestDeclinedEventDict
    | SignatureRequestExpiredEventDict
    | SignatureRequestReassignedEventDict
    | SignatureRequestPreparedEventDict
    | AccountConfirmedEventDict
    | UnknownErrorEventDict
    | FileErrorEventDict
    | TemplateCreatedEventDict
    | TemplateErrorEventDict
    | SignUrlInvalidEventDict
    | CallbackTestEventDict
    | FaxReceivedEventDict
    | FaxSentEventDict
    | FaxOnHoldEventDict
    | FaxBusyEventDict
    | FaxNoAnswerEventDict
    | FaxDisconnectedEventDict
    | FaxBlacklistedEventDict
)
