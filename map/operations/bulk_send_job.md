<!-- Generated file — do not edit; regenerated with the SDK. -->

# BulkSendJob — operations

Accessor: `client.bulk_send_job` · Source: `dropbox_sign_api/apis/bulk_send_job.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.bulk_send_job.bulk_send_job_get

- **Route**: `GET /bulk_send_job/{bulk_send_job_id}`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def bulk_send_job_get(bulk_send_job_id: str, *, page: int | None = 1, page_size: int | None = 20, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `bulk_send_job_id`
- **Params**: `bulk_send_job_id` — path · `page` — query · `page_size` — query
- **Returns (parsed)**: `BulkSendJobGetResponse`
- **Returns (raw)**: `ApiResult[BulkSendJobGetResponse, BulkSendJobGetErrorBody]`
- **Error**: `BulkSendJobGetErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `BulkSendJobGetResponse` | `dropbox_sign_api/models/bulk_send_job_get_response.py` |
| `BulkSendJobGetErrorBody` | `dropbox_sign_api/errors/bulk_send_job_get_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.bulk_send_job.bulk_send_job_list

- **Route**: `GET /bulk_send_job/list`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def bulk_send_job_list(*, page: int | None = 1, page_size: int | None = 20, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page` — query · `page_size` — query
- **Returns (parsed)**: `BulkSendJobListResponse`
- **Returns (raw)**: `ApiResult[BulkSendJobListResponse, BulkSendJobListErrorBody]`
- **Error**: `BulkSendJobListErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `BulkSendJobListResponse` | `dropbox_sign_api/models/bulk_send_job_list_response.py` |
| `BulkSendJobListErrorBody` | `dropbox_sign_api/errors/bulk_send_job_list_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

