from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_response import ErrorResponse

UnclaimedDraftCreateEmbeddedWithTemplateErrorBody: TypeAlias = ErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _UnclaimedDraftCreateEmbeddedWithTemplateError:
    def map(self, status_code: int, content: bytes) -> UnclaimedDraftCreateEmbeddedWithTemplateErrorBody:
        match status_code:
            case code if 400 <= code <= 499:
                return decode_json[ErrorResponse](content)
            case _:
                return RawError(status_code, content)


unclaimed_draft_create_embedded_with_template_error_mapper: Final[
    ErrorMapper[UnclaimedDraftCreateEmbeddedWithTemplateErrorBody]
] = _UnclaimedDraftCreateEmbeddedWithTemplateError()
