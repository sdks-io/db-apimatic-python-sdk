from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_response import ErrorResponse

TemplateCreateEmbeddedDraftErrorBody: TypeAlias = ErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _TemplateCreateEmbeddedDraftError:
    def map(self, status_code: int, content: bytes) -> TemplateCreateEmbeddedDraftErrorBody:
        match status_code:
            case code if 400 <= code <= 499:
                return decode_json[ErrorResponse](content)
            case _:
                return RawError(status_code, content)


template_create_embedded_draft_error_mapper: Final[
    ErrorMapper[TemplateCreateEmbeddedDraftErrorBody]
] = _TemplateCreateEmbeddedDraftError()
