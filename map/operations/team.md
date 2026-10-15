<!-- Generated file — do not edit; regenerated with the SDK. -->

# Team — operations

Accessor: `client.team` · Source: `dropbox_sign_api/apis/team.py` · 10 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.team.team_add_member

- **Route**: `PUT /team/add_member`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def team_add_member(body: TeamAddMemberRequest | TeamAddMemberRequestDict, *, team_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `team_id` — query · `body` — JSON body
- **Returns (parsed)**: `TeamGetResponse`
- **Returns (raw)**: `ApiResult[TeamGetResponse, TeamAddMemberErrorBody]`
- **Error**: `TeamAddMemberErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TeamAddMemberRequest` | `dropbox_sign_api/models/team_add_member_request.py` |
| `TeamAddMemberRequestDict` | `dropbox_sign_api/models/team_add_member_request.py` |
| `TeamGetResponse` | `dropbox_sign_api/models/team_get_response.py` |
| `TeamAddMemberErrorBody` | `dropbox_sign_api/errors/team_add_member_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.team.team_create

- **Route**: `POST /team/create`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def team_create(body: TeamCreateRequest | TeamCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TeamGetResponse`
- **Returns (raw)**: `ApiResult[TeamGetResponse, TeamCreateErrorBody]`
- **Error**: `TeamCreateErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TeamCreateRequest` | `dropbox_sign_api/models/team_create_request.py` |
| `TeamCreateRequestDict` | `dropbox_sign_api/models/team_create_request.py` |
| `TeamGetResponse` | `dropbox_sign_api/models/team_get_response.py` |
| `TeamCreateErrorBody` | `dropbox_sign_api/errors/team_create_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.team.team_delete

- **Route**: `DELETE /team/destroy`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def team_delete(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, TeamDeleteErrorBody]`
- **Error**: `TeamDeleteErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TeamDeleteErrorBody` | `dropbox_sign_api/errors/team_delete_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.team.team_get

- **Route**: `GET /team`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def team_get(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `TeamGetResponse`
- **Returns (raw)**: `ApiResult[TeamGetResponse, TeamGetErrorBody]`
- **Error**: `TeamGetErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TeamGetResponse` | `dropbox_sign_api/models/team_get_response.py` |
| `TeamGetErrorBody` | `dropbox_sign_api/errors/team_get_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.team.team_info

- **Route**: `GET /team/info`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def team_info(*, team_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `team_id` — query
- **Returns (parsed)**: `TeamGetInfoResponse`
- **Returns (raw)**: `ApiResult[TeamGetInfoResponse, TeamInfoErrorBody]`
- **Error**: `TeamInfoErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TeamGetInfoResponse` | `dropbox_sign_api/models/team_get_info_response.py` |
| `TeamInfoErrorBody` | `dropbox_sign_api/errors/team_info_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.team.team_invites

- **Route**: `GET /team/invites`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def team_invites(*, email_address: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `email_address` — query
- **Returns (parsed)**: `TeamInvitesResponse`
- **Returns (raw)**: `ApiResult[TeamInvitesResponse, TeamInvitesErrorBody]`
- **Error**: `TeamInvitesErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TeamInvitesResponse` | `dropbox_sign_api/models/team_invites_response.py` |
| `TeamInvitesErrorBody` | `dropbox_sign_api/errors/team_invites_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.team.team_members

- **Route**: `GET /team/members/{team_id}`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def team_members(team_id: str, *, page: int | None = 1, page_size: int | None = 20, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `team_id`
- **Params**: `team_id` — path · `page` — query · `page_size` — query
- **Returns (parsed)**: `TeamMembersResponse`
- **Returns (raw)**: `ApiResult[TeamMembersResponse, TeamMembersErrorBody]`
- **Error**: `TeamMembersErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TeamMembersResponse` | `dropbox_sign_api/models/team_members_response.py` |
| `TeamMembersErrorBody` | `dropbox_sign_api/errors/team_members_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.team.team_remove_member

- **Route**: `POST /team/remove_member`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def team_remove_member(body: TeamRemoveMemberRequest | TeamRemoveMemberRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TeamGetResponse`
- **Returns (raw)**: `ApiResult[TeamGetResponse, TeamRemoveMemberErrorBody]`
- **Error**: `TeamRemoveMemberErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TeamRemoveMemberRequest` | `dropbox_sign_api/models/team_remove_member_request.py` |
| `TeamRemoveMemberRequestDict` | `dropbox_sign_api/models/team_remove_member_request.py` |
| `TeamGetResponse` | `dropbox_sign_api/models/team_get_response.py` |
| `TeamRemoveMemberErrorBody` | `dropbox_sign_api/errors/team_remove_member_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.team.team_sub_teams

- **Route**: `GET /team/sub_teams/{team_id}`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def team_sub_teams(team_id: str, *, page: int | None = 1, page_size: int | None = 20, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `team_id`
- **Params**: `team_id` — path · `page` — query · `page_size` — query
- **Returns (parsed)**: `TeamSubTeamsResponse`
- **Returns (raw)**: `ApiResult[TeamSubTeamsResponse, TeamSubTeamsErrorBody]`
- **Error**: `TeamSubTeamsErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TeamSubTeamsResponse` | `dropbox_sign_api/models/team_sub_teams_response.py` |
| `TeamSubTeamsErrorBody` | `dropbox_sign_api/errors/team_sub_teams_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.team.team_update

- **Route**: `PUT /team`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def team_update(body: TeamUpdateRequest | TeamUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TeamGetResponse`
- **Returns (raw)**: `ApiResult[TeamGetResponse, TeamUpdateErrorBody]`
- **Error**: `TeamUpdateErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TeamUpdateRequest` | `dropbox_sign_api/models/team_update_request.py` |
| `TeamUpdateRequestDict` | `dropbox_sign_api/models/team_update_request.py` |
| `TeamGetResponse` | `dropbox_sign_api/models/team_get_response.py` |
| `TeamUpdateErrorBody` | `dropbox_sign_api/errors/team_update_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

