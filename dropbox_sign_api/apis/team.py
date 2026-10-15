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
    async_empty_response,
    async_json_decoder,
    empty_response,
    json_body,
    json_decoder,
    param,
    unwrap,
)
from ..errors.team_add_member_error import TeamAddMemberErrorBody, team_add_member_error_mapper
from ..errors.team_create_error import TeamCreateErrorBody, team_create_error_mapper
from ..errors.team_delete_error import TeamDeleteErrorBody, team_delete_error_mapper
from ..errors.team_get_error import TeamGetErrorBody, team_get_error_mapper
from ..errors.team_info_error import TeamInfoErrorBody, team_info_error_mapper
from ..errors.team_invites_error import TeamInvitesErrorBody, team_invites_error_mapper
from ..errors.team_members_error import TeamMembersErrorBody, team_members_error_mapper
from ..errors.team_remove_member_error import TeamRemoveMemberErrorBody, team_remove_member_error_mapper
from ..errors.team_sub_teams_error import TeamSubTeamsErrorBody, team_sub_teams_error_mapper
from ..errors.team_update_error import TeamUpdateErrorBody, team_update_error_mapper
from ..models.team_add_member_request import TeamAddMemberRequest, TeamAddMemberRequestDict
from ..models.team_create_request import TeamCreateRequest, TeamCreateRequestDict
from ..models.team_get_info_response import TeamGetInfoResponse
from ..models.team_get_response import TeamGetResponse
from ..models.team_invites_response import TeamInvitesResponse
from ..models.team_members_response import TeamMembersResponse
from ..models.team_remove_member_request import TeamRemoveMemberRequest, TeamRemoveMemberRequestDict
from ..models.team_sub_teams_response import TeamSubTeamsResponse
from ..models.team_update_request import TeamUpdateRequest, TeamUpdateRequestDict
from ..server.server import Server


