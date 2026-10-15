# Raw Reference

**Raw** endpoints, reached through `with_raw_response`, return `ApiResult[T, E]` and never raise for an API error. For the parsed endpoints, see [API Reference](api-reference.md).

> Source: [DropboxSignApiClient](dropbox_sign_api/client.py)

## Account

> Source: [Account](dropbox_sign_api/apis/account.py)

<details>
<summary><code>def account_create(body: AccountCreateRequest | AccountCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AccountCreateResponse, AccountCreateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a new Dropbox Sign Account that is associated with the specified `email_address`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.account.with_raw_response.account_create(AccountCreateRequest(email_address="user@example.com"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AccountCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type AccountCreateErrorBody
```

**Async**

```python
result = await async_client.account.with_raw_response.account_create(
    AccountCreateRequest(email_address="user@example.com")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AccountCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type AccountCreateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[AccountCreateRequest](dropbox_sign_api/models/account_create_request.py) \| [AccountCreateRequestDict](dropbox_sign_api/models/account_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[AccountCreateResponse](dropbox_sign_api/models/account_create_response.py), [AccountCreateErrorBody](dropbox_sign_api/errors/account_create_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[AccountCreateResponse](dropbox_sign_api/models/account_create_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[AccountCreateErrorBody](dropbox_sign_api/errors/account_create_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def account_get(*, account_id: str | None = None, email_address: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AccountGetResponse, AccountGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the properties and settings of your Account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.account.with_raw_response.account_get()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AccountGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type AccountGetErrorBody
```

**Async**

```python
result = await async_client.account.with_raw_response.account_get()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AccountGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type AccountGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account_id</code> | <code>str \| None</code> | `account_id` or `email_address` is required. If both are provided, the account id prevails.<br><br>The ID of the Account.<br>**Default**: <code>None</code> |
| <code>email_address</code> | <code>str \| None</code> | `account_id` or `email_address` is required, If both are provided, the account id prevails.<br><br>The email address of the Account.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[AccountGetResponse](dropbox_sign_api/models/account_get_response.py), [AccountGetErrorBody](dropbox_sign_api/errors/account_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[AccountGetResponse](dropbox_sign_api/models/account_get_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[AccountGetErrorBody](dropbox_sign_api/errors/account_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def account_update(body: AccountUpdateRequest | AccountUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AccountGetResponse, AccountUpdateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates the properties and settings of your Account. Currently only allows for updates to the [Callback URL](/api/reference/tag/Callbacks-and-Events) and locale.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.account.with_raw_response.account_update(AccountUpdateRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AccountGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type AccountUpdateErrorBody
```

**Async**

```python
result = await async_client.account.with_raw_response.account_update(AccountUpdateRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AccountGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type AccountUpdateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[AccountUpdateRequest](dropbox_sign_api/models/account_update_request.py) \| [AccountUpdateRequestDict](dropbox_sign_api/models/account_update_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[AccountGetResponse](dropbox_sign_api/models/account_get_response.py), [AccountUpdateErrorBody](dropbox_sign_api/errors/account_update_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[AccountGetResponse](dropbox_sign_api/models/account_get_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[AccountUpdateErrorBody](dropbox_sign_api/errors/account_update_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def account_verify(body: AccountVerifyRequest | AccountVerifyRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AccountVerifyResponse, AccountVerifyErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Verifies whether an Dropbox Sign Account exists for the given email address.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.account.with_raw_response.account_verify(AccountVerifyRequest(email_address="user@example.com"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AccountVerifyResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type AccountVerifyErrorBody
```

**Async**

```python
result = await async_client.account.with_raw_response.account_verify(
    AccountVerifyRequest(email_address="user@example.com")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AccountVerifyResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type AccountVerifyErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[AccountVerifyRequest](dropbox_sign_api/models/account_verify_request.py) \| [AccountVerifyRequestDict](dropbox_sign_api/models/account_verify_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[AccountVerifyResponse](dropbox_sign_api/models/account_verify_response.py), [AccountVerifyErrorBody](dropbox_sign_api/errors/account_verify_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[AccountVerifyResponse](dropbox_sign_api/models/account_verify_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[AccountVerifyErrorBody](dropbox_sign_api/errors/account_verify_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## ApiApp

> Source: [ApiApp](dropbox_sign_api/apis/api_app.py)

<details>
<summary><code>def api_app_create(domains: list[str], name: str, *, callback_url: str | None = None, custom_logo_file: FileInput | None = None, oauth: SubOauth | SubOauthDict | None = None, options: SubOptions | SubOptionsDict | None = None, white_labeling_options: SubWhiteLabelingOptions | SubWhiteLabelingOptionsDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ApiAppGetResponse, ApiAppCreateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a new API App.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.api_app.with_raw_response.api_app_create(["some example string"], "some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ApiAppGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ApiAppCreateErrorBody
```

**Async**

```python
result = await async_client.api_app.with_raw_response.api_app_create(["some example string"], "some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ApiAppGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ApiAppCreateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>domains</code> | <code>list&#91;str&#93;</code> | The domain names the ApiApp will be associated with. |
| <code>name</code> | <code>str</code> | The name you want to assign to the ApiApp. |
| <code>callback_url</code> | <code>str \| None</code> | The URL at which the ApiApp should receive event callbacks.<br>**Default**: <code>None</code> |
| <code>custom_logo_file</code> | <code>FileInput \| None</code> | An image file to use as a custom logo in embedded contexts. (Only applies to some API plans)<br>**Default**: <code>None</code> |
| <code>oauth</code> | <code>[SubOauth](dropbox_sign_api/models/sub_oauth.py) \| [SubOauthDict](dropbox_sign_api/models/sub_oauth.py) \| None</code> | OAuth related parameters.<br>**Default**: <code>None</code> |
| <code>options</code> | <code>[SubOptions](dropbox_sign_api/models/sub_options.py) \| [SubOptionsDict](dropbox_sign_api/models/sub_options.py) \| None</code> | Additional options supported by API App.<br>**Default**: <code>None</code> |
| <code>white_labeling_options</code> | <code>[SubWhiteLabelingOptions](dropbox_sign_api/models/sub_white_labeling_options.py) \| [SubWhiteLabelingOptionsDict](dropbox_sign_api/models/sub_white_labeling_options.py) \| None</code> | An array of elements and values serialized to a string, to be used to customize the app's signer page. (Only applies to some API plans)<br><br>Take a look at our [white labeling guide](https://developers.hellosign.com/api/reference/premium-branding/) to learn more.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[ApiAppGetResponse](dropbox_sign_api/models/api_app_get_response.py), [ApiAppCreateErrorBody](dropbox_sign_api/errors/api_app_create_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ApiAppGetResponse](dropbox_sign_api/models/api_app_get_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[ApiAppCreateErrorBody](dropbox_sign_api/errors/api_app_create_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def api_app_delete(client_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, ApiAppDeleteErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes an API App. Can only be invoked for apps you own.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.api_app.with_raw_response.api_app_delete("0dd3b823a682527788c4e40cb7b6f7e9")
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ApiAppDeleteErrorBody
```

**Async**

```python
result = await async_client.api_app.with_raw_response.api_app_delete("0dd3b823a682527788c4e40cb7b6f7e9")
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ApiAppDeleteErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>client_id</code> | <code>str</code> | The client id of the API App to delete. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;None, [ApiAppDeleteErrorBody](dropbox_sign_api/errors/api_app_delete_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[ApiAppDeleteErrorBody](dropbox_sign_api/errors/api_app_delete_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def api_app_get(client_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ApiAppGetResponse, ApiAppGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns an object with information about an API App.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.api_app.with_raw_response.api_app_get("0dd3b823a682527788c4e40cb7b6f7e9")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ApiAppGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ApiAppGetErrorBody
```

**Async**

```python
result = await async_client.api_app.with_raw_response.api_app_get("0dd3b823a682527788c4e40cb7b6f7e9")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ApiAppGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ApiAppGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>client_id</code> | <code>str</code> | The client id of the API App to retrieve. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[ApiAppGetResponse](dropbox_sign_api/models/api_app_get_response.py), [ApiAppGetErrorBody](dropbox_sign_api/errors/api_app_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ApiAppGetResponse](dropbox_sign_api/models/api_app_get_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[ApiAppGetErrorBody](dropbox_sign_api/errors/api_app_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def api_app_list(*, page: int | None = 1, page_size: int | None = 20, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ApiAppListResponse, ApiAppListErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a list of API Apps that are accessible by you. If you are on a team with an Admin or Developer role, this list will include apps owned by teammates.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.api_app.with_raw_response.api_app_list()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ApiAppListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ApiAppListErrorBody
```

**Async**

```python
result = await async_client.api_app.with_raw_response.api_app_list()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ApiAppListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ApiAppListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>page</code> | <code>int \| None</code> | Which page number of the API App List to return. Defaults to `1`.<br>**Default**: <code>1</code> |
| <code>page_size</code> | <code>int \| None</code> | Number of objects to be returned per page. Must be between `1` and `100`. Default is `20`.<br>**Default**: <code>20</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[ApiAppListResponse](dropbox_sign_api/models/api_app_list_response.py), [ApiAppListErrorBody](dropbox_sign_api/errors/api_app_list_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ApiAppListResponse](dropbox_sign_api/models/api_app_list_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[ApiAppListErrorBody](dropbox_sign_api/errors/api_app_list_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def api_app_update(client_id: str, *, callback_url: str | None = None, custom_logo_file: FileInput | None = None, domains: list[str] | None = None, name: str | None = None, oauth: SubOauth | SubOauthDict | None = None, options: SubOptions | SubOptionsDict | None = None, white_labeling_options: SubWhiteLabelingOptions | SubWhiteLabelingOptionsDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ApiAppGetResponse, ApiAppUpdateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates an existing API App. Can only be invoked for apps you own. Only the fields you provide will be updated. If you wish to clear an existing optional field, provide an empty string.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.api_app.with_raw_response.api_app_update("0dd3b823a682527788c4e40cb7b6f7e9")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ApiAppGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ApiAppUpdateErrorBody
```

**Async**

```python
result = await async_client.api_app.with_raw_response.api_app_update("0dd3b823a682527788c4e40cb7b6f7e9")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ApiAppGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ApiAppUpdateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>client_id</code> | <code>str</code> | The client id of the API App to update. |
| <code>callback_url</code> | <code>str \| None</code> | The URL at which the API App should receive event callbacks.<br>**Default**: <code>None</code> |
| <code>custom_logo_file</code> | <code>FileInput \| None</code> | An image file to use as a custom logo in embedded contexts. (Only applies to some API plans)<br>**Default**: <code>None</code> |
| <code>domains</code> | <code>list&#91;str&#93; \| None</code> | The domain names the ApiApp will be associated with.<br>**Default**: <code>None</code> |
| <code>name</code> | <code>str \| None</code> | The name you want to assign to the ApiApp.<br>**Default**: <code>None</code> |
| <code>oauth</code> | <code>[SubOauth](dropbox_sign_api/models/sub_oauth.py) \| [SubOauthDict](dropbox_sign_api/models/sub_oauth.py) \| None</code> | OAuth related parameters.<br>**Default**: <code>None</code> |
| <code>options</code> | <code>[SubOptions](dropbox_sign_api/models/sub_options.py) \| [SubOptionsDict](dropbox_sign_api/models/sub_options.py) \| None</code> | Additional options supported by API App.<br>**Default**: <code>None</code> |
| <code>white_labeling_options</code> | <code>[SubWhiteLabelingOptions](dropbox_sign_api/models/sub_white_labeling_options.py) \| [SubWhiteLabelingOptionsDict](dropbox_sign_api/models/sub_white_labeling_options.py) \| None</code> | An array of elements and values serialized to a string, to be used to customize the app's signer page. (Only applies to some API plans)<br><br>Take a look at our [white labeling guide](https://developers.hellosign.com/api/reference/premium-branding/) to learn more.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[ApiAppGetResponse](dropbox_sign_api/models/api_app_get_response.py), [ApiAppUpdateErrorBody](dropbox_sign_api/errors/api_app_update_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ApiAppGetResponse](dropbox_sign_api/models/api_app_get_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[ApiAppUpdateErrorBody](dropbox_sign_api/errors/api_app_update_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## BulkSendJob

> Source: [BulkSendJob](dropbox_sign_api/apis/bulk_send_job.py)

<details>
<summary><code>def bulk_send_job_get(bulk_send_job_id: str, *, page: int | None = 1, page_size: int | None = 20, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BulkSendJobGetResponse, BulkSendJobGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the status of the BulkSendJob and its SignatureRequests specified by the `bulk_send_job_id` parameter.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.bulk_send_job.with_raw_response.bulk_send_job_get("6e683bc0369ba3d5b6f43c2c22a8031dbf6bd174")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkSendJobGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type BulkSendJobGetErrorBody
```

**Async**

```python
result = await async_client.bulk_send_job.with_raw_response.bulk_send_job_get(
    "6e683bc0369ba3d5b6f43c2c22a8031dbf6bd174"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkSendJobGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type BulkSendJobGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>bulk_send_job_id</code> | <code>str</code> | The id of the BulkSendJob to retrieve. |
| <code>page</code> | <code>int \| None</code> | Which page number of the BulkSendJob list to return. Defaults to `1`.<br>**Default**: <code>1</code> |
| <code>page_size</code> | <code>int \| None</code> | Number of objects to be returned per page. Must be between `1` and `100`. Default is 20.<br>**Default**: <code>20</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[BulkSendJobGetResponse](dropbox_sign_api/models/bulk_send_job_get_response.py), [BulkSendJobGetErrorBody](dropbox_sign_api/errors/bulk_send_job_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[BulkSendJobGetResponse](dropbox_sign_api/models/bulk_send_job_get_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[BulkSendJobGetErrorBody](dropbox_sign_api/errors/bulk_send_job_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bulk_send_job_list(*, page: int | None = 1, page_size: int | None = 20, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BulkSendJobListResponse, BulkSendJobListErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a list of BulkSendJob that you can access.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.bulk_send_job.with_raw_response.bulk_send_job_list()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkSendJobListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type BulkSendJobListErrorBody
```

**Async**

```python
result = await async_client.bulk_send_job.with_raw_response.bulk_send_job_list()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkSendJobListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type BulkSendJobListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>page</code> | <code>int \| None</code> | Which page number of the BulkSendJob List to return. Defaults to `1`.<br>**Default**: <code>1</code> |
| <code>page_size</code> | <code>int \| None</code> | Number of objects to be returned per page. Must be between `1` and `100`. Default is 20.<br>**Default**: <code>20</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[BulkSendJobListResponse](dropbox_sign_api/models/bulk_send_job_list_response.py), [BulkSendJobListErrorBody](dropbox_sign_api/errors/bulk_send_job_list_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[BulkSendJobListResponse](dropbox_sign_api/models/bulk_send_job_list_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[BulkSendJobListErrorBody](dropbox_sign_api/errors/bulk_send_job_list_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Document

> Source: [Document](dropbox_sign_api/apis/document.py)

<details>
<summary><code>def document_detect_fields(detection_mode: DetectionMode | DetectionModeDict, *, file: FileInput | None = None, file_url: str | None = None, page_range: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DocumentFieldDetectionResponse, DocumentDetectFieldsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Detects form fields in a PDF document using either PDF form annotations or Dropbox Sign text tags.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.document.with_raw_response.document_detect_fields("some example string", page_range="0-2,5,7-9")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DocumentFieldDetectionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DocumentDetectFieldsErrorBody
```

**Async**

```python
result = await async_client.document.with_raw_response.document_detect_fields(
    "some example string", page_range="0-2,5,7-9"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DocumentFieldDetectionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DocumentDetectFieldsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>detection_mode</code> | <code>[DetectionMode](dropbox_sign_api/models/unions/detection_mode.py) \| [DetectionModeDict](dropbox_sign_api/models/unions/detection_mode.py)</code> | The field detection method to use. Set to `annotations` to detect PDF form annotations or `text_tags` to detect Dropbox Sign text tags. |
| <code>file</code> | <code>FileInput \| None</code> | The PDF file to analyze.<br><br>This endpoint requires either `file` or `file_url`, but not both.<br>**Default**: <code>None</code> |
| <code>file_url</code> | <code>str \| None</code> | The URL of the PDF file to analyze.<br><br>This endpoint requires either `file` or `file_url`, but not both.<br>**Default**: <code>None</code> |
| <code>page_range</code> | <code>str \| None</code> | The zero-based page indexes to analyze. Accepts `all`, individual pages, inclusive ranges, or comma-separated combinations, such as `0-2,5,7-9`. Defaults to `all`.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[DocumentFieldDetectionResponse](dropbox_sign_api/models/document_field_detection_response.py), [DocumentDetectFieldsErrorBody](dropbox_sign_api/errors/document_detect_fields_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DocumentFieldDetectionResponse](dropbox_sign_api/models/document_field_detection_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[DocumentDetectFieldsErrorBody](dropbox_sign_api/errors/document_detect_fields_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Embedded

> Source: [Embedded](dropbox_sign_api/apis/embedded.py)

<details>
<summary><code>def embedded_edit_url(template_id: str, body: EmbeddedEditUrlRequest | EmbeddedEditUrlRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[EmbeddedEditUrlResponse, EmbeddedEditUrlErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves an embedded object containing a template url that can be opened in an iFrame. Note that only templates created via the embedded template process are available to be edited with this endpoint.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.embedded.with_raw_response.embedded_edit_url(
    "f57db65d3f933b5316d398057a36176831451a35", EmbeddedEditUrlRequest()
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EmbeddedEditUrlResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type EmbeddedEditUrlErrorBody
```

**Async**

```python
result = await async_client.embedded.with_raw_response.embedded_edit_url(
    "f57db65d3f933b5316d398057a36176831451a35", EmbeddedEditUrlRequest()
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EmbeddedEditUrlResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type EmbeddedEditUrlErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>template_id</code> | <code>str</code> | The id of the template to edit. |
| <code>body</code> | <code>[EmbeddedEditUrlRequest](dropbox_sign_api/models/embedded_edit_url_request.py) \| [EmbeddedEditUrlRequestDict](dropbox_sign_api/models/embedded_edit_url_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[EmbeddedEditUrlResponse](dropbox_sign_api/models/embedded_edit_url_response.py), [EmbeddedEditUrlErrorBody](dropbox_sign_api/errors/embedded_edit_url_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[EmbeddedEditUrlResponse](dropbox_sign_api/models/embedded_edit_url_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[EmbeddedEditUrlErrorBody](dropbox_sign_api/errors/embedded_edit_url_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def embedded_sign_url(signature_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[EmbeddedSignUrlResponse, EmbeddedSignUrlErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves an embedded object containing a signature url that can be opened in an iFrame. Note that templates created via the embedded template process will only be accessible through the API.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.embedded.with_raw_response.embedded_sign_url("50e3542f738adfa7ddd4cbd4c00d2a8ab6e4194b")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EmbeddedSignUrlResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type EmbeddedSignUrlErrorBody
```

**Async**

```python
result = await async_client.embedded.with_raw_response.embedded_sign_url("50e3542f738adfa7ddd4cbd4c00d2a8ab6e4194b")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EmbeddedSignUrlResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type EmbeddedSignUrlErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>signature_id</code> | <code>str</code> | The id of the signature to get a signature url for. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[EmbeddedSignUrlResponse](dropbox_sign_api/models/embedded_sign_url_response.py), [EmbeddedSignUrlErrorBody](dropbox_sign_api/errors/embedded_sign_url_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[EmbeddedSignUrlResponse](dropbox_sign_api/models/embedded_sign_url_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[EmbeddedSignUrlErrorBody](dropbox_sign_api/errors/embedded_sign_url_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Fax

> Source: [Fax](dropbox_sign_api/apis/fax.py)

<details>
<summary><code>def fax_delete(fax_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, FaxDeleteErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes the specified Fax from the system

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.fax.with_raw_response.fax_delete("fa5c8a0b0f492d768749333ad6fcc214c111e967")
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type FaxDeleteErrorBody
```

**Async**

```python
result = await async_client.fax.with_raw_response.fax_delete("fa5c8a0b0f492d768749333ad6fcc214c111e967")
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type FaxDeleteErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>fax_id</code> | <code>str</code> | Fax ID |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;None, [FaxDeleteErrorBody](dropbox_sign_api/errors/fax_delete_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[FaxDeleteErrorBody](dropbox_sign_api/errors/fax_delete_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def fax_files(fax_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, FaxFilesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Downloads files associated with a Fax

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.fax.with_raw_response.fax_files("fa5c8a0b0f492d768749333ad6fcc214c111e967")
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type FaxFilesErrorBody
```

**Async**

```python
result = await async_client.fax.with_raw_response.fax_files("fa5c8a0b0f492d768749333ad6fcc214c111e967")
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type FaxFilesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>fax_id</code> | <code>str</code> | Fax ID |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;None, [FaxFilesErrorBody](dropbox_sign_api/errors/fax_files_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[FaxFilesErrorBody](dropbox_sign_api/errors/fax_files_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def fax_get(fax_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FaxGetResponse, FaxGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns information about a Fax

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.fax.with_raw_response.fax_get("fa5c8a0b0f492d768749333ad6fcc214c111e967")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FaxGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type FaxGetErrorBody
```

**Async**

```python
result = await async_client.fax.with_raw_response.fax_get("fa5c8a0b0f492d768749333ad6fcc214c111e967")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FaxGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type FaxGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>fax_id</code> | <code>str</code> | Fax ID |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[FaxGetResponse](dropbox_sign_api/models/fax_get_response.py), [FaxGetErrorBody](dropbox_sign_api/errors/fax_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[FaxGetResponse](dropbox_sign_api/models/fax_get_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[FaxGetErrorBody](dropbox_sign_api/errors/fax_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def fax_list(*, page: int | None = 1, page_size: int | None = 20, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FaxListResponse, FaxListErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns properties of multiple Faxes

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.fax.with_raw_response.fax_list(page=1, page_size=20)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FaxListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type FaxListErrorBody
```

**Async**

```python
result = await async_client.fax.with_raw_response.fax_list(page=1, page_size=20)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FaxListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type FaxListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>page</code> | <code>int \| None</code> | Which page number of the Fax List to return. Defaults to `1`.<br>**Default**: <code>1</code> |
| <code>page_size</code> | <code>int \| None</code> | Number of objects to be returned per page. Must be between `1` and `100`. Default is `20`.<br>**Default**: <code>20</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[FaxListResponse](dropbox_sign_api/models/fax_list_response.py), [FaxListErrorBody](dropbox_sign_api/errors/fax_list_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[FaxListResponse](dropbox_sign_api/models/fax_list_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[FaxListErrorBody](dropbox_sign_api/errors/fax_list_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def fax_send(recipient: str, *, sender: str | None = None, files: FileInput | None = None, file_urls: list[str] | None = None, test_mode: bool | None = False, cover_page_to: str | None = None, cover_page_from: str | None = None, cover_page_message: str | None = None, title: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FaxGetResponse, FaxSendErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates and sends a new Fax with the submitted file(s)

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.fax.with_raw_response.fax_send(
    "recipient@example.com",
    sender="sender@example.com",
    cover_page_to="Recipient Name",
    cover_page_from="Sender Name",
    cover_page_message="Please find the attached documents.",
    title="Fax Title",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FaxGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type FaxSendErrorBody
```

**Async**

```python
result = await async_client.fax.with_raw_response.fax_send(
    "recipient@example.com",
    sender="sender@example.com",
    cover_page_to="Recipient Name",
    cover_page_from="Sender Name",
    cover_page_message="Please find the attached documents.",
    title="Fax Title",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FaxGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type FaxSendErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>recipient</code> | <code>str</code> | Recipient of the fax <br>Can be a phone number in E.164 format or email address |
| <code>sender</code> | <code>str \| None</code> | Fax Send From Sender (used only with fax number)<br>**Default**: <code>None</code> |
| <code>files</code> | <code>FileInput \| None</code> | Use `files[]` to indicate the uploaded file(s) to fax<br><br>This endpoint requires either **files** or **file_urls[]**, but not both.<br>**Default**: <code>None</code> |
| <code>file_urls</code> | <code>list&#91;str&#93; \| None</code> | Use `file_urls[]` to have Dropbox Fax download the file(s) to fax<br><br>This endpoint requires either **files** or **file_urls[]**, but not both.<br>**Default**: <code>None</code> |
| <code>test_mode</code> | <code>bool \| None</code> | API Test Mode Setting<br>**Default**: <code>False</code> |
| <code>cover_page_to</code> | <code>str \| None</code> | Fax cover page recipient information<br>**Default**: <code>None</code> |
| <code>cover_page_from</code> | <code>str \| None</code> | Fax cover page sender information<br>**Default**: <code>None</code> |
| <code>cover_page_message</code> | <code>str \| None</code> | Fax Cover Page Message<br>**Default**: <code>None</code> |
| <code>title</code> | <code>str \| None</code> | Fax Title<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[FaxGetResponse](dropbox_sign_api/models/fax_get_response.py), [FaxSendErrorBody](dropbox_sign_api/errors/fax_send_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[FaxGetResponse](dropbox_sign_api/models/fax_get_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[FaxSendErrorBody](dropbox_sign_api/errors/fax_send_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## FaxLine

> Source: [FaxLine](dropbox_sign_api/apis/fax_line.py)

<details>
<summary><code>def fax_line_add_user(body: FaxLineAddUserRequest | FaxLineAddUserRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FaxLineResponse, FaxLineAddUserErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Grants a user access to the specified Fax Line.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.fax_line.with_raw_response.fax_line_add_user(FaxLineAddUserRequest(number="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FaxLineResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type FaxLineAddUserErrorBody
```

**Async**

```python
result = await async_client.fax_line.with_raw_response.fax_line_add_user(
    FaxLineAddUserRequest(number="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FaxLineResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type FaxLineAddUserErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[FaxLineAddUserRequest](dropbox_sign_api/models/fax_line_add_user_request.py) \| [FaxLineAddUserRequestDict](dropbox_sign_api/models/fax_line_add_user_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[FaxLineResponse](dropbox_sign_api/models/fax_line_response.py), [FaxLineAddUserErrorBody](dropbox_sign_api/errors/fax_line_add_user_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[FaxLineResponse](dropbox_sign_api/models/fax_line_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[FaxLineAddUserErrorBody](dropbox_sign_api/errors/fax_line_add_user_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def fax_line_area_code_get(country: FaxLineAreaCodeGetCountryEnumOrStr, *, state: FaxLineAreaCodeGetStateEnumOrStr | None = None, province: FaxLineAreaCodeGetProvinceEnumOrStr | None = None, city: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FaxLineAreaCodeGetResponse, FaxLineAreaCodeGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a list of available area codes for a given state/province and city

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.fax_line.with_raw_response.fax_line_area_code_get(FaxLineAreaCodeGetCountryEnum.US)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FaxLineAreaCodeGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type FaxLineAreaCodeGetErrorBody
```

**Async**

```python
result = await async_client.fax_line.with_raw_response.fax_line_area_code_get(FaxLineAreaCodeGetCountryEnum.US)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FaxLineAreaCodeGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type FaxLineAreaCodeGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>country</code> | <code>[FaxLineAreaCodeGetCountryEnumOrStr](dropbox_sign_api/models/enums/fax_line_area_code_get_country_enum.py)</code> | Filter area codes by country |
| <code>state</code> | <code>[FaxLineAreaCodeGetStateEnumOrStr](dropbox_sign_api/models/enums/fax_line_area_code_get_state_enum.py) \| None</code> | Filter area codes by state<br>**Default**: <code>None</code> |
| <code>province</code> | <code>[FaxLineAreaCodeGetProvinceEnumOrStr](dropbox_sign_api/models/enums/fax_line_area_code_get_province_enum.py) \| None</code> | Filter area codes by province<br>**Default**: <code>None</code> |
| <code>city</code> | <code>str \| None</code> | Filter area codes by city<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[FaxLineAreaCodeGetResponse](dropbox_sign_api/models/fax_line_area_code_get_response.py), [FaxLineAreaCodeGetErrorBody](dropbox_sign_api/errors/fax_line_area_code_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[FaxLineAreaCodeGetResponse](dropbox_sign_api/models/fax_line_area_code_get_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[FaxLineAreaCodeGetErrorBody](dropbox_sign_api/errors/fax_line_area_code_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def fax_line_create(body: FaxLineCreateRequest | FaxLineCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FaxLineResponse, FaxLineCreateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Purchases a new Fax Line

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.fax_line.with_raw_response.fax_line_create(FaxLineCreateRequest(area_code=1, country=Country.CA))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FaxLineResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type FaxLineCreateErrorBody
```

**Async**

```python
result = await async_client.fax_line.with_raw_response.fax_line_create(
    FaxLineCreateRequest(area_code=1, country=Country.CA)
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FaxLineResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type FaxLineCreateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[FaxLineCreateRequest](dropbox_sign_api/models/fax_line_create_request.py) \| [FaxLineCreateRequestDict](dropbox_sign_api/models/fax_line_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[FaxLineResponse](dropbox_sign_api/models/fax_line_response.py), [FaxLineCreateErrorBody](dropbox_sign_api/errors/fax_line_create_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[FaxLineResponse](dropbox_sign_api/models/fax_line_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[FaxLineCreateErrorBody](dropbox_sign_api/errors/fax_line_create_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def fax_line_delete(body: FaxLineDeleteRequest | FaxLineDeleteRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Any, FaxLineDeleteErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes the specified Fax Line from the subscription.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.fax_line.with_raw_response.fax_line_delete(FaxLineDeleteRequest(number="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type FaxLineDeleteErrorBody
```

**Async**

```python
result = await async_client.fax_line.with_raw_response.fax_line_delete(
    FaxLineDeleteRequest(number="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type FaxLineDeleteErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[FaxLineDeleteRequest](dropbox_sign_api/models/fax_line_delete_request.py) \| [FaxLineDeleteRequestDict](dropbox_sign_api/models/fax_line_delete_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;Any, [FaxLineDeleteErrorBody](dropbox_sign_api/errors/fax_line_delete_error.py)&#93;</code>

**On `Success`**: `payload` is <code>Any</code> -- successful operation

**On `Failure`**: `error` is <code>[FaxLineDeleteErrorBody](dropbox_sign_api/errors/fax_line_delete_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def fax_line_get(number: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FaxLineResponse, FaxLineGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the properties and settings of a Fax Line.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.fax_line.with_raw_response.fax_line_get("123-123-1234")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FaxLineResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type FaxLineGetErrorBody
```

**Async**

```python
result = await async_client.fax_line.with_raw_response.fax_line_get("123-123-1234")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FaxLineResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type FaxLineGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>number</code> | <code>str</code> | The Fax Line number |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[FaxLineResponse](dropbox_sign_api/models/fax_line_response.py), [FaxLineGetErrorBody](dropbox_sign_api/errors/fax_line_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[FaxLineResponse](dropbox_sign_api/models/fax_line_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[FaxLineGetErrorBody](dropbox_sign_api/errors/fax_line_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def fax_line_list(*, account_id: str | None = None, page: int | None = 1, page_size: int | None = 20, show_team_lines: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FaxLineListResponse, FaxLineListErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the properties and settings of multiple Fax Lines.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.fax_line.with_raw_response.fax_line_list(
    account_id="ab55cd14a97219e36b5ff5fe23f2f9329b0c1e97", page=1, page_size=20
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FaxLineListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type FaxLineListErrorBody
```

**Async**

```python
result = await async_client.fax_line.with_raw_response.fax_line_list(
    account_id="ab55cd14a97219e36b5ff5fe23f2f9329b0c1e97", page=1, page_size=20
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FaxLineListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type FaxLineListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account_id</code> | <code>str \| None</code> | Account ID<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Which page number of the Fax Line List to return. Defaults to `1`.<br>**Default**: <code>1</code> |
| <code>page_size</code> | <code>int \| None</code> | Number of objects to be returned per page. Must be between `1` and `100`. Default is `20`.<br>**Default**: <code>20</code> |
| <code>show_team_lines</code> | <code>bool \| None</code> | Include Fax Lines belonging to team members in the list<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[FaxLineListResponse](dropbox_sign_api/models/fax_line_list_response.py), [FaxLineListErrorBody](dropbox_sign_api/errors/fax_line_list_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[FaxLineListResponse](dropbox_sign_api/models/fax_line_list_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[FaxLineListErrorBody](dropbox_sign_api/errors/fax_line_list_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def fax_line_remove_user(body: FaxLineRemoveUserRequest | FaxLineRemoveUserRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FaxLineResponse, FaxLineRemoveUserErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Removes a user's access to the specified Fax Line

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.fax_line.with_raw_response.fax_line_remove_user(FaxLineRemoveUserRequest(number="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FaxLineResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type FaxLineRemoveUserErrorBody
```

**Async**

```python
result = await async_client.fax_line.with_raw_response.fax_line_remove_user(
    FaxLineRemoveUserRequest(number="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FaxLineResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type FaxLineRemoveUserErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[FaxLineRemoveUserRequest](dropbox_sign_api/models/fax_line_remove_user_request.py) \| [FaxLineRemoveUserRequestDict](dropbox_sign_api/models/fax_line_remove_user_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[FaxLineResponse](dropbox_sign_api/models/fax_line_response.py), [FaxLineRemoveUserErrorBody](dropbox_sign_api/errors/fax_line_remove_user_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[FaxLineResponse](dropbox_sign_api/models/fax_line_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[FaxLineRemoveUserErrorBody](dropbox_sign_api/errors/fax_line_remove_user_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Oauth

> Source: [Oauth](dropbox_sign_api/apis/oauth.py)

<details>
<summary><code>def oauth_token_generate(body: OauthTokenGenerateRequest | OauthTokenGenerateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[OauthTokenResponse, OauthTokenGenerateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Once you have retrieved the code from the user callback, you will need to exchange it for an access token via a backend call.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.oauth.with_raw_response.oauth_token_generate(
    OauthTokenGenerateRequest(
        client_id="some example string",
        client_secret="some example string",
        code="some example string",
        grant_type="some example string",
        state="some example string",
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type OauthTokenResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type OauthTokenGenerateErrorBody
```

**Async**

```python
result = await async_client.oauth.with_raw_response.oauth_token_generate(
    OauthTokenGenerateRequest(
        client_id="some example string",
        client_secret="some example string",
        code="some example string",
        grant_type="some example string",
        state="some example string",
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type OauthTokenResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type OauthTokenGenerateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[OauthTokenGenerateRequest](dropbox_sign_api/models/oauth_token_generate_request.py) \| [OauthTokenGenerateRequestDict](dropbox_sign_api/models/oauth_token_generate_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[OauthTokenResponse](dropbox_sign_api/models/oauth_token_response.py), [OauthTokenGenerateErrorBody](dropbox_sign_api/errors/oauth_token_generate_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[OauthTokenResponse](dropbox_sign_api/models/oauth_token_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[OauthTokenGenerateErrorBody](dropbox_sign_api/errors/oauth_token_generate_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def oauth_token_refresh(body: OauthTokenRefreshRequest | OauthTokenRefreshRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[OauthTokenResponse, OauthTokenRefreshErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Access tokens are only valid for a given period of time (typically one hour) for security reasons. Whenever acquiring an new access token its TTL is also given (see `expires_in`), along with a refresh token that can be used to acquire a new access token after the current one has expired.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.oauth.with_raw_response.oauth_token_refresh(
    OauthTokenRefreshRequest(grant_type="some example string", refresh_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type OauthTokenResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type OauthTokenRefreshErrorBody
```

**Async**

```python
result = await async_client.oauth.with_raw_response.oauth_token_refresh(
    OauthTokenRefreshRequest(grant_type="some example string", refresh_token="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type OauthTokenResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type OauthTokenRefreshErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[OauthTokenRefreshRequest](dropbox_sign_api/models/oauth_token_refresh_request.py) \| [OauthTokenRefreshRequestDict](dropbox_sign_api/models/oauth_token_refresh_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[OauthTokenResponse](dropbox_sign_api/models/oauth_token_response.py), [OauthTokenRefreshErrorBody](dropbox_sign_api/errors/oauth_token_refresh_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[OauthTokenResponse](dropbox_sign_api/models/oauth_token_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[OauthTokenRefreshErrorBody](dropbox_sign_api/errors/oauth_token_refresh_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Report

> Source: [Report](dropbox_sign_api/apis/report.py)

<details>
<summary><code>def report_create(body: ReportCreateRequest | ReportCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ReportCreateResponse, ReportCreateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Request the creation of one or more report(s).

When the report(s) have been generated, you will receive an email (one per requested report type) containing a link to download the report as a CSV file. The requested date range may be up to 12 months in duration, and `start_date` must not be more than 10 years in the past.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.report.with_raw_response.report_create(
    ReportCreateRequest(
        end_date="some example string", report_type=[ReportType.USER_ACTIVITY], start_date="some example string"
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ReportCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ReportCreateErrorBody
```

**Async**

```python
result = await async_client.report.with_raw_response.report_create(
    ReportCreateRequest(
        end_date="some example string", report_type=[ReportType.USER_ACTIVITY], start_date="some example string"
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ReportCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ReportCreateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ReportCreateRequest](dropbox_sign_api/models/report_create_request.py) \| [ReportCreateRequestDict](dropbox_sign_api/models/report_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[ReportCreateResponse](dropbox_sign_api/models/report_create_response.py), [ReportCreateErrorBody](dropbox_sign_api/errors/report_create_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ReportCreateResponse](dropbox_sign_api/models/report_create_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[ReportCreateErrorBody](dropbox_sign_api/errors/report_create_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SignatureRequest

> Source: [SignatureRequest](dropbox_sign_api/apis/signature_request.py)

<details>
<summary><code>def signature_request_bulk_create_embedded_with_template(template_ids: list[str], client_id: str, *, signer_file: FileInput | None = None, signer_list: list[SubBulkSignerList | SubBulkSignerListDict] | None = None, allow_decline: bool | None = False, ccs: list[SubCc | SubCcDict] | None = None, custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None, message: str | None = None, metadata: dict[str, Any] | None = None, signing_redirect_url: str | None = None, subject: str | None = None, test_mode: bool | None = False, title: str | None = None, expires_at: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BulkSendJobSendResponse, SignatureRequestBulkCreateEmbeddedWithTemplateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates BulkSendJob which sends up to 250 SignatureRequests in bulk based off of the provided Template(s) specified with the `template_ids` parameter to be signed in an embedded iFrame. These embedded signature requests can only be signed in embedded iFrames whereas normal signature requests can only be signed on Dropbox Sign.

**NOTE:** Only available for Standard plan and higher.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.signature_request.with_raw_response.signature_request_bulk_create_embedded_with_template(
    ["some example string"], "some example string"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkSendJobSendResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SignatureRequestBulkCreateEmbeddedWithTemplateErrorBody
```

**Async**

```python
result = await async_client.signature_request.with_raw_response.signature_request_bulk_create_embedded_with_template(
    ["some example string"], "some example string"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkSendJobSendResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SignatureRequestBulkCreateEmbeddedWithTemplateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>template_ids</code> | <code>list&#91;str&#93;</code> | Use `template_ids` to create a SignatureRequest from one or more templates, in the order in which the template will be used. |
| <code>client_id</code> | <code>str</code> | Client id of the app you're using to create this embedded signature request. Used for security purposes. |
| <code>signer_file</code> | <code>FileInput \| None</code> | `signer_file` is a CSV file defining values and options for signer fields. Required unless a `signer_list` is used, you may not use both. The CSV can have the following columns:<br><br>- `name`: the name of the signer filling the role of RoleName<br>- `email_address`: email address of the signer filling the role of RoleName<br>- `pin`: the 4- to 12-character access code that will secure this signer's signature page (optional)<br>- `sms_phone_number`: An E.164 formatted phone number that will receive a code via SMS to access this signer's signature page. (optional)<br><br>    By using the feature, you agree you are responsible for obtaining a signer's consent to receive text messages from Dropbox Sign related to this signature request and confirm you have obtained such consent from all signers prior to enabling SMS delivery for this signature request. [Learn more](https://faq.hellosign.com/hc/en-us/articles/15815316468877-Dropbox-Sign-SMS-tools-add-on).<br><br>    **NOTE:** Not available in test mode and requires a Standard plan or higher.<br>- `*_field`: any column with a _field" suffix will be treated as a custom field (optional)<br><br>    You may only specify field values here, any other options should be set in the custom_fields request parameter.<br><br>Example CSV:<br><br>``<br>name, email_address, pin, company_field<br>George, george@example.com, d79a3td, ABC Corp<br>Mary, mary@example.com, gd9as5b, 123 LLC<br>``<br>**Default**: <code>None</code> |
| <code>signer_list</code> | <code>list&#91;[SubBulkSignerList](dropbox_sign_api/models/sub_bulk_signer_list.py) \| [SubBulkSignerListDict](dropbox_sign_api/models/sub_bulk_signer_list.py)&#93; \| None</code> | `signer_list` is an array defining values and options for signer fields. Required unless a `signer_file` is used, you may not use both.<br>**Default**: <code>None</code> |
| <code>allow_decline</code> | <code>bool \| None</code> | Allows signers to decline to sign a document if `true`. Defaults to `false`.<br>**Default**: <code>False</code> |
| <code>ccs</code> | <code>list&#91;[SubCc](dropbox_sign_api/models/sub_cc.py) \| [SubCcDict](dropbox_sign_api/models/sub_cc.py)&#93; \| None</code> | Add CC email recipients. Required when a CC role exists for the Template.<br>**Default**: <code>None</code> |
| <code>custom_fields</code> | <code>list&#91;[SubCustomField](dropbox_sign_api/models/sub_custom_field.py) \| [SubCustomFieldDict](dropbox_sign_api/models/sub_custom_field.py)&#93; \| None</code> | When used together with merge fields, `custom_fields` allows users to add pre-filled data to their signature requests.<br><br>Pre-filled data can be used with "send-once" signature requests by adding merge fields with `form_fields_per_document` or [Text Tags](https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro) while passing values back with `custom_fields` together in one API call.<br><br>For using pre-filled on repeatable signature requests, merge fields are added to templates in the Dropbox Sign UI or by calling [/template/create_embedded_draft](/api/reference/operation/templateCreateEmbeddedDraft) and then passing `custom_fields` on subsequent signature requests referencing that template.<br>**Default**: <code>None</code> |
| <code>message</code> | <code>str \| None</code> | The custom message in the email that will be sent to the signers.<br>**Default**: <code>None</code> |
| <code>metadata</code> | <code>dict&#91;str, Any&#93; \| None</code> | Key-value data that should be attached to the signature request. This metadata is included in all API responses and events involving the signature request. For example, use the metadata field to store a signer's order number for look up when receiving events for the signature request.<br><br>Each request can include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and values up to 1000 characters long.<br>**Default**: <code>None</code> |
| <code>signing_redirect_url</code> | <code>str \| None</code> | The URL you want signers redirected to after they successfully sign.<br>**Default**: <code>None</code> |
| <code>subject</code> | <code>str \| None</code> | The subject in the email that will be sent to the signers.<br>**Default**: <code>None</code> |
| <code>test_mode</code> | <code>bool \| None</code> | Whether this is a test, the signature request will not be legally binding if set to `true`. Defaults to `false`.<br>**Default**: <code>False</code> |
| <code>title</code> | <code>str \| None</code> | The title you want to assign to the SignatureRequest.<br>**Default**: <code>None</code> |
| <code>expires_at</code> | <code>int \| None</code> | When the signature request will expire. Unsigned signatures will be moved to the expired status, and no longer signable. See [Signature Request Expiration Date](https://developers.hellosign.com/docs/signature-request/expiration/) for details.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[BulkSendJobSendResponse](dropbox_sign_api/models/bulk_send_job_send_response.py), [SignatureRequestBulkCreateEmbeddedWithTemplateErrorBody](dropbox_sign_api/errors/signature_request_bulk_create_embedded_with_template_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[BulkSendJobSendResponse](dropbox_sign_api/models/bulk_send_job_send_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[SignatureRequestBulkCreateEmbeddedWithTemplateErrorBody](dropbox_sign_api/errors/signature_request_bulk_create_embedded_with_template_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def signature_request_bulk_send_with_template(template_ids: list[str], *, signer_file: FileInput | None = None, signer_list: list[SubBulkSignerList | SubBulkSignerListDict] | None = None, allow_decline: bool | None = False, ccs: list[SubCc | SubCcDict] | None = None, client_id: str | None = None, custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None, message: str | None = None, metadata: dict[str, Any] | None = None, signing_redirect_url: str | None = None, subject: str | None = None, test_mode: bool | None = False, title: str | None = None, expires_at: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BulkSendJobSendResponse, SignatureRequestBulkSendWithTemplateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates BulkSendJob which sends up to 250 SignatureRequests in bulk based off of the provided Template(s) specified with the `template_ids` parameter.

**NOTE:** Only available for Standard plan and higher.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.signature_request.with_raw_response.signature_request_bulk_send_with_template(["some example string"])
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkSendJobSendResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SignatureRequestBulkSendWithTemplateErrorBody
```

**Async**

```python
result = await async_client.signature_request.with_raw_response.signature_request_bulk_send_with_template(
    ["some example string"]
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkSendJobSendResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SignatureRequestBulkSendWithTemplateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>template_ids</code> | <code>list&#91;str&#93;</code> | Use `template_ids` to create a SignatureRequest from one or more templates, in the order in which the template will be used. |
| <code>signer_file</code> | <code>FileInput \| None</code> | `signer_file` is a CSV file defining values and options for signer fields. Required unless a `signer_list` is used, you may not use both. The CSV can have the following columns:<br><br>- `name`: the name of the signer filling the role of RoleName<br>- `email_address`: email address of the signer filling the role of RoleName<br>- `pin`: the 4- to 12-character access code that will secure this signer's signature page (optional)<br>- `sms_phone_number`: An E.164 formatted phone number that will receive a code via SMS to access this signer's signature page. (optional)<br><br>    By using the feature, you agree you are responsible for obtaining a signer's consent to receive text messages from Dropbox Sign related to this signature request and confirm you have obtained such consent from all signers prior to enabling SMS delivery for this signature request. [Learn more](https://faq.hellosign.com/hc/en-us/articles/15815316468877-Dropbox-Sign-SMS-tools-add-on).<br><br>    **NOTE:** Not available in test mode and requires a Standard plan or higher.<br>- `*_field`: any column with a _field" suffix will be treated as a custom field (optional)<br><br>    You may only specify field values here, any other options should be set in the custom_fields request parameter.<br><br>Example CSV:<br><br>``<br>name, email_address, pin, company_field<br>George, george@example.com, d79a3td, ABC Corp<br>Mary, mary@example.com, gd9as5b, 123 LLC<br>``<br>**Default**: <code>None</code> |
| <code>signer_list</code> | <code>list&#91;[SubBulkSignerList](dropbox_sign_api/models/sub_bulk_signer_list.py) \| [SubBulkSignerListDict](dropbox_sign_api/models/sub_bulk_signer_list.py)&#93; \| None</code> | `signer_list` is an array defining values and options for signer fields. Required unless a `signer_file` is used, you may not use both.<br>**Default**: <code>None</code> |
| <code>allow_decline</code> | <code>bool \| None</code> | Allows signers to decline to sign a document if `true`. Defaults to `false`.<br>**Default**: <code>False</code> |
| <code>ccs</code> | <code>list&#91;[SubCc](dropbox_sign_api/models/sub_cc.py) \| [SubCcDict](dropbox_sign_api/models/sub_cc.py)&#93; \| None</code> | Add CC email recipients. Required when a CC role exists for the Template.<br>**Default**: <code>None</code> |
| <code>client_id</code> | <code>str \| None</code> | The client id of the API App you want to associate with this request. Used to apply the branding and callback url defined for the app.<br>**Default**: <code>None</code> |
| <code>custom_fields</code> | <code>list&#91;[SubCustomField](dropbox_sign_api/models/sub_custom_field.py) \| [SubCustomFieldDict](dropbox_sign_api/models/sub_custom_field.py)&#93; \| None</code> | When used together with merge fields, `custom_fields` allows users to add pre-filled data to their signature requests.<br><br>Pre-filled data can be used with "send-once" signature requests by adding merge fields with `form_fields_per_document` or [Text Tags](https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro) while passing values back with `custom_fields` together in one API call.<br><br>For using pre-filled on repeatable signature requests, merge fields are added to templates in the Dropbox Sign UI or by calling [/template/create_embedded_draft](/api/reference/operation/templateCreateEmbeddedDraft) and then passing `custom_fields` on subsequent signature requests referencing that template.<br>**Default**: <code>None</code> |
| <code>message</code> | <code>str \| None</code> | The custom message in the email that will be sent to the signers.<br>**Default**: <code>None</code> |
| <code>metadata</code> | <code>dict&#91;str, Any&#93; \| None</code> | Key-value data that should be attached to the signature request. This metadata is included in all API responses and events involving the signature request. For example, use the metadata field to store a signer's order number for look up when receiving events for the signature request.<br><br>Each request can include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and values up to 1000 characters long.<br>**Default**: <code>None</code> |
| <code>signing_redirect_url</code> | <code>str \| None</code> | The URL you want signers redirected to after they successfully sign.<br>**Default**: <code>None</code> |
| <code>subject</code> | <code>str \| None</code> | The subject in the email that will be sent to the signers.<br>**Default**: <code>None</code> |
| <code>test_mode</code> | <code>bool \| None</code> | Whether this is a test, the signature request will not be legally binding if set to `true`. Defaults to `false`.<br>**Default**: <code>False</code> |
| <code>title</code> | <code>str \| None</code> | The title you want to assign to the SignatureRequest.<br>**Default**: <code>None</code> |
| <code>expires_at</code> | <code>int \| None</code> | When the signature request will expire. Unsigned signatures will be moved to the expired status, and no longer signable. See [Signature Request Expiration Date](https://developers.hellosign.com/docs/signature-request/expiration/) for details.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[BulkSendJobSendResponse](dropbox_sign_api/models/bulk_send_job_send_response.py), [SignatureRequestBulkSendWithTemplateErrorBody](dropbox_sign_api/errors/signature_request_bulk_send_with_template_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[BulkSendJobSendResponse](dropbox_sign_api/models/bulk_send_job_send_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[SignatureRequestBulkSendWithTemplateErrorBody](dropbox_sign_api/errors/signature_request_bulk_send_with_template_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def signature_request_cancel(signature_request_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Any, SignatureRequestCancelErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Cancels an incomplete signature request. This action is **not reversible**.

The request will be canceled and signers will no longer be able to sign. If they try to access the signature request they will receive a HTTP 410 status code indicating that the resource has been deleted. Cancelation is asynchronous and a successful call to this endpoint will return an empty 200 OK response if the signature request is eligible to be canceled and has been successfully queued.

This 200 OK response does not indicate a successful cancelation of the signature request itself. The cancelation is confirmed via the `signature_request_canceled` event. It is recommended that a [callback handler](/api/reference/tag/Callbacks-and-Events) be implemented to listen for the `signature_request_canceled` event. This callback will be sent only when the cancelation has completed successfully. If a callback handler has been configured and the event has not been received within 60 minutes of making the call, check the status of the request in the [API Dashboard](https://app.hellosign.com/apidashboard) and retry the cancelation if necessary.

To be eligible for cancelation, a signature request must have been sent successfully, must not yet have been signed by all signers, and you must either be the sender or own the API app under which it was sent. A partially signed signature request can be canceled.

**NOTE:** To remove your access to a completed signature request, use the endpoint: `POST /signature_request/remove/[:signature_request_id]`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.signature_request.with_raw_response.signature_request_cancel("fa5c8a0b0f492d768749333ad6fcc214c111e967")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SignatureRequestCancelErrorBody
```

**Async**

```python
result = await async_client.signature_request.with_raw_response.signature_request_cancel(
    "fa5c8a0b0f492d768749333ad6fcc214c111e967"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SignatureRequestCancelErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>signature_request_id</code> | <code>str</code> | The id of the incomplete SignatureRequest to cancel. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;Any, [SignatureRequestCancelErrorBody](dropbox_sign_api/errors/signature_request_cancel_error.py)&#93;</code>

**On `Success`**: `payload` is <code>Any</code> -- successful operation

**On `Failure`**: `error` is <code>[SignatureRequestCancelErrorBody](dropbox_sign_api/errors/signature_request_cancel_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def signature_request_create_embedded(client_id: str, *, files: FileInput | None = None, file_urls: list[str] | None = None, signers: list[SubSignatureRequestSigner | SubSignatureRequestSignerDict] | None = None, grouped_signers: list[SubSignatureRequestGroupedSigners | SubSignatureRequestGroupedSignersDict] | None = None, allow_decline: bool | None = False, allow_reassign: bool | None = False, attachments: list[SubAttachment | SubAttachmentDict] | None = None, cc_email_addresses: list[EmailStr] | None = None, custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None, field_options: SubFieldOptions | SubFieldOptionsDict | None = None, form_field_groups: list[SubFormFieldGroup | SubFormFieldGroupDict] | None = None, form_field_rules: list[SubFormFieldRule | SubFormFieldRuleDict] | None = None, form_fields_per_document: list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None = None, hide_text_tags: bool | None = False, message: str | None = None, metadata: dict[str, Any] | None = None, signing_options: SubSigningOptions | SubSigningOptionsDict | None = None, subject: str | None = None, test_mode: bool | None = False, title: str | None = None, use_text_tags: bool | None = False, ignore_text_tags_extraction_errors: bool | None = False, populate_auto_fill_fields: bool | None = False, expires_at: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SignatureRequestGetResponse, SignatureRequestCreateEmbeddedErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a new SignatureRequest with the submitted documents to be signed in an embedded iFrame. If form_fields_per_document is not specified, a signature page will be affixed where all signers will be required to add their signature, signifying their agreement to all contained documents. Note that embedded signature requests can only be signed in embedded iFrames whereas normal signature requests can only be signed on Dropbox Sign.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.signature_request.with_raw_response.signature_request_create_embedded("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SignatureRequestGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SignatureRequestCreateEmbeddedErrorBody
```

**Async**

```python
result = await async_client.signature_request.with_raw_response.signature_request_create_embedded("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SignatureRequestGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SignatureRequestCreateEmbeddedErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>client_id</code> | <code>str</code> | Client id of the app you're using to create this embedded signature request. Used for security purposes. |
| <code>files</code> | <code>FileInput \| None</code> | Use `files[]` to indicate the uploaded file(s) to send for signature.<br><br>This endpoint requires either **files** or **file_urls[]**, but not both.<br>**Default**: <code>None</code> |
| <code>file_urls</code> | <code>list&#91;str&#93; \| None</code> | Use `file_urls[]` to have Dropbox Sign download the file(s) to send for signature.<br><br>This endpoint requires either **files** or **file_urls[]**, but not both.<br>**Default**: <code>None</code> |
| <code>signers</code> | <code>list&#91;[SubSignatureRequestSigner](dropbox_sign_api/models/sub_signature_request_signer.py) \| [SubSignatureRequestSignerDict](dropbox_sign_api/models/sub_signature_request_signer.py)&#93; \| None</code> | Add Signers to your Signature Request.<br><br>This endpoint requires either **signers** or **grouped_signers**, but not both.<br>**Default**: <code>None</code> |
| <code>grouped_signers</code> | <code>list&#91;[SubSignatureRequestGroupedSigners](dropbox_sign_api/models/sub_signature_request_grouped_signers.py) \| [SubSignatureRequestGroupedSignersDict](dropbox_sign_api/models/sub_signature_request_grouped_signers.py)&#93; \| None</code> | Add Grouped Signers to your Signature Request.<br><br>This endpoint requires either **signers** or **grouped_signers**, but not both.<br>**Default**: <code>None</code> |
| <code>allow_decline</code> | <code>bool \| None</code> | Allows signers to decline to sign a document if `true`. Defaults to `false`.<br>**Default**: <code>False</code> |
| <code>allow_reassign</code> | <code>bool \| None</code> | Allows signers to reassign their signature requests to other signers if set to `true`. Defaults to `false`.<br><br>**NOTE:** Only available for Premium plan.<br>**Default**: <code>False</code> |
| <code>attachments</code> | <code>list&#91;[SubAttachment](dropbox_sign_api/models/sub_attachment.py) \| [SubAttachmentDict](dropbox_sign_api/models/sub_attachment.py)&#93; \| None</code> | A list describing the attachments<br>**Default**: <code>None</code> |
| <code>cc_email_addresses</code> | <code>list&#91;EmailStr&#93; \| None</code> | The email addresses that should be CCed.<br>**Default**: <code>None</code> |
| <code>custom_fields</code> | <code>list&#91;[SubCustomField](dropbox_sign_api/models/sub_custom_field.py) \| [SubCustomFieldDict](dropbox_sign_api/models/sub_custom_field.py)&#93; \| None</code> | When used together with merge fields, `custom_fields` allows users to add pre-filled data to their signature requests.<br><br>Pre-filled data can be used with "send-once" signature requests by adding merge fields with `form_fields_per_document` or [Text Tags](https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro) while passing values back with `custom_fields` together in one API call.<br><br>For using pre-filled on repeatable signature requests, merge fields are added to templates in the Dropbox Sign UI or by calling [/template/create_embedded_draft](/api/reference/operation/templateCreateEmbeddedDraft) and then passing `custom_fields` on subsequent signature requests referencing that template.<br>**Default**: <code>None</code> |
| <code>field_options</code> | <code>[SubFieldOptions](dropbox_sign_api/models/sub_field_options.py) \| [SubFieldOptionsDict](dropbox_sign_api/models/sub_field_options.py) \| None</code> | This allows the requester to specify field options for a signature request.<br>**Default**: <code>None</code> |
| <code>form_field_groups</code> | <code>list&#91;[SubFormFieldGroup](dropbox_sign_api/models/sub_form_field_group.py) \| [SubFormFieldGroupDict](dropbox_sign_api/models/sub_form_field_group.py)&#93; \| None</code> | Group information for fields defined in `form_fields_per_document`. String-indexed JSON array with `group_label` and `requirement` keys. `form_fields_per_document` must contain fields referencing a group defined in `form_field_groups`.<br>**Default**: <code>None</code> |
| <code>form_field_rules</code> | <code>list&#91;[SubFormFieldRule](dropbox_sign_api/models/sub_form_field_rule.py) \| [SubFormFieldRuleDict](dropbox_sign_api/models/sub_form_field_rule.py)&#93; \| None</code> | Conditional Logic rules for fields defined in `form_fields_per_document`.<br>**Default**: <code>None</code> |
| <code>form_fields_per_document</code> | <code>list&#91;[SubFormFieldsPerDocumentBase](dropbox_sign_api/models/unions/sub_form_fields_per_document_base.py) \| [SubFormFieldsPerDocumentBaseDict](dropbox_sign_api/models/unions/sub_form_fields_per_document_base.py)&#93; \| None</code> | The fields that should appear on the document, expressed as an array of objects. (For more details you can read about it here: [Using Form Fields per Document](/docs/openapi/form-fields-per-document).)<br><br>**NOTE:** Fields like **text**, **dropdown**, **checkbox**, **radio**, and **hyperlink** have additional required and optional parameters. Check out the list of [additional parameters](/api/reference/constants/#form-fields-per-document) for these field types.<br><br>* Text Field use `SubFormFieldsPerDocumentText`<br>* Dropdown Field use `SubFormFieldsPerDocumentDropdown`<br>* Hyperlink Field use `SubFormFieldsPerDocumentHyperlink`<br>* Checkbox Field use `SubFormFieldsPerDocumentCheckbox`<br>* Radio Field use `SubFormFieldsPerDocumentRadio`<br>* Signature Field use `SubFormFieldsPerDocumentSignature`<br>* Date Signed Field use `SubFormFieldsPerDocumentDateSigned`<br>* Initials Field use `SubFormFieldsPerDocumentInitials`<br>* Text Merge Field use `SubFormFieldsPerDocumentTextMerge`<br>* Checkbox Merge Field use `SubFormFieldsPerDocumentCheckboxMerge`<br>**Default**: <code>None</code> |
| <code>hide_text_tags</code> | <code>bool \| None</code> | Enables automatic Text Tag removal when set to true.<br><br>**NOTE:** Removing text tags this way can cause unwanted clipping. We recommend leaving this setting on `false` and instead hiding your text tags using white text or a similar approach. See the [Text Tags Walkthrough](https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro) for more information.<br>**Default**: <code>False</code> |
| <code>message</code> | <code>str \| None</code> | The custom message in the email that will be sent to the signers.<br>**Default**: <code>None</code> |
| <code>metadata</code> | <code>dict&#91;str, Any&#93; \| None</code> | Key-value data that should be attached to the signature request. This metadata is included in all API responses and events involving the signature request. For example, use the metadata field to store a signer's order number for look up when receiving events for the signature request.<br><br>Each request can include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and values up to 1000 characters long.<br>**Default**: <code>None</code> |
| <code>signing_options</code> | <code>[SubSigningOptions](dropbox_sign_api/models/sub_signing_options.py) \| [SubSigningOptionsDict](dropbox_sign_api/models/sub_signing_options.py) \| None</code> | This allows the requester to specify the types allowed for creating a signature and specify another signing options.<br><br>**NOTE:** If `signing_options` are not defined in the request, the allowed types will default to those specified in the account settings.<br><br>**NOTE:** If `force_advanced_signature_details` is set, allowed types has to be defined too.<br>**Default**: <code>None</code> |
| <code>subject</code> | <code>str \| None</code> | The subject in the email that will be sent to the signers.<br>**Default**: <code>None</code> |
| <code>test_mode</code> | <code>bool \| None</code> | Whether this is a test, the signature request will not be legally binding if set to `true`. Defaults to `false`.<br>**Default**: <code>False</code> |
| <code>title</code> | <code>str \| None</code> | The title you want to assign to the SignatureRequest.<br>**Default**: <code>None</code> |
| <code>use_text_tags</code> | <code>bool \| None</code> | Send with a value of `true` if you wish to enable [Text Tags](https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro) parsing in your document. Defaults to disabled, or `false`.<br>**Default**: <code>False</code> |
| <code>ignore_text_tags_extraction_errors</code> | <code>bool \| None</code> | Sent with a value of `true` to ignore the validation errors from text tags extraction. Defaults to `false`.<br>**Default**: <code>False</code> |
| <code>populate_auto_fill_fields</code> | <code>bool \| None</code> | Controls whether [auto fill fields](https://faq.hellosign.com/hc/en-us/articles/360051467511-Auto-Fill-Fields) can automatically populate a signer's information during signing.<br><br>**NOTE:** Keep your signer's information safe by ensuring that the _signer on your signature request is the intended party_ before using this feature.<br>**Default**: <code>False</code> |
| <code>expires_at</code> | <code>int \| None</code> | When the signature request will expire. Unsigned signatures will be moved to the expired status, and no longer signable. See [Signature Request Expiration Date](https://developers.hellosign.com/docs/signature-request/expiration/) for details.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[SignatureRequestGetResponse](dropbox_sign_api/models/signature_request_get_response.py), [SignatureRequestCreateEmbeddedErrorBody](dropbox_sign_api/errors/signature_request_create_embedded_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SignatureRequestGetResponse](dropbox_sign_api/models/signature_request_get_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[SignatureRequestCreateEmbeddedErrorBody](dropbox_sign_api/errors/signature_request_create_embedded_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def signature_request_create_embedded_with_template(template_ids: list[str], client_id: str, signers: list[SubSignatureRequestTemplateSigner | SubSignatureRequestTemplateSignerDict], *, allow_decline: bool | None = False, ccs: list[SubCc | SubCcDict] | None = None, custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None, files: FileInput | None = None, file_urls: list[str] | None = None, message: str | None = None, metadata: dict[str, Any] | None = None, signing_options: SubSigningOptions | SubSigningOptionsDict | None = None, subject: str | None = None, test_mode: bool | None = False, title: str | None = None, populate_auto_fill_fields: bool | None = False, expires_at: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SignatureRequestGetResponse, SignatureRequestCreateEmbeddedWithTemplateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a new SignatureRequest based on the given Template(s) to be signed in an embedded iFrame. Note that embedded signature requests can only be signed in embedded iFrames whereas normal signature requests can only be signed on Dropbox Sign.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.signature_request.with_raw_response.signature_request_create_embedded_with_template(
    ["some example string"],
    "some example string",
    [
        SubSignatureRequestTemplateSigner(
            role="some example string", name="some example string", email_address="user@example.com"
        ),
    ],
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SignatureRequestGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SignatureRequestCreateEmbeddedWithTemplateErrorBody
```

**Async**

```python
result = await async_client.signature_request.with_raw_response.signature_request_create_embedded_with_template(
    ["some example string"],
    "some example string",
    [
        SubSignatureRequestTemplateSigner(
            role="some example string", name="some example string", email_address="user@example.com"
        ),
    ],
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SignatureRequestGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SignatureRequestCreateEmbeddedWithTemplateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>template_ids</code> | <code>list&#91;str&#93;</code> | Use `template_ids` to create a SignatureRequest from one or more templates, in the order in which the template will be used. |
| <code>client_id</code> | <code>str</code> | Client id of the app you're using to create this embedded signature request. Used for security purposes. |
| <code>signers</code> | <code>list&#91;[SubSignatureRequestTemplateSigner](dropbox_sign_api/models/sub_signature_request_template_signer.py) \| [SubSignatureRequestTemplateSignerDict](dropbox_sign_api/models/sub_signature_request_template_signer.py)&#93;</code> | Add Signers to your Templated-based Signature Request. |
| <code>allow_decline</code> | <code>bool \| None</code> | Allows signers to decline to sign a document if `true`. Defaults to `false`.<br>**Default**: <code>False</code> |
| <code>ccs</code> | <code>list&#91;[SubCc](dropbox_sign_api/models/sub_cc.py) \| [SubCcDict](dropbox_sign_api/models/sub_cc.py)&#93; \| None</code> | Add CC email recipients. Required when a CC role exists for the Template.<br>**Default**: <code>None</code> |
| <code>custom_fields</code> | <code>list&#91;[SubCustomField](dropbox_sign_api/models/sub_custom_field.py) \| [SubCustomFieldDict](dropbox_sign_api/models/sub_custom_field.py)&#93; \| None</code> | An array defining values and options for custom fields. Required when a custom field exists in the Template.<br>**Default**: <code>None</code> |
| <code>files</code> | <code>FileInput \| None</code> | Use `files[]` to indicate the uploaded file(s) to send for signature.<br><br>This endpoint requires either **files** or **file_urls[]**, but not both.<br>**Default**: <code>None</code> |
| <code>file_urls</code> | <code>list&#91;str&#93; \| None</code> | Use `file_urls[]` to have Dropbox Sign download the file(s) to send for signature.<br><br>This endpoint requires either **files** or **file_urls[]**, but not both.<br>**Default**: <code>None</code> |
| <code>message</code> | <code>str \| None</code> | The custom message in the email that will be sent to the signers.<br>**Default**: <code>None</code> |
| <code>metadata</code> | <code>dict&#91;str, Any&#93; \| None</code> | Key-value data that should be attached to the signature request. This metadata is included in all API responses and events involving the signature request. For example, use the metadata field to store a signer's order number for look up when receiving events for the signature request.<br><br>Each request can include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and values up to 1000 characters long.<br>**Default**: <code>None</code> |
| <code>signing_options</code> | <code>[SubSigningOptions](dropbox_sign_api/models/sub_signing_options.py) \| [SubSigningOptionsDict](dropbox_sign_api/models/sub_signing_options.py) \| None</code> | This allows the requester to specify the types allowed for creating a signature and specify another signing options.<br><br>**NOTE:** If `signing_options` are not defined in the request, the allowed types will default to those specified in the account settings.<br><br>**NOTE:** If `force_advanced_signature_details` is set, allowed types has to be defined too.<br>**Default**: <code>None</code> |
| <code>subject</code> | <code>str \| None</code> | The subject in the email that will be sent to the signers.<br>**Default**: <code>None</code> |
| <code>test_mode</code> | <code>bool \| None</code> | Whether this is a test, the signature request will not be legally binding if set to `true`. Defaults to `false`.<br>**Default**: <code>False</code> |
| <code>title</code> | <code>str \| None</code> | The title you want to assign to the SignatureRequest.<br>**Default**: <code>None</code> |
| <code>populate_auto_fill_fields</code> | <code>bool \| None</code> | Controls whether [auto fill fields](https://faq.hellosign.com/hc/en-us/articles/360051467511-Auto-Fill-Fields) can automatically populate a signer's information during signing.<br><br>**NOTE:** Keep your signer's information safe by ensuring that the _signer on your signature request is the intended party_ before using this feature.<br>**Default**: <code>False</code> |
| <code>expires_at</code> | <code>int \| None</code> | When the signature request will expire. Unsigned signatures will be moved to the expired status, and no longer signable. See [Signature Request Expiration Date](https://developers.hellosign.com/docs/signature-request/expiration/) for details.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[SignatureRequestGetResponse](dropbox_sign_api/models/signature_request_get_response.py), [SignatureRequestCreateEmbeddedWithTemplateErrorBody](dropbox_sign_api/errors/signature_request_create_embedded_with_template_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SignatureRequestGetResponse](dropbox_sign_api/models/signature_request_get_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[SignatureRequestCreateEmbeddedWithTemplateErrorBody](dropbox_sign_api/errors/signature_request_create_embedded_with_template_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def signature_request_edit(signature_request_id: str, *, files: FileInput | None = None, file_urls: list[str] | None = None, signers: list[SubSignatureRequestSigner | SubSignatureRequestSignerDict] | None = None, grouped_signers: list[SubSignatureRequestGroupedSigners | SubSignatureRequestGroupedSignersDict] | None = None, allow_decline: bool | None = False, allow_reassign: bool | None = False, attachments: list[SubAttachment | SubAttachmentDict] | None = None, cc_email_addresses: list[EmailStr] | None = None, client_id: str | None = None, custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None, field_options: SubFieldOptions | SubFieldOptionsDict | None = None, form_field_groups: list[SubFormFieldGroup | SubFormFieldGroupDict] | None = None, form_field_rules: list[SubFormFieldRule | SubFormFieldRuleDict] | None = None, form_fields_per_document: list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None = None, hide_text_tags: bool | None = False, is_eid: bool | None = False, message: str | None = None, metadata: dict[str, Any] | None = None, signing_options: SubSigningOptions | SubSigningOptionsDict | None = None, signing_redirect_url: str | None = None, subject: str | None = None, test_mode: bool | None = False, title: str | None = None, use_text_tags: bool | None = False, ignore_text_tags_extraction_errors: bool | None = False, expires_at: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SignatureRequestGetResponse, SignatureRequestEditErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Edits and sends a SignatureRequest with the submitted documents. If `form_fields_per_document` is not specified, a signature page will be affixed where all signers will be required to add their signature, signifying their agreement to all contained documents.

**NOTE:** Edit and resend *will* deduct your signature request quota.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.signature_request.with_raw_response.signature_request_edit("fa5c8a0b0f492d768749333ad6fcc214c111e967")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SignatureRequestGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SignatureRequestEditErrorBody
```

**Async**

```python
result = await async_client.signature_request.with_raw_response.signature_request_edit(
    "fa5c8a0b0f492d768749333ad6fcc214c111e967"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SignatureRequestGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SignatureRequestEditErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>signature_request_id</code> | <code>str</code> | The id of the SignatureRequest to edit. |
| <code>files</code> | <code>FileInput \| None</code> | Use `files[]` to indicate the uploaded file(s) to send for signature.<br><br>This endpoint requires either **files** or **file_urls[]**, but not both.<br>**Default**: <code>None</code> |
| <code>file_urls</code> | <code>list&#91;str&#93; \| None</code> | Use `file_urls[]` to have Dropbox Sign download the file(s) to send for signature.<br><br>This endpoint requires either **files** or **file_urls[]**, but not both.<br>**Default**: <code>None</code> |
| <code>signers</code> | <code>list&#91;[SubSignatureRequestSigner](dropbox_sign_api/models/sub_signature_request_signer.py) \| [SubSignatureRequestSignerDict](dropbox_sign_api/models/sub_signature_request_signer.py)&#93; \| None</code> | Add Signers to your Signature Request.<br><br>This endpoint requires either **signers** or **grouped_signers**, but not both.<br>**Default**: <code>None</code> |
| <code>grouped_signers</code> | <code>list&#91;[SubSignatureRequestGroupedSigners](dropbox_sign_api/models/sub_signature_request_grouped_signers.py) \| [SubSignatureRequestGroupedSignersDict](dropbox_sign_api/models/sub_signature_request_grouped_signers.py)&#93; \| None</code> | Add Grouped Signers to your Signature Request.<br><br>This endpoint requires either **signers** or **grouped_signers**, but not both.<br>**Default**: <code>None</code> |
| <code>allow_decline</code> | <code>bool \| None</code> | Allows signers to decline to sign a document if `true`. Defaults to `false`.<br>**Default**: <code>False</code> |
| <code>allow_reassign</code> | <code>bool \| None</code> | Allows signers to reassign their signature requests to other signers if set to `true`. Defaults to `false`.<br><br>**NOTE:** Only available for Premium plan and higher.<br>**Default**: <code>False</code> |
| <code>attachments</code> | <code>list&#91;[SubAttachment](dropbox_sign_api/models/sub_attachment.py) \| [SubAttachmentDict](dropbox_sign_api/models/sub_attachment.py)&#93; \| None</code> | A list describing the attachments<br>**Default**: <code>None</code> |
| <code>cc_email_addresses</code> | <code>list&#91;EmailStr&#93; \| None</code> | The email addresses that should be CCed.<br>**Default**: <code>None</code> |
| <code>client_id</code> | <code>str \| None</code> | The client id of the API App you want to associate with this request. Used to apply the branding and callback url defined for the app.<br>**Default**: <code>None</code> |
| <code>custom_fields</code> | <code>list&#91;[SubCustomField](dropbox_sign_api/models/sub_custom_field.py) \| [SubCustomFieldDict](dropbox_sign_api/models/sub_custom_field.py)&#93; \| None</code> | When used together with merge fields, `custom_fields` allows users to add pre-filled data to their signature requests.<br><br>Pre-filled data can be used with "send-once" signature requests by adding merge fields with `form_fields_per_document` or [Text Tags](https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro) while passing values back with `custom_fields` together in one API call.<br><br>For using pre-filled on repeatable signature requests, merge fields are added to templates in the Dropbox Sign UI or by calling [/template/create_embedded_draft](/api/reference/operation/templateCreateEmbeddedDraft) and then passing `custom_fields` on subsequent signature requests referencing that template.<br>**Default**: <code>None</code> |
| <code>field_options</code> | <code>[SubFieldOptions](dropbox_sign_api/models/sub_field_options.py) \| [SubFieldOptionsDict](dropbox_sign_api/models/sub_field_options.py) \| None</code> | This allows the requester to specify field options for a signature request.<br>**Default**: <code>None</code> |
| <code>form_field_groups</code> | <code>list&#91;[SubFormFieldGroup](dropbox_sign_api/models/sub_form_field_group.py) \| [SubFormFieldGroupDict](dropbox_sign_api/models/sub_form_field_group.py)&#93; \| None</code> | Group information for fields defined in `form_fields_per_document`. String-indexed JSON array with `group_label` and `requirement` keys. `form_fields_per_document` must contain fields referencing a group defined in `form_field_groups`.<br>**Default**: <code>None</code> |
| <code>form_field_rules</code> | <code>list&#91;[SubFormFieldRule](dropbox_sign_api/models/sub_form_field_rule.py) \| [SubFormFieldRuleDict](dropbox_sign_api/models/sub_form_field_rule.py)&#93; \| None</code> | Conditional Logic rules for fields defined in `form_fields_per_document`.<br>**Default**: <code>None</code> |
| <code>form_fields_per_document</code> | <code>list&#91;[SubFormFieldsPerDocumentBase](dropbox_sign_api/models/unions/sub_form_fields_per_document_base.py) \| [SubFormFieldsPerDocumentBaseDict](dropbox_sign_api/models/unions/sub_form_fields_per_document_base.py)&#93; \| None</code> | The fields that should appear on the document, expressed as an array of objects. (For more details you can read about it here: [Using Form Fields per Document](/docs/openapi/form-fields-per-document).)<br><br>**NOTE:** Fields like **text**, **dropdown**, **checkbox**, **radio**, and **hyperlink** have additional required and optional parameters. Check out the list of [additional parameters](/api/reference/constants/#form-fields-per-document) for these field types.<br><br>* Text Field use `SubFormFieldsPerDocumentText`<br>* Dropdown Field use `SubFormFieldsPerDocumentDropdown`<br>* Hyperlink Field use `SubFormFieldsPerDocumentHyperlink`<br>* Checkbox Field use `SubFormFieldsPerDocumentCheckbox`<br>* Radio Field use `SubFormFieldsPerDocumentRadio`<br>* Signature Field use `SubFormFieldsPerDocumentSignature`<br>* Date Signed Field use `SubFormFieldsPerDocumentDateSigned`<br>* Initials Field use `SubFormFieldsPerDocumentInitials`<br>* Text Merge Field use `SubFormFieldsPerDocumentTextMerge`<br>* Checkbox Merge Field use `SubFormFieldsPerDocumentCheckboxMerge`<br>**Default**: <code>None</code> |
| <code>hide_text_tags</code> | <code>bool \| None</code> | Enables automatic Text Tag removal when set to true.<br><br>**NOTE:** Removing text tags this way can cause unwanted clipping. We recommend leaving this setting on `false` and instead hiding your text tags using white text or a similar approach. See the [Text Tags Walkthrough](https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro) for more information.<br>**Default**: <code>False</code> |
| <code>is_eid</code> | <code>bool \| None</code> | Send with a value of `true` if you wish to enable<br>[electronic identification (eID)](https://www.hellosign.com/features/electronic-id),<br>which requires the signer to verify their identity with an eID provider to sign a document.<br><br>**NOTE:** You need the eID add-on to use this feature. Please [contact sales](https://sign.dropbox.com/form/contact-sales) for more information. Cannot be used in `test_mode`. Only works on requests with one signer.<br>**Default**: <code>False</code> |
| <code>message</code> | <code>str \| None</code> | The custom message in the email that will be sent to the signers.<br>**Default**: <code>None</code> |
| <code>metadata</code> | <code>dict&#91;str, Any&#93; \| None</code> | Key-value data that should be attached to the signature request. This metadata is included in all API responses and events involving the signature request. For example, use the metadata field to store a signer's order number for look up when receiving events for the signature request.<br><br>Each request can include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and values up to 1000 characters long.<br>**Default**: <code>None</code> |
| <code>signing_options</code> | <code>[SubSigningOptions](dropbox_sign_api/models/sub_signing_options.py) \| [SubSigningOptionsDict](dropbox_sign_api/models/sub_signing_options.py) \| None</code> | This allows the requester to specify the types allowed for creating a signature and specify another signing options.<br><br>**NOTE:** If `signing_options` are not defined in the request, the allowed types will default to those specified in the account settings.<br><br>**NOTE:** If `force_advanced_signature_details` is set, allowed types has to be defined too.<br>**Default**: <code>None</code> |
| <code>signing_redirect_url</code> | <code>str \| None</code> | The URL you want signers redirected to after they successfully sign.<br>**Default**: <code>None</code> |
| <code>subject</code> | <code>str \| None</code> | The subject in the email that will be sent to the signers.<br>**Default**: <code>None</code> |
| <code>test_mode</code> | <code>bool \| None</code> | Whether this is a test, the signature request will not be legally binding if set to `true`. Defaults to `false`.<br>**Default**: <code>False</code> |
| <code>title</code> | <code>str \| None</code> | The title you want to assign to the SignatureRequest.<br>**Default**: <code>None</code> |
| <code>use_text_tags</code> | <code>bool \| None</code> | Send with a value of `true` if you wish to enable [Text Tags](https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro) parsing in your document. Defaults to disabled, or `false`.<br>**Default**: <code>False</code> |
| <code>ignore_text_tags_extraction_errors</code> | <code>bool \| None</code> | Sent with a value of `true` to ignore the validation errors from text tags extraction. Defaults to `false`.<br>**Default**: <code>False</code> |
| <code>expires_at</code> | <code>int \| None</code> | When the signature request will expire. Unsigned signatures will be moved to the expired status, and no longer signable. See [Signature Request Expiration Date](https://developers.hellosign.com/docs/signature-request/expiration/) for details.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[SignatureRequestGetResponse](dropbox_sign_api/models/signature_request_get_response.py), [SignatureRequestEditErrorBody](dropbox_sign_api/errors/signature_request_edit_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SignatureRequestGetResponse](dropbox_sign_api/models/signature_request_get_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[SignatureRequestEditErrorBody](dropbox_sign_api/errors/signature_request_edit_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def signature_request_edit_embedded(signature_request_id: str, client_id: str, *, files: FileInput | None = None, file_urls: list[str] | None = None, signers: list[SubSignatureRequestSigner | SubSignatureRequestSignerDict] | None = None, grouped_signers: list[SubSignatureRequestGroupedSigners | SubSignatureRequestGroupedSignersDict] | None = None, allow_decline: bool | None = False, allow_reassign: bool | None = False, attachments: list[SubAttachment | SubAttachmentDict] | None = None, cc_email_addresses: list[EmailStr] | None = None, custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None, field_options: SubFieldOptions | SubFieldOptionsDict | None = None, form_field_groups: list[SubFormFieldGroup | SubFormFieldGroupDict] | None = None, form_field_rules: list[SubFormFieldRule | SubFormFieldRuleDict] | None = None, form_fields_per_document: list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None = None, hide_text_tags: bool | None = False, message: str | None = None, metadata: dict[str, Any] | None = None, signing_options: SubSigningOptions | SubSigningOptionsDict | None = None, subject: str | None = None, test_mode: bool | None = False, title: str | None = None, use_text_tags: bool | None = False, ignore_text_tags_extraction_errors: bool | None = False, populate_auto_fill_fields: bool | None = False, expires_at: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SignatureRequestGetResponse, SignatureRequestEditEmbeddedErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Edits a SignatureRequest with the submitted documents to be signed in an embedded iFrame. If form_fields_per_document is not specified, a signature page will be affixed where all signers will be required to add their signature, signifying their agreement to all contained documents. Note that embedded signature requests can only be signed in embedded iFrames whereas normal signature requests can only be signed on Dropbox Sign.

**NOTE:** Edit and resend *will* deduct your signature request quota.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.signature_request.with_raw_response.signature_request_edit_embedded(
    "fa5c8a0b0f492d768749333ad6fcc214c111e967", "some example string"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SignatureRequestGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SignatureRequestEditEmbeddedErrorBody
```

**Async**

```python
result = await async_client.signature_request.with_raw_response.signature_request_edit_embedded(
    "fa5c8a0b0f492d768749333ad6fcc214c111e967", "some example string"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SignatureRequestGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SignatureRequestEditEmbeddedErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>signature_request_id</code> | <code>str</code> | The id of the SignatureRequest to edit. |
| <code>client_id</code> | <code>str</code> | Client id of the app you're using to create this embedded signature request. Used for security purposes. |
| <code>files</code> | <code>FileInput \| None</code> | Use `files[]` to indicate the uploaded file(s) to send for signature.<br><br>This endpoint requires either **files** or **file_urls[]**, but not both.<br>**Default**: <code>None</code> |
| <code>file_urls</code> | <code>list&#91;str&#93; \| None</code> | Use `file_urls[]` to have Dropbox Sign download the file(s) to send for signature.<br><br>This endpoint requires either **files** or **file_urls[]**, but not both.<br>**Default**: <code>None</code> |
| <code>signers</code> | <code>list&#91;[SubSignatureRequestSigner](dropbox_sign_api/models/sub_signature_request_signer.py) \| [SubSignatureRequestSignerDict](dropbox_sign_api/models/sub_signature_request_signer.py)&#93; \| None</code> | Add Signers to your Signature Request.<br><br>This endpoint requires either **signers** or **grouped_signers**, but not both.<br>**Default**: <code>None</code> |
| <code>grouped_signers</code> | <code>list&#91;[SubSignatureRequestGroupedSigners](dropbox_sign_api/models/sub_signature_request_grouped_signers.py) \| [SubSignatureRequestGroupedSignersDict](dropbox_sign_api/models/sub_signature_request_grouped_signers.py)&#93; \| None</code> | Add Grouped Signers to your Signature Request.<br><br>This endpoint requires either **signers** or **grouped_signers**, but not both.<br>**Default**: <code>None</code> |
| <code>allow_decline</code> | <code>bool \| None</code> | Allows signers to decline to sign a document if `true`. Defaults to `false`.<br>**Default**: <code>False</code> |
| <code>allow_reassign</code> | <code>bool \| None</code> | Allows signers to reassign their signature requests to other signers if set to `true`. Defaults to `false`.<br><br>**NOTE:** Only available for Premium plan.<br>**Default**: <code>False</code> |
| <code>attachments</code> | <code>list&#91;[SubAttachment](dropbox_sign_api/models/sub_attachment.py) \| [SubAttachmentDict](dropbox_sign_api/models/sub_attachment.py)&#93; \| None</code> | A list describing the attachments<br>**Default**: <code>None</code> |
| <code>cc_email_addresses</code> | <code>list&#91;EmailStr&#93; \| None</code> | The email addresses that should be CCed.<br>**Default**: <code>None</code> |
| <code>custom_fields</code> | <code>list&#91;[SubCustomField](dropbox_sign_api/models/sub_custom_field.py) \| [SubCustomFieldDict](dropbox_sign_api/models/sub_custom_field.py)&#93; \| None</code> | When used together with merge fields, `custom_fields` allows users to add pre-filled data to their signature requests.<br><br>Pre-filled data can be used with "send-once" signature requests by adding merge fields with `form_fields_per_document` or [Text Tags](https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro) while passing values back with `custom_fields` together in one API call.<br><br>For using pre-filled on repeatable signature requests, merge fields are added to templates in the Dropbox Sign UI or by calling [/template/create_embedded_draft](/api/reference/operation/templateCreateEmbeddedDraft) and then passing `custom_fields` on subsequent signature requests referencing that template.<br>**Default**: <code>None</code> |
| <code>field_options</code> | <code>[SubFieldOptions](dropbox_sign_api/models/sub_field_options.py) \| [SubFieldOptionsDict](dropbox_sign_api/models/sub_field_options.py) \| None</code> | This allows the requester to specify field options for a signature request.<br>**Default**: <code>None</code> |
| <code>form_field_groups</code> | <code>list&#91;[SubFormFieldGroup](dropbox_sign_api/models/sub_form_field_group.py) \| [SubFormFieldGroupDict](dropbox_sign_api/models/sub_form_field_group.py)&#93; \| None</code> | Group information for fields defined in `form_fields_per_document`. String-indexed JSON array with `group_label` and `requirement` keys. `form_fields_per_document` must contain fields referencing a group defined in `form_field_groups`.<br>**Default**: <code>None</code> |
| <code>form_field_rules</code> | <code>list&#91;[SubFormFieldRule](dropbox_sign_api/models/sub_form_field_rule.py) \| [SubFormFieldRuleDict](dropbox_sign_api/models/sub_form_field_rule.py)&#93; \| None</code> | Conditional Logic rules for fields defined in `form_fields_per_document`.<br>**Default**: <code>None</code> |
| <code>form_fields_per_document</code> | <code>list&#91;[SubFormFieldsPerDocumentBase](dropbox_sign_api/models/unions/sub_form_fields_per_document_base.py) \| [SubFormFieldsPerDocumentBaseDict](dropbox_sign_api/models/unions/sub_form_fields_per_document_base.py)&#93; \| None</code> | The fields that should appear on the document, expressed as an array of objects. (For more details you can read about it here: [Using Form Fields per Document](/docs/openapi/form-fields-per-document).)<br><br>**NOTE:** Fields like **text**, **dropdown**, **checkbox**, **radio**, and **hyperlink** have additional required and optional parameters. Check out the list of [additional parameters](/api/reference/constants/#form-fields-per-document) for these field types.<br><br>* Text Field use `SubFormFieldsPerDocumentText`<br>* Dropdown Field use `SubFormFieldsPerDocumentDropdown`<br>* Hyperlink Field use `SubFormFieldsPerDocumentHyperlink`<br>* Checkbox Field use `SubFormFieldsPerDocumentCheckbox`<br>* Radio Field use `SubFormFieldsPerDocumentRadio`<br>* Signature Field use `SubFormFieldsPerDocumentSignature`<br>* Date Signed Field use `SubFormFieldsPerDocumentDateSigned`<br>* Initials Field use `SubFormFieldsPerDocumentInitials`<br>* Text Merge Field use `SubFormFieldsPerDocumentTextMerge`<br>* Checkbox Merge Field use `SubFormFieldsPerDocumentCheckboxMerge`<br>**Default**: <code>None</code> |
| <code>hide_text_tags</code> | <code>bool \| None</code> | Enables automatic Text Tag removal when set to true.<br><br>**NOTE:** Removing text tags this way can cause unwanted clipping. We recommend leaving this setting on `false` and instead hiding your text tags using white text or a similar approach. See the [Text Tags Walkthrough](https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro) for more information.<br>**Default**: <code>False</code> |
| <code>message</code> | <code>str \| None</code> | The custom message in the email that will be sent to the signers.<br>**Default**: <code>None</code> |
| <code>metadata</code> | <code>dict&#91;str, Any&#93; \| None</code> | Key-value data that should be attached to the signature request. This metadata is included in all API responses and events involving the signature request. For example, use the metadata field to store a signer's order number for look up when receiving events for the signature request.<br><br>Each request can include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and values up to 1000 characters long.<br>**Default**: <code>None</code> |
| <code>signing_options</code> | <code>[SubSigningOptions](dropbox_sign_api/models/sub_signing_options.py) \| [SubSigningOptionsDict](dropbox_sign_api/models/sub_signing_options.py) \| None</code> | This allows the requester to specify the types allowed for creating a signature and specify another signing options.<br><br>**NOTE:** If `signing_options` are not defined in the request, the allowed types will default to those specified in the account settings.<br><br>**NOTE:** If `force_advanced_signature_details` is set, allowed types has to be defined too.<br>**Default**: <code>None</code> |
| <code>subject</code> | <code>str \| None</code> | The subject in the email that will be sent to the signers.<br>**Default**: <code>None</code> |
| <code>test_mode</code> | <code>bool \| None</code> | Whether this is a test, the signature request will not be legally binding if set to `true`. Defaults to `false`.<br>**Default**: <code>False</code> |
| <code>title</code> | <code>str \| None</code> | The title you want to assign to the SignatureRequest.<br>**Default**: <code>None</code> |
| <code>use_text_tags</code> | <code>bool \| None</code> | Send with a value of `true` if you wish to enable [Text Tags](https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro) parsing in your document. Defaults to disabled, or `false`.<br>**Default**: <code>False</code> |
| <code>ignore_text_tags_extraction_errors</code> | <code>bool \| None</code> | Sent with a value of `true` to ignore the validation errors from text tags extraction. Defaults to `false`.<br>**Default**: <code>False</code> |
| <code>populate_auto_fill_fields</code> | <code>bool \| None</code> | Controls whether [auto fill fields](https://faq.hellosign.com/hc/en-us/articles/360051467511-Auto-Fill-Fields) can automatically populate a signer's information during signing.<br><br>**NOTE:** Keep your signer's information safe by ensuring that the _signer on your signature request is the intended party_ before using this feature.<br>**Default**: <code>False</code> |
| <code>expires_at</code> | <code>int \| None</code> | When the signature request will expire. Unsigned signatures will be moved to the expired status, and no longer signable. See [Signature Request Expiration Date](https://developers.hellosign.com/docs/signature-request/expiration/) for details.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[SignatureRequestGetResponse](dropbox_sign_api/models/signature_request_get_response.py), [SignatureRequestEditEmbeddedErrorBody](dropbox_sign_api/errors/signature_request_edit_embedded_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SignatureRequestGetResponse](dropbox_sign_api/models/signature_request_get_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[SignatureRequestEditEmbeddedErrorBody](dropbox_sign_api/errors/signature_request_edit_embedded_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def signature_request_edit_embedded_with_template(signature_request_id: str, template_ids: list[str], client_id: str, signers: list[SubSignatureRequestTemplateSigner | SubSignatureRequestTemplateSignerDict], *, allow_decline: bool | None = False, ccs: list[SubCc | SubCcDict] | None = None, custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None, files: FileInput | None = None, file_urls: list[str] | None = None, message: str | None = None, metadata: dict[str, Any] | None = None, signing_options: SubSigningOptions | SubSigningOptionsDict | None = None, subject: str | None = None, test_mode: bool | None = False, title: str | None = None, populate_auto_fill_fields: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SignatureRequestGetResponse, SignatureRequestEditEmbeddedWithTemplateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Edits a SignatureRequest based on the given Template(s) to be signed in an embedded iFrame. Note that embedded signature requests can only be signed in embedded iFrames whereas normal signature requests can only be signed on Dropbox Sign.

**NOTE:** Edit and resend *will* deduct your signature request quota.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.signature_request.with_raw_response.signature_request_edit_embedded_with_template(
    "fa5c8a0b0f492d768749333ad6fcc214c111e967",
    ["some example string"],
    "some example string",
    [
        SubSignatureRequestTemplateSigner(
            role="some example string", name="some example string", email_address="user@example.com"
        ),
    ],
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SignatureRequestGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SignatureRequestEditEmbeddedWithTemplateErrorBody
```

**Async**

```python
result = await async_client.signature_request.with_raw_response.signature_request_edit_embedded_with_template(
    "fa5c8a0b0f492d768749333ad6fcc214c111e967",
    ["some example string"],
    "some example string",
    [
        SubSignatureRequestTemplateSigner(
            role="some example string", name="some example string", email_address="user@example.com"
        ),
    ],
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SignatureRequestGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SignatureRequestEditEmbeddedWithTemplateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>signature_request_id</code> | <code>str</code> | The id of the SignatureRequest to edit. |
| <code>template_ids</code> | <code>list&#91;str&#93;</code> | Use `template_ids` to create a SignatureRequest from one or more templates, in the order in which the template will be used. |
| <code>client_id</code> | <code>str</code> | Client id of the app you're using to create this embedded signature request. Used for security purposes. |
| <code>signers</code> | <code>list&#91;[SubSignatureRequestTemplateSigner](dropbox_sign_api/models/sub_signature_request_template_signer.py) \| [SubSignatureRequestTemplateSignerDict](dropbox_sign_api/models/sub_signature_request_template_signer.py)&#93;</code> | Add Signers to your Templated-based Signature Request. |
| <code>allow_decline</code> | <code>bool \| None</code> | Allows signers to decline to sign a document if `true`. Defaults to `false`.<br>**Default**: <code>False</code> |
| <code>ccs</code> | <code>list&#91;[SubCc](dropbox_sign_api/models/sub_cc.py) \| [SubCcDict](dropbox_sign_api/models/sub_cc.py)&#93; \| None</code> | Add CC email recipients. Required when a CC role exists for the Template.<br>**Default**: <code>None</code> |
| <code>custom_fields</code> | <code>list&#91;[SubCustomField](dropbox_sign_api/models/sub_custom_field.py) \| [SubCustomFieldDict](dropbox_sign_api/models/sub_custom_field.py)&#93; \| None</code> | An array defining values and options for custom fields. Required when a custom field exists in the Template.<br>**Default**: <code>None</code> |
| <code>files</code> | <code>FileInput \| None</code> | Use `files[]` to indicate the uploaded file(s) to send for signature.<br><br>This endpoint requires either **files** or **file_urls[]**, but not both.<br>**Default**: <code>None</code> |
| <code>file_urls</code> | <code>list&#91;str&#93; \| None</code> | Use `file_urls[]` to have Dropbox Sign download the file(s) to send for signature.<br><br>This endpoint requires either **files** or **file_urls[]**, but not both.<br>**Default**: <code>None</code> |
| <code>message</code> | <code>str \| None</code> | The custom message in the email that will be sent to the signers.<br>**Default**: <code>None</code> |
| <code>metadata</code> | <code>dict&#91;str, Any&#93; \| None</code> | Key-value data that should be attached to the signature request. This metadata is included in all API responses and events involving the signature request. For example, use the metadata field to store a signer's order number for look up when receiving events for the signature request.<br><br>Each request can include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and values up to 1000 characters long.<br>**Default**: <code>None</code> |
| <code>signing_options</code> | <code>[SubSigningOptions](dropbox_sign_api/models/sub_signing_options.py) \| [SubSigningOptionsDict](dropbox_sign_api/models/sub_signing_options.py) \| None</code> | This allows the requester to specify the types allowed for creating a signature and specify another signing options.<br><br>**NOTE:** If `signing_options` are not defined in the request, the allowed types will default to those specified in the account settings.<br><br>**NOTE:** If `force_advanced_signature_details` is set, allowed types has to be defined too.<br>**Default**: <code>None</code> |
| <code>subject</code> | <code>str \| None</code> | The subject in the email that will be sent to the signers.<br>**Default**: <code>None</code> |
| <code>test_mode</code> | <code>bool \| None</code> | Whether this is a test, the signature request will not be legally binding if set to `true`. Defaults to `false`.<br>**Default**: <code>False</code> |
| <code>title</code> | <code>str \| None</code> | The title you want to assign to the SignatureRequest.<br>**Default**: <code>None</code> |
| <code>populate_auto_fill_fields</code> | <code>bool \| None</code> | Controls whether [auto fill fields](https://faq.hellosign.com/hc/en-us/articles/360051467511-Auto-Fill-Fields) can automatically populate a signer's information during signing.<br><br>**NOTE:** Keep your signer's information safe by ensuring that the _signer on your signature request is the intended party_ before using this feature.<br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[SignatureRequestGetResponse](dropbox_sign_api/models/signature_request_get_response.py), [SignatureRequestEditEmbeddedWithTemplateErrorBody](dropbox_sign_api/errors/signature_request_edit_embedded_with_template_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SignatureRequestGetResponse](dropbox_sign_api/models/signature_request_get_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[SignatureRequestEditEmbeddedWithTemplateErrorBody](dropbox_sign_api/errors/signature_request_edit_embedded_with_template_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def signature_request_edit_with_template(signature_request_id: str, template_ids: list[str], signers: list[SubSignatureRequestTemplateSigner | SubSignatureRequestTemplateSignerDict], *, allow_decline: bool | None = False, ccs: list[SubCc | SubCcDict] | None = None, client_id: str | None = None, custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None, files: FileInput | None = None, file_urls: list[str] | None = None, is_eid: bool | None = False, message: str | None = None, metadata: dict[str, Any] | None = None, signing_options: SubSigningOptions | SubSigningOptionsDict | None = None, signing_redirect_url: str | None = None, subject: str | None = None, test_mode: bool | None = False, title: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SignatureRequestGetResponse, SignatureRequestEditWithTemplateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Edits and sends a SignatureRequest based off of the Template(s) specified with the template_ids parameter.

**NOTE:** Edit and resend *will* deduct your signature request quota.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.signature_request.with_raw_response.signature_request_edit_with_template(
    "fa5c8a0b0f492d768749333ad6fcc214c111e967",
    ["some example string"],
    [
        SubSignatureRequestTemplateSigner(
            role="some example string", name="some example string", email_address="user@example.com"
        ),
    ],
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SignatureRequestGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SignatureRequestEditWithTemplateErrorBody
```

**Async**

```python
result = await async_client.signature_request.with_raw_response.signature_request_edit_with_template(
    "fa5c8a0b0f492d768749333ad6fcc214c111e967",
    ["some example string"],
    [
        SubSignatureRequestTemplateSigner(
            role="some example string", name="some example string", email_address="user@example.com"
        ),
    ],
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SignatureRequestGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SignatureRequestEditWithTemplateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>signature_request_id</code> | <code>str</code> | The id of the SignatureRequest to edit. |
| <code>template_ids</code> | <code>list&#91;str&#93;</code> | Use `template_ids` to create a SignatureRequest from one or more templates, in the order in which the template will be used. |
| <code>signers</code> | <code>list&#91;[SubSignatureRequestTemplateSigner](dropbox_sign_api/models/sub_signature_request_template_signer.py) \| [SubSignatureRequestTemplateSignerDict](dropbox_sign_api/models/sub_signature_request_template_signer.py)&#93;</code> | Add Signers to your Templated-based Signature Request. |
| <code>allow_decline</code> | <code>bool \| None</code> | Allows signers to decline to sign a document if `true`. Defaults to `false`.<br>**Default**: <code>False</code> |
| <code>ccs</code> | <code>list&#91;[SubCc](dropbox_sign_api/models/sub_cc.py) \| [SubCcDict](dropbox_sign_api/models/sub_cc.py)&#93; \| None</code> | Add CC email recipients. Required when a CC role exists for the Template.<br>**Default**: <code>None</code> |
| <code>client_id</code> | <code>str \| None</code> | Client id of the app to associate with the signature request. Used to apply the branding and callback url defined for the app.<br>**Default**: <code>None</code> |
| <code>custom_fields</code> | <code>list&#91;[SubCustomField](dropbox_sign_api/models/sub_custom_field.py) \| [SubCustomFieldDict](dropbox_sign_api/models/sub_custom_field.py)&#93; \| None</code> | An array defining values and options for custom fields. Required when a custom field exists in the Template.<br>**Default**: <code>None</code> |
| <code>files</code> | <code>FileInput \| None</code> | Use `files[]` to indicate the uploaded file(s) to send for signature.<br><br>This endpoint requires either **files** or **file_urls[]**, but not both.<br>**Default**: <code>None</code> |
| <code>file_urls</code> | <code>list&#91;str&#93; \| None</code> | Use `file_urls[]` to have Dropbox Sign download the file(s) to send for signature.<br><br>This endpoint requires either **files** or **file_urls[]**, but not both.<br>**Default**: <code>None</code> |
| <code>is_eid</code> | <code>bool \| None</code> | Send with a value of `true` if you wish to enable<br>[electronic identification (eID)](https://www.hellosign.com/features/electronic-id),<br>which requires the signer to verify their identity with an eID provider to sign a document.<br><br>**NOTE:** You need the eID add-on to use this feature. Please [contact sales](https://sign.dropbox.com/form/contact-sales) for more information. Cannot be used in `test_mode`. Only works on requests with one signer.<br>**Default**: <code>False</code> |
| <code>message</code> | <code>str \| None</code> | The custom message in the email that will be sent to the signers.<br>**Default**: <code>None</code> |
| <code>metadata</code> | <code>dict&#91;str, Any&#93; \| None</code> | Key-value data that should be attached to the signature request. This metadata is included in all API responses and events involving the signature request. For example, use the metadata field to store a signer's order number for look up when receiving events for the signature request.<br><br>Each request can include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and values up to 1000 characters long.<br>**Default**: <code>None</code> |
| <code>signing_options</code> | <code>[SubSigningOptions](dropbox_sign_api/models/sub_signing_options.py) \| [SubSigningOptionsDict](dropbox_sign_api/models/sub_signing_options.py) \| None</code> | This allows the requester to specify the types allowed for creating a signature and specify another signing options.<br><br>**NOTE:** If `signing_options` are not defined in the request, the allowed types will default to those specified in the account settings.<br><br>**NOTE:** If `force_advanced_signature_details` is set, allowed types has to be defined too.<br>**Default**: <code>None</code> |
| <code>signing_redirect_url</code> | <code>str \| None</code> | The URL you want signers redirected to after they successfully sign.<br>**Default**: <code>None</code> |
| <code>subject</code> | <code>str \| None</code> | The subject in the email that will be sent to the signers.<br>**Default**: <code>None</code> |
| <code>test_mode</code> | <code>bool \| None</code> | Whether this is a test, the signature request will not be legally binding if set to `true`. Defaults to `false`.<br>**Default**: <code>False</code> |
| <code>title</code> | <code>str \| None</code> | The title you want to assign to the SignatureRequest.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[SignatureRequestGetResponse](dropbox_sign_api/models/signature_request_get_response.py), [SignatureRequestEditWithTemplateErrorBody](dropbox_sign_api/errors/signature_request_edit_with_template_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SignatureRequestGetResponse](dropbox_sign_api/models/signature_request_get_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[SignatureRequestEditWithTemplateErrorBody](dropbox_sign_api/errors/signature_request_edit_with_template_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def signature_request_files(signature_request_id: str, *, file_type: FileTypeOrStr | None = FileType.PDF, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, SignatureRequestFilesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Obtain a copy of the current documents specified by the `signature_request_id` parameter. Returns a PDF or ZIP file.

If the files are currently being prepared, a status code of `409` will be returned instead.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.signature_request.with_raw_response.signature_request_files("fa5c8a0b0f492d768749333ad6fcc214c111e967")
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SignatureRequestFilesErrorBody
```

**Async**

```python
result = await async_client.signature_request.with_raw_response.signature_request_files(
    "fa5c8a0b0f492d768749333ad6fcc214c111e967"
)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SignatureRequestFilesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>signature_request_id</code> | <code>str</code> | The id of the SignatureRequest to retrieve. |
| <code>file_type</code> | <code>[FileTypeOrStr](dropbox_sign_api/models/enums/file_type.py) \| None</code> | Set to `pdf` for a single merged document or `zip` for a collection of individual documents.<br>**Default**: <code>FileType.PDF</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;None, [SignatureRequestFilesErrorBody](dropbox_sign_api/errors/signature_request_files_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[SignatureRequestFilesErrorBody](dropbox_sign_api/errors/signature_request_files_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def signature_request_files_as_data_uri(signature_request_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FileResponseDataUri, SignatureRequestFilesAsDataUriErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Obtain a copy of the current documents specified by the `signature_request_id` parameter. Returns a JSON object with a `data_uri` representing the base64 encoded file (PDFs only).

If the files are currently being prepared, a status code of `409` will be returned instead.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.signature_request.with_raw_response.signature_request_files_as_data_uri(
    "fa5c8a0b0f492d768749333ad6fcc214c111e967"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FileResponseDataUri
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SignatureRequestFilesAsDataUriErrorBody
```

**Async**

```python
result = await async_client.signature_request.with_raw_response.signature_request_files_as_data_uri(
    "fa5c8a0b0f492d768749333ad6fcc214c111e967"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FileResponseDataUri
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SignatureRequestFilesAsDataUriErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>signature_request_id</code> | <code>str</code> | The id of the SignatureRequest to retrieve. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[FileResponseDataUri](dropbox_sign_api/models/file_response_data_uri.py), [SignatureRequestFilesAsDataUriErrorBody](dropbox_sign_api/errors/signature_request_files_as_data_uri_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[FileResponseDataUri](dropbox_sign_api/models/file_response_data_uri.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[SignatureRequestFilesAsDataUriErrorBody](dropbox_sign_api/errors/signature_request_files_as_data_uri_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def signature_request_files_as_file_url(signature_request_id: str, *, force_download: int | None = 1, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FileResponseModel, SignatureRequestFilesAsFileUrlErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Obtain a copy of the current documents specified by the `signature_request_id` parameter. Returns a JSON object with a url to the file (PDFs only).

If the files are currently being prepared, a status code of `409` will be returned instead.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.signature_request.with_raw_response.signature_request_files_as_file_url(
    "fa5c8a0b0f492d768749333ad6fcc214c111e967"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FileResponseModel
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SignatureRequestFilesAsFileUrlErrorBody
```

**Async**

```python
result = await async_client.signature_request.with_raw_response.signature_request_files_as_file_url(
    "fa5c8a0b0f492d768749333ad6fcc214c111e967"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FileResponseModel
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SignatureRequestFilesAsFileUrlErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>signature_request_id</code> | <code>str</code> | The id of the SignatureRequest to retrieve. |
| <code>force_download</code> | <code>int \| None</code> | By default when opening the `file_url` a browser will download the PDF and save it locally. When set to `0` the PDF file will be displayed in the browser.<br>**Default**: <code>1</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[FileResponseModel](dropbox_sign_api/models/file_response_model.py), [SignatureRequestFilesAsFileUrlErrorBody](dropbox_sign_api/errors/signature_request_files_as_file_url_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[FileResponseModel](dropbox_sign_api/models/file_response_model.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[SignatureRequestFilesAsFileUrlErrorBody](dropbox_sign_api/errors/signature_request_files_as_file_url_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def signature_request_get(signature_request_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SignatureRequestGetResponse, SignatureRequestGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the status of the SignatureRequest specified by the `signature_request_id` parameter.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.signature_request.with_raw_response.signature_request_get("fa5c8a0b0f492d768749333ad6fcc214c111e967")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SignatureRequestGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SignatureRequestGetErrorBody
```

**Async**

```python
result = await async_client.signature_request.with_raw_response.signature_request_get(
    "fa5c8a0b0f492d768749333ad6fcc214c111e967"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SignatureRequestGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SignatureRequestGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>signature_request_id</code> | <code>str</code> | The id of the SignatureRequest to retrieve. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[SignatureRequestGetResponse](dropbox_sign_api/models/signature_request_get_response.py), [SignatureRequestGetErrorBody](dropbox_sign_api/errors/signature_request_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SignatureRequestGetResponse](dropbox_sign_api/models/signature_request_get_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[SignatureRequestGetErrorBody](dropbox_sign_api/errors/signature_request_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def signature_request_list(*, account_id: str | None = None, page: int | None = 1, page_size: int | None = 20, query: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SignatureRequestListResponse, SignatureRequestListErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a list of SignatureRequests that you can access. This includes SignatureRequests you have sent as well as received, but not ones that you have been CCed on.

Take a look at our [search guide](/api/reference/search/) to learn more about querying signature requests.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.signature_request.with_raw_response.signature_request_list(page=1)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SignatureRequestListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SignatureRequestListErrorBody
```

**Async**

```python
result = await async_client.signature_request.with_raw_response.signature_request_list(page=1)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SignatureRequestListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SignatureRequestListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account_id</code> | <code>str \| None</code> | Which account to return SignatureRequests for. Must be a team member. Use `all` to indicate all team members. Defaults to your account.<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Which page number of the SignatureRequest List to return. Defaults to `1`.<br>**Default**: <code>1</code> |
| <code>page_size</code> | <code>int \| None</code> | Number of objects to be returned per page. Must be between `1` and `100`. Default is `20`.<br>**Default**: <code>20</code> |
| <code>query</code> | <code>str \| None</code> | String that includes search terms and/or fields to be used to filter the SignatureRequest objects.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[SignatureRequestListResponse](dropbox_sign_api/models/signature_request_list_response.py), [SignatureRequestListErrorBody](dropbox_sign_api/errors/signature_request_list_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SignatureRequestListResponse](dropbox_sign_api/models/signature_request_list_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[SignatureRequestListErrorBody](dropbox_sign_api/errors/signature_request_list_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def signature_request_release_hold(signature_request_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SignatureRequestGetResponse, SignatureRequestReleaseHoldErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Releases a held SignatureRequest that was claimed and prepared from an [UnclaimedDraft](/api/reference/tag/Unclaimed-Draft). The owner of the Draft must indicate at Draft creation that the SignatureRequest created from the Draft should be held. Releasing the SignatureRequest will send requests to all signers.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.signature_request.with_raw_response.signature_request_release_hold(
    "fa5c8a0b0f492d768749333ad6fcc214c111e967"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SignatureRequestGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SignatureRequestReleaseHoldErrorBody
```

**Async**

```python
result = await async_client.signature_request.with_raw_response.signature_request_release_hold(
    "fa5c8a0b0f492d768749333ad6fcc214c111e967"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SignatureRequestGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SignatureRequestReleaseHoldErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>signature_request_id</code> | <code>str</code> | The id of the SignatureRequest to release. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[SignatureRequestGetResponse](dropbox_sign_api/models/signature_request_get_response.py), [SignatureRequestReleaseHoldErrorBody](dropbox_sign_api/errors/signature_request_release_hold_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SignatureRequestGetResponse](dropbox_sign_api/models/signature_request_get_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[SignatureRequestReleaseHoldErrorBody](dropbox_sign_api/errors/signature_request_release_hold_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def signature_request_remind(signature_request_id: str, body: SignatureRequestRemindRequest | SignatureRequestRemindRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SignatureRequestGetResponse, SignatureRequestRemindErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Sends an email to the signer reminding them to sign the signature request. You cannot send a reminder within 1 hour of the last reminder that was sent. This includes manual AND automatic reminders.

**NOTE:** This action can **not** be used with embedded signature requests.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.signature_request.with_raw_response.signature_request_remind(
    "fa5c8a0b0f492d768749333ad6fcc214c111e967", SignatureRequestRemindRequest(email_address="user@example.com")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SignatureRequestGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SignatureRequestRemindErrorBody
```

**Async**

```python
result = await async_client.signature_request.with_raw_response.signature_request_remind(
    "fa5c8a0b0f492d768749333ad6fcc214c111e967", SignatureRequestRemindRequest(email_address="user@example.com")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SignatureRequestGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SignatureRequestRemindErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>signature_request_id</code> | <code>str</code> | The id of the SignatureRequest to send a reminder for. |
| <code>body</code> | <code>[SignatureRequestRemindRequest](dropbox_sign_api/models/signature_request_remind_request.py) \| [SignatureRequestRemindRequestDict](dropbox_sign_api/models/signature_request_remind_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[SignatureRequestGetResponse](dropbox_sign_api/models/signature_request_get_response.py), [SignatureRequestRemindErrorBody](dropbox_sign_api/errors/signature_request_remind_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SignatureRequestGetResponse](dropbox_sign_api/models/signature_request_get_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[SignatureRequestRemindErrorBody](dropbox_sign_api/errors/signature_request_remind_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def signature_request_remove(signature_request_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Any, SignatureRequestRemoveErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Removes your access to a completed signature request. This action is **not reversible**.

The signature request must be fully executed by all parties (signed or declined to sign). Other parties will continue to maintain access to the completed signature request document(s).

Unlike /signature_request/cancel, this endpoint is synchronous and your access will be immediately removed. Upon successful removal, this endpoint will return a 200 OK response.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.signature_request.with_raw_response.signature_request_remove("fa5c8a0b0f492d768749333ad6fcc214c111e967")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SignatureRequestRemoveErrorBody
```

**Async**

```python
result = await async_client.signature_request.with_raw_response.signature_request_remove(
    "fa5c8a0b0f492d768749333ad6fcc214c111e967"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SignatureRequestRemoveErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>signature_request_id</code> | <code>str</code> | The id of the SignatureRequest to remove. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;Any, [SignatureRequestRemoveErrorBody](dropbox_sign_api/errors/signature_request_remove_error.py)&#93;</code>

**On `Success`**: `payload` is <code>Any</code> -- successful operation

**On `Failure`**: `error` is <code>[SignatureRequestRemoveErrorBody](dropbox_sign_api/errors/signature_request_remove_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def signature_request_send(*, files: FileInput | None = None, file_urls: list[str] | None = None, signers: list[SubSignatureRequestSigner | SubSignatureRequestSignerDict] | None = None, grouped_signers: list[SubSignatureRequestGroupedSigners | SubSignatureRequestGroupedSignersDict] | None = None, allow_decline: bool | None = False, allow_reassign: bool | None = False, attachments: list[SubAttachment | SubAttachmentDict] | None = None, cc_email_addresses: list[EmailStr] | None = None, client_id: str | None = None, custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None, field_options: SubFieldOptions | SubFieldOptionsDict | None = None, form_field_groups: list[SubFormFieldGroup | SubFormFieldGroupDict] | None = None, form_field_rules: list[SubFormFieldRule | SubFormFieldRuleDict] | None = None, form_fields_per_document: list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None = None, hide_text_tags: bool | None = False, is_eid: bool | None = False, message: str | None = None, metadata: dict[str, Any] | None = None, signing_options: SubSigningOptions | SubSigningOptionsDict | None = None, signing_redirect_url: str | None = None, subject: str | None = None, test_mode: bool | None = False, title: str | None = None, use_text_tags: bool | None = False, ignore_text_tags_extraction_errors: bool | None = False, expires_at: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SignatureRequestGetResponse, SignatureRequestSendErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates and sends a new SignatureRequest with the submitted documents. If `form_fields_per_document` is not specified, a signature page will be affixed where all signers will be required to add their signature, signifying their agreement to all contained documents.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.signature_request.with_raw_response.signature_request_send()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SignatureRequestGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SignatureRequestSendErrorBody
```

**Async**

```python
result = await async_client.signature_request.with_raw_response.signature_request_send()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SignatureRequestGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SignatureRequestSendErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>files</code> | <code>FileInput \| None</code> | Use `files[]` to indicate the uploaded file(s) to send for signature.<br><br>This endpoint requires either **files** or **file_urls[]**, but not both.<br>**Default**: <code>None</code> |
| <code>file_urls</code> | <code>list&#91;str&#93; \| None</code> | Use `file_urls[]` to have Dropbox Sign download the file(s) to send for signature.<br><br>This endpoint requires either **files** or **file_urls[]**, but not both.<br>**Default**: <code>None</code> |
| <code>signers</code> | <code>list&#91;[SubSignatureRequestSigner](dropbox_sign_api/models/sub_signature_request_signer.py) \| [SubSignatureRequestSignerDict](dropbox_sign_api/models/sub_signature_request_signer.py)&#93; \| None</code> | Add Signers to your Signature Request.<br><br>This endpoint requires either **signers** or **grouped_signers**, but not both.<br>**Default**: <code>None</code> |
| <code>grouped_signers</code> | <code>list&#91;[SubSignatureRequestGroupedSigners](dropbox_sign_api/models/sub_signature_request_grouped_signers.py) \| [SubSignatureRequestGroupedSignersDict](dropbox_sign_api/models/sub_signature_request_grouped_signers.py)&#93; \| None</code> | Add Grouped Signers to your Signature Request.<br><br>This endpoint requires either **signers** or **grouped_signers**, but not both.<br>**Default**: <code>None</code> |
| <code>allow_decline</code> | <code>bool \| None</code> | Allows signers to decline to sign a document if `true`. Defaults to `false`.<br>**Default**: <code>False</code> |
| <code>allow_reassign</code> | <code>bool \| None</code> | Allows signers to reassign their signature requests to other signers if set to `true`. Defaults to `false`.<br><br>**NOTE:** Only available for Premium plan and higher.<br>**Default**: <code>False</code> |
| <code>attachments</code> | <code>list&#91;[SubAttachment](dropbox_sign_api/models/sub_attachment.py) \| [SubAttachmentDict](dropbox_sign_api/models/sub_attachment.py)&#93; \| None</code> | A list describing the attachments<br>**Default**: <code>None</code> |
| <code>cc_email_addresses</code> | <code>list&#91;EmailStr&#93; \| None</code> | The email addresses that should be CCed.<br>**Default**: <code>None</code> |
| <code>client_id</code> | <code>str \| None</code> | The client id of the API App you want to associate with this request. Used to apply the branding and callback url defined for the app.<br>**Default**: <code>None</code> |
| <code>custom_fields</code> | <code>list&#91;[SubCustomField](dropbox_sign_api/models/sub_custom_field.py) \| [SubCustomFieldDict](dropbox_sign_api/models/sub_custom_field.py)&#93; \| None</code> | When used together with merge fields, `custom_fields` allows users to add pre-filled data to their signature requests.<br><br>Pre-filled data can be used with "send-once" signature requests by adding merge fields with `form_fields_per_document` or [Text Tags](https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro) while passing values back with `custom_fields` together in one API call.<br><br>For using pre-filled on repeatable signature requests, merge fields are added to templates in the Dropbox Sign UI or by calling [/template/create_embedded_draft](/api/reference/operation/templateCreateEmbeddedDraft) and then passing `custom_fields` on subsequent signature requests referencing that template.<br>**Default**: <code>None</code> |
| <code>field_options</code> | <code>[SubFieldOptions](dropbox_sign_api/models/sub_field_options.py) \| [SubFieldOptionsDict](dropbox_sign_api/models/sub_field_options.py) \| None</code> | This allows the requester to specify field options for a signature request.<br>**Default**: <code>None</code> |
| <code>form_field_groups</code> | <code>list&#91;[SubFormFieldGroup](dropbox_sign_api/models/sub_form_field_group.py) \| [SubFormFieldGroupDict](dropbox_sign_api/models/sub_form_field_group.py)&#93; \| None</code> | Group information for fields defined in `form_fields_per_document`. String-indexed JSON array with `group_label` and `requirement` keys. `form_fields_per_document` must contain fields referencing a group defined in `form_field_groups`.<br>**Default**: <code>None</code> |
| <code>form_field_rules</code> | <code>list&#91;[SubFormFieldRule](dropbox_sign_api/models/sub_form_field_rule.py) \| [SubFormFieldRuleDict](dropbox_sign_api/models/sub_form_field_rule.py)&#93; \| None</code> | Conditional Logic rules for fields defined in `form_fields_per_document`.<br>**Default**: <code>None</code> |
| <code>form_fields_per_document</code> | <code>list&#91;[SubFormFieldsPerDocumentBase](dropbox_sign_api/models/unions/sub_form_fields_per_document_base.py) \| [SubFormFieldsPerDocumentBaseDict](dropbox_sign_api/models/unions/sub_form_fields_per_document_base.py)&#93; \| None</code> | The fields that should appear on the document, expressed as an array of objects. (For more details you can read about it here: [Using Form Fields per Document](/docs/openapi/form-fields-per-document).)<br><br>**NOTE:** Fields like **text**, **dropdown**, **checkbox**, **radio**, and **hyperlink** have additional required and optional parameters. Check out the list of [additional parameters](/api/reference/constants/#form-fields-per-document) for these field types.<br><br>* Text Field use `SubFormFieldsPerDocumentText`<br>* Dropdown Field use `SubFormFieldsPerDocumentDropdown`<br>* Hyperlink Field use `SubFormFieldsPerDocumentHyperlink`<br>* Checkbox Field use `SubFormFieldsPerDocumentCheckbox`<br>* Radio Field use `SubFormFieldsPerDocumentRadio`<br>* Signature Field use `SubFormFieldsPerDocumentSignature`<br>* Date Signed Field use `SubFormFieldsPerDocumentDateSigned`<br>* Initials Field use `SubFormFieldsPerDocumentInitials`<br>* Text Merge Field use `SubFormFieldsPerDocumentTextMerge`<br>* Checkbox Merge Field use `SubFormFieldsPerDocumentCheckboxMerge`<br>**Default**: <code>None</code> |
| <code>hide_text_tags</code> | <code>bool \| None</code> | Enables automatic Text Tag removal when set to true.<br><br>**NOTE:** Removing text tags this way can cause unwanted clipping. We recommend leaving this setting on `false` and instead hiding your text tags using white text or a similar approach. See the [Text Tags Walkthrough](https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro) for more information.<br>**Default**: <code>False</code> |
| <code>is_eid</code> | <code>bool \| None</code> | Send with a value of `true` if you wish to enable<br>[electronic identification (eID)](https://www.hellosign.com/features/electronic-id),<br>which requires the signer to verify their identity with an eID provider to sign a document.<br><br>**NOTE:** You need the eID add-on to use this feature. Please [contact sales](https://sign.dropbox.com/form/contact-sales) for more information. Cannot be used in `test_mode`. Only works on requests with one signer.<br>**Default**: <code>False</code> |
| <code>message</code> | <code>str \| None</code> | The custom message in the email that will be sent to the signers.<br>**Default**: <code>None</code> |
| <code>metadata</code> | <code>dict&#91;str, Any&#93; \| None</code> | Key-value data that should be attached to the signature request. This metadata is included in all API responses and events involving the signature request. For example, use the metadata field to store a signer's order number for look up when receiving events for the signature request.<br><br>Each request can include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and values up to 1000 characters long.<br>**Default**: <code>None</code> |
| <code>signing_options</code> | <code>[SubSigningOptions](dropbox_sign_api/models/sub_signing_options.py) \| [SubSigningOptionsDict](dropbox_sign_api/models/sub_signing_options.py) \| None</code> | This allows the requester to specify the types allowed for creating a signature and specify another signing options.<br><br>**NOTE:** If `signing_options` are not defined in the request, the allowed types will default to those specified in the account settings.<br><br>**NOTE:** If `force_advanced_signature_details` is set, allowed types has to be defined too.<br>**Default**: <code>None</code> |
| <code>signing_redirect_url</code> | <code>str \| None</code> | The URL you want signers redirected to after they successfully sign.<br>**Default**: <code>None</code> |
| <code>subject</code> | <code>str \| None</code> | The subject in the email that will be sent to the signers.<br>**Default**: <code>None</code> |
| <code>test_mode</code> | <code>bool \| None</code> | Whether this is a test, the signature request will not be legally binding if set to `true`. Defaults to `false`.<br>**Default**: <code>False</code> |
| <code>title</code> | <code>str \| None</code> | The title you want to assign to the SignatureRequest.<br>**Default**: <code>None</code> |
| <code>use_text_tags</code> | <code>bool \| None</code> | Send with a value of `true` if you wish to enable [Text Tags](https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro) parsing in your document. Defaults to disabled, or `false`.<br>**Default**: <code>False</code> |
| <code>ignore_text_tags_extraction_errors</code> | <code>bool \| None</code> | Sent with a value of `true` to ignore the validation errors from text tags extraction. Defaults to `false`.<br>**Default**: <code>False</code> |
| <code>expires_at</code> | <code>int \| None</code> | When the signature request will expire. Unsigned signatures will be moved to the expired status, and no longer signable. See [Signature Request Expiration Date](https://developers.hellosign.com/docs/signature-request/expiration/) for details.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[SignatureRequestGetResponse](dropbox_sign_api/models/signature_request_get_response.py), [SignatureRequestSendErrorBody](dropbox_sign_api/errors/signature_request_send_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SignatureRequestGetResponse](dropbox_sign_api/models/signature_request_get_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[SignatureRequestSendErrorBody](dropbox_sign_api/errors/signature_request_send_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def signature_request_send_with_template(template_ids: list[str], signers: list[SubSignatureRequestTemplateSigner | SubSignatureRequestTemplateSignerDict], *, allow_decline: bool | None = False, ccs: list[SubCc | SubCcDict] | None = None, client_id: str | None = None, custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None, files: FileInput | None = None, file_urls: list[str] | None = None, is_eid: bool | None = False, message: str | None = None, metadata: dict[str, Any] | None = None, signing_options: SubSigningOptions | SubSigningOptionsDict | None = None, signing_redirect_url: str | None = None, subject: str | None = None, test_mode: bool | None = False, title: str | None = None, expires_at: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SignatureRequestGetResponse, SignatureRequestSendWithTemplateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates and sends a new SignatureRequest based off of the Template(s) specified with the `template_ids` parameter.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.signature_request.with_raw_response.signature_request_send_with_template(
    ["some example string"],
    [
        SubSignatureRequestTemplateSigner(
            role="some example string", name="some example string", email_address="user@example.com"
        ),
    ],
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SignatureRequestGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SignatureRequestSendWithTemplateErrorBody
```

**Async**

```python
result = await async_client.signature_request.with_raw_response.signature_request_send_with_template(
    ["some example string"],
    [
        SubSignatureRequestTemplateSigner(
            role="some example string", name="some example string", email_address="user@example.com"
        ),
    ],
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SignatureRequestGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SignatureRequestSendWithTemplateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>template_ids</code> | <code>list&#91;str&#93;</code> | Use `template_ids` to create a SignatureRequest from one or more templates, in the order in which the template will be used. |
| <code>signers</code> | <code>list&#91;[SubSignatureRequestTemplateSigner](dropbox_sign_api/models/sub_signature_request_template_signer.py) \| [SubSignatureRequestTemplateSignerDict](dropbox_sign_api/models/sub_signature_request_template_signer.py)&#93;</code> | Add Signers to your Templated-based Signature Request. |
| <code>allow_decline</code> | <code>bool \| None</code> | Allows signers to decline to sign a document if `true`. Defaults to `false`.<br>**Default**: <code>False</code> |
| <code>ccs</code> | <code>list&#91;[SubCc](dropbox_sign_api/models/sub_cc.py) \| [SubCcDict](dropbox_sign_api/models/sub_cc.py)&#93; \| None</code> | Add CC email recipients. Required when a CC role exists for the Template.<br>**Default**: <code>None</code> |
| <code>client_id</code> | <code>str \| None</code> | Client id of the app to associate with the signature request. Used to apply the branding and callback url defined for the app.<br>**Default**: <code>None</code> |
| <code>custom_fields</code> | <code>list&#91;[SubCustomField](dropbox_sign_api/models/sub_custom_field.py) \| [SubCustomFieldDict](dropbox_sign_api/models/sub_custom_field.py)&#93; \| None</code> | An array defining values and options for custom fields. Required when a custom field exists in the Template.<br>**Default**: <code>None</code> |
| <code>files</code> | <code>FileInput \| None</code> | Use `files[]` to indicate the uploaded file(s) to send for signature.<br><br>This endpoint requires either **files** or **file_urls[]**, but not both.<br>**Default**: <code>None</code> |
| <code>file_urls</code> | <code>list&#91;str&#93; \| None</code> | Use `file_urls[]` to have Dropbox Sign download the file(s) to send for signature.<br><br>This endpoint requires either **files** or **file_urls[]**, but not both.<br>**Default**: <code>None</code> |
| <code>is_eid</code> | <code>bool \| None</code> | Send with a value of `true` if you wish to enable<br>[electronic identification (eID)](https://www.hellosign.com/features/electronic-id),<br>which requires the signer to verify their identity with an eID provider to sign a document.<br><br>**NOTE:** You need the eID add-on to use this feature. Please [contact sales](https://sign.dropbox.com/form/contact-sales) for more information. Cannot be used in `test_mode`. Only works on requests with one signer.<br>**Default**: <code>False</code> |
| <code>message</code> | <code>str \| None</code> | The custom message in the email that will be sent to the signers.<br>**Default**: <code>None</code> |
| <code>metadata</code> | <code>dict&#91;str, Any&#93; \| None</code> | Key-value data that should be attached to the signature request. This metadata is included in all API responses and events involving the signature request. For example, use the metadata field to store a signer's order number for look up when receiving events for the signature request.<br><br>Each request can include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and values up to 1000 characters long.<br>**Default**: <code>None</code> |
| <code>signing_options</code> | <code>[SubSigningOptions](dropbox_sign_api/models/sub_signing_options.py) \| [SubSigningOptionsDict](dropbox_sign_api/models/sub_signing_options.py) \| None</code> | This allows the requester to specify the types allowed for creating a signature and specify another signing options.<br><br>**NOTE:** If `signing_options` are not defined in the request, the allowed types will default to those specified in the account settings.<br><br>**NOTE:** If `force_advanced_signature_details` is set, allowed types has to be defined too.<br>**Default**: <code>None</code> |
| <code>signing_redirect_url</code> | <code>str \| None</code> | The URL you want signers redirected to after they successfully sign.<br>**Default**: <code>None</code> |
| <code>subject</code> | <code>str \| None</code> | The subject in the email that will be sent to the signers.<br>**Default**: <code>None</code> |
| <code>test_mode</code> | <code>bool \| None</code> | Whether this is a test, the signature request will not be legally binding if set to `true`. Defaults to `false`.<br>**Default**: <code>False</code> |
| <code>title</code> | <code>str \| None</code> | The title you want to assign to the SignatureRequest.<br>**Default**: <code>None</code> |
| <code>expires_at</code> | <code>int \| None</code> | When the signature request will expire. Unsigned signatures will be moved to the expired status, and no longer signable. See [Signature Request Expiration Date](https://developers.hellosign.com/docs/signature-request/expiration/) for details.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[SignatureRequestGetResponse](dropbox_sign_api/models/signature_request_get_response.py), [SignatureRequestSendWithTemplateErrorBody](dropbox_sign_api/errors/signature_request_send_with_template_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SignatureRequestGetResponse](dropbox_sign_api/models/signature_request_get_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[SignatureRequestSendWithTemplateErrorBody](dropbox_sign_api/errors/signature_request_send_with_template_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def signature_request_update(signature_request_id: str, body: SignatureRequestUpdateRequest | SignatureRequestUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SignatureRequestGetResponse, SignatureRequestUpdateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates the email address and/or the name for a given signer on a signature request. You can listen for the `signature_request_email_bounce` event on your app or account to detect bounced emails, and respond with this method.

Updating the email address of a signer will generate a new `signature_id` value.

**NOTE:** This action cannot be performed on a signature request with an appended signature page.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.signature_request.with_raw_response.signature_request_update(
    "fa5c8a0b0f492d768749333ad6fcc214c111e967", SignatureRequestUpdateRequest(signature_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SignatureRequestGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SignatureRequestUpdateErrorBody
```

**Async**

```python
result = await async_client.signature_request.with_raw_response.signature_request_update(
    "fa5c8a0b0f492d768749333ad6fcc214c111e967", SignatureRequestUpdateRequest(signature_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SignatureRequestGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SignatureRequestUpdateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>signature_request_id</code> | <code>str</code> | The id of the SignatureRequest to update. |
| <code>body</code> | <code>[SignatureRequestUpdateRequest](dropbox_sign_api/models/signature_request_update_request.py) \| [SignatureRequestUpdateRequestDict](dropbox_sign_api/models/signature_request_update_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[SignatureRequestGetResponse](dropbox_sign_api/models/signature_request_get_response.py), [SignatureRequestUpdateErrorBody](dropbox_sign_api/errors/signature_request_update_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SignatureRequestGetResponse](dropbox_sign_api/models/signature_request_get_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[SignatureRequestUpdateErrorBody](dropbox_sign_api/errors/signature_request_update_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Team

> Source: [Team](dropbox_sign_api/apis/team.py)

<details>
<summary><code>def team_add_member(body: TeamAddMemberRequest | TeamAddMemberRequestDict, *, team_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TeamGetResponse, TeamAddMemberErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Invites a user (specified using the `email_address` parameter) to your Team. If the user does not currently have a Dropbox Sign Account, a new one will be created for them. If a user is already a part of another Team, a `team_invite_failed` error will be returned.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.team.with_raw_response.team_add_member(
    TeamAddMemberRequest(), team_id="4fea99bfcf2b26bfccf6cea3e127fb8bb74d8d9c"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TeamGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type TeamAddMemberErrorBody
```

**Async**

```python
result = await async_client.team.with_raw_response.team_add_member(
    TeamAddMemberRequest(), team_id="4fea99bfcf2b26bfccf6cea3e127fb8bb74d8d9c"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TeamGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type TeamAddMemberErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TeamAddMemberRequest](dropbox_sign_api/models/team_add_member_request.py) \| [TeamAddMemberRequestDict](dropbox_sign_api/models/team_add_member_request.py)</code> | The request body. |
| <code>team_id</code> | <code>str \| None</code> | The id of the team.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[TeamGetResponse](dropbox_sign_api/models/team_get_response.py), [TeamAddMemberErrorBody](dropbox_sign_api/errors/team_add_member_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[TeamGetResponse](dropbox_sign_api/models/team_get_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[TeamAddMemberErrorBody](dropbox_sign_api/errors/team_add_member_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def team_create(body: TeamCreateRequest | TeamCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TeamGetResponse, TeamCreateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a new Team and makes you a member. You must not currently belong to a Team to invoke.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.team.with_raw_response.team_create(TeamCreateRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TeamGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type TeamCreateErrorBody
```

**Async**

```python
result = await async_client.team.with_raw_response.team_create(TeamCreateRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TeamGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type TeamCreateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TeamCreateRequest](dropbox_sign_api/models/team_create_request.py) \| [TeamCreateRequestDict](dropbox_sign_api/models/team_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[TeamGetResponse](dropbox_sign_api/models/team_get_response.py), [TeamCreateErrorBody](dropbox_sign_api/errors/team_create_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[TeamGetResponse](dropbox_sign_api/models/team_get_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[TeamCreateErrorBody](dropbox_sign_api/errors/team_create_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def team_delete(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, TeamDeleteErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes your Team. Can only be invoked when you have a Team with only one member (yourself).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.team.with_raw_response.team_delete()
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type TeamDeleteErrorBody
```

**Async**

```python
result = await async_client.team.with_raw_response.team_delete()
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type TeamDeleteErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;None, [TeamDeleteErrorBody](dropbox_sign_api/errors/team_delete_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[TeamDeleteErrorBody](dropbox_sign_api/errors/team_delete_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def team_get(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TeamGetResponse, TeamGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns information about your Team as well as a list of its members. If you do not belong to a Team, a 404 error with an error_name of "not_found" will be returned.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.team.with_raw_response.team_get()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TeamGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type TeamGetErrorBody
```

**Async**

```python
result = await async_client.team.with_raw_response.team_get()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TeamGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type TeamGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[TeamGetResponse](dropbox_sign_api/models/team_get_response.py), [TeamGetErrorBody](dropbox_sign_api/errors/team_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[TeamGetResponse](dropbox_sign_api/models/team_get_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[TeamGetErrorBody](dropbox_sign_api/errors/team_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def team_info(*, team_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TeamGetInfoResponse, TeamInfoErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Provides information about a team.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.team.with_raw_response.team_info(team_id="4fea99bfcf2b26bfccf6cea3e127fb8bb74d8d9c")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TeamGetInfoResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type TeamInfoErrorBody
```

**Async**

```python
result = await async_client.team.with_raw_response.team_info(team_id="4fea99bfcf2b26bfccf6cea3e127fb8bb74d8d9c")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TeamGetInfoResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type TeamInfoErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>team_id</code> | <code>str \| None</code> | The id of the team.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[TeamGetInfoResponse](dropbox_sign_api/models/team_get_info_response.py), [TeamInfoErrorBody](dropbox_sign_api/errors/team_info_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[TeamGetInfoResponse](dropbox_sign_api/models/team_get_info_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[TeamInfoErrorBody](dropbox_sign_api/errors/team_info_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def team_invites(*, email_address: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TeamInvitesResponse, TeamInvitesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Provides a list of team invites (and their roles).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.team.with_raw_response.team_invites()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TeamInvitesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type TeamInvitesErrorBody
```

**Async**

```python
result = await async_client.team.with_raw_response.team_invites()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TeamInvitesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type TeamInvitesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>email_address</code> | <code>str \| None</code> | The email address for which to display the team invites.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[TeamInvitesResponse](dropbox_sign_api/models/team_invites_response.py), [TeamInvitesErrorBody](dropbox_sign_api/errors/team_invites_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[TeamInvitesResponse](dropbox_sign_api/models/team_invites_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[TeamInvitesErrorBody](dropbox_sign_api/errors/team_invites_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def team_members(team_id: str, *, page: int | None = 1, page_size: int | None = 20, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TeamMembersResponse, TeamMembersErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Provides a paginated list of members (and their roles) that belong to a given team.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.team.with_raw_response.team_members("4fea99bfcf2b26bfccf6cea3e127fb8bb74d8d9c")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TeamMembersResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type TeamMembersErrorBody
```

**Async**

```python
result = await async_client.team.with_raw_response.team_members("4fea99bfcf2b26bfccf6cea3e127fb8bb74d8d9c")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TeamMembersResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type TeamMembersErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>team_id</code> | <code>str</code> | The id of the team that a member list is being requested from. |
| <code>page</code> | <code>int \| None</code> | Which page number of the team member list to return. Defaults to `1`.<br>**Default**: <code>1</code> |
| <code>page_size</code> | <code>int \| None</code> | Number of objects to be returned per page. Must be between `1` and `100`. Default is `20`.<br>**Default**: <code>20</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[TeamMembersResponse](dropbox_sign_api/models/team_members_response.py), [TeamMembersErrorBody](dropbox_sign_api/errors/team_members_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[TeamMembersResponse](dropbox_sign_api/models/team_members_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[TeamMembersErrorBody](dropbox_sign_api/errors/team_members_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def team_remove_member(body: TeamRemoveMemberRequest | TeamRemoveMemberRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TeamGetResponse, TeamRemoveMemberErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Removes the provided user Account from your Team. If the Account had an outstanding invitation to your Team, the invitation will be expired. If you choose to transfer documents from the removed Account to an Account provided in the `new_owner_email_address` parameter (available only for Enterprise plans), the response status code will be 201, which indicates that your request has been queued but not fully executed.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.team.with_raw_response.team_remove_member(TeamRemoveMemberRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TeamGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type TeamRemoveMemberErrorBody
```

**Async**

```python
result = await async_client.team.with_raw_response.team_remove_member(TeamRemoveMemberRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TeamGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type TeamRemoveMemberErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TeamRemoveMemberRequest](dropbox_sign_api/models/team_remove_member_request.py) \| [TeamRemoveMemberRequestDict](dropbox_sign_api/models/team_remove_member_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[TeamGetResponse](dropbox_sign_api/models/team_get_response.py), [TeamRemoveMemberErrorBody](dropbox_sign_api/errors/team_remove_member_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[TeamGetResponse](dropbox_sign_api/models/team_get_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[TeamRemoveMemberErrorBody](dropbox_sign_api/errors/team_remove_member_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def team_sub_teams(team_id: str, *, page: int | None = 1, page_size: int | None = 20, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TeamSubTeamsResponse, TeamSubTeamsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Provides a paginated list of sub teams that belong to a given team.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.team.with_raw_response.team_sub_teams("4fea99bfcf2b26bfccf6cea3e127fb8bb74d8d9c")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TeamSubTeamsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type TeamSubTeamsErrorBody
```

**Async**

```python
result = await async_client.team.with_raw_response.team_sub_teams("4fea99bfcf2b26bfccf6cea3e127fb8bb74d8d9c")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TeamSubTeamsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type TeamSubTeamsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>team_id</code> | <code>str</code> | The id of the parent Team. |
| <code>page</code> | <code>int \| None</code> | Which page number of the SubTeam List to return. Defaults to `1`.<br>**Default**: <code>1</code> |
| <code>page_size</code> | <code>int \| None</code> | Number of objects to be returned per page. Must be between `1` and `100`. Default is `20`.<br>**Default**: <code>20</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[TeamSubTeamsResponse](dropbox_sign_api/models/team_sub_teams_response.py), [TeamSubTeamsErrorBody](dropbox_sign_api/errors/team_sub_teams_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[TeamSubTeamsResponse](dropbox_sign_api/models/team_sub_teams_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[TeamSubTeamsErrorBody](dropbox_sign_api/errors/team_sub_teams_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def team_update(body: TeamUpdateRequest | TeamUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TeamGetResponse, TeamUpdateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates the name of your Team.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.team.with_raw_response.team_update(TeamUpdateRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TeamGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type TeamUpdateErrorBody
```

**Async**

```python
result = await async_client.team.with_raw_response.team_update(TeamUpdateRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TeamGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type TeamUpdateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TeamUpdateRequest](dropbox_sign_api/models/team_update_request.py) \| [TeamUpdateRequestDict](dropbox_sign_api/models/team_update_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[TeamGetResponse](dropbox_sign_api/models/team_get_response.py), [TeamUpdateErrorBody](dropbox_sign_api/errors/team_update_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[TeamGetResponse](dropbox_sign_api/models/team_get_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[TeamUpdateErrorBody](dropbox_sign_api/errors/team_update_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Template

> Source: [Template](dropbox_sign_api/apis/template.py)

<details>
<summary><code>def template_add_user(template_id: str, body: TemplateAddUserRequest | TemplateAddUserRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TemplateGetResponse, TemplateAddUserErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Gives the specified Account access to the specified Template. The specified Account must be a part of your Team.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.template.with_raw_response.template_add_user(
    "f57db65d3f933b5316d398057a36176831451a35", TemplateAddUserRequest()
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TemplateGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type TemplateAddUserErrorBody
```

**Async**

```python
result = await async_client.template.with_raw_response.template_add_user(
    "f57db65d3f933b5316d398057a36176831451a35", TemplateAddUserRequest()
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TemplateGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type TemplateAddUserErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>template_id</code> | <code>str</code> | The id of the Template to give the Account access to. |
| <code>body</code> | <code>[TemplateAddUserRequest](dropbox_sign_api/models/template_add_user_request.py) \| [TemplateAddUserRequestDict](dropbox_sign_api/models/template_add_user_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[TemplateGetResponse](dropbox_sign_api/models/template_get_response.py), [TemplateAddUserErrorBody](dropbox_sign_api/errors/template_add_user_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[TemplateGetResponse](dropbox_sign_api/models/template_get_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[TemplateAddUserErrorBody](dropbox_sign_api/errors/template_add_user_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def template_create(form_fields_per_document: list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict], signer_roles: list[SubTemplateRole | SubTemplateRoleDict], *, files: FileInput | None = None, file_urls: list[str] | None = None, allow_reassign: bool | None = False, attachments: list[SubAttachment | SubAttachmentDict] | None = None, cc_roles: list[str] | None = None, client_id: str | None = None, field_options: SubFieldOptions | SubFieldOptionsDict | None = None, form_field_groups: list[SubFormFieldGroup | SubFormFieldGroupDict] | None = None, form_field_rules: list[SubFormFieldRule | SubFormFieldRuleDict] | None = None, merge_fields: list[SubMergeField | SubMergeFieldDict] | None = None, message: str | None = None, metadata: dict[str, Any] | None = None, subject: str | None = None, test_mode: bool | None = False, title: str | None = None, use_preexisting_fields: bool | None = False, ignore_text_tags_extraction_errors: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TemplateCreateResponse, TemplateCreateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a template that can be used in future signature requests.

If `client_id` is provided, the template will be created as an embedded template. Embedded templates can be used for embedded signature requests and can be edited later by generating a new `edit_url` with [/embedded/edit_url/{template_id}](/api/reference/operation/embeddedEditUrl/).

Template creation may complete asynchronously after the initial request is accepted. It is recommended that a callback be implemented to listen for the callback event. A `template_created` event indicates the template is ready to use, while a `template_error` event indicates there was a problem while creating the template. If a callback handler has been configured and the event has not been received within 60 minutes of making the call, check the status of the request in the API dashboard and retry the request if necessary.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.template.with_raw_response.template_create(
    [
        SubFormFieldsPerDocumentCheckbox(
            document_index=1,
            api_id="some example string",
            height=1,
            required=True,
            signer="some example string",
            type_="checkbox",
            width=1,
            x=1,
            y=1,
            is_checked=True,
        ),
    ],
    [SubTemplateRole()],
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TemplateCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type TemplateCreateErrorBody
```

**Async**

```python
result = await async_client.template.with_raw_response.template_create(
    [
        SubFormFieldsPerDocumentCheckbox(
            document_index=1,
            api_id="some example string",
            height=1,
            required=True,
            signer="some example string",
            type_="checkbox",
            width=1,
            x=1,
            y=1,
            is_checked=True,
        ),
    ],
    [SubTemplateRole()],
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TemplateCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type TemplateCreateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>form_fields_per_document</code> | <code>list&#91;[SubFormFieldsPerDocumentBase](dropbox_sign_api/models/unions/sub_form_fields_per_document_base.py) \| [SubFormFieldsPerDocumentBaseDict](dropbox_sign_api/models/unions/sub_form_fields_per_document_base.py)&#93;</code> | The fields that should appear on the document, expressed as an array of objects. (For more details you can read about it here: [Using Form Fields per Document](/docs/openapi/form-fields-per-document).)<br><br>**NOTE:** Fields like **text**, **dropdown**, **checkbox**, **radio**, and **hyperlink** have additional required and optional parameters. Check out the list of [additional parameters](/api/reference/constants/#form-fields-per-document) for these field types.<br><br>* Text Field use `SubFormFieldsPerDocumentText`<br>* Dropdown Field use `SubFormFieldsPerDocumentDropdown`<br>* Hyperlink Field use `SubFormFieldsPerDocumentHyperlink`<br>* Checkbox Field use `SubFormFieldsPerDocumentCheckbox`<br>* Radio Field use `SubFormFieldsPerDocumentRadio`<br>* Signature Field use `SubFormFieldsPerDocumentSignature`<br>* Date Signed Field use `SubFormFieldsPerDocumentDateSigned`<br>* Initials Field use `SubFormFieldsPerDocumentInitials`<br>* Text Merge Field use `SubFormFieldsPerDocumentTextMerge`<br>* Checkbox Merge Field use `SubFormFieldsPerDocumentCheckboxMerge` |
| <code>signer_roles</code> | <code>list&#91;[SubTemplateRole](dropbox_sign_api/models/sub_template_role.py) \| [SubTemplateRoleDict](dropbox_sign_api/models/sub_template_role.py)&#93;</code> | An array of the designated signer roles that must be specified when sending a SignatureRequest using this Template. |
| <code>files</code> | <code>FileInput \| None</code> | Use `files[]` to indicate the uploaded file(s) to send for signature.<br><br>This endpoint requires either **files** or **file_urls[]**, but not both.<br>**Default**: <code>None</code> |
| <code>file_urls</code> | <code>list&#91;str&#93; \| None</code> | Use `file_urls[]` to have Dropbox Sign download the file(s) to send for signature.<br><br>This endpoint requires either **files** or **file_urls[]**, but not both.<br>**Default**: <code>None</code> |
| <code>allow_reassign</code> | <code>bool \| None</code> | Allows signers to reassign their signature requests to other signers if set to `true`. Defaults to `false`.<br><br>**NOTE:** Only available for Premium plan and higher.<br>**Default**: <code>False</code> |
| <code>attachments</code> | <code>list&#91;[SubAttachment](dropbox_sign_api/models/sub_attachment.py) \| [SubAttachmentDict](dropbox_sign_api/models/sub_attachment.py)&#93; \| None</code> | A list describing the attachments<br>**Default**: <code>None</code> |
| <code>cc_roles</code> | <code>list&#91;str&#93; \| None</code> | The CC roles that must be assigned when using the template to send a signature request<br>**Default**: <code>None</code> |
| <code>client_id</code> | <code>str \| None</code> | Client id of the app you're using to create this draft. Used to apply the branding and callback url defined for the app.<br>**Default**: <code>None</code> |
| <code>field_options</code> | <code>[SubFieldOptions](dropbox_sign_api/models/sub_field_options.py) \| [SubFieldOptionsDict](dropbox_sign_api/models/sub_field_options.py) \| None</code> | This allows the requester to specify field options for a signature request.<br>**Default**: <code>None</code> |
| <code>form_field_groups</code> | <code>list&#91;[SubFormFieldGroup](dropbox_sign_api/models/sub_form_field_group.py) \| [SubFormFieldGroupDict](dropbox_sign_api/models/sub_form_field_group.py)&#93; \| None</code> | Group information for fields defined in `form_fields_per_document`. String-indexed JSON array with `group_label` and `requirement` keys. `form_fields_per_document` must contain fields referencing a group defined in `form_field_groups`.<br>**Default**: <code>None</code> |
| <code>form_field_rules</code> | <code>list&#91;[SubFormFieldRule](dropbox_sign_api/models/sub_form_field_rule.py) \| [SubFormFieldRuleDict](dropbox_sign_api/models/sub_form_field_rule.py)&#93; \| None</code> | Conditional Logic rules for fields defined in `form_fields_per_document`.<br>**Default**: <code>None</code> |
| <code>merge_fields</code> | <code>list&#91;[SubMergeField](dropbox_sign_api/models/sub_merge_field.py) \| [SubMergeFieldDict](dropbox_sign_api/models/sub_merge_field.py)&#93; \| None</code> | Add merge fields to the template. Merge fields are placed by the user creating the template and used to pre-fill data by passing values into signature requests with the `custom_fields` parameter.<br>If the signature request using that template *does not* pass a value into a merge field, then an empty field remains in the document.<br>**Default**: <code>None</code> |
| <code>message</code> | <code>str \| None</code> | The default template email message.<br>**Default**: <code>None</code> |
| <code>metadata</code> | <code>dict&#91;str, Any&#93; \| None</code> | Key-value data that should be attached to the signature request. This metadata is included in all API responses and events involving the signature request. For example, use the metadata field to store a signer's order number for look up when receiving events for the signature request.<br><br>Each request can include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and values up to 1000 characters long.<br>**Default**: <code>None</code> |
| <code>subject</code> | <code>str \| None</code> | The template title (alias).<br>**Default**: <code>None</code> |
| <code>test_mode</code> | <code>bool \| None</code> | Whether this is a test, the signature request created from this draft will not be legally binding if set to `true`. Defaults to `false`.<br>**Default**: <code>False</code> |
| <code>title</code> | <code>str \| None</code> | The title you want to assign to the SignatureRequest.<br>**Default**: <code>None</code> |
| <code>use_preexisting_fields</code> | <code>bool \| None</code> | Enable the detection of predefined PDF fields by setting the `use_preexisting_fields` to `true` (defaults to disabled, or `false`).<br>**Default**: <code>False</code> |
| <code>ignore_text_tags_extraction_errors</code> | <code>bool \| None</code> | Sent with a value of `true` to ignore the validation errors from text tags extraction. Defaults to `false`.<br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[TemplateCreateResponse](dropbox_sign_api/models/template_create_response.py), [TemplateCreateErrorBody](dropbox_sign_api/errors/template_create_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[TemplateCreateResponse](dropbox_sign_api/models/template_create_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[TemplateCreateErrorBody](dropbox_sign_api/errors/template_create_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def template_create_embedded_draft(client_id: str, *, files: FileInput | None = None, file_urls: list[str] | None = None, allow_ccs: bool | None = True, allow_reassign: bool | None = False, attachments: list[SubAttachment | SubAttachmentDict] | None = None, cc_roles: list[str] | None = None, editor_options: SubEditorOptions | SubEditorOptionsDict | None = None, field_options: SubFieldOptions | SubFieldOptionsDict | None = None, force_signer_roles: bool | None = False, force_subject_message: bool | None = False, form_field_groups: list[SubFormFieldGroup | SubFormFieldGroupDict] | None = None, form_field_rules: list[SubFormFieldRule | SubFormFieldRuleDict] | None = None, form_fields_per_document: list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None = None, merge_fields: list[SubMergeField | SubMergeFieldDict] | None = None, message: str | None = None, metadata: dict[str, Any] | None = None, show_preview: bool | None = False, show_progress_stepper: bool | None = True, signer_roles: list[SubTemplateRole | SubTemplateRoleDict] | None = None, skip_me_now: bool | None = False, subject: str | None = None, test_mode: bool | None = False, title: str | None = None, use_preexisting_fields: bool | None = False, ignore_text_tags_extraction_errors: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TemplateCreateEmbeddedDraftResponse, TemplateCreateEmbeddedDraftErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The first step in an embedded template workflow. Creates a draft template that can then be further set up in the template 'edit' stage.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.template.with_raw_response.template_create_embedded_draft("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TemplateCreateEmbeddedDraftResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type TemplateCreateEmbeddedDraftErrorBody
```

**Async**

```python
result = await async_client.template.with_raw_response.template_create_embedded_draft("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TemplateCreateEmbeddedDraftResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type TemplateCreateEmbeddedDraftErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>client_id</code> | <code>str</code> | Client id of the app you're using to create this draft. Used to apply the branding and callback url defined for the app. |
| <code>files</code> | <code>FileInput \| None</code> | Use `files[]` to indicate the uploaded file(s) to send for signature.<br><br>This endpoint requires either **files** or **file_urls[]**, but not both.<br>**Default**: <code>None</code> |
| <code>file_urls</code> | <code>list&#91;str&#93; \| None</code> | Use `file_urls[]` to have Dropbox Sign download the file(s) to send for signature.<br><br>This endpoint requires either **files** or **file_urls[]**, but not both.<br>**Default**: <code>None</code> |
| <code>allow_ccs</code> | <code>bool \| None</code> | This allows the requester to specify whether the user is allowed to provide email addresses to CC when creating a template.<br>**Default**: <code>True</code> |
| <code>allow_reassign</code> | <code>bool \| None</code> | Allows signers to reassign their signature requests to other signers if set to `true`. Defaults to `false`.<br><br>**NOTE:** Only available for Premium plan and higher.<br>**Default**: <code>False</code> |
| <code>attachments</code> | <code>list&#91;[SubAttachment](dropbox_sign_api/models/sub_attachment.py) \| [SubAttachmentDict](dropbox_sign_api/models/sub_attachment.py)&#93; \| None</code> | A list describing the attachments<br>**Default**: <code>None</code> |
| <code>cc_roles</code> | <code>list&#91;str&#93; \| None</code> | The CC roles that must be assigned when using the template to send a signature request<br>**Default**: <code>None</code> |
| <code>editor_options</code> | <code>[SubEditorOptions](dropbox_sign_api/models/sub_editor_options.py) \| [SubEditorOptionsDict](dropbox_sign_api/models/sub_editor_options.py) \| None</code> | This allows the requester to specify editor options when a preparing a document<br>**Default**: <code>None</code> |
| <code>field_options</code> | <code>[SubFieldOptions](dropbox_sign_api/models/sub_field_options.py) \| [SubFieldOptionsDict](dropbox_sign_api/models/sub_field_options.py) \| None</code> | This allows the requester to specify field options for a signature request.<br>**Default**: <code>None</code> |
| <code>force_signer_roles</code> | <code>bool \| None</code> | Provide users the ability to review/edit the template signer roles.<br>**Default**: <code>False</code> |
| <code>force_subject_message</code> | <code>bool \| None</code> | Provide users the ability to review/edit the template subject and message.<br>**Default**: <code>False</code> |
| <code>form_field_groups</code> | <code>list&#91;[SubFormFieldGroup](dropbox_sign_api/models/sub_form_field_group.py) \| [SubFormFieldGroupDict](dropbox_sign_api/models/sub_form_field_group.py)&#93; \| None</code> | Group information for fields defined in `form_fields_per_document`. String-indexed JSON array with `group_label` and `requirement` keys. `form_fields_per_document` must contain fields referencing a group defined in `form_field_groups`.<br>**Default**: <code>None</code> |
| <code>form_field_rules</code> | <code>list&#91;[SubFormFieldRule](dropbox_sign_api/models/sub_form_field_rule.py) \| [SubFormFieldRuleDict](dropbox_sign_api/models/sub_form_field_rule.py)&#93; \| None</code> | Conditional Logic rules for fields defined in `form_fields_per_document`.<br>**Default**: <code>None</code> |
| <code>form_fields_per_document</code> | <code>list&#91;[SubFormFieldsPerDocumentBase](dropbox_sign_api/models/unions/sub_form_fields_per_document_base.py) \| [SubFormFieldsPerDocumentBaseDict](dropbox_sign_api/models/unions/sub_form_fields_per_document_base.py)&#93; \| None</code> | The fields that should appear on the document, expressed as an array of objects. (For more details you can read about it here: [Using Form Fields per Document](/docs/openapi/form-fields-per-document).)<br><br>**NOTE:** Fields like **text**, **dropdown**, **checkbox**, **radio**, and **hyperlink** have additional required and optional parameters. Check out the list of [additional parameters](/api/reference/constants/#form-fields-per-document) for these field types.<br><br>* Text Field use `SubFormFieldsPerDocumentText`<br>* Dropdown Field use `SubFormFieldsPerDocumentDropdown`<br>* Hyperlink Field use `SubFormFieldsPerDocumentHyperlink`<br>* Checkbox Field use `SubFormFieldsPerDocumentCheckbox`<br>* Radio Field use `SubFormFieldsPerDocumentRadio`<br>* Signature Field use `SubFormFieldsPerDocumentSignature`<br>* Date Signed Field use `SubFormFieldsPerDocumentDateSigned`<br>* Initials Field use `SubFormFieldsPerDocumentInitials`<br>* Text Merge Field use `SubFormFieldsPerDocumentTextMerge`<br>* Checkbox Merge Field use `SubFormFieldsPerDocumentCheckboxMerge`<br>**Default**: <code>None</code> |
| <code>merge_fields</code> | <code>list&#91;[SubMergeField](dropbox_sign_api/models/sub_merge_field.py) \| [SubMergeFieldDict](dropbox_sign_api/models/sub_merge_field.py)&#93; \| None</code> | Add merge fields to the template. Merge fields are placed by the user creating the template and used to pre-fill data by passing values into signature requests with the `custom_fields` parameter.<br>If the signature request using that template *does not* pass a value into a merge field, then an empty field remains in the document.<br>**Default**: <code>None</code> |
| <code>message</code> | <code>str \| None</code> | The default template email message.<br>**Default**: <code>None</code> |
| <code>metadata</code> | <code>dict&#91;str, Any&#93; \| None</code> | Key-value data that should be attached to the signature request. This metadata is included in all API responses and events involving the signature request. For example, use the metadata field to store a signer's order number for look up when receiving events for the signature request.<br><br>Each request can include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and values up to 1000 characters long.<br>**Default**: <code>None</code> |
| <code>show_preview</code> | <code>bool \| None</code> | This allows the requester to enable the editor/preview experience.<br><br>- `show_preview=true`: Allows requesters to enable the editor/preview experience.<br>- `show_preview=false`: Allows requesters to disable the editor/preview experience.<br>**Default**: <code>False</code> |
| <code>show_progress_stepper</code> | <code>bool \| None</code> | When only one step remains in the signature request process and this parameter is set to `false` then the progress stepper will be hidden.<br>**Default**: <code>True</code> |
| <code>signer_roles</code> | <code>list&#91;[SubTemplateRole](dropbox_sign_api/models/sub_template_role.py) \| [SubTemplateRoleDict](dropbox_sign_api/models/sub_template_role.py)&#93; \| None</code> | An array of the designated signer roles that must be specified when sending a SignatureRequest using this Template.<br>**Default**: <code>None</code> |
| <code>skip_me_now</code> | <code>bool \| None</code> | Disables the "Me (Now)" option for the person preparing the document. Does not work with type `send_document`. Defaults to `false`.<br>**Default**: <code>False</code> |
| <code>subject</code> | <code>str \| None</code> | The template title (alias).<br>**Default**: <code>None</code> |
| <code>test_mode</code> | <code>bool \| None</code> | Whether this is a test, the signature request created from this draft will not be legally binding if set to `true`. Defaults to `false`.<br>**Default**: <code>False</code> |
| <code>title</code> | <code>str \| None</code> | The title you want to assign to the SignatureRequest.<br>**Default**: <code>None</code> |
| <code>use_preexisting_fields</code> | <code>bool \| None</code> | Enable the detection of predefined PDF fields by setting the `use_preexisting_fields` to `true` (defaults to disabled, or `false`).<br>**Default**: <code>False</code> |
| <code>ignore_text_tags_extraction_errors</code> | <code>bool \| None</code> | Sent with a value of `true` to ignore the validation errors from text tags extraction. Defaults to `false`.<br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[TemplateCreateEmbeddedDraftResponse](dropbox_sign_api/models/template_create_embedded_draft_response.py), [TemplateCreateEmbeddedDraftErrorBody](dropbox_sign_api/errors/template_create_embedded_draft_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[TemplateCreateEmbeddedDraftResponse](dropbox_sign_api/models/template_create_embedded_draft_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[TemplateCreateEmbeddedDraftErrorBody](dropbox_sign_api/errors/template_create_embedded_draft_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def template_delete(template_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Any, TemplateDeleteErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Completely deletes the template specified from the account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.template.with_raw_response.template_delete("f57db65d3f933b5316d398057a36176831451a35")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type TemplateDeleteErrorBody
```

**Async**

```python
result = await async_client.template.with_raw_response.template_delete("f57db65d3f933b5316d398057a36176831451a35")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type TemplateDeleteErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>template_id</code> | <code>str</code> | The id of the Template to delete. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;Any, [TemplateDeleteErrorBody](dropbox_sign_api/errors/template_delete_error.py)&#93;</code>

**On `Success`**: `payload` is <code>Any</code> -- successful operation

**On `Failure`**: `error` is <code>[TemplateDeleteErrorBody](dropbox_sign_api/errors/template_delete_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def template_files(template_id: str, *, file_type: FileTypeOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, TemplateFilesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Obtain a copy of the current documents specified by the `template_id` parameter. Returns a PDF or ZIP file.

If the files are currently being prepared, a status code of `409` will be returned instead. In this case please wait for the `template_created` callback event.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.template.with_raw_response.template_files("f57db65d3f933b5316d398057a36176831451a35")
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type TemplateFilesErrorBody
```

**Async**

```python
result = await async_client.template.with_raw_response.template_files("f57db65d3f933b5316d398057a36176831451a35")
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type TemplateFilesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>template_id</code> | <code>str</code> | The id of the template files to retrieve. |
| <code>file_type</code> | <code>[FileTypeOrStr](dropbox_sign_api/models/enums/file_type.py) \| None</code> | Set to `pdf` for a single merged document or `zip` for a collection of individual documents.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;None, [TemplateFilesErrorBody](dropbox_sign_api/errors/template_files_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[TemplateFilesErrorBody](dropbox_sign_api/errors/template_files_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def template_files_as_data_uri(template_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FileResponseDataUri, TemplateFilesAsDataUriErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Obtain a copy of the current documents specified by the `template_id` parameter. Returns a JSON object with a `data_uri` representing the base64 encoded file (PDFs only).

If the files are currently being prepared, a status code of `409` will be returned instead. In this case please wait for the `template_created` callback event.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.template.with_raw_response.template_files_as_data_uri("f57db65d3f933b5316d398057a36176831451a35")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FileResponseDataUri
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type TemplateFilesAsDataUriErrorBody
```

**Async**

```python
result = await async_client.template.with_raw_response.template_files_as_data_uri(
    "f57db65d3f933b5316d398057a36176831451a35"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FileResponseDataUri
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type TemplateFilesAsDataUriErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>template_id</code> | <code>str</code> | The id of the template files to retrieve. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[FileResponseDataUri](dropbox_sign_api/models/file_response_data_uri.py), [TemplateFilesAsDataUriErrorBody](dropbox_sign_api/errors/template_files_as_data_uri_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[FileResponseDataUri](dropbox_sign_api/models/file_response_data_uri.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[TemplateFilesAsDataUriErrorBody](dropbox_sign_api/errors/template_files_as_data_uri_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def template_files_as_file_url(template_id: str, *, force_download: int | None = 1, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FileResponseModel, TemplateFilesAsFileUrlErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Obtain a copy of the current documents specified by the `template_id` parameter. Returns a JSON object with a url to the file (PDFs only).

If the files are currently being prepared, a status code of `409` will be returned instead. In this case please wait for the `template_created` callback event.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.template.with_raw_response.template_files_as_file_url("f57db65d3f933b5316d398057a36176831451a35")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FileResponseModel
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type TemplateFilesAsFileUrlErrorBody
```

**Async**

```python
result = await async_client.template.with_raw_response.template_files_as_file_url(
    "f57db65d3f933b5316d398057a36176831451a35"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FileResponseModel
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type TemplateFilesAsFileUrlErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>template_id</code> | <code>str</code> | The id of the template files to retrieve. |
| <code>force_download</code> | <code>int \| None</code> | By default when opening the `file_url` a browser will download the PDF and save it locally. When set to `0` the PDF file will be displayed in the browser.<br>**Default**: <code>1</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[FileResponseModel](dropbox_sign_api/models/file_response_model.py), [TemplateFilesAsFileUrlErrorBody](dropbox_sign_api/errors/template_files_as_file_url_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[FileResponseModel](dropbox_sign_api/models/file_response_model.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[TemplateFilesAsFileUrlErrorBody](dropbox_sign_api/errors/template_files_as_file_url_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def template_get(template_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TemplateGetResponse, TemplateGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the Template specified by the `template_id` parameter.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.template.with_raw_response.template_get("f57db65d3f933b5316d398057a36176831451a35")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TemplateGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type TemplateGetErrorBody
```

**Async**

```python
result = await async_client.template.with_raw_response.template_get("f57db65d3f933b5316d398057a36176831451a35")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TemplateGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type TemplateGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>template_id</code> | <code>str</code> | The id of the Template to retrieve. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[TemplateGetResponse](dropbox_sign_api/models/template_get_response.py), [TemplateGetErrorBody](dropbox_sign_api/errors/template_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[TemplateGetResponse](dropbox_sign_api/models/template_get_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[TemplateGetErrorBody](dropbox_sign_api/errors/template_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def template_list(*, account_id: str | None = None, page: int | None = 1, page_size: int | None = 20, query: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TemplateListResponse, TemplateListErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a list of the Templates that are accessible by you.

Take a look at our [search guide](/api/reference/search/) to learn more about querying templates.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.template.with_raw_response.template_list()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TemplateListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type TemplateListErrorBody
```

**Async**

```python
result = await async_client.template.with_raw_response.template_list()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TemplateListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type TemplateListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account_id</code> | <code>str \| None</code> | Which account to return Templates for. Must be a team member. Use `all` to indicate all team members. Defaults to your account.<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Which page number of the Template List to return. Defaults to `1`.<br>**Default**: <code>1</code> |
| <code>page_size</code> | <code>int \| None</code> | Number of objects to be returned per page. Must be between `1` and `100`. Default is `20`.<br>**Default**: <code>20</code> |
| <code>query</code> | <code>str \| None</code> | String that includes search terms and/or fields to be used to filter the Template objects.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[TemplateListResponse](dropbox_sign_api/models/template_list_response.py), [TemplateListErrorBody](dropbox_sign_api/errors/template_list_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[TemplateListResponse](dropbox_sign_api/models/template_list_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[TemplateListErrorBody](dropbox_sign_api/errors/template_list_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def template_remove_user(template_id: str, body: TemplateRemoveUserRequest | TemplateRemoveUserRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TemplateGetResponse, TemplateRemoveUserErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Removes the specified Account's access to the specified Template.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.template.with_raw_response.template_remove_user(
    "f57db65d3f933b5316d398057a36176831451a35", TemplateRemoveUserRequest()
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TemplateGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type TemplateRemoveUserErrorBody
```

**Async**

```python
result = await async_client.template.with_raw_response.template_remove_user(
    "f57db65d3f933b5316d398057a36176831451a35", TemplateRemoveUserRequest()
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TemplateGetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type TemplateRemoveUserErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>template_id</code> | <code>str</code> | The id of the Template to remove the Account's access to. |
| <code>body</code> | <code>[TemplateRemoveUserRequest](dropbox_sign_api/models/template_remove_user_request.py) \| [TemplateRemoveUserRequestDict](dropbox_sign_api/models/template_remove_user_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[TemplateGetResponse](dropbox_sign_api/models/template_get_response.py), [TemplateRemoveUserErrorBody](dropbox_sign_api/errors/template_remove_user_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[TemplateGetResponse](dropbox_sign_api/models/template_get_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[TemplateRemoveUserErrorBody](dropbox_sign_api/errors/template_remove_user_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def template_update_files(template_id: str, *, client_id: str | None = None, files: FileInput | None = None, file_urls: list[str] | None = None, message: str | None = None, subject: str | None = None, test_mode: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TemplateUpdateFilesResponse, TemplateUpdateFilesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Overlays a new file with the overlay of an existing template. The new file(s) must:

1. have the same or higher page count
2. the same orientation as the file(s) being replaced.

This will not overwrite or in any way affect the existing template. Both the existing template and new template will be available for use after executing this endpoint. Also note that this will decrement your template quota.

Overlaying new files is asynchronous and a successful call to this endpoint will return 200 OK response if the request passes initial validation checks.

It is recommended that a callback be implemented to listen for the callback event. A `template_created` event will be sent when the files are updated or a `template_error` event will be sent if there was a problem while updating the files. If a callback handler has been configured and the event has not been received within 60 minutes of making the call, check the status of the request in the API dashboard and retry the request if necessary.

If the page orientation or page count is different from the original template document, we will notify you with a `template_error` [callback event](https://app.hellosign.com/api/eventsAndCallbacksWalkthrough).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.template.with_raw_response.template_update_files("f57db65d3f933b5316d398057a36176831451a35")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TemplateUpdateFilesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type TemplateUpdateFilesErrorBody
```

**Async**

```python
result = await async_client.template.with_raw_response.template_update_files("f57db65d3f933b5316d398057a36176831451a35")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TemplateUpdateFilesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type TemplateUpdateFilesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>template_id</code> | <code>str</code> | The ID of the template whose files to update. |
| <code>client_id</code> | <code>str \| None</code> | Client id of the app you're using to update this template.<br>**Default**: <code>None</code> |
| <code>files</code> | <code>FileInput \| None</code> | Use `files[]` to indicate the uploaded file(s) to use for the template.<br><br>This endpoint requires either **files** or **file_urls[]**, but not both.<br>**Default**: <code>None</code> |
| <code>file_urls</code> | <code>list&#91;str&#93; \| None</code> | Use `file_urls[]` to have Dropbox Sign download the file(s) to use for the template.<br><br>This endpoint requires either **files** or **file_urls[]**, but not both.<br>**Default**: <code>None</code> |
| <code>message</code> | <code>str \| None</code> | The new default template email message.<br>**Default**: <code>None</code> |
| <code>subject</code> | <code>str \| None</code> | The new default template email subject.<br>**Default**: <code>None</code> |
| <code>test_mode</code> | <code>bool \| None</code> | Whether this is a test, the signature request created from this draft will not be legally binding if set to `true`. Defaults to `false`.<br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[TemplateUpdateFilesResponse](dropbox_sign_api/models/template_update_files_response.py), [TemplateUpdateFilesErrorBody](dropbox_sign_api/errors/template_update_files_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[TemplateUpdateFilesResponse](dropbox_sign_api/models/template_update_files_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[TemplateUpdateFilesErrorBody](dropbox_sign_api/errors/template_update_files_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## UnclaimedDraft

> Source: [UnclaimedDraft](dropbox_sign_api/apis/unclaimed_draft.py)

<details>
<summary><code>def unclaimed_draft_create(type_: Type2OrStr, *, files: FileInput | None = None, file_urls: list[str] | None = None, allow_decline: bool | None = False, attachments: list[SubAttachment | SubAttachmentDict] | None = None, cc_email_addresses: list[EmailStr] | None = None, client_id: str | None = None, custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None, field_options: SubFieldOptions | SubFieldOptionsDict | None = None, form_field_groups: list[SubFormFieldGroup | SubFormFieldGroupDict] | None = None, form_field_rules: list[SubFormFieldRule | SubFormFieldRuleDict] | None = None, form_fields_per_document: list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None = None, hide_text_tags: bool | None = False, message: str | None = None, metadata: dict[str, Any] | None = None, show_progress_stepper: bool | None = True, signers: list[SubUnclaimedDraftSigner | SubUnclaimedDraftSignerDict] | None = None, signing_options: SubSigningOptions | SubSigningOptionsDict | None = None, signing_redirect_url: str | None = None, subject: str | None = None, test_mode: bool | None = False, use_preexisting_fields: bool | None = False, use_text_tags: bool | None = False, ignore_text_tags_extraction_errors: bool | None = False, expires_at: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UnclaimedDraftCreateResponse, UnclaimedDraftCreateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a new Draft that can be claimed using the claim URL. The first authenticated user to access the URL will claim the Draft and will be shown either the "Sign and send" or the "Request signature" page with the Draft loaded. Subsequent access to the claim URL will result in a 404.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.unclaimed_draft.with_raw_response.unclaimed_draft_create(Type2.SEND_DOCUMENT)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UnclaimedDraftCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UnclaimedDraftCreateErrorBody
```

**Async**

```python
result = await async_client.unclaimed_draft.with_raw_response.unclaimed_draft_create(Type2.SEND_DOCUMENT)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UnclaimedDraftCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UnclaimedDraftCreateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>type_</code> | <code>[Type2OrStr](dropbox_sign_api/models/enums/type2.py)</code> | The type of unclaimed draft to create. Use `send_document` to create a claimable file, and `request_signature` for a claimable signature request. If the type is `request_signature` then signers name and email_address are not optional. |
| <code>files</code> | <code>FileInput \| None</code> | Use `files[]` to indicate the uploaded file(s) to send for signature.<br><br>This endpoint requires either **files** or **file_urls[]**, but not both.<br>**Default**: <code>None</code> |
| <code>file_urls</code> | <code>list&#91;str&#93; \| None</code> | Use `file_urls[]` to have Dropbox Sign download the file(s) to send for signature.<br><br>This endpoint requires either **files** or **file_urls[]**, but not both.<br>**Default**: <code>None</code> |
| <code>allow_decline</code> | <code>bool \| None</code> | Allows signers to decline to sign a document if `true`. Defaults to `false`.<br>**Default**: <code>False</code> |
| <code>attachments</code> | <code>list&#91;[SubAttachment](dropbox_sign_api/models/sub_attachment.py) \| [SubAttachmentDict](dropbox_sign_api/models/sub_attachment.py)&#93; \| None</code> | A list describing the attachments<br>**Default**: <code>None</code> |
| <code>cc_email_addresses</code> | <code>list&#91;EmailStr&#93; \| None</code> | The email addresses that should be CCed.<br>**Default**: <code>None</code> |
| <code>client_id</code> | <code>str \| None</code> | Client id of the app used to create the draft. Used to apply the branding and callback url defined for the app.<br>**Default**: <code>None</code> |
| <code>custom_fields</code> | <code>list&#91;[SubCustomField](dropbox_sign_api/models/sub_custom_field.py) \| [SubCustomFieldDict](dropbox_sign_api/models/sub_custom_field.py)&#93; \| None</code> | When used together with merge fields, `custom_fields` allows users to add pre-filled data to their signature requests.<br><br>Pre-filled data can be used with "send-once" signature requests by adding merge fields with `form_fields_per_document` or [Text Tags](https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro) while passing values back with `custom_fields` together in one API call.<br><br>For using pre-filled on repeatable signature requests, merge fields are added to templates in the Dropbox Sign UI or by calling [/template/create_embedded_draft](/api/reference/operation/templateCreateEmbeddedDraft) and then passing `custom_fields` on subsequent signature requests referencing that template.<br>**Default**: <code>None</code> |
| <code>field_options</code> | <code>[SubFieldOptions](dropbox_sign_api/models/sub_field_options.py) \| [SubFieldOptionsDict](dropbox_sign_api/models/sub_field_options.py) \| None</code> | This allows the requester to specify field options for a signature request.<br>**Default**: <code>None</code> |
| <code>form_field_groups</code> | <code>list&#91;[SubFormFieldGroup](dropbox_sign_api/models/sub_form_field_group.py) \| [SubFormFieldGroupDict](dropbox_sign_api/models/sub_form_field_group.py)&#93; \| None</code> | Group information for fields defined in `form_fields_per_document`. String-indexed JSON array with `group_label` and `requirement` keys. `form_fields_per_document` must contain fields referencing a group defined in `form_field_groups`.<br>**Default**: <code>None</code> |
| <code>form_field_rules</code> | <code>list&#91;[SubFormFieldRule](dropbox_sign_api/models/sub_form_field_rule.py) \| [SubFormFieldRuleDict](dropbox_sign_api/models/sub_form_field_rule.py)&#93; \| None</code> | Conditional Logic rules for fields defined in `form_fields_per_document`.<br>**Default**: <code>None</code> |
| <code>form_fields_per_document</code> | <code>list&#91;[SubFormFieldsPerDocumentBase](dropbox_sign_api/models/unions/sub_form_fields_per_document_base.py) \| [SubFormFieldsPerDocumentBaseDict](dropbox_sign_api/models/unions/sub_form_fields_per_document_base.py)&#93; \| None</code> | The fields that should appear on the document, expressed as an array of objects. (For more details you can read about it here: [Using Form Fields per Document](/docs/openapi/form-fields-per-document).)<br><br>**NOTE:** Fields like **text**, **dropdown**, **checkbox**, **radio**, and **hyperlink** have additional required and optional parameters. Check out the list of [additional parameters](/api/reference/constants/#form-fields-per-document) for these field types.<br><br>* Text Field use `SubFormFieldsPerDocumentText`<br>* Dropdown Field use `SubFormFieldsPerDocumentDropdown`<br>* Hyperlink Field use `SubFormFieldsPerDocumentHyperlink`<br>* Checkbox Field use `SubFormFieldsPerDocumentCheckbox`<br>* Radio Field use `SubFormFieldsPerDocumentRadio`<br>* Signature Field use `SubFormFieldsPerDocumentSignature`<br>* Date Signed Field use `SubFormFieldsPerDocumentDateSigned`<br>* Initials Field use `SubFormFieldsPerDocumentInitials`<br>* Text Merge Field use `SubFormFieldsPerDocumentTextMerge`<br>* Checkbox Merge Field use `SubFormFieldsPerDocumentCheckboxMerge`<br>**Default**: <code>None</code> |
| <code>hide_text_tags</code> | <code>bool \| None</code> | Send with a value of `true` if you wish to enable automatic Text Tag removal. Defaults to `false`. When using Text Tags it is preferred that you set this to `false` and hide your tags with white text or something similar because the automatic removal system can cause unwanted clipping. See the [Text Tags](https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro) walkthrough for more details.<br>**Default**: <code>False</code> |
| <code>message</code> | <code>str \| None</code> | The custom message in the email that will be sent to the signers.<br>**Default**: <code>None</code> |
| <code>metadata</code> | <code>dict&#91;str, Any&#93; \| None</code> | Key-value data that should be attached to the signature request. This metadata is included in all API responses and events involving the signature request. For example, use the metadata field to store a signer's order number for look up when receiving events for the signature request.<br><br>Each request can include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and values up to 1000 characters long.<br>**Default**: <code>None</code> |
| <code>show_progress_stepper</code> | <code>bool \| None</code> | When only one step remains in the signature request process and this parameter is set to `false` then the progress stepper will be hidden.<br>**Default**: <code>True</code> |
| <code>signers</code> | <code>list&#91;[SubUnclaimedDraftSigner](dropbox_sign_api/models/sub_unclaimed_draft_signer.py) \| [SubUnclaimedDraftSignerDict](dropbox_sign_api/models/sub_unclaimed_draft_signer.py)&#93; \| None</code> | Add Signers to your Unclaimed Draft Signature Request.<br>**Default**: <code>None</code> |
| <code>signing_options</code> | <code>[SubSigningOptions](dropbox_sign_api/models/sub_signing_options.py) \| [SubSigningOptionsDict](dropbox_sign_api/models/sub_signing_options.py) \| None</code> | This allows the requester to specify the types allowed for creating a signature and specify another signing options.<br><br>**NOTE:** If `signing_options` are not defined in the request, the allowed types will default to those specified in the account settings.<br><br>**NOTE:** If `force_advanced_signature_details` is set, allowed types has to be defined too.<br>**Default**: <code>None</code> |
| <code>signing_redirect_url</code> | <code>str \| None</code> | The URL you want signers redirected to after they successfully sign.<br>**Default**: <code>None</code> |
| <code>subject</code> | <code>str \| None</code> | The subject in the email that will be sent to the signers.<br>**Default**: <code>None</code> |
| <code>test_mode</code> | <code>bool \| None</code> | Whether this is a test, the signature request created from this draft will not be legally binding if set to `true`. Defaults to `false`.<br>**Default**: <code>False</code> |
| <code>use_preexisting_fields</code> | <code>bool \| None</code> | Set `use_text_tags` to `true` to enable [Text Tags](https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro) parsing in your document (defaults to disabled, or `false`). Alternatively, if your PDF contains pre-defined fields, enable the detection of these fields by setting the `use_preexisting_fields` to `true` (defaults to disabled, or `false`). Currently we only support use of either `use_text_tags` or `use_preexisting_fields` parameter, not both.<br>**Default**: <code>False</code> |
| <code>use_text_tags</code> | <code>bool \| None</code> | Set `use_text_tags` to `true` to enable [Text Tags](https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro) parsing in your document (defaults to disabled, or `false`). Alternatively, if your PDF contains pre-defined fields, enable the detection of these fields by setting the `use_preexisting_fields` to `true` (defaults to disabled, or `false`). Currently we only support use of either `use_text_tags` or `use_preexisting_fields` parameter, not both.<br>**Default**: <code>False</code> |
| <code>ignore_text_tags_extraction_errors</code> | <code>bool \| None</code> | Sent with a value of `true` to ignore the validation errors from text tags extraction. Defaults to `false`.<br>**Default**: <code>False</code> |
| <code>expires_at</code> | <code>int \| None</code> | When the signature request will expire. Unsigned signatures will be moved to the expired status, and no longer signable. See [Signature Request Expiration Date](https://developers.hellosign.com/docs/signature-request/expiration/) for details.<br><br>**NOTE:** This does not correspond to the **expires_at** returned in the response.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[UnclaimedDraftCreateResponse](dropbox_sign_api/models/unclaimed_draft_create_response.py), [UnclaimedDraftCreateErrorBody](dropbox_sign_api/errors/unclaimed_draft_create_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[UnclaimedDraftCreateResponse](dropbox_sign_api/models/unclaimed_draft_create_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[UnclaimedDraftCreateErrorBody](dropbox_sign_api/errors/unclaimed_draft_create_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def unclaimed_draft_create_embedded(client_id: str, requester_email_address: EmailStr, *, files: FileInput | None = None, file_urls: list[str] | None = None, allow_ccs: bool | None = True, allow_decline: bool | None = False, allow_reassign: bool | None = False, attachments: list[SubAttachment | SubAttachmentDict] | None = None, cc_email_addresses: list[EmailStr] | None = None, custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None, editor_options: SubEditorOptions | SubEditorOptionsDict | None = None, field_options: SubFieldOptions | SubFieldOptionsDict | None = None, force_signer_page: bool | None = False, force_subject_message: bool | None = False, form_field_groups: list[SubFormFieldGroup | SubFormFieldGroupDict] | None = None, form_field_rules: list[SubFormFieldRule | SubFormFieldRuleDict] | None = None, form_fields_per_document: list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None = None, hide_text_tags: bool | None = False, hold_request: bool | None = False, is_for_embedded_signing: bool | None = False, message: str | None = None, metadata: dict[str, Any] | None = None, requesting_redirect_url: str | None = None, show_preview: bool | None = None, show_progress_stepper: bool | None = True, signers: list[SubUnclaimedDraftSigner | SubUnclaimedDraftSignerDict] | None = None, signing_options: SubSigningOptions | SubSigningOptionsDict | None = None, signing_redirect_url: str | None = None, skip_me_now: bool | None = False, subject: str | None = None, test_mode: bool | None = False, type_: Type3OrStr | None = Type3.REQUEST_SIGNATURE, use_preexisting_fields: bool | None = False, use_text_tags: bool | None = False, ignore_text_tags_extraction_errors: bool | None = False, populate_auto_fill_fields: bool | None = False, expires_at: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UnclaimedDraftCreateResponse, UnclaimedDraftCreateEmbeddedErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a new Draft that can be claimed and used in an embedded iFrame. The first authenticated user to access the URL will claim the Draft and will be shown the "Request signature" page with the Draft loaded. Subsequent access to the claim URL will result in a `404`. For this embedded endpoint the `requester_email_address` parameter is required.

**NOTE:** Embedded unclaimed drafts can only be accessed in embedded iFrames whereas normal drafts can be used and accessed on Dropbox Sign.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.unclaimed_draft.with_raw_response.unclaimed_draft_create_embedded(
    "some example string", "user@example.com"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UnclaimedDraftCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UnclaimedDraftCreateEmbeddedErrorBody
```

**Async**

```python
result = await async_client.unclaimed_draft.with_raw_response.unclaimed_draft_create_embedded(
    "some example string", "user@example.com"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UnclaimedDraftCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UnclaimedDraftCreateEmbeddedErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>client_id</code> | <code>str</code> | Client id of the app used to create the draft. Used to apply the branding and callback url defined for the app. |
| <code>requester_email_address</code> | <code>EmailStr</code> | The email address of the user that should be designated as the requester of this draft, if the draft type is `request_signature`. |
| <code>files</code> | <code>FileInput \| None</code> | Use `files[]` to indicate the uploaded file(s) to send for signature.<br><br>This endpoint requires either **files** or **file_urls[]**, but not both.<br>**Default**: <code>None</code> |
| <code>file_urls</code> | <code>list&#91;str&#93; \| None</code> | Use `file_urls[]` to have Dropbox Sign download the file(s) to send for signature.<br><br>This endpoint requires either **files** or **file_urls[]**, but not both.<br>**Default**: <code>None</code> |
| <code>allow_ccs</code> | <code>bool \| None</code> | This allows the requester to specify whether the user is allowed to provide email addresses to CC when claiming the draft.<br>**Default**: <code>True</code> |
| <code>allow_decline</code> | <code>bool \| None</code> | Allows signers to decline to sign a document if `true`. Defaults to `false`.<br>**Default**: <code>False</code> |
| <code>allow_reassign</code> | <code>bool \| None</code> | Allows signers to reassign their signature requests to other signers if set to `true`. Defaults to `false`.<br><br>**NOTE:** Only available for Premium plan and higher.<br>**Default**: <code>False</code> |
| <code>attachments</code> | <code>list&#91;[SubAttachment](dropbox_sign_api/models/sub_attachment.py) \| [SubAttachmentDict](dropbox_sign_api/models/sub_attachment.py)&#93; \| None</code> | A list describing the attachments<br>**Default**: <code>None</code> |
| <code>cc_email_addresses</code> | <code>list&#91;EmailStr&#93; \| None</code> | The email addresses that should be CCed.<br>**Default**: <code>None</code> |
| <code>custom_fields</code> | <code>list&#91;[SubCustomField](dropbox_sign_api/models/sub_custom_field.py) \| [SubCustomFieldDict](dropbox_sign_api/models/sub_custom_field.py)&#93; \| None</code> | When used together with merge fields, `custom_fields` allows users to add pre-filled data to their signature requests.<br><br>Pre-filled data can be used with "send-once" signature requests by adding merge fields with `form_fields_per_document` or [Text Tags](https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro) while passing values back with `custom_fields` together in one API call.<br><br>For using pre-filled on repeatable signature requests, merge fields are added to templates in the Dropbox Sign UI or by calling [/template/create_embedded_draft](/api/reference/operation/templateCreateEmbeddedDraft) and then passing `custom_fields` on subsequent signature requests referencing that template.<br>**Default**: <code>None</code> |
| <code>editor_options</code> | <code>[SubEditorOptions](dropbox_sign_api/models/sub_editor_options.py) \| [SubEditorOptionsDict](dropbox_sign_api/models/sub_editor_options.py) \| None</code> | This allows the requester to specify editor options when a preparing a document<br>**Default**: <code>None</code> |
| <code>field_options</code> | <code>[SubFieldOptions](dropbox_sign_api/models/sub_field_options.py) \| [SubFieldOptionsDict](dropbox_sign_api/models/sub_field_options.py) \| None</code> | This allows the requester to specify field options for a signature request.<br>**Default**: <code>None</code> |
| <code>force_signer_page</code> | <code>bool \| None</code> | Provide users the ability to review/edit the signers.<br>**Default**: <code>False</code> |
| <code>force_subject_message</code> | <code>bool \| None</code> | Provide users the ability to review/edit the subject and message.<br>**Default**: <code>False</code> |
| <code>form_field_groups</code> | <code>list&#91;[SubFormFieldGroup](dropbox_sign_api/models/sub_form_field_group.py) \| [SubFormFieldGroupDict](dropbox_sign_api/models/sub_form_field_group.py)&#93; \| None</code> | Group information for fields defined in `form_fields_per_document`. String-indexed JSON array with `group_label` and `requirement` keys. `form_fields_per_document` must contain fields referencing a group defined in `form_field_groups`.<br>**Default**: <code>None</code> |
| <code>form_field_rules</code> | <code>list&#91;[SubFormFieldRule](dropbox_sign_api/models/sub_form_field_rule.py) \| [SubFormFieldRuleDict](dropbox_sign_api/models/sub_form_field_rule.py)&#93; \| None</code> | Conditional Logic rules for fields defined in `form_fields_per_document`.<br>**Default**: <code>None</code> |
| <code>form_fields_per_document</code> | <code>list&#91;[SubFormFieldsPerDocumentBase](dropbox_sign_api/models/unions/sub_form_fields_per_document_base.py) \| [SubFormFieldsPerDocumentBaseDict](dropbox_sign_api/models/unions/sub_form_fields_per_document_base.py)&#93; \| None</code> | The fields that should appear on the document, expressed as an array of objects. (For more details you can read about it here: [Using Form Fields per Document](/docs/openapi/form-fields-per-document).)<br><br>**NOTE:** Fields like **text**, **dropdown**, **checkbox**, **radio**, and **hyperlink** have additional required and optional parameters. Check out the list of [additional parameters](/api/reference/constants/#form-fields-per-document) for these field types.<br><br>* Text Field use `SubFormFieldsPerDocumentText`<br>* Dropdown Field use `SubFormFieldsPerDocumentDropdown`<br>* Hyperlink Field use `SubFormFieldsPerDocumentHyperlink`<br>* Checkbox Field use `SubFormFieldsPerDocumentCheckbox`<br>* Radio Field use `SubFormFieldsPerDocumentRadio`<br>* Signature Field use `SubFormFieldsPerDocumentSignature`<br>* Date Signed Field use `SubFormFieldsPerDocumentDateSigned`<br>* Initials Field use `SubFormFieldsPerDocumentInitials`<br>* Text Merge Field use `SubFormFieldsPerDocumentTextMerge`<br>* Checkbox Merge Field use `SubFormFieldsPerDocumentCheckboxMerge`<br>**Default**: <code>None</code> |
| <code>hide_text_tags</code> | <code>bool \| None</code> | Send with a value of `true` if you wish to enable automatic Text Tag removal. Defaults to `false`. When using Text Tags it is preferred that you set this to `false` and hide your tags with white text or something similar because the automatic removal system can cause unwanted clipping. See the [Text Tags](https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro) walkthrough for more details.<br>**Default**: <code>False</code> |
| <code>hold_request</code> | <code>bool \| None</code> | The request from this draft will not automatically send to signers post-claim if set to `true`. Requester must [release](/api/reference/operation/signatureRequestReleaseHold/) the request from hold when ready to send. Defaults to `false`.<br>**Default**: <code>False</code> |
| <code>is_for_embedded_signing</code> | <code>bool \| None</code> | The request created from this draft will also be signable in embedded mode if set to `true`. Defaults to `false`.<br>**Default**: <code>False</code> |
| <code>message</code> | <code>str \| None</code> | The custom message in the email that will be sent to the signers.<br>**Default**: <code>None</code> |
| <code>metadata</code> | <code>dict&#91;str, Any&#93; \| None</code> | Key-value data that should be attached to the signature request. This metadata is included in all API responses and events involving the signature request. For example, use the metadata field to store a signer's order number for look up when receiving events for the signature request.<br><br>Each request can include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and values up to 1000 characters long.<br>**Default**: <code>None</code> |
| <code>requesting_redirect_url</code> | <code>str \| None</code> | The URL you want signers redirected to after they successfully request a signature.<br>**Default**: <code>None</code> |
| <code>show_preview</code> | <code>bool \| None</code> | This allows the requester to enable the editor/preview experience.<br><br>- `show_preview=true`: Allows requesters to enable the editor/preview experience.<br>- `show_preview=false`: Allows requesters to disable the editor/preview experience.<br>**Default**: <code>None</code> |
| <code>show_progress_stepper</code> | <code>bool \| None</code> | When only one step remains in the signature request process and this parameter is set to `false` then the progress stepper will be hidden.<br>**Default**: <code>True</code> |
| <code>signers</code> | <code>list&#91;[SubUnclaimedDraftSigner](dropbox_sign_api/models/sub_unclaimed_draft_signer.py) \| [SubUnclaimedDraftSignerDict](dropbox_sign_api/models/sub_unclaimed_draft_signer.py)&#93; \| None</code> | Add Signers to your Unclaimed Draft Signature Request.<br>**Default**: <code>None</code> |
| <code>signing_options</code> | <code>[SubSigningOptions](dropbox_sign_api/models/sub_signing_options.py) \| [SubSigningOptionsDict](dropbox_sign_api/models/sub_signing_options.py) \| None</code> | This allows the requester to specify the types allowed for creating a signature and specify another signing options.<br><br>**NOTE:** If `signing_options` are not defined in the request, the allowed types will default to those specified in the account settings.<br><br>**NOTE:** If `force_advanced_signature_details` is set, allowed types has to be defined too.<br>**Default**: <code>None</code> |
| <code>signing_redirect_url</code> | <code>str \| None</code> | The URL you want signers redirected to after they successfully sign.<br>**Default**: <code>None</code> |
| <code>skip_me_now</code> | <code>bool \| None</code> | Disables the "Me (Now)" option for the person preparing the document. Does not work with type `send_document`. Defaults to `false`.<br>**Default**: <code>False</code> |
| <code>subject</code> | <code>str \| None</code> | The subject in the email that will be sent to the signers.<br>**Default**: <code>None</code> |
| <code>test_mode</code> | <code>bool \| None</code> | Whether this is a test, the signature request created from this draft will not be legally binding if set to `true`. Defaults to `false`.<br>**Default**: <code>False</code> |
| <code>type_</code> | <code>[Type3OrStr](dropbox_sign_api/models/enums/type3.py) \| None</code> | The type of the draft. By default this is `request_signature`, but you can set it to `send_document` if you want to self sign a document and download it.<br>**Default**: <code>Type3.REQUEST_SIGNATURE</code> |
| <code>use_preexisting_fields</code> | <code>bool \| None</code> | Set `use_text_tags` to `true` to enable [Text Tags](https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro) parsing in your document (defaults to disabled, or `false`). Alternatively, if your PDF contains pre-defined fields, enable the detection of these fields by setting the `use_preexisting_fields` to `true` (defaults to disabled, or `false`). Currently we only support use of either `use_text_tags` or `use_preexisting_fields` parameter, not both.<br>**Default**: <code>False</code> |
| <code>use_text_tags</code> | <code>bool \| None</code> | Set `use_text_tags` to `true` to enable [Text Tags](https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro) parsing in your document (defaults to disabled, or `false`). Alternatively, if your PDF contains pre-defined fields, enable the detection of these fields by setting the `use_preexisting_fields` to `true` (defaults to disabled, or `false`). Currently we only support use of either `use_text_tags` or `use_preexisting_fields` parameter, not both.<br>**Default**: <code>False</code> |
| <code>ignore_text_tags_extraction_errors</code> | <code>bool \| None</code> | Sent with a value of `true` to ignore the validation errors from text tags extraction. Defaults to `false`.<br>**Default**: <code>False</code> |
| <code>populate_auto_fill_fields</code> | <code>bool \| None</code> | Controls whether [auto fill fields](https://faq.hellosign.com/hc/en-us/articles/360051467511-Auto-Fill-Fields) can automatically populate a signer's information during signing.<br><br>**NOTE:** Keep your signer's information safe by ensuring that the _signer on your signature request is the intended party_ before using this feature.<br>**Default**: <code>False</code> |
| <code>expires_at</code> | <code>int \| None</code> | When the signature request will expire. Unsigned signatures will be moved to the expired status, and no longer signable. See [Signature Request Expiration Date](https://developers.hellosign.com/docs/signature-request/expiration/) for details.<br><br>**NOTE:** This does not correspond to the **expires_at** returned in the response.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[UnclaimedDraftCreateResponse](dropbox_sign_api/models/unclaimed_draft_create_response.py), [UnclaimedDraftCreateEmbeddedErrorBody](dropbox_sign_api/errors/unclaimed_draft_create_embedded_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[UnclaimedDraftCreateResponse](dropbox_sign_api/models/unclaimed_draft_create_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[UnclaimedDraftCreateEmbeddedErrorBody](dropbox_sign_api/errors/unclaimed_draft_create_embedded_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def unclaimed_draft_create_embedded_with_template(client_id: str, requester_email_address: EmailStr, template_ids: list[str], *, allow_decline: bool | None = False, allow_reassign: bool | None = False, ccs: list[SubCc | SubCcDict] | None = None, custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None, editor_options: SubEditorOptions | SubEditorOptionsDict | None = None, field_options: SubFieldOptions | SubFieldOptionsDict | None = None, files: FileInput | None = None, file_urls: list[str] | None = None, force_signer_roles: bool | None = False, force_subject_message: bool | None = False, hold_request: bool | None = False, is_for_embedded_signing: bool | None = False, message: str | None = None, metadata: dict[str, Any] | None = None, preview_only: bool | None = False, requesting_redirect_url: str | None = None, show_preview: bool | None = False, show_progress_stepper: bool | None = True, signers: list[SubUnclaimedDraftTemplateSigner | SubUnclaimedDraftTemplateSignerDict] | None = None, signing_options: SubSigningOptions | SubSigningOptionsDict | None = None, signing_redirect_url: str | None = None, skip_me_now: bool | None = False, subject: str | None = None, test_mode: bool | None = False, title: str | None = None, populate_auto_fill_fields: bool | None = False, allow_ccs: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UnclaimedDraftCreateResponse, UnclaimedDraftCreateEmbeddedWithTemplateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a new Draft with a previously saved template(s) that can be claimed and used in an embedded iFrame. The first authenticated user to access the URL will claim the Draft and will be shown the "Request signature" page with the Draft loaded. Subsequent access to the claim URL will result in a `404`. For this embedded endpoint the `requester_email_address` parameter is required.

**NOTE:** Embedded unclaimed drafts can only be accessed in embedded iFrames whereas normal drafts can be used and accessed on Dropbox Sign.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.unclaimed_draft.with_raw_response.unclaimed_draft_create_embedded_with_template(
    "some example string", "user@example.com", ["some example string"]
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UnclaimedDraftCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UnclaimedDraftCreateEmbeddedWithTemplateErrorBody
```

**Async**

```python
result = await async_client.unclaimed_draft.with_raw_response.unclaimed_draft_create_embedded_with_template(
    "some example string", "user@example.com", ["some example string"]
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UnclaimedDraftCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UnclaimedDraftCreateEmbeddedWithTemplateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>client_id</code> | <code>str</code> | Client id of the app used to create the draft. Used to apply the branding and callback url defined for the app. |
| <code>requester_email_address</code> | <code>EmailStr</code> | The email address of the user that should be designated as the requester of this draft. |
| <code>template_ids</code> | <code>list&#91;str&#93;</code> | Use `template_ids` to create a SignatureRequest from one or more templates, in the order in which the templates will be used. |
| <code>allow_decline</code> | <code>bool \| None</code> | Allows signers to decline to sign a document if `true`. Defaults to `false`.<br>**Default**: <code>False</code> |
| <code>allow_reassign</code> | <code>bool \| None</code> | Allows signers to reassign their signature requests to other signers if set to `true`. Defaults to `false`.<br><br>**NOTE:** Only available for Premium plan and higher.<br>**Default**: <code>False</code> |
| <code>ccs</code> | <code>list&#91;[SubCc](dropbox_sign_api/models/sub_cc.py) \| [SubCcDict](dropbox_sign_api/models/sub_cc.py)&#93; \| None</code> | Add CC email recipients. Required when a CC role exists for the Template.<br>**Default**: <code>None</code> |
| <code>custom_fields</code> | <code>list&#91;[SubCustomField](dropbox_sign_api/models/sub_custom_field.py) \| [SubCustomFieldDict](dropbox_sign_api/models/sub_custom_field.py)&#93; \| None</code> | An array defining values and options for custom fields. Required when a custom field exists in the Template.<br>**Default**: <code>None</code> |
| <code>editor_options</code> | <code>[SubEditorOptions](dropbox_sign_api/models/sub_editor_options.py) \| [SubEditorOptionsDict](dropbox_sign_api/models/sub_editor_options.py) \| None</code> | This allows the requester to specify editor options when a preparing a document<br>**Default**: <code>None</code> |
| <code>field_options</code> | <code>[SubFieldOptions](dropbox_sign_api/models/sub_field_options.py) \| [SubFieldOptionsDict](dropbox_sign_api/models/sub_field_options.py) \| None</code> | This allows the requester to specify field options for a signature request.<br>**Default**: <code>None</code> |
| <code>files</code> | <code>FileInput \| None</code> | Use `files[]` to append additional files to the signature request being created from the template. Dropbox Sign will parse the files for [text tags](https://app.hellosign.com/api/textTagsWalkthrough) and append it to the signature request. Text tags for signers not on the template(s) will be ignored.<br><br>**files** or **file_urls[]** is required, but not both.<br>**Default**: <code>None</code> |
| <code>file_urls</code> | <code>list&#91;str&#93; \| None</code> | Use file_urls[] to append additional files to the signature request being created from the template. Dropbox Sign will download the file, then parse it for [text tags](https://app.hellosign.com/api/textTagsWalkthrough), and append to the signature request. Text tags for signers not on the template(s) will be ignored.<br><br>**files** or **file_urls[]** is required, but not both.<br>**Default**: <code>None</code> |
| <code>force_signer_roles</code> | <code>bool \| None</code> | Provide users the ability to review/edit the template signer roles.<br>**Default**: <code>False</code> |
| <code>force_subject_message</code> | <code>bool \| None</code> | Provide users the ability to review/edit the template subject and message.<br>**Default**: <code>False</code> |
| <code>hold_request</code> | <code>bool \| None</code> | The request from this draft will not automatically send to signers post-claim if set to 1. Requester must [release](/api/reference/operation/signatureRequestReleaseHold/) the request from hold when ready to send. Defaults to `false`.<br>**Default**: <code>False</code> |
| <code>is_for_embedded_signing</code> | <code>bool \| None</code> | The request created from this draft will also be signable in embedded mode if set to `true`. Defaults to `false`.<br>**Default**: <code>False</code> |
| <code>message</code> | <code>str \| None</code> | The custom message in the email that will be sent to the signers.<br>**Default**: <code>None</code> |
| <code>metadata</code> | <code>dict&#91;str, Any&#93; \| None</code> | Key-value data that should be attached to the signature request. This metadata is included in all API responses and events involving the signature request. For example, use the metadata field to store a signer's order number for look up when receiving events for the signature request.<br><br>Each request can include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and values up to 1000 characters long.<br>**Default**: <code>None</code> |
| <code>preview_only</code> | <code>bool \| None</code> | This allows the requester to enable the preview experience (i.e. does not allow the requester's end user to add any additional fields via the editor).<br><br>- `preview_only=true`: Allows requesters to enable the preview only experience.<br>- `preview_only=false`: Allows requesters to disable the preview only experience.<br><br>**NOTE:** This parameter overwrites `show_preview=1` (if set).<br>**Default**: <code>False</code> |
| <code>requesting_redirect_url</code> | <code>str \| None</code> | The URL you want signers redirected to after they successfully request a signature.<br>**Default**: <code>None</code> |
| <code>show_preview</code> | <code>bool \| None</code> | This allows the requester to enable the editor/preview experience.<br><br>- `show_preview=true`: Allows requesters to enable the editor/preview experience.<br>- `show_preview=false`: Allows requesters to disable the editor/preview experience.<br>**Default**: <code>False</code> |
| <code>show_progress_stepper</code> | <code>bool \| None</code> | When only one step remains in the signature request process and this parameter is set to `false` then the progress stepper will be hidden.<br>**Default**: <code>True</code> |
| <code>signers</code> | <code>list&#91;[SubUnclaimedDraftTemplateSigner](dropbox_sign_api/models/sub_unclaimed_draft_template_signer.py) \| [SubUnclaimedDraftTemplateSignerDict](dropbox_sign_api/models/sub_unclaimed_draft_template_signer.py)&#93; \| None</code> | Add Signers to your Templated-based Signature Request.<br>**Default**: <code>None</code> |
| <code>signing_options</code> | <code>[SubSigningOptions](dropbox_sign_api/models/sub_signing_options.py) \| [SubSigningOptionsDict](dropbox_sign_api/models/sub_signing_options.py) \| None</code> | This allows the requester to specify the types allowed for creating a signature and specify another signing options.<br><br>**NOTE:** If `signing_options` are not defined in the request, the allowed types will default to those specified in the account settings.<br><br>**NOTE:** If `force_advanced_signature_details` is set, allowed types has to be defined too.<br>**Default**: <code>None</code> |
| <code>signing_redirect_url</code> | <code>str \| None</code> | The URL you want signers redirected to after they successfully sign.<br>**Default**: <code>None</code> |
| <code>skip_me_now</code> | <code>bool \| None</code> | Disables the "Me (Now)" option for the person preparing the document. Does not work with type `send_document`. Defaults to `false`.<br>**Default**: <code>False</code> |
| <code>subject</code> | <code>str \| None</code> | The subject in the email that will be sent to the signers.<br>**Default**: <code>None</code> |
| <code>test_mode</code> | <code>bool \| None</code> | Whether this is a test, the signature request created from this draft will not be legally binding if set to `true`. Defaults to `false`.<br>**Default**: <code>False</code> |
| <code>title</code> | <code>str \| None</code> | The title you want to assign to the SignatureRequest.<br>**Default**: <code>None</code> |
| <code>populate_auto_fill_fields</code> | <code>bool \| None</code> | Controls whether [auto fill fields](https://faq.hellosign.com/hc/en-us/articles/360051467511-Auto-Fill-Fields) can automatically populate a signer's information during signing.<br><br>**NOTE:** Keep your signer's information safe by ensuring that the _signer on your signature request is the intended party_ before using this feature.<br>**Default**: <code>False</code> |
| <code>allow_ccs</code> | <code>bool \| None</code> | This allows the requester to specify whether the user is allowed to provide email addresses to CC when claiming the draft.<br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[UnclaimedDraftCreateResponse](dropbox_sign_api/models/unclaimed_draft_create_response.py), [UnclaimedDraftCreateEmbeddedWithTemplateErrorBody](dropbox_sign_api/errors/unclaimed_draft_create_embedded_with_template_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[UnclaimedDraftCreateResponse](dropbox_sign_api/models/unclaimed_draft_create_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[UnclaimedDraftCreateEmbeddedWithTemplateErrorBody](dropbox_sign_api/errors/unclaimed_draft_create_embedded_with_template_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def unclaimed_draft_edit_and_resend(signature_request_id: str, body: UnclaimedDraftEditAndResendRequest | UnclaimedDraftEditAndResendRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UnclaimedDraftCreateResponse, UnclaimedDraftEditAndResendErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a new signature request from an embedded request that can be edited prior to being sent to the recipients. Parameter `test_mode` can be edited prior to request. Signers can be edited in embedded editor. Requester's email address will remain unchanged if `requester_email_address` parameter is not set.

**NOTE:** Embedded unclaimed drafts can only be accessed in embedded iFrames whereas normal drafts can be used and accessed on Dropbox Sign.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.unclaimed_draft.with_raw_response.unclaimed_draft_edit_and_resend(
    "fa5c8a0b0f492d768749333ad6fcc214c111e967", UnclaimedDraftEditAndResendRequest(client_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UnclaimedDraftCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UnclaimedDraftEditAndResendErrorBody
```

**Async**

```python
result = await async_client.unclaimed_draft.with_raw_response.unclaimed_draft_edit_and_resend(
    "fa5c8a0b0f492d768749333ad6fcc214c111e967", UnclaimedDraftEditAndResendRequest(client_id="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UnclaimedDraftCreateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UnclaimedDraftEditAndResendErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>signature_request_id</code> | <code>str</code> | The ID of the signature request to edit and resend. |
| <code>body</code> | <code>[UnclaimedDraftEditAndResendRequest](dropbox_sign_api/models/unclaimed_draft_edit_and_resend_request.py) \| [UnclaimedDraftEditAndResendRequestDict](dropbox_sign_api/models/unclaimed_draft_edit_and_resend_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](dropbox_sign_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](dropbox_sign_api/core/results.py)&#91;[UnclaimedDraftCreateResponse](dropbox_sign_api/models/unclaimed_draft_create_response.py), [UnclaimedDraftEditAndResendErrorBody](dropbox_sign_api/errors/unclaimed_draft_edit_and_resend_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[UnclaimedDraftCreateResponse](dropbox_sign_api/models/unclaimed_draft_create_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[UnclaimedDraftEditAndResendErrorBody](dropbox_sign_api/errors/unclaimed_draft_edit_and_resend_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400-499 | <code>[ErrorResponse](dropbox_sign_api/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](dropbox_sign_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

