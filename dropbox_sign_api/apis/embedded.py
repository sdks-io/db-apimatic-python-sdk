from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AnySchemes,
    ApiResult,
    AsyncAnySchemes,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_json_decoder,
    json_body,
    json_decoder,
    param,
    unwrap,
)
from ..errors.embedded_edit_url_error import EmbeddedEditUrlErrorBody, embedded_edit_url_error_mapper
from ..errors.embedded_sign_url_error import EmbeddedSignUrlErrorBody, embedded_sign_url_error_mapper
from ..models.embedded_edit_url_request import EmbeddedEditUrlRequest, EmbeddedEditUrlRequestDict
from ..models.embedded_edit_url_response import EmbeddedEditUrlResponse
from ..models.embedded_sign_url_response import EmbeddedSignUrlResponse
from ..server.server import Server


class Embedded:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = EmbeddedWithRawResponse(client, server, auth)

    def embedded_edit_url(
        self,
        template_id: str,
        body: EmbeddedEditUrlRequest | EmbeddedEditUrlRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EmbeddedEditUrlResponse:
        """Retrieves an embedded object containing a template url that can be opened in an iFrame. Note that only
        templates created via the embedded template process are available to be edited with this endpoint.

        Args:
            template_id: The id of the template to edit.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(self._with_raw_response.embedded_edit_url(template_id, body, request_options=request_options))

    def embedded_sign_url(
        self, signature_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> EmbeddedSignUrlResponse:
        """Retrieves an embedded object containing a signature url that can be opened in an iFrame. Note that templates
        created via the embedded template process will only be accessible through the API.

        Args:
            signature_id: The id of the signature to get a signature url for.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(self._with_raw_response.embedded_sign_url(signature_id, request_options=request_options))

    @property
    def with_raw_response(self) -> EmbeddedWithRawResponse:
        return self._with_raw_response


class AsyncEmbedded:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncEmbeddedWithRawResponse(client, server, auth)

    async def embedded_edit_url(
        self,
        template_id: str,
        body: EmbeddedEditUrlRequest | EmbeddedEditUrlRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EmbeddedEditUrlResponse:
        """Retrieves an embedded object containing a template url that can be opened in an iFrame. Note that only
        templates created via the embedded template process are available to be edited with this endpoint.

        Args:
            template_id: The id of the template to edit.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.embedded_edit_url(template_id, body, request_options=request_options)
        )

    async def embedded_sign_url(
        self, signature_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> EmbeddedSignUrlResponse:
        """Retrieves an embedded object containing a signature url that can be opened in an iFrame. Note that templates
        created via the embedded template process will only be accessible through the API.

        Args:
            signature_id: The id of the signature to get a signature url for.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(await self._with_raw_response.embedded_sign_url(signature_id, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncEmbeddedWithRawResponse:
        return self._with_raw_response


class EmbeddedWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def embedded_edit_url(
        self,
        template_id: str,
        body: EmbeddedEditUrlRequest | EmbeddedEditUrlRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EmbeddedEditUrlResponse, EmbeddedEditUrlErrorBody]:
        """Retrieves an embedded object containing a template url that can be opened in an iFrame. Note that only
        templates created via the embedded template process are available to be edited with this endpoint.

        Args:
            template_id: The id of the template to edit.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/embedded/edit_url/{template_id}"),
            path_params=[param[str]("template_id", template_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[EmbeddedEditUrlRequest | EmbeddedEditUrlRequestDict](body),
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[EmbeddedEditUrlResponse],
            error_mapper=embedded_edit_url_error_mapper,
            request_options=request_options,
        )

    def embedded_sign_url(
        self, signature_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EmbeddedSignUrlResponse, EmbeddedSignUrlErrorBody]:
        """Retrieves an embedded object containing a signature url that can be opened in an iFrame. Note that templates
        created via the embedded template process will only be accessible through the API.

        Args:
            signature_id: The id of the signature to get a signature url for.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/embedded/sign_url/{signature_id}"),
            path_params=[param[str]("signature_id", signature_id)],
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[EmbeddedSignUrlResponse],
            error_mapper=embedded_sign_url_error_mapper,
            request_options=request_options,
        )


class AsyncEmbeddedWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def embedded_edit_url(
        self,
        template_id: str,
        body: EmbeddedEditUrlRequest | EmbeddedEditUrlRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EmbeddedEditUrlResponse, EmbeddedEditUrlErrorBody]:
        """Retrieves an embedded object containing a template url that can be opened in an iFrame. Note that only
        templates created via the embedded template process are available to be edited with this endpoint.

        Args:
            template_id: The id of the template to edit.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/embedded/edit_url/{template_id}"),
            path_params=[param[str]("template_id", template_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[EmbeddedEditUrlRequest | EmbeddedEditUrlRequestDict](body),
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[EmbeddedEditUrlResponse],
            error_mapper=embedded_edit_url_error_mapper,
            request_options=request_options,
        )

    async def embedded_sign_url(
        self, signature_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EmbeddedSignUrlResponse, EmbeddedSignUrlErrorBody]:
        """Retrieves an embedded object containing a signature url that can be opened in an iFrame. Note that templates
        created via the embedded template process will only be accessible through the API.

        Args:
            signature_id: The id of the signature to get a signature url for.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/embedded/sign_url/{signature_id}"),
            path_params=[param[str]("signature_id", signature_id)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[EmbeddedSignUrlResponse],
            error_mapper=embedded_sign_url_error_mapper,
            request_options=request_options,
        )
