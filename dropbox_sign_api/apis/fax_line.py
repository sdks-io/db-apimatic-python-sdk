from __future__ import annotations

from typing import Any
from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
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
from ..errors.fax_line_add_user_error import FaxLineAddUserErrorBody, fax_line_add_user_error_mapper
from ..errors.fax_line_area_code_get_error import FaxLineAreaCodeGetErrorBody, fax_line_area_code_get_error_mapper
from ..errors.fax_line_create_error import FaxLineCreateErrorBody, fax_line_create_error_mapper
from ..errors.fax_line_delete_error import FaxLineDeleteErrorBody, fax_line_delete_error_mapper
from ..errors.fax_line_get_error import FaxLineGetErrorBody, fax_line_get_error_mapper
from ..errors.fax_line_list_error import FaxLineListErrorBody, fax_line_list_error_mapper
from ..errors.fax_line_remove_user_error import FaxLineRemoveUserErrorBody, fax_line_remove_user_error_mapper
from ..models.enums.fax_line_area_code_get_country_enum import FaxLineAreaCodeGetCountryEnumOrStr
from ..models.enums.fax_line_area_code_get_province_enum import FaxLineAreaCodeGetProvinceEnumOrStr
from ..models.enums.fax_line_area_code_get_state_enum import FaxLineAreaCodeGetStateEnumOrStr
from ..models.fax_line_add_user_request import FaxLineAddUserRequest, FaxLineAddUserRequestDict
from ..models.fax_line_area_code_get_response import FaxLineAreaCodeGetResponse
from ..models.fax_line_create_request import FaxLineCreateRequest, FaxLineCreateRequestDict
from ..models.fax_line_delete_request import FaxLineDeleteRequest, FaxLineDeleteRequestDict
from ..models.fax_line_list_response import FaxLineListResponse
from ..models.fax_line_remove_user_request import FaxLineRemoveUserRequest, FaxLineRemoveUserRequestDict
from ..models.fax_line_response import FaxLineResponse
from ..server.server import Server


