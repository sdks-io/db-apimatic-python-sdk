<!-- Generated file — do not edit; regenerated with the SDK. -->

# FaxLine — operations

Accessor: `client.fax_line` · Source: `dropbox_sign_api/apis/fax_line.py` · 7 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.fax_line.fax_line_add_user

- **Route**: `PUT /fax_line/add_user`
- **Auth**: `api_key`
- **Signature**: `def fax_line_add_user(body: FaxLineAddUserRequest | FaxLineAddUserRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `FaxLineResponse`
- **Returns (raw)**: `ApiResult[FaxLineResponse, FaxLineAddUserErrorBody]`
- **Error**: `FaxLineAddUserErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FaxLineAddUserRequest` | `dropbox_sign_api/models/fax_line_add_user_request.py` |
| `FaxLineAddUserRequestDict` | `dropbox_sign_api/models/fax_line_add_user_request.py` |
| `FaxLineResponse` | `dropbox_sign_api/models/fax_line_response.py` |
| `FaxLineAddUserErrorBody` | `dropbox_sign_api/errors/fax_line_add_user_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.fax_line.fax_line_area_code_get

- **Route**: `GET /fax_line/area_codes`
- **Auth**: `api_key`
- **Signature**: `def fax_line_area_code_get(country: FaxLineAreaCodeGetCountryEnumOrStr, *, state: FaxLineAreaCodeGetStateEnumOrStr | None = None, province: FaxLineAreaCodeGetProvinceEnumOrStr | None = None, city: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `country`
- **Params**: `country` — query · `state` — query · `province` — query · `city` — query
- **Returns (parsed)**: `FaxLineAreaCodeGetResponse`
- **Returns (raw)**: `ApiResult[FaxLineAreaCodeGetResponse, FaxLineAreaCodeGetErrorBody]`
- **Error**: `FaxLineAreaCodeGetErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FaxLineAreaCodeGetCountryEnumOrStr` | `dropbox_sign_api/models/enums/fax_line_area_code_get_country_enum.py` |
| `FaxLineAreaCodeGetStateEnumOrStr` | `dropbox_sign_api/models/enums/fax_line_area_code_get_state_enum.py` |
| `FaxLineAreaCodeGetProvinceEnumOrStr` | `dropbox_sign_api/models/enums/fax_line_area_code_get_province_enum.py` |
| `FaxLineAreaCodeGetResponse` | `dropbox_sign_api/models/fax_line_area_code_get_response.py` |
| `FaxLineAreaCodeGetErrorBody` | `dropbox_sign_api/errors/fax_line_area_code_get_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.fax_line.fax_line_create

- **Route**: `POST /fax_line/create`
- **Auth**: `api_key`
- **Signature**: `def fax_line_create(body: FaxLineCreateRequest | FaxLineCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `FaxLineResponse`
- **Returns (raw)**: `ApiResult[FaxLineResponse, FaxLineCreateErrorBody]`
- **Error**: `FaxLineCreateErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FaxLineCreateRequest` | `dropbox_sign_api/models/fax_line_create_request.py` |
| `FaxLineCreateRequestDict` | `dropbox_sign_api/models/fax_line_create_request.py` |
| `FaxLineResponse` | `dropbox_sign_api/models/fax_line_response.py` |
| `FaxLineCreateErrorBody` | `dropbox_sign_api/errors/fax_line_create_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.fax_line.fax_line_delete

- **Route**: `DELETE /fax_line`
- **Auth**: `api_key`
- **Signature**: `def fax_line_delete(body: FaxLineDeleteRequest | FaxLineDeleteRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, FaxLineDeleteErrorBody]`
- **Error**: `FaxLineDeleteErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FaxLineDeleteRequest` | `dropbox_sign_api/models/fax_line_delete_request.py` |
| `FaxLineDeleteRequestDict` | `dropbox_sign_api/models/fax_line_delete_request.py` |
| `FaxLineDeleteErrorBody` | `dropbox_sign_api/errors/fax_line_delete_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.fax_line.fax_line_get

- **Route**: `GET /fax_line`
- **Auth**: `api_key`
- **Signature**: `def fax_line_get(number: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `number`
- **Params**: `number` — query
- **Returns (parsed)**: `FaxLineResponse`
- **Returns (raw)**: `ApiResult[FaxLineResponse, FaxLineGetErrorBody]`
- **Error**: `FaxLineGetErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FaxLineResponse` | `dropbox_sign_api/models/fax_line_response.py` |
| `FaxLineGetErrorBody` | `dropbox_sign_api/errors/fax_line_get_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.fax_line.fax_line_list

- **Route**: `GET /fax_line/list`
- **Auth**: `api_key`
- **Signature**: `def fax_line_list(*, account_id: str | None = None, page: int | None = 1, page_size: int | None = 20, show_team_lines: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `account_id` — query · `page` — query · `page_size` — query · `show_team_lines` — query
- **Returns (parsed)**: `FaxLineListResponse`
- **Returns (raw)**: `ApiResult[FaxLineListResponse, FaxLineListErrorBody]`
- **Error**: `FaxLineListErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FaxLineListResponse` | `dropbox_sign_api/models/fax_line_list_response.py` |
| `FaxLineListErrorBody` | `dropbox_sign_api/errors/fax_line_list_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.fax_line.fax_line_remove_user

- **Route**: `PUT /fax_line/remove_user`
- **Auth**: `api_key`
- **Signature**: `def fax_line_remove_user(body: FaxLineRemoveUserRequest | FaxLineRemoveUserRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `FaxLineResponse`
- **Returns (raw)**: `ApiResult[FaxLineResponse, FaxLineRemoveUserErrorBody]`
- **Error**: `FaxLineRemoveUserErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FaxLineRemoveUserRequest` | `dropbox_sign_api/models/fax_line_remove_user_request.py` |
| `FaxLineRemoveUserRequestDict` | `dropbox_sign_api/models/fax_line_remove_user_request.py` |
| `FaxLineResponse` | `dropbox_sign_api/models/fax_line_response.py` |
| `FaxLineRemoveUserErrorBody` | `dropbox_sign_api/errors/fax_line_remove_user_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

