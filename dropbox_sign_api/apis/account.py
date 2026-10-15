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
from ..errors.account_create_error import AccountCreateErrorBody, account_create_error_mapper
from ..errors.account_get_error import AccountGetErrorBody, account_get_error_mapper
from ..errors.account_update_error import AccountUpdateErrorBody, account_update_error_mapper
from ..errors.account_verify_error import AccountVerifyErrorBody, account_verify_error_mapper
from ..models.account_create_request import AccountCreateRequest, AccountCreateRequestDict
from ..models.account_create_response import AccountCreateResponse
from ..models.account_get_response import AccountGetResponse
from ..models.account_update_request import AccountUpdateRequest, AccountUpdateRequestDict
from ..models.account_verify_request import AccountVerifyRequest, AccountVerifyRequestDict
from ..models.account_verify_response import AccountVerifyResponse
from ..server.server import Server


class Account:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AccountWithRawResponse(client, server, auth)

    def account_create(
        self,
        body: AccountCreateRequest | AccountCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AccountCreateResponse:
        """Creates a new Dropbox Sign Account that is associated with the specified ``email_address``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(self._with_raw_response.account_create(body, request_options=request_options))

    def account_get(
        self,
        *,
        account_id: str | None = None,
        email_address: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AccountGetResponse:
        """Returns the properties and settings of your Account.

        Args:
            account_id: ``account_id`` or ``email_address`` is required. If both are provided, the account id prevails.
                The ID of the Account.
            email_address: ``account_id`` or ``email_address`` is required, If both are provided, the account id
                prevails. The email address of the Account.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.account_get(
                account_id=account_id, email_address=email_address, request_options=request_options
            ),
        )

    def account_update(
        self,
        body: AccountUpdateRequest | AccountUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AccountGetResponse:
        """Updates the properties and settings of your Account. Currently only allows for updates to the `Callback URL
        </api/reference/tag/Callbacks-and-Events>`__ and locale.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(self._with_raw_response.account_update(body, request_options=request_options))

    def account_verify(
        self,
        body: AccountVerifyRequest | AccountVerifyRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AccountVerifyResponse:
        """Verifies whether an Dropbox Sign Account exists for the given email address.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(self._with_raw_response.account_verify(body, request_options=request_options))

    @property
    def with_raw_response(self) -> AccountWithRawResponse:
        return self._with_raw_response


class AsyncAccount:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAccountWithRawResponse(client, server, auth)

    async def account_create(
        self,
        body: AccountCreateRequest | AccountCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AccountCreateResponse:
        """Creates a new Dropbox Sign Account that is associated with the specified ``email_address``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(await self._with_raw_response.account_create(body, request_options=request_options))

    async def account_get(
        self,
        *,
        account_id: str | None = None,
        email_address: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AccountGetResponse:
        """Returns the properties and settings of your Account.

        Args:
            account_id: ``account_id`` or ``email_address`` is required. If both are provided, the account id prevails.
                The ID of the Account.
            email_address: ``account_id`` or ``email_address`` is required, If both are provided, the account id
                prevails. The email address of the Account.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.account_get(
                account_id=account_id, email_address=email_address, request_options=request_options
            ),
        )

    async def account_update(
        self,
        body: AccountUpdateRequest | AccountUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AccountGetResponse:
        """Updates the properties and settings of your Account. Currently only allows for updates to the `Callback URL
        </api/reference/tag/Callbacks-and-Events>`__ and locale.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(await self._with_raw_response.account_update(body, request_options=request_options))

    async def account_verify(
        self,
        body: AccountVerifyRequest | AccountVerifyRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AccountVerifyResponse:
        """Verifies whether an Dropbox Sign Account exists for the given email address.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(await self._with_raw_response.account_verify(body, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncAccountWithRawResponse:
        return self._with_raw_response


class AccountWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def account_create(
        self,
        body: AccountCreateRequest | AccountCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AccountCreateResponse, AccountCreateErrorBody]:
        """Creates a new Dropbox Sign Account that is associated with the specified ``email_address``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/account/create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AccountCreateRequest | AccountCreateRequestDict](body),
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[AccountCreateResponse],
            error_mapper=account_create_error_mapper,
            request_options=request_options,
        )

    def account_get(
        self,
        *,
        account_id: str | None = None,
        email_address: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AccountGetResponse, AccountGetErrorBody]:
        """Returns the properties and settings of your Account.

        Args:
            account_id: ``account_id`` or ``email_address`` is required. If both are provided, the account id prevails.
                The ID of the Account.
            email_address: ``account_id`` or ``email_address`` is required, If both are provided, the account id
                prevails. The email address of the Account.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/account"),
            query_params=[
                param[str | None]("account_id", account_id), param[str | None]("email_address", email_address)
            ],
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[AccountGetResponse],
            error_mapper=account_get_error_mapper,
            request_options=request_options,
        )

    def account_update(
        self,
        body: AccountUpdateRequest | AccountUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AccountGetResponse, AccountUpdateErrorBody]:
        """Updates the properties and settings of your Account. Currently only allows for updates to the `Callback URL
        </api/reference/tag/Callbacks-and-Events>`__ and locale.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/account"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AccountUpdateRequest | AccountUpdateRequestDict](body),
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[AccountGetResponse],
            error_mapper=account_update_error_mapper,
            request_options=request_options,
        )

    def account_verify(
        self,
        body: AccountVerifyRequest | AccountVerifyRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AccountVerifyResponse, AccountVerifyErrorBody]:
        """Verifies whether an Dropbox Sign Account exists for the given email address.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/account/verify"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AccountVerifyRequest | AccountVerifyRequestDict](body),
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[AccountVerifyResponse],
            error_mapper=account_verify_error_mapper,
            request_options=request_options,
        )


class AsyncAccountWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def account_create(
        self,
        body: AccountCreateRequest | AccountCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AccountCreateResponse, AccountCreateErrorBody]:
        """Creates a new Dropbox Sign Account that is associated with the specified ``email_address``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/account/create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AccountCreateRequest | AccountCreateRequestDict](body),
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[AccountCreateResponse],
            error_mapper=account_create_error_mapper,
            request_options=request_options,
        )

    async def account_get(
        self,
        *,
        account_id: str | None = None,
        email_address: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AccountGetResponse, AccountGetErrorBody]:
        """Returns the properties and settings of your Account.

        Args:
            account_id: ``account_id`` or ``email_address`` is required. If both are provided, the account id prevails.
                The ID of the Account.
            email_address: ``account_id`` or ``email_address`` is required, If both are provided, the account id
                prevails. The email address of the Account.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/account"),
            query_params=[
                param[str | None]("account_id", account_id), param[str | None]("email_address", email_address)
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[AccountGetResponse],
            error_mapper=account_get_error_mapper,
            request_options=request_options,
        )

    async def account_update(
        self,
        body: AccountUpdateRequest | AccountUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AccountGetResponse, AccountUpdateErrorBody]:
        """Updates the properties and settings of your Account. Currently only allows for updates to the `Callback URL
        </api/reference/tag/Callbacks-and-Events>`__ and locale.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/account"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AccountUpdateRequest | AccountUpdateRequestDict](body),
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[AccountGetResponse],
            error_mapper=account_update_error_mapper,
            request_options=request_options,
        )

    async def account_verify(
        self,
        body: AccountVerifyRequest | AccountVerifyRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AccountVerifyResponse, AccountVerifyErrorBody]:
        """Verifies whether an Dropbox Sign Account exists for the given email address.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/account/verify"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AccountVerifyRequest | AccountVerifyRequestDict](body),
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[AccountVerifyResponse],
            error_mapper=account_verify_error_mapper,
            request_options=request_options,
        )
