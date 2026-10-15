from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_response import ErrorResponse

OauthTokenGenerateErrorBody: TypeAlias = ErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _OauthTokenGenerateError:
    def map(self, status_code: int, content: bytes) -> OauthTokenGenerateErrorBody:
        match status_code:
            case code if 400 <= code <= 499:
                return decode_json[ErrorResponse](content)
            case _:
                return RawError(status_code, content)


oauth_token_generate_error_mapper: Final[ErrorMapper[OauthTokenGenerateErrorBody]] = _OauthTokenGenerateError()
