<!-- Generated file — do not edit; regenerated with the SDK. -->

# UnclaimedDraft — operations

Accessor: `client.unclaimed_draft` · Source: `dropbox_sign_api/apis/unclaimed_draft.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.unclaimed_draft.unclaimed_draft_create

- **Route**: `POST /unclaimed_draft/create`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def unclaimed_draft_create(type_: Type2OrStr, *, files: FileInput | None = None, file_urls: list[str] | None = None, allow_decline: bool | None = False, attachments: list[SubAttachment | SubAttachmentDict] | None = None, cc_email_addresses: list[EmailStr] | None = None, client_id: str | None = None, custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None, field_options: SubFieldOptions | SubFieldOptionsDict | None = None, form_field_groups: list[SubFormFieldGroup | SubFormFieldGroupDict] | None = None, form_field_rules: list[SubFormFieldRule | SubFormFieldRuleDict] | None = None, form_fields_per_document: list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None = None, hide_text_tags: bool | None = False, message: str | None = None, metadata: dict[str, Any] | None = None, show_progress_stepper: bool | None = True, signers: list[SubUnclaimedDraftSigner | SubUnclaimedDraftSignerDict] | None = None, signing_options: SubSigningOptions | SubSigningOptionsDict | None = None, signing_redirect_url: str | None = None, subject: str | None = None, test_mode: bool | None = False, use_preexisting_fields: bool | None = False, use_text_tags: bool | None = False, ignore_text_tags_extraction_errors: bool | None = False, expires_at: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `type_`
- **Params**: `type_` — multipart field `type` · `files` — multipart file · `file_urls` — multipart field · `allow_decline` — multipart field · `attachments` — multipart field · `cc_email_addresses` — multipart field · `client_id` — multipart field · `custom_fields` — multipart field · `field_options` — multipart field · `form_field_groups` — multipart field · `form_field_rules` — multipart field · `form_fields_per_document` — multipart field · `hide_text_tags` — multipart field · `message` — multipart field · `metadata` — multipart field · `show_progress_stepper` — multipart field · `signers` — multipart field · `signing_options` — multipart field · `signing_redirect_url` — multipart field · `subject` — multipart field · `test_mode` — multipart field · `use_preexisting_fields` — multipart field · `use_text_tags` — multipart field · `ignore_text_tags_extraction_errors` — multipart field · `expires_at` — multipart field
- **Returns (parsed)**: `UnclaimedDraftCreateResponse`
- **Returns (raw)**: `ApiResult[UnclaimedDraftCreateResponse, UnclaimedDraftCreateErrorBody]`
- **Error**: `UnclaimedDraftCreateErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Type2OrStr` | `dropbox_sign_api/models/enums/type2.py` |
| `SubAttachment` | `dropbox_sign_api/models/sub_attachment.py` |
| `SubAttachmentDict` | `dropbox_sign_api/models/sub_attachment.py` |
| `SubCustomField` | `dropbox_sign_api/models/sub_custom_field.py` |
| `SubCustomFieldDict` | `dropbox_sign_api/models/sub_custom_field.py` |
| `SubFieldOptions` | `dropbox_sign_api/models/sub_field_options.py` |
| `SubFieldOptionsDict` | `dropbox_sign_api/models/sub_field_options.py` |
| `SubFormFieldGroup` | `dropbox_sign_api/models/sub_form_field_group.py` |
| `SubFormFieldGroupDict` | `dropbox_sign_api/models/sub_form_field_group.py` |
| `SubFormFieldRule` | `dropbox_sign_api/models/sub_form_field_rule.py` |
| `SubFormFieldRuleDict` | `dropbox_sign_api/models/sub_form_field_rule.py` |
| `SubFormFieldsPerDocumentBase` | `dropbox_sign_api/models/unions/sub_form_fields_per_document_base.py` |
| `SubFormFieldsPerDocumentBaseDict` | `dropbox_sign_api/models/unions/sub_form_fields_per_document_base.py` |
| `SubUnclaimedDraftSigner` | `dropbox_sign_api/models/sub_unclaimed_draft_signer.py` |
| `SubUnclaimedDraftSignerDict` | `dropbox_sign_api/models/sub_unclaimed_draft_signer.py` |
| `SubSigningOptions` | `dropbox_sign_api/models/sub_signing_options.py` |
| `SubSigningOptionsDict` | `dropbox_sign_api/models/sub_signing_options.py` |
| `UnclaimedDraftCreateResponse` | `dropbox_sign_api/models/unclaimed_draft_create_response.py` |
| `UnclaimedDraftCreateErrorBody` | `dropbox_sign_api/errors/unclaimed_draft_create_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.unclaimed_draft.unclaimed_draft_create_embedded