class FaxLine:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = FaxLineWithRawResponse(client, server, auth)

    def fax_line_add_user(
        self,
        body: FaxLineAddUserRequest | FaxLineAddUserRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FaxLineResponse:
        """Grants a user access to the specified Fax Line.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(self._with_raw_response.fax_line_add_user(body, request_options=request_options))

    def fax_line_area_code_get(
        self,
        country: FaxLineAreaCodeGetCountryEnumOrStr,
        *,
        state: FaxLineAreaCodeGetStateEnumOrStr | None = None,
        province: FaxLineAreaCodeGetProvinceEnumOrStr | None = None,
        city: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FaxLineAreaCodeGetResponse:
        """Returns a list of available area codes for a given state/province and city

        Args:
            country: Filter area codes by country
            state: Filter area codes by state
            province: Filter area codes by province
            city: Filter area codes by city
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.fax_line_area_code_get(
                country, state=state, province=province, city=city, request_options=request_options
            ),
        )

    def fax_line_create(
        self,
        body: FaxLineCreateRequest | FaxLineCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FaxLineResponse:
        """Purchases a new Fax Line

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(self._with_raw_response.fax_line_create(body, request_options=request_options))

    def fax_line_delete(
        self,
        body: FaxLineDeleteRequest | FaxLineDeleteRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Deletes the specified Fax Line from the subscription.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(self._with_raw_response.fax_line_delete(body, request_options=request_options))

    def fax_line_get(self, number: str, *, request_options: RequestOptionsOrDict | None = None) -> FaxLineResponse:
        """Returns the properties and settings of a Fax Line.

        Args:
            number: The Fax Line number
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(self._with_raw_response.fax_line_get(number, request_options=request_options))

    def fax_line_list(
        self,
        *,
        account_id: str | None = None,
        page: int | None = 1,
        page_size: int | None = 20,
        show_team_lines: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FaxLineListResponse:
        """Returns the properties and settings of multiple Fax Lines.

        Args:
            account_id: Account ID
            page: Which page number of the Fax Line List to return. Defaults to ``1``.
            page_size: Number of objects to be returned per page. Must be between ``1`` and ``100``. Default is ``20``.
            show_team_lines: Include Fax Lines belonging to team members in the list
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.fax_line_list(
                account_id=account_id,
                page=page,
                page_size=page_size,
                show_team_lines=show_team_lines,
                request_options=request_options,
            ),
        )

    def fax_line_remove_user(
        self,
        body: FaxLineRemoveUserRequest | FaxLineRemoveUserRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FaxLineResponse:
        """Removes a user's access to the specified Fax Line

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(self._with_raw_response.fax_line_remove_user(body, request_options=request_options))

    @property
    def with_raw_response(self) -> FaxLineWithRawResponse:
        return self._with_raw_response


class AsyncFaxLine:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncFaxLineWithRawResponse(client, server, auth)

    async def fax_line_add_user(
        self,
        body: FaxLineAddUserRequest | FaxLineAddUserRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FaxLineResponse:
        """Grants a user access to the specified Fax Line.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(await self._with_raw_response.fax_line_add_user(body, request_options=request_options))

    async def fax_line_area_code_get(
        self,
        country: FaxLineAreaCodeGetCountryEnumOrStr,
        *,
        state: FaxLineAreaCodeGetStateEnumOrStr | None = None,
        province: FaxLineAreaCodeGetProvinceEnumOrStr | None = None,
        city: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FaxLineAreaCodeGetResponse:
        """Returns a list of available area codes for a given state/province and city

        Args:
            country: Filter area codes by country
            state: Filter area codes by state
            province: Filter area codes by province
            city: Filter area codes by city
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.fax_line_area_code_get(
                country, state=state, province=province, city=city, request_options=request_options
            ),
        )

    async def fax_line_create(
        self,
        body: FaxLineCreateRequest | FaxLineCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FaxLineResponse:
        """Purchases a new Fax Line

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(await self._with_raw_response.fax_line_create(body, request_options=request_options))

    async def fax_line_delete(
        self,
        body: FaxLineDeleteRequest | FaxLineDeleteRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Deletes the specified Fax Line from the subscription.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(await self._with_raw_response.fax_line_delete(body, request_options=request_options))

    async def fax_line_get(
        self, number: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> FaxLineResponse:
        """Returns the properties and settings of a Fax Line.

        Args:
            number: The Fax Line number
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(await self._with_raw_response.fax_line_get(number, request_options=request_options))

    async def fax_line_list(
        self,
        *,
        account_id: str | None = None,
        page: int | None = 1,
        page_size: int | None = 20,
        show_team_lines: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FaxLineListResponse:
        """Returns the properties and settings of multiple Fax Lines.

        Args:
            account_id: Account ID
            page: Which page number of the Fax Line List to return. Defaults to ``1``.
            page_size: Number of objects to be returned per page. Must be between ``1`` and ``100``. Default is ``20``.
            show_team_lines: Include Fax Lines belonging to team members in the list
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.fax_line_list(
                account_id=account_id,
                page=page,
                page_size=page_size,
                show_team_lines=show_team_lines,
                request_options=request_options,
            ),
        )

    async def fax_line_remove_user(
        self,
        body: FaxLineRemoveUserRequest | FaxLineRemoveUserRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FaxLineResponse:
        """Removes a user's access to the specified Fax Line

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(await self._with_raw_response.fax_line_remove_user(body, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncFaxLineWithRawResponse:
        return self._with_raw_response


class FaxLineWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fax_line_add_user(
        self,
        body: FaxLineAddUserRequest | FaxLineAddUserRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FaxLineResponse, FaxLineAddUserErrorBody]:
        """Grants a user access to the specified Fax Line.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/fax_line/add_user"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[FaxLineAddUserRequest | FaxLineAddUserRequestDict](body),
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[FaxLineResponse],
            error_mapper=fax_line_add_user_error_mapper,
            request_options=request_options,
        )

    def fax_line_area_code_get(
        self,
        country: FaxLineAreaCodeGetCountryEnumOrStr,
        *,
        state: FaxLineAreaCodeGetStateEnumOrStr | None = None,
        province: FaxLineAreaCodeGetProvinceEnumOrStr | None = None,
        city: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FaxLineAreaCodeGetResponse, FaxLineAreaCodeGetErrorBody]:
        """Returns a list of available area codes for a given state/province and city

        Args:
            country: Filter area codes by country
            state: Filter area codes by state
            province: Filter area codes by province
            city: Filter area codes by city
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/fax_line/area_codes"),
            query_params=[
                param[FaxLineAreaCodeGetCountryEnumOrStr]("country", country),
                param[FaxLineAreaCodeGetStateEnumOrStr | None]("state", state),
                param[FaxLineAreaCodeGetProvinceEnumOrStr | None]("province", province),
                param[str | None]("city", city),
            ],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[FaxLineAreaCodeGetResponse],
            error_mapper=fax_line_area_code_get_error_mapper,
            request_options=request_options,
        )

    def fax_line_create(
        self,
        body: FaxLineCreateRequest | FaxLineCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FaxLineResponse, FaxLineCreateErrorBody]:
        """Purchases a new Fax Line

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/fax_line/create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[FaxLineCreateRequest | FaxLineCreateRequestDict](body),
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[FaxLineResponse],
            error_mapper=fax_line_create_error_mapper,
            request_options=request_options,
        )

    def fax_line_delete(
        self,
        body: FaxLineDeleteRequest | FaxLineDeleteRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, FaxLineDeleteErrorBody]:
        """Deletes the specified Fax Line from the subscription.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/fax_line"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[FaxLineDeleteRequest | FaxLineDeleteRequestDict](body),
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[Any],
            error_mapper=fax_line_delete_error_mapper,
            request_options=request_options,
        )

    def fax_line_get(
        self, number: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FaxLineResponse, FaxLineGetErrorBody]:
        """Returns the properties and settings of a Fax Line.

        Args:
            number: The Fax Line number
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/fax_line"),
            query_params=[param[str]("number", number)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[FaxLineResponse],
            error_mapper=fax_line_get_error_mapper,
            request_options=request_options,
        )

    def fax_line_list(
        self,
        *,
        account_id: str | None = None,
        page: int | None = 1,
        page_size: int | None = 20,
        show_team_lines: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FaxLineListResponse, FaxLineListErrorBody]:
        """Returns the properties and settings of multiple Fax Lines.

        Args:
            account_id: Account ID
            page: Which page number of the Fax Line List to return. Defaults to ``1``.
            page_size: Number of objects to be returned per page. Must be between ``1`` and ``100``. Default is ``20``.
            show_team_lines: Include Fax Lines belonging to team members in the list
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/fax_line/list"),
            query_params=[
                param[str | None]("account_id", account_id),
                param[int | None]("page", page),
                param[int | None]("page_size", page_size),
                param[bool | None]("show_team_lines", show_team_lines),
            ],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[FaxLineListResponse],
            error_mapper=fax_line_list_error_mapper,
            request_options=request_options,
        )

    def fax_line_remove_user(
        self,
        body: FaxLineRemoveUserRequest | FaxLineRemoveUserRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FaxLineResponse, FaxLineRemoveUserErrorBody]:
        """Removes a user's access to the specified Fax Line

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/fax_line/remove_user"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[FaxLineRemoveUserRequest | FaxLineRemoveUserRequestDict](body),
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[FaxLineResponse],
            error_mapper=fax_line_remove_user_error_mapper,
            request_options=request_options,
        )


class AsyncFaxLineWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fax_line_add_user(
        self,
        body: FaxLineAddUserRequest | FaxLineAddUserRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FaxLineResponse, FaxLineAddUserErrorBody]:
        """Grants a user access to the specified Fax Line.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/fax_line/add_user"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[FaxLineAddUserRequest | FaxLineAddUserRequestDict](body),
            auth_scheme=self._auth.api_key,
            decoder=async_json_decoder[FaxLineResponse],
            error_mapper=fax_line_add_user_error_mapper,
            request_options=request_options,
        )

    async def fax_line_area_code_get(
        self,
        country: FaxLineAreaCodeGetCountryEnumOrStr,
        *,
        state: FaxLineAreaCodeGetStateEnumOrStr | None = None,
        province: FaxLineAreaCodeGetProvinceEnumOrStr | None = None,
        city: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FaxLineAreaCodeGetResponse, FaxLineAreaCodeGetErrorBody]:
        """Returns a list of available area codes for a given state/province and city

        Args:
            country: Filter area codes by country
            state: Filter area codes by state
            province: Filter area codes by province
            city: Filter area codes by city
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/fax_line/area_codes"),
            query_params=[
                param[FaxLineAreaCodeGetCountryEnumOrStr]("country", country),
                param[FaxLineAreaCodeGetStateEnumOrStr | None]("state", state),
                param[FaxLineAreaCodeGetProvinceEnumOrStr | None]("province", province),
                param[str | None]("city", city),
            ],
            auth_scheme=self._auth.api_key,
            decoder=async_json_decoder[FaxLineAreaCodeGetResponse],
            error_mapper=fax_line_area_code_get_error_mapper,
            request_options=request_options,
        )

    async def fax_line_create(
        self,
        body: FaxLineCreateRequest | FaxLineCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FaxLineResponse, FaxLineCreateErrorBody]:
        """Purchases a new Fax Line

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/fax_line/create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[FaxLineCreateRequest | FaxLineCreateRequestDict](body),
            auth_scheme=self._auth.api_key,
            decoder=async_json_decoder[FaxLineResponse],
            error_mapper=fax_line_create_error_mapper,
            request_options=request_options,
        )

    async def fax_line_delete(
        self,
        body: FaxLineDeleteRequest | FaxLineDeleteRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, FaxLineDeleteErrorBody]:
        """Deletes the specified Fax Line from the subscription.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/fax_line"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[FaxLineDeleteRequest | FaxLineDeleteRequestDict](body),
            auth_scheme=self._auth.api_key,
            decoder=async_json_decoder[Any],
            error_mapper=fax_line_delete_error_mapper,
            request_options=request_options,
        )

    async def fax_line_get(
        self, number: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FaxLineResponse, FaxLineGetErrorBody]:
        """Returns the properties and settings of a Fax Line.

        Args:
            number: The Fax Line number
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/fax_line"),
            query_params=[param[str]("number", number)],
            auth_scheme=self._auth.api_key,
            decoder=async_json_decoder[FaxLineResponse],
            error_mapper=fax_line_get_error_mapper,
            request_options=request_options,
        )

    async def fax_line_list(
        self,
        *,
        account_id: str | None = None,
        page: int | None = 1,
        page_size: int | None = 20,
        show_team_lines: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FaxLineListResponse, FaxLineListErrorBody]:
        """Returns the properties and settings of multiple Fax Lines.

        Args:
            account_id: Account ID
            page: Which page number of the Fax Line List to return. Defaults to ``1``.
            page_size: Number of objects to be returned per page. Must be between ``1`` and ``100``. Default is ``20``.
            show_team_lines: Include Fax Lines belonging to team members in the list
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/fax_line/list"),
            query_params=[
                param[str | None]("account_id", account_id),
                param[int | None]("page", page),
                param[int | None]("page_size", page_size),
                param[bool | None]("show_team_lines", show_team_lines),
            ],
            auth_scheme=self._auth.api_key,
            decoder=async_json_decoder[FaxLineListResponse],
            error_mapper=fax_line_list_error_mapper,
            request_options=request_options,
        )

    async def fax_line_remove_user(
        self,
        body: FaxLineRemoveUserRequest | FaxLineRemoveUserRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FaxLineResponse, FaxLineRemoveUserErrorBody]:
        """Removes a user's access to the specified Fax Line

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/fax_line/remove_user"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[FaxLineRemoveUserRequest | FaxLineRemoveUserRequestDict](body),
            auth_scheme=self._auth.api_key,
            decoder=async_json_decoder[FaxLineResponse],
            error_mapper=fax_line_remove_user_error_mapper,
            request_options=request_options,
        )
