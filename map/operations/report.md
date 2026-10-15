<!-- Generated file — do not edit; regenerated with the SDK. -->

# Report — operations

Accessor: `client.report` · Source: `dropbox_sign_api/apis/report.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.report.report_create

- **Route**: `POST /report/create`
- **Auth**: `api_key`
- **Signature**: `def report_create(body: ReportCreateRequest | ReportCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ReportCreateResponse`
- **Returns (raw)**: `ApiResult[ReportCreateResponse, ReportCreateErrorBody]`
- **Error**: `ReportCreateErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ReportCreateRequest` | `dropbox_sign_api/models/report_create_request.py` |
| `ReportCreateRequestDict` | `dropbox_sign_api/models/report_create_request.py` |
| `ReportCreateResponse` | `dropbox_sign_api/models/report_create_response.py` |
| `ReportCreateErrorBody` | `dropbox_sign_api/errors/report_create_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