- **Route**: `POST /unclaimed_draft/create_embedded`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def unclaimed_draft_create_embedded(client_id: str, requester_email_address: EmailStr, *, files: FileInput | None = None, file_urls: list[str] | None = None, allow_ccs: bool | None = True, allow_decline: bool | None = False, allow_reassign: bool | None = False, attachments: list[SubAttachment | SubAttachmentDict] | None = None, cc_email_addresses: list[EmailStr] | None = None, custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None, editor_options: SubEditorOptions | SubEditorOptionsDict | None = None, field_options: SubFieldOptions | SubFieldOptionsDict | None = None, force_signer_page: bool | None = False, force_subject_message: bool | None = False, form_field_groups: list[SubFormFieldGroup | SubFormFieldGroupDict] | None = None, form_field_rules: list[SubFormFieldRule | SubFormFieldRuleDict] | None = None, form_fields_per_document: list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None = None, hide_text_tags: bool | None = False, hold_request: bool | None = False, is_for_embedded_signing: bool | None = False, message: str | None = None, metadata: dict[str, Any] | None = None, requesting_redirect_url: str | None = None, show_preview: bool | None = None, show_progress_stepper: bool | None = True, signers: list[SubUnclaimedDraftSigner | SubUnclaimedDraftSignerDict] | None = None, signing_options: SubSigningOptions | SubSigningOptionsDict | None = None, signing_redirect_url: str | None = None, skip_me_now: bool | None = False, subject: str | None = None, test_mode: bool | None = False, type_: Type3OrStr | None = Type3.REQUEST_SIGNATURE, use_preexisting_fields: bool | None = False, use_text_tags: bool | None = False, ignore_text_tags_extraction_errors: bool | None = False, populate_auto_fill_fields: bool | None = False, expires_at: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `client_id`, `requester_email_address`
- **Params**: `client_id` — multipart field · `requester_email_address` — multipart field · `files` — multipart file · `file_urls` — multipart field · `allow_ccs` — multipart field · `allow_decline` — multipart field · `allow_reassign` — multipart field · `attachments` — multipart field · `cc_email_addresses` — multipart field · `custom_fields` — multipart field · `editor_options` — multipart field · `field_options` — multipart field · `force_signer_page` — multipart field · `force_subject_message` — multipart field · `form_field_groups` — multipart field · `form_field_rules` — multipart field · `form_fields_per_document` — multipart field · `hide_text_tags` — multipart field · `hold_request` — multipart field · `is_for_embedded_signing` — multipart field · `message` — multipart field · `metadata` — multipart field · `requesting_redirect_url` — multipart field · `show_preview` — multipart field · `show_progress_stepper` — multipart field · `signers` — multipart field · `signing_options` — multipart field · `signing_redirect_url` — multipart field · `skip_me_now` — multipart field · `subject` — multipart field · `test_mode` — multipart field · `type_` — multipart field `type` · `use_preexisting_fields` — multipart field · `use_text_tags` — multipart field · `ignore_text_tags_extraction_errors` — multipart field · `populate_auto_fill_fields` — multipart field · `expires_at` — multipart field
- **Returns (parsed)**: `UnclaimedDraftCreateResponse`
- **Returns (raw)**: `ApiResult[UnclaimedDraftCreateResponse, UnclaimedDraftCreateEmbeddedErrorBody]`
- **Error**: `UnclaimedDraftCreateEmbeddedErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SubAttachment` | `dropbox_sign_api/models/sub_attachment.py` |
| `SubAttachmentDict` | `dropbox_sign_api/models/sub_attachment.py` |
| `SubCustomField` | `dropbox_sign_api/models/sub_custom_field.py` |
| `SubCustomFieldDict` | `dropbox_sign_api/models/sub_custom_field.py` |
| `SubEditorOptions` | `dropbox_sign_api/models/sub_editor_options.py` |
| `SubEditorOptionsDict` | `dropbox_sign_api/models/sub_editor_options.py` |
| `SubFieldOptions` | `dropbox_sign_api/models/sub_field_options.py` |
| `SubFieldOptionsDict` | `dropbox_sign_api/models/sub_field_options.py` |
| `SubFormFieldGroup` | `dropbox_sign_api/models/sub_form_field_group.py` |
| `SubFormFieldGroupDict` | `dropbox_sign_api/models/sub_form_field_group.py` |
| `SubFormFieldRule` | `dropbox_sign_api/models/sub_form_field_rule.py` |
| `SubFormFieldRuleDict` | `dropbox_sign_api/models/sub_form_field_rule.py` |
| `SubFormFieldsPerDocumentBase` | `dropbox_sign_api/models/unions/sub_form_fields_per_document_base.py` |
| `SubFormFieldsPerDocumentBaseDict` | `dropbox_sign_api/models/unions/sub_form_fields_per_document_base.py` |
| `SubUnclaimedDraftSigner` | `dropbox_sign_api/models/sub_unclaimed_draft_signer.py` |
| `SubUnclaimedDraftSignerDict` | `dropbox_sign_api/models/sub_unclaimed_draft_signer.py` |
| `SubSigningOptions` | `dropbox_sign_api/models/sub_signing_options.py` |
| `SubSigningOptionsDict` | `dropbox_sign_api/models/sub_signing_options.py` |
| `Type3OrStr` | `dropbox_sign_api/models/enums/type3.py` |
| `UnclaimedDraftCreateResponse` | `dropbox_sign_api/models/unclaimed_draft_create_response.py` |
| `UnclaimedDraftCreateEmbeddedErrorBody` | `dropbox_sign_api/errors/unclaimed_draft_create_embedded_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.unclaimed_draft.unclaimed_draft_create_embedded_with_template

- **Route**: `POST /unclaimed_draft/create_embedded_with_template`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def unclaimed_draft_create_embedded_with_template(client_id: str, requester_email_address: EmailStr, template_ids: list[str], *, allow_decline: bool | None = False, allow_reassign: bool | None = False, ccs: list[SubCc | SubCcDict] | None = None, custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None, editor_options: SubEditorOptions | SubEditorOptionsDict | None = None, field_options: SubFieldOptions | SubFieldOptionsDict | None = None, files: FileInput | None = None, file_urls: list[str] | None = None, force_signer_roles: bool | None = False, force_subject_message: bool | None = False, hold_request: bool | None = False, is_for_embedded_signing: bool | None = False, message: str | None = None, metadata: dict[str, Any] | None = None, preview_only: bool | None = False, requesting_redirect_url: str | None = None, show_preview: bool | None = False, show_progress_stepper: bool | None = True, signers: list[SubUnclaimedDraftTemplateSigner | SubUnclaimedDraftTemplateSignerDict] | None = None, signing_options: SubSigningOptions | SubSigningOptionsDict | None = None, signing_redirect_url: str | None = None, skip_me_now: bool | None = False, subject: str | None = None, test_mode: bool | None = False, title: str | None = None, populate_auto_fill_fields: bool | None = False, allow_ccs: bool | None = False, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `client_id`, `requester_email_address`, `template_ids`
- **Params**: `client_id` — multipart field · `requester_email_address` — multipart field · `template_ids` — multipart field · `allow_decline` — multipart field · `allow_reassign` — multipart field · `ccs` — multipart field · `custom_fields` — multipart field · `editor_options` — multipart field · `field_options` — multipart field · `files` — multipart file · `file_urls` — multipart field · `force_signer_roles` — multipart field · `force_subject_message` — multipart field · `hold_request` — multipart field · `is_for_embedded_signing` — multipart field · `message` — multipart field · `metadata` — multipart field · `preview_only` — multipart field · `requesting_redirect_url` — multipart field · `show_preview` — multipart field · `show_progress_stepper` — multipart field · `signers` — multipart field · `signing_options` — multipart field · `signing_redirect_url` — multipart field · `skip_me_now` — multipart field · `subject` — multipart field · `test_mode` — multipart field · `title` — multipart field · `populate_auto_fill_fields` — multipart field · `allow_ccs` — multipart field
- **Returns (parsed)**: `UnclaimedDraftCreateResponse`
- **Returns (raw)**: `ApiResult[UnclaimedDraftCreateResponse, UnclaimedDraftCreateEmbeddedWithTemplateErrorBody]`
- **Error**: `UnclaimedDraftCreateEmbeddedWithTemplateErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SubCc` | `dropbox_sign_api/models/sub_cc.py` |
| `SubCcDict` | `dropbox_sign_api/models/sub_cc.py` |
| `SubCustomField` | `dropbox_sign_api/models/sub_custom_field.py` |
| `SubCustomFieldDict` | `dropbox_sign_api/models/sub_custom_field.py` |
| `SubEditorOptions` | `dropbox_sign_api/models/sub_editor_options.py` |
| `SubEditorOptionsDict` | `dropbox_sign_api/models/sub_editor_options.py` |
| `SubFieldOptions` | `dropbox_sign_api/models/sub_field_options.py` |
| `SubFieldOptionsDict` | `dropbox_sign_api/models/sub_field_options.py` |
| `SubUnclaimedDraftTemplateSigner` | `dropbox_sign_api/models/sub_unclaimed_draft_template_signer.py` |
| `SubUnclaimedDraftTemplateSignerDict` | `dropbox_sign_api/models/sub_unclaimed_draft_template_signer.py` |
| `SubSigningOptions` | `dropbox_sign_api/models/sub_signing_options.py` |
| `SubSigningOptionsDict` | `dropbox_sign_api/models/sub_signing_options.py` |
| `UnclaimedDraftCreateResponse` | `dropbox_sign_api/models/unclaimed_draft_create_response.py` |
| `UnclaimedDraftCreateEmbeddedWithTemplateErrorBody` | `dropbox_sign_api/errors/unclaimed_draft_create_embedded_with_template_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.unclaimed_draft.unclaimed_draft_edit_and_resend

- **Route**: `POST /unclaimed_draft/edit_and_resend/{signature_request_id}`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def unclaimed_draft_edit_and_resend(signature_request_id: str, body: UnclaimedDraftEditAndResendRequest | UnclaimedDraftEditAndResendRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `signature_request_id`, `body`
- **Params**: `signature_request_id` — path · `body` — JSON body
- **Returns (parsed)**: `UnclaimedDraftCreateResponse`
- **Returns (raw)**: `ApiResult[UnclaimedDraftCreateResponse, UnclaimedDraftEditAndResendErrorBody]`
- **Error**: `UnclaimedDraftEditAndResendErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UnclaimedDraftEditAndResendRequest` | `dropbox_sign_api/models/unclaimed_draft_edit_and_resend_request.py` |
| `UnclaimedDraftEditAndResendRequestDict` | `dropbox_sign_api/models/unclaimed_draft_edit_and_resend_request.py` |
| `UnclaimedDraftCreateResponse` | `dropbox_sign_api/models/unclaimed_draft_create_response.py` |
| `UnclaimedDraftEditAndResendErrorBody` | `dropbox_sign_api/errors/unclaimed_draft_edit_and_resend_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