class Team:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TeamWithRawResponse(client, server, auth)

    def team_add_member(
        self,
        body: TeamAddMemberRequest | TeamAddMemberRequestDict,
        *,
        team_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TeamGetResponse:
        """Invites a user (specified using the ``email_address`` parameter) to your Team. If the user does not currently
        have a Dropbox Sign Account, a new one will be created for them. If a user is already a part of another Team, a
        ``team_invite_failed`` error will be returned.

        Args:
            body: The request body.
            team_id: The id of the team.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(self._with_raw_response.team_add_member(body, team_id=team_id, request_options=request_options))

    def team_create(
        self, body: TeamCreateRequest | TeamCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> TeamGetResponse:
        """Creates a new Team and makes you a member. You must not currently belong to a Team to invoke.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(self._with_raw_response.team_create(body, request_options=request_options))

    def team_delete(self, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Deletes your Team. Can only be invoked when you have a Team with only one member (yourself).

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(self._with_raw_response.team_delete(request_options=request_options))

    def team_get(self, *, request_options: RequestOptionsOrDict | None = None) -> TeamGetResponse:
        """Returns information about your Team as well as a list of its members. If you do not belong to a Team, a 404
        error with an error_name of "not_found" will be returned.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(self._with_raw_response.team_get(request_options=request_options))

    def team_info(
        self, *, team_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> TeamGetInfoResponse:
        """Provides information about a team.

        Args:
            team_id: The id of the team.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(self._with_raw_response.team_info(team_id=team_id, request_options=request_options))

    def team_invites(
        self, *, email_address: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> TeamInvitesResponse:
        """Provides a list of team invites (and their roles).

        Args:
            email_address: The email address for which to display the team invites.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.team_invites(email_address=email_address, request_options=request_options)
        )

    def team_members(
        self,
        team_id: str,
        *,
        page: int | None = 1,
        page_size: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TeamMembersResponse:
        """Provides a paginated list of members (and their roles) that belong to a given team.

        Args:
            team_id: The id of the team that a member list is being requested from.
            page: Which page number of the team member list to return. Defaults to ``1``.
            page_size: Number of objects to be returned per page. Must be between ``1`` and ``100``. Default is ``20``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.team_members(
                team_id, page=page, page_size=page_size, request_options=request_options
            ),
        )

    def team_remove_member(
        self,
        body: TeamRemoveMemberRequest | TeamRemoveMemberRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TeamGetResponse:
        """Removes the provided user Account from your Team. If the Account had an outstanding invitation to your Team,
        the invitation will be expired. If you choose to transfer documents from the removed Account to an Account
        provided in the ``new_owner_email_address`` parameter (available only for Enterprise plans), the response status
        code will be 201, which indicates that your request has been queued but not fully executed.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(self._with_raw_response.team_remove_member(body, request_options=request_options))

    def team_sub_teams(
        self,
        team_id: str,
        *,
        page: int | None = 1,
        page_size: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TeamSubTeamsResponse:
        """Provides a paginated list of sub teams that belong to a given team.

        Args:
            team_id: The id of the parent Team.
            page: Which page number of the SubTeam List to return. Defaults to ``1``.
            page_size: Number of objects to be returned per page. Must be between ``1`` and ``100``. Default is ``20``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.team_sub_teams(
                team_id, page=page, page_size=page_size, request_options=request_options
            ),
        )

    def team_update(
        self, body: TeamUpdateRequest | TeamUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> TeamGetResponse:
        """Updates the name of your Team.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(self._with_raw_response.team_update(body, request_options=request_options))

    @property
    def with_raw_response(self) -> TeamWithRawResponse:
        return self._with_raw_response


class AsyncTeam:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTeamWithRawResponse(client, server, auth)

    async def team_add_member(
        self,
        body: TeamAddMemberRequest | TeamAddMemberRequestDict,
        *,
        team_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TeamGetResponse:
        """Invites a user (specified using the ``email_address`` parameter) to your Team. If the user does not currently
        have a Dropbox Sign Account, a new one will be created for them. If a user is already a part of another Team, a
        ``team_invite_failed`` error will be returned.

        Args:
            body: The request body.
            team_id: The id of the team.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.team_add_member(body, team_id=team_id, request_options=request_options)
        )

    async def team_create(
        self, body: TeamCreateRequest | TeamCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> TeamGetResponse:
        """Creates a new Team and makes you a member. You must not currently belong to a Team to invoke.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(await self._with_raw_response.team_create(body, request_options=request_options))

    async def team_delete(self, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Deletes your Team. Can only be invoked when you have a Team with only one member (yourself).

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(await self._with_raw_response.team_delete(request_options=request_options))

    async def team_get(self, *, request_options: RequestOptionsOrDict | None = None) -> TeamGetResponse:
        """Returns information about your Team as well as a list of its members. If you do not belong to a Team, a 404
        error with an error_name of "not_found" will be returned.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(await self._with_raw_response.team_get(request_options=request_options))

    async def team_info(
        self, *, team_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> TeamGetInfoResponse:
        """Provides information about a team.

        Args:
            team_id: The id of the team.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(await self._with_raw_response.team_info(team_id=team_id, request_options=request_options))

    async def team_invites(
        self, *, email_address: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> TeamInvitesResponse:
        """Provides a list of team invites (and their roles).

        Args:
            email_address: The email address for which to display the team invites.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.team_invites(email_address=email_address, request_options=request_options)
        )

    async def team_members(
        self,
        team_id: str,
        *,
        page: int | None = 1,
        page_size: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TeamMembersResponse:
        """Provides a paginated list of members (and their roles) that belong to a given team.

        Args:
            team_id: The id of the team that a member list is being requested from.
            page: Which page number of the team member list to return. Defaults to ``1``.
            page_size: Number of objects to be returned per page. Must be between ``1`` and ``100``. Default is ``20``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.team_members(
                team_id, page=page, page_size=page_size, request_options=request_options
            ),
        )

    async def team_remove_member(
        self,
        body: TeamRemoveMemberRequest | TeamRemoveMemberRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TeamGetResponse:
        """Removes the provided user Account from your Team. If the Account had an outstanding invitation to your Team,
        the invitation will be expired. If you choose to transfer documents from the removed Account to an Account
        provided in the ``new_owner_email_address`` parameter (available only for Enterprise plans), the response status
        code will be 201, which indicates that your request has been queued but not fully executed.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(await self._with_raw_response.team_remove_member(body, request_options=request_options))

    async def team_sub_teams(
        self,
        team_id: str,
        *,
        page: int | None = 1,
        page_size: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TeamSubTeamsResponse:
        """Provides a paginated list of sub teams that belong to a given team.

        Args:
            team_id: The id of the parent Team.
            page: Which page number of the SubTeam List to return. Defaults to ``1``.
            page_size: Number of objects to be returned per page. Must be between ``1`` and ``100``. Default is ``20``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.team_sub_teams(
                team_id, page=page, page_size=page_size, request_options=request_options
            ),
        )

    async def team_update(
        self, body: TeamUpdateRequest | TeamUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> TeamGetResponse:
        """Updates the name of your Team.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(await self._with_raw_response.team_update(body, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncTeamWithRawResponse:
        return self._with_raw_response


class TeamWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def team_add_member(
        self,
        body: TeamAddMemberRequest | TeamAddMemberRequestDict,
        *,
        team_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TeamGetResponse, TeamAddMemberErrorBody]:
        """Invites a user (specified using the ``email_address`` parameter) to your Team. If the user does not currently
        have a Dropbox Sign Account, a new one will be created for them. If a user is already a part of another Team, a
        ``team_invite_failed`` error will be returned.

        Args:
            body: The request body.
            team_id: The id of the team.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/team/add_member"),
            query_params=[param[str | None]("team_id", team_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TeamAddMemberRequest | TeamAddMemberRequestDict](body),
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[TeamGetResponse],
            error_mapper=team_add_member_error_mapper,
            request_options=request_options,
        )

    def team_create(
        self, body: TeamCreateRequest | TeamCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TeamGetResponse, TeamCreateErrorBody]:
        """Creates a new Team and makes you a member. You must not currently belong to a Team to invoke.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/team/create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TeamCreateRequest | TeamCreateRequestDict](body),
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[TeamGetResponse],
            error_mapper=team_create_error_mapper,
            request_options=request_options,
        )

    def team_delete(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, TeamDeleteErrorBody]:
        """Deletes your Team. Can only be invoked when you have a Team with only one member (yourself).

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/team/destroy"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=empty_response,
            error_mapper=team_delete_error_mapper,
            request_options=request_options,
        )

    def team_get(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TeamGetResponse, TeamGetErrorBody]:
        """Returns information about your Team as well as a list of its members. If you do not belong to a Team, a 404
        error with an error_name of "not_found" will be returned.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/team"),
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[TeamGetResponse],
            error_mapper=team_get_error_mapper,
            request_options=request_options,
        )

    def team_info(
        self, *, team_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TeamGetInfoResponse, TeamInfoErrorBody]:
        """Provides information about a team.

        Args:
            team_id: The id of the team.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/team/info"),
            query_params=[param[str | None]("team_id", team_id)],
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[TeamGetInfoResponse],
            error_mapper=team_info_error_mapper,
            request_options=request_options,
        )

    def team_invites(
        self, *, email_address: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TeamInvitesResponse, TeamInvitesErrorBody]:
        """Provides a list of team invites (and their roles).

        Args:
            email_address: The email address for which to display the team invites.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/team/invites"),
            query_params=[param[str | None]("email_address", email_address)],
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[TeamInvitesResponse],
            error_mapper=team_invites_error_mapper,
            request_options=request_options,
        )

    def team_members(
        self,
        team_id: str,
        *,
        page: int | None = 1,
        page_size: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TeamMembersResponse, TeamMembersErrorBody]:
        """Provides a paginated list of members (and their roles) that belong to a given team.

        Args:
            team_id: The id of the team that a member list is being requested from.
            page: Which page number of the team member list to return. Defaults to ``1``.
            page_size: Number of objects to be returned per page. Must be between ``1`` and ``100``. Default is ``20``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/team/members/{team_id}"),
            path_params=[param[str]("team_id", team_id)],
            query_params=[param[int | None]("page", page), param[int | None]("page_size", page_size)],
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[TeamMembersResponse],
            error_mapper=team_members_error_mapper,
            request_options=request_options,
        )

    def team_remove_member(
        self,
        body: TeamRemoveMemberRequest | TeamRemoveMemberRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TeamGetResponse, TeamRemoveMemberErrorBody]:
        """Removes the provided user Account from your Team. If the Account had an outstanding invitation to your Team,
        the invitation will be expired. If you choose to transfer documents from the removed Account to an Account
        provided in the ``new_owner_email_address`` parameter (available only for Enterprise plans), the response status
        code will be 201, which indicates that your request has been queued but not fully executed.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/team/remove_member"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TeamRemoveMemberRequest | TeamRemoveMemberRequestDict](body),
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[TeamGetResponse],
            error_mapper=team_remove_member_error_mapper,
            request_options=request_options,
        )

    def team_sub_teams(
        self,
        team_id: str,
        *,
        page: int | None = 1,
        page_size: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TeamSubTeamsResponse, TeamSubTeamsErrorBody]:
        """Provides a paginated list of sub teams that belong to a given team.

        Args:
            team_id: The id of the parent Team.
            page: Which page number of the SubTeam List to return. Defaults to ``1``.
            page_size: Number of objects to be returned per page. Must be between ``1`` and ``100``. Default is ``20``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/team/sub_teams/{team_id}"),
            path_params=[param[str]("team_id", team_id)],
            query_params=[param[int | None]("page", page), param[int | None]("page_size", page_size)],
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[TeamSubTeamsResponse],
            error_mapper=team_sub_teams_error_mapper,
            request_options=request_options,
        )

    def team_update(
        self, body: TeamUpdateRequest | TeamUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TeamGetResponse, TeamUpdateErrorBody]:
        """Updates the name of your Team.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/team"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TeamUpdateRequest | TeamUpdateRequestDict](body),
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[TeamGetResponse],
            error_mapper=team_update_error_mapper,
            request_options=request_options,
        )


class AsyncTeamWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def team_add_member(
        self,
        body: TeamAddMemberRequest | TeamAddMemberRequestDict,
        *,
        team_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TeamGetResponse, TeamAddMemberErrorBody]:
        """Invites a user (specified using the ``email_address`` parameter) to your Team. If the user does not currently
        have a Dropbox Sign Account, a new one will be created for them. If a user is already a part of another Team, a
        ``team_invite_failed`` error will be returned.

        Args:
            body: The request body.
            team_id: The id of the team.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/team/add_member"),
            query_params=[param[str | None]("team_id", team_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TeamAddMemberRequest | TeamAddMemberRequestDict](body),
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[TeamGetResponse],
            error_mapper=team_add_member_error_mapper,
            request_options=request_options,
        )

    async def team_create(
        self, body: TeamCreateRequest | TeamCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TeamGetResponse, TeamCreateErrorBody]:
        """Creates a new Team and makes you a member. You must not currently belong to a Team to invoke.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/team/create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TeamCreateRequest | TeamCreateRequestDict](body),
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[TeamGetResponse],
            error_mapper=team_create_error_mapper,
            request_options=request_options,
        )

    async def team_delete(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, TeamDeleteErrorBody]:
        """Deletes your Team. Can only be invoked when you have a Team with only one member (yourself).

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/team/destroy"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_empty_response,
            error_mapper=team_delete_error_mapper,
            request_options=request_options,
        )

    async def team_get(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TeamGetResponse, TeamGetErrorBody]:
        """Returns information about your Team as well as a list of its members. If you do not belong to a Team, a 404
        error with an error_name of "not_found" will be returned.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/team"),
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[TeamGetResponse],
            error_mapper=team_get_error_mapper,
            request_options=request_options,
        )

    async def team_info(
        self, *, team_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TeamGetInfoResponse, TeamInfoErrorBody]:
        """Provides information about a team.

        Args:
            team_id: The id of the team.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/team/info"),
            query_params=[param[str | None]("team_id", team_id)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[TeamGetInfoResponse],
            error_mapper=team_info_error_mapper,
            request_options=request_options,
        )

    async def team_invites(
        self, *, email_address: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TeamInvitesResponse, TeamInvitesErrorBody]:
        """Provides a list of team invites (and their roles).

        Args:
            email_address: The email address for which to display the team invites.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/team/invites"),
            query_params=[param[str | None]("email_address", email_address)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[TeamInvitesResponse],
            error_mapper=team_invites_error_mapper,
            request_options=request_options,
        )

    async def team_members(
        self,
        team_id: str,
        *,
        page: int | None = 1,
        page_size: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TeamMembersResponse, TeamMembersErrorBody]:
        """Provides a paginated list of members (and their roles) that belong to a given team.

        Args:
            team_id: The id of the team that a member list is being requested from.
            page: Which page number of the team member list to return. Defaults to ``1``.
            page_size: Number of objects to be returned per page. Must be between ``1`` and ``100``. Default is ``20``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/team/members/{team_id}"),
            path_params=[param[str]("team_id", team_id)],
            query_params=[param[int | None]("page", page), param[int | None]("page_size", page_size)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[TeamMembersResponse],
            error_mapper=team_members_error_mapper,
            request_options=request_options,
        )

    async def team_remove_member(
        self,
        body: TeamRemoveMemberRequest | TeamRemoveMemberRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TeamGetResponse, TeamRemoveMemberErrorBody]:
        """Removes the provided user Account from your Team. If the Account had an outstanding invitation to your Team,
        the invitation will be expired. If you choose to transfer documents from the removed Account to an Account
        provided in the ``new_owner_email_address`` parameter (available only for Enterprise plans), the response status
        code will be 201, which indicates that your request has been queued but not fully executed.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/team/remove_member"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TeamRemoveMemberRequest | TeamRemoveMemberRequestDict](body),
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[TeamGetResponse],
            error_mapper=team_remove_member_error_mapper,
            request_options=request_options,
        )

    async def team_sub_teams(
        self,
        team_id: str,
        *,
        page: int | None = 1,
        page_size: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TeamSubTeamsResponse, TeamSubTeamsErrorBody]:
        """Provides a paginated list of sub teams that belong to a given team.

        Args:
            team_id: The id of the parent Team.
            page: Which page number of the SubTeam List to return. Defaults to ``1``.
            page_size: Number of objects to be returned per page. Must be between ``1`` and ``100``. Default is ``20``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/team/sub_teams/{team_id}"),
            path_params=[param[str]("team_id", team_id)],
            query_params=[param[int | None]("page", page), param[int | None]("page_size", page_size)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[TeamSubTeamsResponse],
            error_mapper=team_sub_teams_error_mapper,
            request_options=request_options,
        )

    async def team_update(
        self, body: TeamUpdateRequest | TeamUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TeamGetResponse, TeamUpdateErrorBody]:
        """Updates the name of your Team.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/team"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TeamUpdateRequest | TeamUpdateRequestDict](body),
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[TeamGetResponse],
            error_mapper=team_update_error_mapper,
            request_options=request_options,
        )
