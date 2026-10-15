from __future__ import annotations

from uuid import UUID, uuid4

from ..core import (
    ApiResult,
    AsyncRawClient,
    BaseRawResponse,
    RawClient,
    RequestOptionsOrDict,
    async_json_decoder,
    json_body,
    json_decoder,
    param,
    unwrap,
)
from ..errors.oauth_token_generate_error import OauthTokenGenerateErrorBody, oauth_token_generate_error_mapper
from ..errors.oauth_token_refresh_error import OauthTokenRefreshErrorBody, oauth_token_refresh_error_mapper
from ..models.oauth_token_generate_request import OauthTokenGenerateRequest, OauthTokenGenerateRequestDict
from ..models.oauth_token_refresh_request import OauthTokenRefreshRequest, OauthTokenRefreshRequestDict
from ..models.oauth_token_response import OauthTokenResponse
from ..server.server import Server


class Oauth:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = OauthWithRawResponse(client, server)

    def oauth_token_generate(
        self,
        body: OauthTokenGenerateRequest | OauthTokenGenerateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OauthTokenResponse:
        """Once you have retrieved the code from the user callback, you will need to exchange it for an access token via
        a backend call.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(self._with_raw_response.oauth_token_generate(body, request_options=request_options))

    def oauth_token_refresh(
        self,
        body: OauthTokenRefreshRequest | OauthTokenRefreshRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OauthTokenResponse:
        """Access tokens are only valid for a given period of time (typically one hour) for security reasons. Whenever
        acquiring an new access token its TTL is also given (see ``expires_in``), along with a refresh token that can be
        used to acquire a new access token after the current one has expired.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(self._with_raw_response.oauth_token_refresh(body, request_options=request_options))

    @property
    def with_raw_response(self) -> OauthWithRawResponse:
        return self._with_raw_response


class AsyncOauth:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncOauthWithRawResponse(client, server)

    async def oauth_token_generate(
        self,
        body: OauthTokenGenerateRequest | OauthTokenGenerateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OauthTokenResponse:
        """Once you have retrieved the code from the user callback, you will need to exchange it for an access token via
        a backend call.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(await self._with_raw_response.oauth_token_generate(body, request_options=request_options))

    async def oauth_token_refresh(
        self,
        body: OauthTokenRefreshRequest | OauthTokenRefreshRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OauthTokenResponse:
        """Access tokens are only valid for a given period of time (typically one hour) for security reasons. Whenever
        acquiring an new access token its TTL is also given (see ``expires_in``), along with a refresh token that can be
        used to acquire a new access token after the current one has expired.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(await self._with_raw_response.oauth_token_refresh(body, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncOauthWithRawResponse:
        return self._with_raw_response


class OauthWithRawResponse(BaseRawResponse[RawClient, Server]):
    def oauth_token_generate(
        self,
        body: OauthTokenGenerateRequest | OauthTokenGenerateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OauthTokenResponse, OauthTokenGenerateErrorBody]:
        """Once you have retrieved the code from the user callback, you will need to exchange it for an access token via
        a backend call.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/oauth/token"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[OauthTokenGenerateRequest | OauthTokenGenerateRequestDict](body),
            decoder=json_decoder[OauthTokenResponse],
            error_mapper=oauth_token_generate_error_mapper,
            request_options=request_options,
        )

    def oauth_token_refresh(
        self,
        body: OauthTokenRefreshRequest | OauthTokenRefreshRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OauthTokenResponse, OauthTokenRefreshErrorBody]:
        """Access tokens are only valid for a given period of time (typically one hour) for security reasons. Whenever
        acquiring an new access token its TTL is also given (see ``expires_in``), along with a refresh token that can be
        used to acquire a new access token after the current one has expired.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/oauth/token?refresh"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[OauthTokenRefreshRequest | OauthTokenRefreshRequestDict](body),
            decoder=json_decoder[OauthTokenResponse],
            error_mapper=oauth_token_refresh_error_mapper,
            request_options=request_options,
        )


class AsyncOauthWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def oauth_token_generate(
        self,
        body: OauthTokenGenerateRequest | OauthTokenGenerateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OauthTokenResponse, OauthTokenGenerateErrorBody]:
        """Once you have retrieved the code from the user callback, you will need to exchange it for an access token via
        a backend call.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/oauth/token"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[OauthTokenGenerateRequest | OauthTokenGenerateRequestDict](body),
            decoder=async_json_decoder[OauthTokenResponse],
            error_mapper=oauth_token_generate_error_mapper,
            request_options=request_options,
        )

    async def oauth_token_refresh(
        self,
        body: OauthTokenRefreshRequest | OauthTokenRefreshRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OauthTokenResponse, OauthTokenRefreshErrorBody]:
        """Access tokens are only valid for a given period of time (typically one hour) for security reasons. Whenever
        acquiring an new access token its TTL is also given (see ``expires_in``), along with a refresh token that can be
        used to acquire a new access token after the current one has expired.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/oauth/token?refresh"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[OauthTokenRefreshRequest | OauthTokenRefreshRequestDict](body),
            decoder=async_json_decoder[OauthTokenResponse],
            error_mapper=oauth_token_refresh_error_mapper,
            request_options=request_options,
        )
