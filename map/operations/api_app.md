<!-- Generated file — do not edit; regenerated with the SDK. -->

# ApiApp — operations

Accessor: `client.api_app` · Source: `dropbox_sign_api/apis/api_app.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.api_app.api_app_create

- **Route**: `POST /api_app`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def api_app_create(domains: list[str], name: str, *, callback_url: str | None = None, custom_logo_file: FileInput | None = None, oauth: SubOauth | SubOauthDict | None = None, options: SubOptions | SubOptionsDict | None = None, white_labeling_options: SubWhiteLabelingOptions | SubWhiteLabelingOptionsDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `domains`, `name`
- **Params**: `domains` — multipart field · `name` — multipart field · `callback_url` — multipart field · `custom_logo_file` — multipart file · `oauth` — multipart field · `options` — multipart field · `white_labeling_options` — multipart field
- **Returns (parsed)**: `ApiAppGetResponse`
- **Returns (raw)**: `ApiResult[ApiAppGetResponse, ApiAppCreateErrorBody]`
- **Error**: `ApiAppCreateErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SubOauth` | `dropbox_sign_api/models/sub_oauth.py` |
| `SubOauthDict` | `dropbox_sign_api/models/sub_oauth.py` |
| `SubOptions` | `dropbox_sign_api/models/sub_options.py` |
| `SubOptionsDict` | `dropbox_sign_api/models/sub_options.py` |
| `SubWhiteLabelingOptions` | `dropbox_sign_api/models/sub_white_labeling_options.py` |
| `SubWhiteLabelingOptionsDict` | `dropbox_sign_api/models/sub_white_labeling_options.py` |
| `ApiAppGetResponse` | `dropbox_sign_api/models/api_app_get_response.py` |
| `ApiAppCreateErrorBody` | `dropbox_sign_api/errors/api_app_create_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.api_app.api_app_delete

- **Route**: `DELETE /api_app/{client_id}`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def api_app_delete(client_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `client_id`
- **Params**: `client_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, ApiAppDeleteErrorBody]`
- **Error**: `ApiAppDeleteErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ApiAppDeleteErrorBody` | `dropbox_sign_api/errors/api_app_delete_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.api_app.api_app_get

- **Route**: `GET /api_app/{client_id}`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def api_app_get(client_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `client_id`
- **Params**: `client_id` — path
- **Returns (parsed)**: `ApiAppGetResponse`
- **Returns (raw)**: `ApiResult[ApiAppGetResponse, ApiAppGetErrorBody]`
- **Error**: `ApiAppGetErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ApiAppGetResponse` | `dropbox_sign_api/models/api_app_get_response.py` |
| `ApiAppGetErrorBody` | `dropbox_sign_api/errors/api_app_get_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.api_app.api_app_list

- **Route**: `GET /api_app/list`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def api_app_list(*, page: int | None = 1, page_size: int | None = 20, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page` — query · `page_size` — query
- **Returns (parsed)**: `ApiAppListResponse`
- **Returns (raw)**: `ApiResult[ApiAppListResponse, ApiAppListErrorBody]`
- **Error**: `ApiAppListErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ApiAppListResponse` | `dropbox_sign_api/models/api_app_list_response.py` |
| `ApiAppListErrorBody` | `dropbox_sign_api/errors/api_app_list_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.api_app.api_app_update

- **Route**: `PUT /api_app/{client_id}`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def api_app_update(client_id: str, *, callback_url: str | None = None, custom_logo_file: FileInput | None = None, domains: list[str] | None = None, name: str | None = None, oauth: SubOauth | SubOauthDict | None = None, options: SubOptions | SubOptionsDict | None = None, white_labeling_options: SubWhiteLabelingOptions | SubWhiteLabelingOptionsDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `client_id`
- **Params**: `client_id` — path · `callback_url` — multipart field · `custom_logo_file` — multipart file · `domains` — multipart field · `name` — multipart field · `oauth` — multipart field · `options` — multipart field · `white_labeling_options` — multipart field
- **Returns (parsed)**: `ApiAppGetResponse`
- **Returns (raw)**: `ApiResult[ApiAppGetResponse, ApiAppUpdateErrorBody]`
- **Error**: `ApiAppUpdateErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SubOauth` | `dropbox_sign_api/models/sub_oauth.py` |
| `SubOauthDict` | `dropbox_sign_api/models/sub_oauth.py` |
| `SubOptions` | `dropbox_sign_api/models/sub_options.py` |
| `SubOptionsDict` | `dropbox_sign_api/models/sub_options.py` |
| `SubWhiteLabelingOptions` | `dropbox_sign_api/models/sub_white_labeling_options.py` |
| `SubWhiteLabelingOptionsDict` | `dropbox_sign_api/models/sub_white_labeling_options.py` |
| `ApiAppGetResponse` | `dropbox_sign_api/models/api_app_get_response.py` |
| `ApiAppUpdateErrorBody` | `dropbox_sign_api/errors/api_app_update_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

