from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AnySchemes,
    ApiResult,
    AsyncAnySchemes,
    AsyncFileInput,
    AsyncRawClient,
    FileInput,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_empty_response,
    async_json_decoder,
    empty_response,
    file_part,
    json_decoder,
    multipart_body,
    param,
    unwrap,
)
from ..errors.api_app_create_error import ApiAppCreateErrorBody, api_app_create_error_mapper
from ..errors.api_app_delete_error import ApiAppDeleteErrorBody, api_app_delete_error_mapper
from ..errors.api_app_get_error import ApiAppGetErrorBody, api_app_get_error_mapper
from ..errors.api_app_list_error import ApiAppListErrorBody, api_app_list_error_mapper
from ..errors.api_app_update_error import ApiAppUpdateErrorBody, api_app_update_error_mapper
from ..models.api_app_get_response import ApiAppGetResponse
from ..models.api_app_list_response import ApiAppListResponse
from ..models.sub_oauth import SubOauth, SubOauthDict
from ..models.sub_options import SubOptions, SubOptionsDict
from ..models.sub_white_labeling_options import SubWhiteLabelingOptions, SubWhiteLabelingOptionsDict
from ..server.server import Server


class ApiApp:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ApiAppWithRawResponse(client, server, auth)

    def api_app_create(
        self,
        domains: list[str],
        name: str,
        *,
        callback_url: str | None = None,
        custom_logo_file: FileInput | None = None,
        oauth: SubOauth | SubOauthDict | None = None,
        options: SubOptions | SubOptionsDict | None = None,
        white_labeling_options: SubWhiteLabelingOptions | SubWhiteLabelingOptionsDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiAppGetResponse:
        """Creates a new API App.

        Args:
            domains: The domain names the ApiApp will be associated with.
            name: The name you want to assign to the ApiApp.
            callback_url: The URL at which the ApiApp should receive event callbacks.
            custom_logo_file: An image file to use as a custom logo in embedded contexts. (Only applies to some API
                plans)
            oauth: OAuth related parameters.
            options: Additional options supported by API App.
            white_labeling_options: An array of elements and values serialized to a string, to be used to customize the
                app's signer page. (Only applies to some API plans) Take a look at our `white labeling guide
                <https://developers.hellosign.com/api/reference/premium-branding/>`__ to learn more.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.api_app_create(
                domains,
                name,
                callback_url=callback_url,
                custom_logo_file=custom_logo_file,
                oauth=oauth,
                options=options,
                white_labeling_options=white_labeling_options,
                request_options=request_options,
            ),
        )

    def api_app_delete(self, client_id: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Deletes an API App. Can only be invoked for apps you own.

        Args:
            client_id: The client id of the API App to delete.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(self._with_raw_response.api_app_delete(client_id, request_options=request_options))

    def api_app_get(self, client_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiAppGetResponse:
        """Returns an object with information about an API App.

        Args:
            client_id: The client id of the API App to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(self._with_raw_response.api_app_get(client_id, request_options=request_options))

    def api_app_list(
        self, *, page: int | None = 1, page_size: int | None = 20, request_options: RequestOptionsOrDict | None = None
    ) -> ApiAppListResponse:
        """Returns a list of API Apps that are accessible by you. If you are on a team with an Admin or Developer role,
        this list will include apps owned by teammates.

        Args:
            page: Which page number of the API App List to return. Defaults to ``1``.
            page_size: Number of objects to be returned per page. Must be between ``1`` and ``100``. Default is ``20``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.api_app_list(page=page, page_size=page_size, request_options=request_options)
        )

    def api_app_update(
        self,
        client_id: str,
        *,
        callback_url: str | None = None,
        custom_logo_file: FileInput | None = None,
        domains: list[str] | None = None,
        name: str | None = None,
        oauth: SubOauth | SubOauthDict | None = None,
        options: SubOptions | SubOptionsDict | None = None,
        white_labeling_options: SubWhiteLabelingOptions | SubWhiteLabelingOptionsDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiAppGetResponse:
        """Updates an existing API App. Can only be invoked for apps you own. Only the fields you provide will be
        updated. If you wish to clear an existing optional field, provide an empty string.

        Args:
            client_id: The client id of the API App to update.
            callback_url: The URL at which the API App should receive event callbacks.
            custom_logo_file: An image file to use as a custom logo in embedded contexts. (Only applies to some API
                plans)
            domains: The domain names the ApiApp will be associated with.
            name: The name you want to assign to the ApiApp.
            oauth: OAuth related parameters.
            options: Additional options supported by API App.
            white_labeling_options: An array of elements and values serialized to a string, to be used to customize the
                app's signer page. (Only applies to some API plans) Take a look at our `white labeling guide
                <https://developers.hellosign.com/api/reference/premium-branding/>`__ to learn more.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.api_app_update(
                client_id,
                callback_url=callback_url,
                custom_logo_file=custom_logo_file,
                domains=domains,
                name=name,
                oauth=oauth,
                options=options,
                white_labeling_options=white_labeling_options,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> ApiAppWithRawResponse:
        return self._with_raw_response


class AsyncApiApp:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApiAppWithRawResponse(client, server, auth)

    async def api_app_create(
        self,
        domains: list[str],
        name: str,
        *,
        callback_url: str | None = None,
        custom_logo_file: AsyncFileInput | None = None,
        oauth: SubOauth | SubOauthDict | None = None,
        options: SubOptions | SubOptionsDict | None = None,
        white_labeling_options: SubWhiteLabelingOptions | SubWhiteLabelingOptionsDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiAppGetResponse:
        """Creates a new API App.

        Args:
            domains: The domain names the ApiApp will be associated with.
            name: The name you want to assign to the ApiApp.
            callback_url: The URL at which the ApiApp should receive event callbacks.
            custom_logo_file: An image file to use as a custom logo in embedded contexts. (Only applies to some API
                plans)
            oauth: OAuth related parameters.
            options: Additional options supported by API App.
            white_labeling_options: An array of elements and values serialized to a string, to be used to customize the
                app's signer page. (Only applies to some API plans) Take a look at our `white labeling guide
                <https://developers.hellosign.com/api/reference/premium-branding/>`__ to learn more.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.api_app_create(
                domains,
                name,
                callback_url=callback_url,
                custom_logo_file=custom_logo_file,
                oauth=oauth,
                options=options,
                white_labeling_options=white_labeling_options,
                request_options=request_options,
            ),
        )

    async def api_app_delete(self, client_id: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Deletes an API App. Can only be invoked for apps you own.

        Args:
            client_id: The client id of the API App to delete.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(await self._with_raw_response.api_app_delete(client_id, request_options=request_options))

    async def api_app_get(
        self, client_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiAppGetResponse:
        """Returns an object with information about an API App.

        Args:
            client_id: The client id of the API App to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(await self._with_raw_response.api_app_get(client_id, request_options=request_options))

    async def api_app_list(
        self, *, page: int | None = 1, page_size: int | None = 20, request_options: RequestOptionsOrDict | None = None
    ) -> ApiAppListResponse:
        """Returns a list of API Apps that are accessible by you. If you are on a team with an Admin or Developer role,
        this list will include apps owned by teammates.

        Args:
            page: Which page number of the API App List to return. Defaults to ``1``.
            page_size: Number of objects to be returned per page. Must be between ``1`` and ``100``. Default is ``20``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.api_app_list(page=page, page_size=page_size, request_options=request_options)
        )

    async def api_app_update(
        self,
        client_id: str,
        *,
        callback_url: str | None = None,
        custom_logo_file: AsyncFileInput | None = None,
        domains: list[str] | None = None,
        name: str | None = None,
        oauth: SubOauth | SubOauthDict | None = None,
        options: SubOptions | SubOptionsDict | None = None,
        white_labeling_options: SubWhiteLabelingOptions | SubWhiteLabelingOptionsDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiAppGetResponse:
        """Updates an existing API App. Can only be invoked for apps you own. Only the fields you provide will be
        updated. If you wish to clear an existing optional field, provide an empty string.

        Args:
            client_id: The client id of the API App to update.
            callback_url: The URL at which the API App should receive event callbacks.
            custom_logo_file: An image file to use as a custom logo in embedded contexts. (Only applies to some API
                plans)
            domains: The domain names the ApiApp will be associated with.
            name: The name you want to assign to the ApiApp.
            oauth: OAuth related parameters.
            options: Additional options supported by API App.
            white_labeling_options: An array of elements and values serialized to a string, to be used to customize the
                app's signer page. (Only applies to some API plans) Take a look at our `white labeling guide
                <https://developers.hellosign.com/api/reference/premium-branding/>`__ to learn more.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.api_app_update(
                client_id,
                callback_url=callback_url,
                custom_logo_file=custom_logo_file,
                domains=domains,
                name=name,
                oauth=oauth,
                options=options,
                white_labeling_options=white_labeling_options,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncApiAppWithRawResponse:
        return self._with_raw_response


class ApiAppWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def api_app_create(
        self,
        domains: list[str],
        name: str,
        *,
        callback_url: str | None = None,
        custom_logo_file: FileInput | None = None,
        oauth: SubOauth | SubOauthDict | None = None,
        options: SubOptions | SubOptionsDict | None = None,
        white_labeling_options: SubWhiteLabelingOptions | SubWhiteLabelingOptionsDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiAppGetResponse, ApiAppCreateErrorBody]:
        """Creates a new API App.

        Args:
            domains: The domain names the ApiApp will be associated with.
            name: The name you want to assign to the ApiApp.
            callback_url: The URL at which the ApiApp should receive event callbacks.
            custom_logo_file: An image file to use as a custom logo in embedded contexts. (Only applies to some API
                plans)
            oauth: OAuth related parameters.
            options: Additional options supported by API App.
            white_labeling_options: An array of elements and values serialized to a string, to be used to customize the
                app's signer page. (Only applies to some API plans) Take a look at our `white labeling guide
                <https://developers.hellosign.com/api/reference/premium-branding/>`__ to learn more.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api_app"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(
                param[list[str]]("domains", domains),
                param[str]("name", name),
                param[str | None]("callback_url", callback_url),
                file_part("custom_logo_file", custom_logo_file) if custom_logo_file is not None else None,
                param[SubOauth | SubOauthDict | None]("oauth", oauth),
                param[SubOptions | SubOptionsDict | None]("options", options),
                param[SubWhiteLabelingOptions | SubWhiteLabelingOptionsDict | None](
                    "white_labeling_options", white_labeling_options
                ),
            ),
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[ApiAppGetResponse],
            error_mapper=api_app_create_error_mapper,
            request_options=request_options,
        )

    def api_app_delete(
        self, client_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, ApiAppDeleteErrorBody]:
        """Deletes an API App. Can only be invoked for apps you own.

        Args:
            client_id: The client id of the API App to delete.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/api_app/{client_id}"),
            path_params=[param[str]("client_id", client_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=empty_response,
            error_mapper=api_app_delete_error_mapper,
            request_options=request_options,
        )

    def api_app_get(
        self, client_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiAppGetResponse, ApiAppGetErrorBody]:
        """Returns an object with information about an API App.

        Args:
            client_id: The client id of the API App to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api_app/{client_id}"),
            path_params=[param[str]("client_id", client_id)],
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[ApiAppGetResponse],
            error_mapper=api_app_get_error_mapper,
            request_options=request_options,
        )

    def api_app_list(
        self, *, page: int | None = 1, page_size: int | None = 20, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiAppListResponse, ApiAppListErrorBody]:
        """Returns a list of API Apps that are accessible by you. If you are on a team with an Admin or Developer role,
        this list will include apps owned by teammates.

        Args:
            page: Which page number of the API App List to return. Defaults to ``1``.
            page_size: Number of objects to be returned per page. Must be between ``1`` and ``100``. Default is ``20``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api_app/list"),
            query_params=[param[int | None]("page", page), param[int | None]("page_size", page_size)],
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[ApiAppListResponse],
            error_mapper=api_app_list_error_mapper,
            request_options=request_options,
        )

    def api_app_update(
        self,
        client_id: str,
        *,
        callback_url: str | None = None,
        custom_logo_file: FileInput | None = None,
        domains: list[str] | None = None,
        name: str | None = None,
        oauth: SubOauth | SubOauthDict | None = None,
        options: SubOptions | SubOptionsDict | None = None,
        white_labeling_options: SubWhiteLabelingOptions | SubWhiteLabelingOptionsDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiAppGetResponse, ApiAppUpdateErrorBody]:
        """Updates an existing API App. Can only be invoked for apps you own. Only the fields you provide will be
        updated. If you wish to clear an existing optional field, provide an empty string.

        Args:
            client_id: The client id of the API App to update.
            callback_url: The URL at which the API App should receive event callbacks.
            custom_logo_file: An image file to use as a custom logo in embedded contexts. (Only applies to some API
                plans)
            domains: The domain names the ApiApp will be associated with.
            name: The name you want to assign to the ApiApp.
            oauth: OAuth related parameters.
            options: Additional options supported by API App.
            white_labeling_options: An array of elements and values serialized to a string, to be used to customize the
                app's signer page. (Only applies to some API plans) Take a look at our `white labeling guide
                <https://developers.hellosign.com/api/reference/premium-branding/>`__ to learn more.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/api_app/{client_id}"),
            path_params=[param[str]("client_id", client_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(
                param[str | None]("callback_url", callback_url),
                file_part("custom_logo_file", custom_logo_file) if custom_logo_file is not None else None,
                param[list[str] | None]("domains", domains),
                param[str | None]("name", name),
                param[SubOauth | SubOauthDict | None]("oauth", oauth),
                param[SubOptions | SubOptionsDict | None]("options", options),
                param[SubWhiteLabelingOptions | SubWhiteLabelingOptionsDict | None](
                    "white_labeling_options", white_labeling_options
                ),
            ),
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[ApiAppGetResponse],
            error_mapper=api_app_update_error_mapper,
            request_options=request_options,
        )


class AsyncApiAppWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def api_app_create(
        self,
        domains: list[str],
        name: str,
        *,
        callback_url: str | None = None,
        custom_logo_file: AsyncFileInput | None = None,
        oauth: SubOauth | SubOauthDict | None = None,
        options: SubOptions | SubOptionsDict | None = None,
        white_labeling_options: SubWhiteLabelingOptions | SubWhiteLabelingOptionsDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiAppGetResponse, ApiAppCreateErrorBody]:
        """Creates a new API App.

        Args:
            domains: The domain names the ApiApp will be associated with.
            name: The name you want to assign to the ApiApp.
            callback_url: The URL at which the ApiApp should receive event callbacks.
            custom_logo_file: An image file to use as a custom logo in embedded contexts. (Only applies to some API
                plans)
            oauth: OAuth related parameters.
            options: Additional options supported by API App.
            white_labeling_options: An array of elements and values serialized to a string, to be used to customize the
                app's signer page. (Only applies to some API plans) Take a look at our `white labeling guide
                <https://developers.hellosign.com/api/reference/premium-branding/>`__ to learn more.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api_app"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(
                param[list[str]]("domains", domains),
                param[str]("name", name),
                param[str | None]("callback_url", callback_url),
                file_part("custom_logo_file", custom_logo_file) if custom_logo_file is not None else None,
                param[SubOauth | SubOauthDict | None]("oauth", oauth),
                param[SubOptions | SubOptionsDict | None]("options", options),
                param[SubWhiteLabelingOptions | SubWhiteLabelingOptionsDict | None](
                    "white_labeling_options", white_labeling_options
                ),
            ),
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[ApiAppGetResponse],
            error_mapper=api_app_create_error_mapper,
            request_options=request_options,
        )

    async def api_app_delete(
        self, client_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, ApiAppDeleteErrorBody]:
        """Deletes an API App. Can only be invoked for apps you own.

        Args:
            client_id: The client id of the API App to delete.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/api_app/{client_id}"),
            path_params=[param[str]("client_id", client_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_empty_response,
            error_mapper=api_app_delete_error_mapper,
            request_options=request_options,
        )

    async def api_app_get(
        self, client_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiAppGetResponse, ApiAppGetErrorBody]:
        """Returns an object with information about an API App.

        Args:
            client_id: The client id of the API App to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api_app/{client_id}"),
            path_params=[param[str]("client_id", client_id)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[ApiAppGetResponse],
            error_mapper=api_app_get_error_mapper,
            request_options=request_options,
        )

    async def api_app_list(
        self, *, page: int | None = 1, page_size: int | None = 20, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiAppListResponse, ApiAppListErrorBody]:
        """Returns a list of API Apps that are accessible by you. If you are on a team with an Admin or Developer role,
        this list will include apps owned by teammates.

        Args:
            page: Which page number of the API App List to return. Defaults to ``1``.
            page_size: Number of objects to be returned per page. Must be between ``1`` and ``100``. Default is ``20``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api_app/list"),
            query_params=[param[int | None]("page", page), param[int | None]("page_size", page_size)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[ApiAppListResponse],
            error_mapper=api_app_list_error_mapper,
            request_options=request_options,
        )

    async def api_app_update(
        self,
        client_id: str,
        *,
        callback_url: str | None = None,
        custom_logo_file: AsyncFileInput | None = None,
        domains: list[str] | None = None,
        name: str | None = None,
        oauth: SubOauth | SubOauthDict | None = None,
        options: SubOptions | SubOptionsDict | None = None,
        white_labeling_options: SubWhiteLabelingOptions | SubWhiteLabelingOptionsDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiAppGetResponse, ApiAppUpdateErrorBody]:
        """Updates an existing API App. Can only be invoked for apps you own. Only the fields you provide will be
        updated. If you wish to clear an existing optional field, provide an empty string.

        Args:
            client_id: The client id of the API App to update.
            callback_url: The URL at which the API App should receive event callbacks.
            custom_logo_file: An image file to use as a custom logo in embedded contexts. (Only applies to some API
                plans)
            domains: The domain names the ApiApp will be associated with.
            name: The name you want to assign to the ApiApp.
            oauth: OAuth related parameters.
            options: Additional options supported by API App.
            white_labeling_options: An array of elements and values serialized to a string, to be used to customize the
                app's signer page. (Only applies to some API plans) Take a look at our `white labeling guide
                <https://developers.hellosign.com/api/reference/premium-branding/>`__ to learn more.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/api_app/{client_id}"),
            path_params=[param[str]("client_id", client_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(
                param[str | None]("callback_url", callback_url),
                file_part("custom_logo_file", custom_logo_file) if custom_logo_file is not None else None,
                param[list[str] | None]("domains", domains),
                param[str | None]("name", name),
                param[SubOauth | SubOauthDict | None]("oauth", oauth),
                param[SubOptions | SubOptionsDict | None]("options", options),
                param[SubWhiteLabelingOptions | SubWhiteLabelingOptionsDict | None](
                    "white_labeling_options", white_labeling_options
                ),
            ),
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[ApiAppGetResponse],
            error_mapper=api_app_update_error_mapper,
            request_options=request_options,
        )
