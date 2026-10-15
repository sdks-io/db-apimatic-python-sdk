from __future__ import annotations

from typing import Any
from uuid import UUID, uuid4

from pydantic import EmailStr

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
    json_body,
    json_decoder,
    multipart_body,
    param,
    unwrap,
)
from ..errors.signature_request_bulk_create_embedded_with_template_error import (
    SignatureRequestBulkCreateEmbeddedWithTemplateErrorBody,
    signature_request_bulk_create_embedded_with_template_error_mapper,
)
from ..errors.signature_request_bulk_send_with_template_error import (
    SignatureRequestBulkSendWithTemplateErrorBody,
    signature_request_bulk_send_with_template_error_mapper,
)
from ..errors.signature_request_cancel_error import (
    SignatureRequestCancelErrorBody,
    signature_request_cancel_error_mapper,
)
from ..errors.signature_request_create_embedded_error import (
    SignatureRequestCreateEmbeddedErrorBody,
    signature_request_create_embedded_error_mapper,
)
from ..errors.signature_request_create_embedded_with_template_error import (
    SignatureRequestCreateEmbeddedWithTemplateErrorBody,
    signature_request_create_embedded_with_template_error_mapper,
)
from ..errors.signature_request_edit_embedded_error import (
    SignatureRequestEditEmbeddedErrorBody,
    signature_request_edit_embedded_error_mapper,
)
from ..errors.signature_request_edit_embedded_with_template_error import (
    SignatureRequestEditEmbeddedWithTemplateErrorBody,
    signature_request_edit_embedded_with_template_error_mapper,
)
from ..errors.signature_request_edit_error import SignatureRequestEditErrorBody, signature_request_edit_error_mapper
from ..errors.signature_request_edit_with_template_error import (
    SignatureRequestEditWithTemplateErrorBody,
    signature_request_edit_with_template_error_mapper,
)
from ..errors.signature_request_files_as_data_uri_error import (
    SignatureRequestFilesAsDataUriErrorBody,
    signature_request_files_as_data_uri_error_mapper,
)
from ..errors.signature_request_files_as_file_url_error import (
    SignatureRequestFilesAsFileUrlErrorBody,
    signature_request_files_as_file_url_error_mapper,
)
from ..errors.signature_request_files_error import SignatureRequestFilesErrorBody, signature_request_files_error_mapper
from ..errors.signature_request_get_error import SignatureRequestGetErrorBody, signature_request_get_error_mapper
from ..errors.signature_request_list_error import SignatureRequestListErrorBody, signature_request_list_error_mapper
from ..errors.signature_request_release_hold_error import (
    SignatureRequestReleaseHoldErrorBody,
    signature_request_release_hold_error_mapper,
)
from ..errors.signature_request_remind_error import (
    SignatureRequestRemindErrorBody,
    signature_request_remind_error_mapper,
)
from ..errors.signature_request_remove_error import (
    SignatureRequestRemoveErrorBody,
    signature_request_remove_error_mapper,
)
from ..errors.signature_request_send_error import SignatureRequestSendErrorBody, signature_request_send_error_mapper
from ..errors.signature_request_send_with_template_error import (
    SignatureRequestSendWithTemplateErrorBody,
    signature_request_send_with_template_error_mapper,
)
from ..errors.signature_request_update_error import (
    SignatureRequestUpdateErrorBody,
    signature_request_update_error_mapper,
)
from ..models.bulk_send_job_send_response import BulkSendJobSendResponse
from ..models.enums.file_type import FileType, FileTypeOrStr
from ..models.file_response_data_uri import FileResponseDataUri
from ..models.file_response_model import FileResponseModel
from ..models.signature_request_get_response import SignatureRequestGetResponse
from ..models.signature_request_list_response import SignatureRequestListResponse
from ..models.signature_request_remind_request import SignatureRequestRemindRequest, SignatureRequestRemindRequestDict
from ..models.signature_request_update_request import SignatureRequestUpdateRequest, SignatureRequestUpdateRequestDict
from ..models.sub_attachment import SubAttachment, SubAttachmentDict
from ..models.sub_bulk_signer_list import SubBulkSignerList, SubBulkSignerListDict
from ..models.sub_cc import SubCc, SubCcDict
from ..models.sub_custom_field import SubCustomField, SubCustomFieldDict
from ..models.sub_field_options import SubFieldOptions, SubFieldOptionsDict
from ..models.sub_form_field_group import SubFormFieldGroup, SubFormFieldGroupDict
from ..models.sub_form_field_rule import SubFormFieldRule, SubFormFieldRuleDict
from ..models.sub_signature_request_grouped_signers import (
    SubSignatureRequestGroupedSigners,
    SubSignatureRequestGroupedSignersDict,
)
from ..models.sub_signature_request_signer import SubSignatureRequestSigner, SubSignatureRequestSignerDict
from ..models.sub_signature_request_template_signer import (
    SubSignatureRequestTemplateSigner,
    SubSignatureRequestTemplateSignerDict,
)
from ..models.sub_signing_options import SubSigningOptions, SubSigningOptionsDict
from ..models.unions.sub_form_fields_per_document_base import (
    SubFormFieldsPerDocumentBase,
    SubFormFieldsPerDocumentBaseDict,
)
from ..server.server import Server


class SignatureRequest:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SignatureRequestWithRawResponse(client, server, auth)

    def signature_request_bulk_create_embedded_with_template(
        self,
        template_ids: list[str],
        client_id: str,
        *,
        signer_file: FileInput | None = None,
        signer_list: list[SubBulkSignerList | SubBulkSignerListDict] | None = None,
        allow_decline: bool | None = False,
        ccs: list[SubCc | SubCcDict] | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        signing_redirect_url: str | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        expires_at: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkSendJobSendResponse:
        """Creates BulkSendJob which sends up to 250 SignatureRequests in bulk based off of the provided Template(s)
        specified with the ``template_ids`` parameter to be signed in an embedded iFrame. These embedded signature
        requests can only be signed in embedded iFrames whereas normal signature requests can only be signed on Dropbox
        Sign.

        **NOTE:** Only available for Standard plan and higher.

        Args:
            template_ids: Use ``template_ids`` to create a SignatureRequest from one or more templates, in the order in
                which the template will be used.
            client_id: Client id of the app you're using to create this embedded signature request. Used for security
                purposes.
            signer_file: ``signer_file`` is a CSV file defining values and options for signer fields. Required unless a
                ``signer_list`` is used, you may not use both. The CSV can have the following columns: - ``name``: the
                name of the signer filling the role of RoleName - ``email_address``: email address of the signer filling
                the role of RoleName - ``pin``: the 4- to 12-character access code that will secure this signer's
                signature page (optional) - ``sms_phone_number``: An E.164 formatted phone number that will receive a
                code via SMS to access this signer's signature page. (optional) By using the feature, you agree you are
                responsible for obtaining a signer's consent to receive text messages from Dropbox Sign related to this
                signature request and confirm you have obtained such consent from all signers prior to enabling SMS
                delivery for this signature request. `Learn more
                <https://faq.hellosign.com/hc/en-us/articles/15815316468877-Dropbox-Sign-SMS-tools-add-on>`__. **NOTE:**
                Not available in test mode and requires a Standard plan or higher. - ``*_field``: any column with a
                _field" suffix will be treated as a custom field (optional) You may only specify field values here, any
                other options should be set in the custom_fields request parameter. Example CSV: ``` name,
                email_address, pin, company_field George, george@example.com, d79a3td, ABC Corp Mary, mary@example.com,
                gd9as5b, 123 LLC ```
            signer_list: ``signer_list`` is an array defining values and options for signer fields. Required unless a
                ``signer_file`` is used, you may not use both.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            ccs: Add CC email recipients. Required when a CC role exists for the Template.
            custom_fields: When used together with merge fields, ``custom_fields`` allows users to add pre-filled data
                to their signature requests. Pre-filled data can be used with "send-once" signature requests by adding
                merge fields with ``form_fields_per_document`` or `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ while passing values back with
                ``custom_fields`` together in one API call. For using pre-filled on repeatable signature requests, merge
                fields are added to templates in the Dropbox Sign UI or by calling `/template/create_embedded_draft
                </api/reference/operation/templateCreateEmbeddedDraft>`__ and then passing ``custom_fields`` on
                subsequent signature requests referencing that template.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            signing_redirect_url: The URL you want signers redirected to after they successfully sign.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request will not be legally binding if set to ``true``.
                Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            expires_at: When the signature request will expire. Unsigned signatures will be moved to the expired status,
                and no longer signable. See `Signature Request Expiration Date
                <https://developers.hellosign.com/docs/signature-request/expiration/>`__ for details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.signature_request_bulk_create_embedded_with_template(
                template_ids,
                client_id,
                signer_file=signer_file,
                signer_list=signer_list,
                allow_decline=allow_decline,
                ccs=ccs,
                custom_fields=custom_fields,
                message=message,
                metadata=metadata,
                signing_redirect_url=signing_redirect_url,
                subject=subject,
                test_mode=test_mode,
                title=title,
                expires_at=expires_at,
                request_options=request_options,
            ),
        )

    def signature_request_bulk_send_with_template(
        self,
        template_ids: list[str],
        *,
        signer_file: FileInput | None = None,
        signer_list: list[SubBulkSignerList | SubBulkSignerListDict] | None = None,
        allow_decline: bool | None = False,
        ccs: list[SubCc | SubCcDict] | None = None,
        client_id: str | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        signing_redirect_url: str | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        expires_at: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkSendJobSendResponse:
        """Creates BulkSendJob which sends up to 250 SignatureRequests in bulk based off of the provided Template(s)
        specified with the ``template_ids`` parameter.

        **NOTE:** Only available for Standard plan and higher.

        Args:
            template_ids: Use ``template_ids`` to create a SignatureRequest from one or more templates, in the order in
                which the template will be used.
            signer_file: ``signer_file`` is a CSV file defining values and options for signer fields. Required unless a
                ``signer_list`` is used, you may not use both. The CSV can have the following columns: - ``name``: the
                name of the signer filling the role of RoleName - ``email_address``: email address of the signer filling
                the role of RoleName - ``pin``: the 4- to 12-character access code that will secure this signer's
                signature page (optional) - ``sms_phone_number``: An E.164 formatted phone number that will receive a
                code via SMS to access this signer's signature page. (optional) By using the feature, you agree you are
                responsible for obtaining a signer's consent to receive text messages from Dropbox Sign related to this
                signature request and confirm you have obtained such consent from all signers prior to enabling SMS
                delivery for this signature request. `Learn more
                <https://faq.hellosign.com/hc/en-us/articles/15815316468877-Dropbox-Sign-SMS-tools-add-on>`__. **NOTE:**
                Not available in test mode and requires a Standard plan or higher. - ``*_field``: any column with a
                _field" suffix will be treated as a custom field (optional) You may only specify field values here, any
                other options should be set in the custom_fields request parameter. Example CSV: ``` name,
                email_address, pin, company_field George, george@example.com, d79a3td, ABC Corp Mary, mary@example.com,
                gd9as5b, 123 LLC ```
            signer_list: ``signer_list`` is an array defining values and options for signer fields. Required unless a
                ``signer_file`` is used, you may not use both.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            ccs: Add CC email recipients. Required when a CC role exists for the Template.
            client_id: The client id of the API App you want to associate with this request. Used to apply the branding
                and callback url defined for the app.
            custom_fields: When used together with merge fields, ``custom_fields`` allows users to add pre-filled data
                to their signature requests. Pre-filled data can be used with "send-once" signature requests by adding
                merge fields with ``form_fields_per_document`` or `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ while passing values back with
                ``custom_fields`` together in one API call. For using pre-filled on repeatable signature requests, merge
                fields are added to templates in the Dropbox Sign UI or by calling `/template/create_embedded_draft
                </api/reference/operation/templateCreateEmbeddedDraft>`__ and then passing ``custom_fields`` on
                subsequent signature requests referencing that template.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            signing_redirect_url: The URL you want signers redirected to after they successfully sign.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request will not be legally binding if set to ``true``.
                Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            expires_at: When the signature request will expire. Unsigned signatures will be moved to the expired status,
                and no longer signable. See `Signature Request Expiration Date
                <https://developers.hellosign.com/docs/signature-request/expiration/>`__ for details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.signature_request_bulk_send_with_template(
                template_ids,
                signer_file=signer_file,
                signer_list=signer_list,
                allow_decline=allow_decline,
                ccs=ccs,
                client_id=client_id,
                custom_fields=custom_fields,
                message=message,
                metadata=metadata,
                signing_redirect_url=signing_redirect_url,
                subject=subject,
                test_mode=test_mode,
                title=title,
                expires_at=expires_at,
                request_options=request_options,
            ),
        )

    def signature_request_cancel(
        self, signature_request_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Any:
        """Cancels an incomplete signature request. This action is **not reversible**.

        The request will be canceled and signers will no longer be able to sign. If they try to access the signature
        request they will receive a HTTP 410 status code indicating that the resource has been deleted. Cancelation is
        asynchronous and a successful call to this endpoint will return an empty 200 OK response if the signature
        request is eligible to be canceled and has been successfully queued.

        This 200 OK response does not indicate a successful cancelation of the signature request itself. The cancelation
        is confirmed via the ``signature_request_canceled`` event. It is recommended that a `callback handler
        </api/reference/tag/Callbacks-and-Events>`__ be implemented to listen for the ``signature_request_canceled``
        event. This callback will be sent only when the cancelation has completed successfully. If a callback handler
        has been configured and the event has not been received within 60 minutes of making the call, check the status
        of the request in the `API Dashboard <https://app.hellosign.com/apidashboard>`__ and retry the cancelation if
        necessary.

        To be eligible for cancelation, a signature request must have been sent successfully, must not yet have been
        signed by all signers, and you must either be the sender or own the API app under which it was sent. A partially
        signed signature request can be canceled.

        **NOTE:** To remove your access to a completed signature request, use the endpoint: ``POST
        /signature_request/remove/[:signature_request_id]``.

        Args:
            signature_request_id: The id of the incomplete SignatureRequest to cancel.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.signature_request_cancel(signature_request_id, request_options=request_options)
        )

    def signature_request_create_embedded(
        self,
        client_id: str,
        *,
        files: FileInput | None = None,
        file_urls: list[str] | None = None,
        signers: list[SubSignatureRequestSigner | SubSignatureRequestSignerDict] | None = None,
        grouped_signers: list[SubSignatureRequestGroupedSigners | SubSignatureRequestGroupedSignersDict] | None = None,
        allow_decline: bool | None = False,
        allow_reassign: bool | None = False,
        attachments: list[SubAttachment | SubAttachmentDict] | None = None,
        cc_email_addresses: list[EmailStr] | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        field_options: SubFieldOptions | SubFieldOptionsDict | None = None,
        form_field_groups: list[SubFormFieldGroup | SubFormFieldGroupDict] | None = None,
        form_field_rules: list[SubFormFieldRule | SubFormFieldRuleDict] | None = None,
        form_fields_per_document: list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None = None,
        hide_text_tags: bool | None = False,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        signing_options: SubSigningOptions | SubSigningOptionsDict | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        use_text_tags: bool | None = False,
        ignore_text_tags_extraction_errors: bool | None = False,
        populate_auto_fill_fields: bool | None = False,
        expires_at: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SignatureRequestGetResponse:
        """Creates a new SignatureRequest with the submitted documents to be signed in an embedded iFrame. If
        form_fields_per_document is not specified, a signature page will be affixed where all signers will be required
        to add their signature, signifying their agreement to all contained documents. Note that embedded signature
        requests can only be signed in embedded iFrames whereas normal signature requests can only be signed on Dropbox
        Sign.

        Args:
            client_id: Client id of the app you're using to create this embedded signature request. Used for security
                purposes.
            files: Use ``files[]`` to indicate the uploaded file(s) to send for signature. This endpoint requires either
                **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            signers: Add Signers to your Signature Request. This endpoint requires either **signers** or
                **grouped_signers**, but not both.
            grouped_signers: Add Grouped Signers to your Signature Request. This endpoint requires either **signers** or
                **grouped_signers**, but not both.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            allow_reassign: Allows signers to reassign their signature requests to other signers if set to ``true``.
                Defaults to ``false``. **NOTE:** Only available for Premium plan.
            attachments: A list describing the attachments
            cc_email_addresses: The email addresses that should be CCed.
            custom_fields: When used together with merge fields, ``custom_fields`` allows users to add pre-filled data
                to their signature requests. Pre-filled data can be used with "send-once" signature requests by adding
                merge fields with ``form_fields_per_document`` or `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ while passing values back with
                ``custom_fields`` together in one API call. For using pre-filled on repeatable signature requests, merge
                fields are added to templates in the Dropbox Sign UI or by calling `/template/create_embedded_draft
                </api/reference/operation/templateCreateEmbeddedDraft>`__ and then passing ``custom_fields`` on
                subsequent signature requests referencing that template.
            field_options: This allows the requester to specify field options for a signature request.
            form_field_groups: Group information for fields defined in ``form_fields_per_document``. String-indexed JSON
                array with ``group_label`` and ``requirement`` keys. ``form_fields_per_document`` must contain fields
                referencing a group defined in ``form_field_groups``.
            form_field_rules: Conditional Logic rules for fields defined in ``form_fields_per_document``.
            form_fields_per_document: The fields that should appear on the document, expressed as an array of objects.
                (For more details you can read about it here: `Using Form Fields per Document
                </docs/openapi/form-fields-per-document>`__.) **NOTE:** Fields like **text**, **dropdown**,
                **checkbox**, **radio**, and **hyperlink** have additional required and optional parameters. Check out
                the list of `additional parameters </api/reference/constants/#form-fields-per-document>`__ for these
                field types. * Text Field use ``SubFormFieldsPerDocumentText`` * Dropdown Field use
                ``SubFormFieldsPerDocumentDropdown`` * Hyperlink Field use ``SubFormFieldsPerDocumentHyperlink`` *
                Checkbox Field use ``SubFormFieldsPerDocumentCheckbox`` * Radio Field use
                ``SubFormFieldsPerDocumentRadio`` * Signature Field use ``SubFormFieldsPerDocumentSignature`` * Date
                Signed Field use ``SubFormFieldsPerDocumentDateSigned`` * Initials Field use
                ``SubFormFieldsPerDocumentInitials`` * Text Merge Field use ``SubFormFieldsPerDocumentTextMerge`` *
                Checkbox Merge Field use ``SubFormFieldsPerDocumentCheckboxMerge``
            hide_text_tags: Enables automatic Text Tag removal when set to true. **NOTE:** Removing text tags this way
                can cause unwanted clipping. We recommend leaving this setting on ``false`` and instead hiding your text
                tags using white text or a similar approach. See the `Text Tags Walkthrough
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ for more information.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            signing_options: This allows the requester to specify the types allowed for creating a signature and specify
                another signing options. **NOTE:** If ``signing_options`` are not defined in the request, the allowed
                types will default to those specified in the account settings. **NOTE:** If
                ``force_advanced_signature_details`` is set, allowed types has to be defined too.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request will not be legally binding if set to ``true``.
                Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            use_text_tags: Send with a value of ``true`` if you wish to enable `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ parsing in your document. Defaults
                to disabled, or ``false``.
            ignore_text_tags_extraction_errors: Sent with a value of ``true`` to ignore the validation errors from text
                tags extraction. Defaults to ``false``.
            populate_auto_fill_fields: Controls whether `auto fill fields
                <https://faq.hellosign.com/hc/en-us/articles/360051467511-Auto-Fill-Fields>`__ can automatically
                populate a signer's information during signing. **NOTE:** Keep your signer's information safe by
                ensuring that the _signer on your signature request is the intended party_ before using this feature.
            expires_at: When the signature request will expire. Unsigned signatures will be moved to the expired status,
                and no longer signable. See `Signature Request Expiration Date
                <https://developers.hellosign.com/docs/signature-request/expiration/>`__ for details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.signature_request_create_embedded(
                client_id,
                files=files,
                file_urls=file_urls,
                signers=signers,
                grouped_signers=grouped_signers,
                allow_decline=allow_decline,
                allow_reassign=allow_reassign,
                attachments=attachments,
                cc_email_addresses=cc_email_addresses,
                custom_fields=custom_fields,
                field_options=field_options,
                form_field_groups=form_field_groups,
                form_field_rules=form_field_rules,
                form_fields_per_document=form_fields_per_document,
                hide_text_tags=hide_text_tags,
                message=message,
                metadata=metadata,
                signing_options=signing_options,
                subject=subject,
                test_mode=test_mode,
                title=title,
                use_text_tags=use_text_tags,
                ignore_text_tags_extraction_errors=ignore_text_tags_extraction_errors,
                populate_auto_fill_fields=populate_auto_fill_fields,
                expires_at=expires_at,
                request_options=request_options,
            ),
        )

    def signature_request_create_embedded_with_template(
        self,
        template_ids: list[str],
        client_id: str,
        signers: list[SubSignatureRequestTemplateSigner | SubSignatureRequestTemplateSignerDict],
        *,
        allow_decline: bool | None = False,
        ccs: list[SubCc | SubCcDict] | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        files: FileInput | None = None,
        file_urls: list[str] | None = None,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        signing_options: SubSigningOptions | SubSigningOptionsDict | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        populate_auto_fill_fields: bool | None = False,
        expires_at: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SignatureRequestGetResponse:
        """Creates a new SignatureRequest based on the given Template(s) to be signed in an embedded iFrame. Note that
        embedded signature requests can only be signed in embedded iFrames whereas normal signature requests can only be
        signed on Dropbox Sign.

        Args:
            template_ids: Use ``template_ids`` to create a SignatureRequest from one or more templates, in the order in
                which the template will be used.
            client_id: Client id of the app you're using to create this embedded signature request. Used for security
                purposes.
            signers: Add Signers to your Templated-based Signature Request.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            ccs: Add CC email recipients. Required when a CC role exists for the Template.
            custom_fields: An array defining values and options for custom fields. Required when a custom field exists
                in the Template.
            files: Use ``files[]`` to indicate the uploaded file(s) to send for signature. This endpoint requires either
                **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            signing_options: This allows the requester to specify the types allowed for creating a signature and specify
                another signing options. **NOTE:** If ``signing_options`` are not defined in the request, the allowed
                types will default to those specified in the account settings. **NOTE:** If
                ``force_advanced_signature_details`` is set, allowed types has to be defined too.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request will not be legally binding if set to ``true``.
                Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            populate_auto_fill_fields: Controls whether `auto fill fields
                <https://faq.hellosign.com/hc/en-us/articles/360051467511-Auto-Fill-Fields>`__ can automatically
                populate a signer's information during signing. **NOTE:** Keep your signer's information safe by
                ensuring that the _signer on your signature request is the intended party_ before using this feature.
            expires_at: When the signature request will expire. Unsigned signatures will be moved to the expired status,
                and no longer signable. See `Signature Request Expiration Date
                <https://developers.hellosign.com/docs/signature-request/expiration/>`__ for details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.signature_request_create_embedded_with_template(
                template_ids,
                client_id,
                signers,
                allow_decline=allow_decline,
                ccs=ccs,
                custom_fields=custom_fields,
                files=files,
                file_urls=file_urls,
                message=message,
                metadata=metadata,
                signing_options=signing_options,
                subject=subject,
                test_mode=test_mode,
                title=title,
                populate_auto_fill_fields=populate_auto_fill_fields,
                expires_at=expires_at,
                request_options=request_options,
            ),
        )

    def signature_request_edit(
        self,
        signature_request_id: str,
        *,
        files: FileInput | None = None,
        file_urls: list[str] | None = None,
        signers: list[SubSignatureRequestSigner | SubSignatureRequestSignerDict] | None = None,
        grouped_signers: list[SubSignatureRequestGroupedSigners | SubSignatureRequestGroupedSignersDict] | None = None,
        allow_decline: bool | None = False,
        allow_reassign: bool | None = False,
        attachments: list[SubAttachment | SubAttachmentDict] | None = None,
        cc_email_addresses: list[EmailStr] | None = None,
        client_id: str | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        field_options: SubFieldOptions | SubFieldOptionsDict | None = None,
        form_field_groups: list[SubFormFieldGroup | SubFormFieldGroupDict] | None = None,
        form_field_rules: list[SubFormFieldRule | SubFormFieldRuleDict] | None = None,
        form_fields_per_document: list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None = None,
        hide_text_tags: bool | None = False,
        is_eid: bool | None = False,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        signing_options: SubSigningOptions | SubSigningOptionsDict | None = None,
        signing_redirect_url: str | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        use_text_tags: bool | None = False,
        ignore_text_tags_extraction_errors: bool | None = False,
        expires_at: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SignatureRequestGetResponse:
        """Edits and sends a SignatureRequest with the submitted documents. If ``form_fields_per_document`` is not
        specified, a signature page will be affixed where all signers will be required to add their signature,
        signifying their agreement to all contained documents.

        **NOTE:** Edit and resend *will* deduct your signature request quota.

        Args:
            signature_request_id: The id of the SignatureRequest to edit.
            files: Use ``files[]`` to indicate the uploaded file(s) to send for signature. This endpoint requires either
                **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            signers: Add Signers to your Signature Request. This endpoint requires either **signers** or
                **grouped_signers**, but not both.
            grouped_signers: Add Grouped Signers to your Signature Request. This endpoint requires either **signers** or
                **grouped_signers**, but not both.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            allow_reassign: Allows signers to reassign their signature requests to other signers if set to ``true``.
                Defaults to ``false``. **NOTE:** Only available for Premium plan and higher.
            attachments: A list describing the attachments
            cc_email_addresses: The email addresses that should be CCed.
            client_id: The client id of the API App you want to associate with this request. Used to apply the branding
                and callback url defined for the app.
            custom_fields: When used together with merge fields, ``custom_fields`` allows users to add pre-filled data
                to their signature requests. Pre-filled data can be used with "send-once" signature requests by adding
                merge fields with ``form_fields_per_document`` or `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ while passing values back with
                ``custom_fields`` together in one API call. For using pre-filled on repeatable signature requests, merge
                fields are added to templates in the Dropbox Sign UI or by calling `/template/create_embedded_draft
                </api/reference/operation/templateCreateEmbeddedDraft>`__ and then passing ``custom_fields`` on
                subsequent signature requests referencing that template.
            field_options: This allows the requester to specify field options for a signature request.
            form_field_groups: Group information for fields defined in ``form_fields_per_document``. String-indexed JSON
                array with ``group_label`` and ``requirement`` keys. ``form_fields_per_document`` must contain fields
                referencing a group defined in ``form_field_groups``.
            form_field_rules: Conditional Logic rules for fields defined in ``form_fields_per_document``.
            form_fields_per_document: The fields that should appear on the document, expressed as an array of objects.
                (For more details you can read about it here: `Using Form Fields per Document
                </docs/openapi/form-fields-per-document>`__.) **NOTE:** Fields like **text**, **dropdown**,
                **checkbox**, **radio**, and **hyperlink** have additional required and optional parameters. Check out
                the list of `additional parameters </api/reference/constants/#form-fields-per-document>`__ for these
                field types. * Text Field use ``SubFormFieldsPerDocumentText`` * Dropdown Field use
                ``SubFormFieldsPerDocumentDropdown`` * Hyperlink Field use ``SubFormFieldsPerDocumentHyperlink`` *
                Checkbox Field use ``SubFormFieldsPerDocumentCheckbox`` * Radio Field use
                ``SubFormFieldsPerDocumentRadio`` * Signature Field use ``SubFormFieldsPerDocumentSignature`` * Date
                Signed Field use ``SubFormFieldsPerDocumentDateSigned`` * Initials Field use
                ``SubFormFieldsPerDocumentInitials`` * Text Merge Field use ``SubFormFieldsPerDocumentTextMerge`` *
                Checkbox Merge Field use ``SubFormFieldsPerDocumentCheckboxMerge``
            hide_text_tags: Enables automatic Text Tag removal when set to true. **NOTE:** Removing text tags this way
                can cause unwanted clipping. We recommend leaving this setting on ``false`` and instead hiding your text
                tags using white text or a similar approach. See the `Text Tags Walkthrough
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ for more information.
            is_eid: Send with a value of ``true`` if you wish to enable `electronic identification (eID)
                <https://www.hellosign.com/features/electronic-id>`__, which requires the signer to verify their
                identity with an eID provider to sign a document.<br> **NOTE:** You need the eID add-on to use this
                feature. Please `contact sales <https://sign.dropbox.com/form/contact-sales>`__ for more information.
                Cannot be used in ``test_mode``. Only works on requests with one signer.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            signing_options: This allows the requester to specify the types allowed for creating a signature and specify
                another signing options. **NOTE:** If ``signing_options`` are not defined in the request, the allowed
                types will default to those specified in the account settings. **NOTE:** If
                ``force_advanced_signature_details`` is set, allowed types has to be defined too.
            signing_redirect_url: The URL you want signers redirected to after they successfully sign.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request will not be legally binding if set to ``true``.
                Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            use_text_tags: Send with a value of ``true`` if you wish to enable `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ parsing in your document. Defaults
                to disabled, or ``false``.
            ignore_text_tags_extraction_errors: Sent with a value of ``true`` to ignore the validation errors from text
                tags extraction. Defaults to ``false``.
            expires_at: When the signature request will expire. Unsigned signatures will be moved to the expired status,
                and no longer signable. See `Signature Request Expiration Date
                <https://developers.hellosign.com/docs/signature-request/expiration/>`__ for details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.signature_request_edit(
                signature_request_id,
                files=files,
                file_urls=file_urls,
                signers=signers,
                grouped_signers=grouped_signers,
                allow_decline=allow_decline,
                allow_reassign=allow_reassign,
                attachments=attachments,
                cc_email_addresses=cc_email_addresses,
                client_id=client_id,
                custom_fields=custom_fields,
                field_options=field_options,
                form_field_groups=form_field_groups,
                form_field_rules=form_field_rules,
                form_fields_per_document=form_fields_per_document,
                hide_text_tags=hide_text_tags,
                is_eid=is_eid,
                message=message,
                metadata=metadata,
                signing_options=signing_options,
                signing_redirect_url=signing_redirect_url,
                subject=subject,
                test_mode=test_mode,
                title=title,
                use_text_tags=use_text_tags,
                ignore_text_tags_extraction_errors=ignore_text_tags_extraction_errors,
                expires_at=expires_at,
                request_options=request_options,
            ),
        )

    def signature_request_edit_embedded(
        self,
        signature_request_id: str,
        client_id: str,
        *,
        files: FileInput | None = None,
        file_urls: list[str] | None = None,
        signers: list[SubSignatureRequestSigner | SubSignatureRequestSignerDict] | None = None,
        grouped_signers: list[SubSignatureRequestGroupedSigners | SubSignatureRequestGroupedSignersDict] | None = None,
        allow_decline: bool | None = False,
        allow_reassign: bool | None = False,
        attachments: list[SubAttachment | SubAttachmentDict] | None = None,
        cc_email_addresses: list[EmailStr] | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        field_options: SubFieldOptions | SubFieldOptionsDict | None = None,
        form_field_groups: list[SubFormFieldGroup | SubFormFieldGroupDict] | None = None,
        form_field_rules: list[SubFormFieldRule | SubFormFieldRuleDict] | None = None,
        form_fields_per_document: list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None = None,
        hide_text_tags: bool | None = False,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        signing_options: SubSigningOptions | SubSigningOptionsDict | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        use_text_tags: bool | None = False,
        ignore_text_tags_extraction_errors: bool | None = False,
        populate_auto_fill_fields: bool | None = False,
        expires_at: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SignatureRequestGetResponse:
        """Edits a SignatureRequest with the submitted documents to be signed in an embedded iFrame. If
        form_fields_per_document is not specified, a signature page will be affixed where all signers will be required
        to add their signature, signifying their agreement to all contained documents. Note that embedded signature
        requests can only be signed in embedded iFrames whereas normal signature requests can only be signed on Dropbox
        Sign.

        **NOTE:** Edit and resend *will* deduct your signature request quota.

        Args:
            signature_request_id: The id of the SignatureRequest to edit.
            client_id: Client id of the app you're using to create this embedded signature request. Used for security
                purposes.
            files: Use ``files[]`` to indicate the uploaded file(s) to send for signature. This endpoint requires either
                **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            signers: Add Signers to your Signature Request. This endpoint requires either **signers** or
                **grouped_signers**, but not both.
            grouped_signers: Add Grouped Signers to your Signature Request. This endpoint requires either **signers** or
                **grouped_signers**, but not both.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            allow_reassign: Allows signers to reassign their signature requests to other signers if set to ``true``.
                Defaults to ``false``. **NOTE:** Only available for Premium plan.
            attachments: A list describing the attachments
            cc_email_addresses: The email addresses that should be CCed.
            custom_fields: When used together with merge fields, ``custom_fields`` allows users to add pre-filled data
                to their signature requests. Pre-filled data can be used with "send-once" signature requests by adding
                merge fields with ``form_fields_per_document`` or `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ while passing values back with
                ``custom_fields`` together in one API call. For using pre-filled on repeatable signature requests, merge
                fields are added to templates in the Dropbox Sign UI or by calling `/template/create_embedded_draft
                </api/reference/operation/templateCreateEmbeddedDraft>`__ and then passing ``custom_fields`` on
                subsequent signature requests referencing that template.
            field_options: This allows the requester to specify field options for a signature request.
            form_field_groups: Group information for fields defined in ``form_fields_per_document``. String-indexed JSON
                array with ``group_label`` and ``requirement`` keys. ``form_fields_per_document`` must contain fields
                referencing a group defined in ``form_field_groups``.
            form_field_rules: Conditional Logic rules for fields defined in ``form_fields_per_document``.
            form_fields_per_document: The fields that should appear on the document, expressed as an array of objects.
                (For more details you can read about it here: `Using Form Fields per Document
                </docs/openapi/form-fields-per-document>`__.) **NOTE:** Fields like **text**, **dropdown**,
                **checkbox**, **radio**, and **hyperlink** have additional required and optional parameters. Check out
                the list of `additional parameters </api/reference/constants/#form-fields-per-document>`__ for these
                field types. * Text Field use ``SubFormFieldsPerDocumentText`` * Dropdown Field use
                ``SubFormFieldsPerDocumentDropdown`` * Hyperlink Field use ``SubFormFieldsPerDocumentHyperlink`` *
                Checkbox Field use ``SubFormFieldsPerDocumentCheckbox`` * Radio Field use
                ``SubFormFieldsPerDocumentRadio`` * Signature Field use ``SubFormFieldsPerDocumentSignature`` * Date
                Signed Field use ``SubFormFieldsPerDocumentDateSigned`` * Initials Field use
                ``SubFormFieldsPerDocumentInitials`` * Text Merge Field use ``SubFormFieldsPerDocumentTextMerge`` *
                Checkbox Merge Field use ``SubFormFieldsPerDocumentCheckboxMerge``
            hide_text_tags: Enables automatic Text Tag removal when set to true. **NOTE:** Removing text tags this way
                can cause unwanted clipping. We recommend leaving this setting on ``false`` and instead hiding your text
                tags using white text or a similar approach. See the `Text Tags Walkthrough
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ for more information.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            signing_options: This allows the requester to specify the types allowed for creating a signature and specify
                another signing options. **NOTE:** If ``signing_options`` are not defined in the request, the allowed
                types will default to those specified in the account settings. **NOTE:** If
                ``force_advanced_signature_details`` is set, allowed types has to be defined too.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request will not be legally binding if set to ``true``.
                Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            use_text_tags: Send with a value of ``true`` if you wish to enable `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ parsing in your document. Defaults
                to disabled, or ``false``.
            ignore_text_tags_extraction_errors: Sent with a value of ``true`` to ignore the validation errors from text
                tags extraction. Defaults to ``false``.
            populate_auto_fill_fields: Controls whether `auto fill fields
                <https://faq.hellosign.com/hc/en-us/articles/360051467511-Auto-Fill-Fields>`__ can automatically
                populate a signer's information during signing. **NOTE:** Keep your signer's information safe by
                ensuring that the _signer on your signature request is the intended party_ before using this feature.
            expires_at: When the signature request will expire. Unsigned signatures will be moved to the expired status,
                and no longer signable. See `Signature Request Expiration Date
                <https://developers.hellosign.com/docs/signature-request/expiration/>`__ for details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.signature_request_edit_embedded(
                signature_request_id,
                client_id,
                files=files,
                file_urls=file_urls,
                signers=signers,
                grouped_signers=grouped_signers,
                allow_decline=allow_decline,
                allow_reassign=allow_reassign,
                attachments=attachments,
                cc_email_addresses=cc_email_addresses,
                custom_fields=custom_fields,
                field_options=field_options,
                form_field_groups=form_field_groups,
                form_field_rules=form_field_rules,
                form_fields_per_document=form_fields_per_document,
                hide_text_tags=hide_text_tags,
                message=message,
                metadata=metadata,
                signing_options=signing_options,
                subject=subject,
                test_mode=test_mode,
                title=title,
                use_text_tags=use_text_tags,
                ignore_text_tags_extraction_errors=ignore_text_tags_extraction_errors,
                populate_auto_fill_fields=populate_auto_fill_fields,
                expires_at=expires_at,
                request_options=request_options,
            ),
        )

    def signature_request_edit_embedded_with_template(
        self,
        signature_request_id: str,
        template_ids: list[str],
        client_id: str,
        signers: list[SubSignatureRequestTemplateSigner | SubSignatureRequestTemplateSignerDict],
        *,
        allow_decline: bool | None = False,
        ccs: list[SubCc | SubCcDict] | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        files: FileInput | None = None,
        file_urls: list[str] | None = None,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        signing_options: SubSigningOptions | SubSigningOptionsDict | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        populate_auto_fill_fields: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SignatureRequestGetResponse:
        """Edits a SignatureRequest based on the given Template(s) to be signed in an embedded iFrame. Note that
        embedded signature requests can only be signed in embedded iFrames whereas normal signature requests can only be
        signed on Dropbox Sign.

        **NOTE:** Edit and resend *will* deduct your signature request quota.

        Args:
            signature_request_id: The id of the SignatureRequest to edit.
            template_ids: Use ``template_ids`` to create a SignatureRequest from one or more templates, in the order in
                which the template will be used.
            client_id: Client id of the app you're using to create this embedded signature request. Used for security
                purposes.
            signers: Add Signers to your Templated-based Signature Request.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            ccs: Add CC email recipients. Required when a CC role exists for the Template.
            custom_fields: An array defining values and options for custom fields. Required when a custom field exists
                in the Template.
            files: Use ``files[]`` to indicate the uploaded file(s) to send for signature. This endpoint requires either
                **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            signing_options: This allows the requester to specify the types allowed for creating a signature and specify
                another signing options. **NOTE:** If ``signing_options`` are not defined in the request, the allowed
                types will default to those specified in the account settings. **NOTE:** If
                ``force_advanced_signature_details`` is set, allowed types has to be defined too.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request will not be legally binding if set to ``true``.
                Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            populate_auto_fill_fields: Controls whether `auto fill fields
                <https://faq.hellosign.com/hc/en-us/articles/360051467511-Auto-Fill-Fields>`__ can automatically
                populate a signer's information during signing. **NOTE:** Keep your signer's information safe by
                ensuring that the _signer on your signature request is the intended party_ before using this feature.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.signature_request_edit_embedded_with_template(
                signature_request_id,
                template_ids,
                client_id,
                signers,
                allow_decline=allow_decline,
                ccs=ccs,
                custom_fields=custom_fields,
                files=files,
                file_urls=file_urls,
                message=message,
                metadata=metadata,
                signing_options=signing_options,
                subject=subject,
                test_mode=test_mode,
                title=title,
                populate_auto_fill_fields=populate_auto_fill_fields,
                request_options=request_options,
            ),
        )

    def signature_request_edit_with_template(
        self,
        signature_request_id: str,
        template_ids: list[str],
        signers: list[SubSignatureRequestTemplateSigner | SubSignatureRequestTemplateSignerDict],
        *,
        allow_decline: bool | None = False,
        ccs: list[SubCc | SubCcDict] | None = None,
        client_id: str | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        files: FileInput | None = None,
        file_urls: list[str] | None = None,
        is_eid: bool | None = False,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        signing_options: SubSigningOptions | SubSigningOptionsDict | None = None,
        signing_redirect_url: str | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SignatureRequestGetResponse:
        """Edits and sends a SignatureRequest based off of the Template(s) specified with the template_ids parameter.

        **NOTE:** Edit and resend *will* deduct your signature request quota.

        Args:
            signature_request_id: The id of the SignatureRequest to edit.
            template_ids: Use ``template_ids`` to create a SignatureRequest from one or more templates, in the order in
                which the template will be used.
            signers: Add Signers to your Templated-based Signature Request.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            ccs: Add CC email recipients. Required when a CC role exists for the Template.
            client_id: Client id of the app to associate with the signature request. Used to apply the branding and
                callback url defined for the app.
            custom_fields: An array defining values and options for custom fields. Required when a custom field exists
                in the Template.
            files: Use ``files[]`` to indicate the uploaded file(s) to send for signature. This endpoint requires either
                **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            is_eid: Send with a value of ``true`` if you wish to enable `electronic identification (eID)
                <https://www.hellosign.com/features/electronic-id>`__, which requires the signer to verify their
                identity with an eID provider to sign a document.<br> **NOTE:** You need the eID add-on to use this
                feature. Please `contact sales <https://sign.dropbox.com/form/contact-sales>`__ for more information.
                Cannot be used in ``test_mode``. Only works on requests with one signer.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            signing_options: This allows the requester to specify the types allowed for creating a signature and specify
                another signing options. **NOTE:** If ``signing_options`` are not defined in the request, the allowed
                types will default to those specified in the account settings. **NOTE:** If
                ``force_advanced_signature_details`` is set, allowed types has to be defined too.
            signing_redirect_url: The URL you want signers redirected to after they successfully sign.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request will not be legally binding if set to ``true``.
                Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.signature_request_edit_with_template(
                signature_request_id,
                template_ids,
                signers,
                allow_decline=allow_decline,
                ccs=ccs,
                client_id=client_id,
                custom_fields=custom_fields,
                files=files,
                file_urls=file_urls,
                is_eid=is_eid,
                message=message,
                metadata=metadata,
                signing_options=signing_options,
                signing_redirect_url=signing_redirect_url,
                subject=subject,
                test_mode=test_mode,
                title=title,
                request_options=request_options,
            ),
        )

    def signature_request_files(
        self,
        signature_request_id: str,
        *,
        file_type: FileTypeOrStr | None = FileType.PDF,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Obtain a copy of the current documents specified by the ``signature_request_id`` parameter. Returns a PDF or
        ZIP file.

        If the files are currently being prepared, a status code of ``409`` will be returned instead.

        Args:
            signature_request_id: The id of the SignatureRequest to retrieve.
            file_type: Set to ``pdf`` for a single merged document or ``zip`` for a collection of individual documents.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.signature_request_files(
                signature_request_id, file_type=file_type, request_options=request_options
            ),
        )

    def signature_request_files_as_data_uri(
        self, signature_request_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> FileResponseDataUri:
        """Obtain a copy of the current documents specified by the ``signature_request_id`` parameter. Returns a JSON
        object with a ``data_uri`` representing the base64 encoded file (PDFs only).

        If the files are currently being prepared, a status code of ``409`` will be returned instead.

        Args:
            signature_request_id: The id of the SignatureRequest to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.signature_request_files_as_data_uri(
                signature_request_id, request_options=request_options
            ),
        )

    def signature_request_files_as_file_url(
        self,
        signature_request_id: str,
        *,
        force_download: int | None = 1,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FileResponseModel:
        """Obtain a copy of the current documents specified by the ``signature_request_id`` parameter. Returns a JSON
        object with a url to the file (PDFs only).

        If the files are currently being prepared, a status code of ``409`` will be returned instead.

        Args:
            signature_request_id: The id of the SignatureRequest to retrieve.
            force_download: By default when opening the ``file_url`` a browser will download the PDF and save it
                locally. When set to ``0`` the PDF file will be displayed in the browser.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.signature_request_files_as_file_url(
                signature_request_id, force_download=force_download, request_options=request_options
            ),
        )

    def signature_request_get(
        self, signature_request_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SignatureRequestGetResponse:
        """Returns the status of the SignatureRequest specified by the ``signature_request_id`` parameter.

        Args:
            signature_request_id: The id of the SignatureRequest to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.signature_request_get(signature_request_id, request_options=request_options)
        )

    def signature_request_list(
        self,
        *,
        account_id: str | None = None,
        page: int | None = 1,
        page_size: int | None = 20,
        query: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SignatureRequestListResponse:
        """Returns a list of SignatureRequests that you can access. This includes SignatureRequests you have sent as
        well as received, but not ones that you have been CCed on.

        Take a look at our `search guide </api/reference/search/>`__ to learn more about querying signature requests.

        Args:
            account_id: Which account to return SignatureRequests for. Must be a team member. Use ``all`` to indicate
                all team members. Defaults to your account.
            page: Which page number of the SignatureRequest List to return. Defaults to ``1``.
            page_size: Number of objects to be returned per page. Must be between ``1`` and ``100``. Default is ``20``.
            query: String that includes search terms and/or fields to be used to filter the SignatureRequest objects.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.signature_request_list(
                account_id=account_id, page=page, page_size=page_size, query=query, request_options=request_options
            ),
        )

    def signature_request_release_hold(
        self, signature_request_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SignatureRequestGetResponse:
        """Releases a held SignatureRequest that was claimed and prepared from an `UnclaimedDraft
        </api/reference/tag/Unclaimed-Draft>`__. The owner of the Draft must indicate at Draft creation that the
        SignatureRequest created from the Draft should be held. Releasing the SignatureRequest will send requests to all
        signers.

        Args:
            signature_request_id: The id of the SignatureRequest to release.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.signature_request_release_hold(
                signature_request_id, request_options=request_options
            ),
        )

    def signature_request_remind(
        self,
        signature_request_id: str,
        body: SignatureRequestRemindRequest | SignatureRequestRemindRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SignatureRequestGetResponse:
        """Sends an email to the signer reminding them to sign the signature request. You cannot send a reminder within
        1 hour of the last reminder that was sent. This includes manual AND automatic reminders.

        **NOTE:** This action can **not** be used with embedded signature requests.

        Args:
            signature_request_id: The id of the SignatureRequest to send a reminder for.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.signature_request_remind(
                signature_request_id, body, request_options=request_options
            ),
        )

    def signature_request_remove(
        self, signature_request_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Any:
        """Removes your access to a completed signature request. This action is **not reversible**.

        The signature request must be fully executed by all parties (signed or declined to sign). Other parties will
        continue to maintain access to the completed signature request document(s).

        Unlike /signature_request/cancel, this endpoint is synchronous and your access will be immediately removed. Upon
        successful removal, this endpoint will return a 200 OK response.

        Args:
            signature_request_id: The id of the SignatureRequest to remove.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.signature_request_remove(signature_request_id, request_options=request_options)
        )

    def signature_request_send(
        self,
        *,
        files: FileInput | None = None,
        file_urls: list[str] | None = None,
        signers: list[SubSignatureRequestSigner | SubSignatureRequestSignerDict] | None = None,
        grouped_signers: list[SubSignatureRequestGroupedSigners | SubSignatureRequestGroupedSignersDict] | None = None,
        allow_decline: bool | None = False,
        allow_reassign: bool | None = False,
        attachments: list[SubAttachment | SubAttachmentDict] | None = None,
        cc_email_addresses: list[EmailStr] | None = None,
        client_id: str | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        field_options: SubFieldOptions | SubFieldOptionsDict | None = None,
        form_field_groups: list[SubFormFieldGroup | SubFormFieldGroupDict] | None = None,
        form_field_rules: list[SubFormFieldRule | SubFormFieldRuleDict] | None = None,
        form_fields_per_document: list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None = None,
        hide_text_tags: bool | None = False,
        is_eid: bool | None = False,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        signing_options: SubSigningOptions | SubSigningOptionsDict | None = None,
        signing_redirect_url: str | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        use_text_tags: bool | None = False,
        ignore_text_tags_extraction_errors: bool | None = False,
        expires_at: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SignatureRequestGetResponse:
        """Creates and sends a new SignatureRequest with the submitted documents. If ``form_fields_per_document`` is not
        specified, a signature page will be affixed where all signers will be required to add their signature,
        signifying their agreement to all contained documents.

        Args:
            files: Use ``files[]`` to indicate the uploaded file(s) to send for signature. This endpoint requires either
                **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            signers: Add Signers to your Signature Request. This endpoint requires either **signers** or
                **grouped_signers**, but not both.
            grouped_signers: Add Grouped Signers to your Signature Request. This endpoint requires either **signers** or
                **grouped_signers**, but not both.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            allow_reassign: Allows signers to reassign their signature requests to other signers if set to ``true``.
                Defaults to ``false``. **NOTE:** Only available for Premium plan and higher.
            attachments: A list describing the attachments
            cc_email_addresses: The email addresses that should be CCed.
            client_id: The client id of the API App you want to associate with this request. Used to apply the branding
                and callback url defined for the app.
            custom_fields: When used together with merge fields, ``custom_fields`` allows users to add pre-filled data
                to their signature requests. Pre-filled data can be used with "send-once" signature requests by adding
                merge fields with ``form_fields_per_document`` or `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ while passing values back with
                ``custom_fields`` together in one API call. For using pre-filled on repeatable signature requests, merge
                fields are added to templates in the Dropbox Sign UI or by calling `/template/create_embedded_draft
                </api/reference/operation/templateCreateEmbeddedDraft>`__ and then passing ``custom_fields`` on
                subsequent signature requests referencing that template.
            field_options: This allows the requester to specify field options for a signature request.
            form_field_groups: Group information for fields defined in ``form_fields_per_document``. String-indexed JSON
                array with ``group_label`` and ``requirement`` keys. ``form_fields_per_document`` must contain fields
                referencing a group defined in ``form_field_groups``.
            form_field_rules: Conditional Logic rules for fields defined in ``form_fields_per_document``.
            form_fields_per_document: The fields that should appear on the document, expressed as an array of objects.
                (For more details you can read about it here: `Using Form Fields per Document
                </docs/openapi/form-fields-per-document>`__.) **NOTE:** Fields like **text**, **dropdown**,
                **checkbox**, **radio**, and **hyperlink** have additional required and optional parameters. Check out
                the list of `additional parameters </api/reference/constants/#form-fields-per-document>`__ for these
                field types. * Text Field use ``SubFormFieldsPerDocumentText`` * Dropdown Field use
                ``SubFormFieldsPerDocumentDropdown`` * Hyperlink Field use ``SubFormFieldsPerDocumentHyperlink`` *
                Checkbox Field use ``SubFormFieldsPerDocumentCheckbox`` * Radio Field use
                ``SubFormFieldsPerDocumentRadio`` * Signature Field use ``SubFormFieldsPerDocumentSignature`` * Date
                Signed Field use ``SubFormFieldsPerDocumentDateSigned`` * Initials Field use
                ``SubFormFieldsPerDocumentInitials`` * Text Merge Field use ``SubFormFieldsPerDocumentTextMerge`` *
                Checkbox Merge Field use ``SubFormFieldsPerDocumentCheckboxMerge``
            hide_text_tags: Enables automatic Text Tag removal when set to true. **NOTE:** Removing text tags this way
                can cause unwanted clipping. We recommend leaving this setting on ``false`` and instead hiding your text
                tags using white text or a similar approach. See the `Text Tags Walkthrough
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ for more information.
            is_eid: Send with a value of ``true`` if you wish to enable `electronic identification (eID)
                <https://www.hellosign.com/features/electronic-id>`__, which requires the signer to verify their
                identity with an eID provider to sign a document.<br> **NOTE:** You need the eID add-on to use this
                feature. Please `contact sales <https://sign.dropbox.com/form/contact-sales>`__ for more information.
                Cannot be used in ``test_mode``. Only works on requests with one signer.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            signing_options: This allows the requester to specify the types allowed for creating a signature and specify
                another signing options. **NOTE:** If ``signing_options`` are not defined in the request, the allowed
                types will default to those specified in the account settings. **NOTE:** If
                ``force_advanced_signature_details`` is set, allowed types has to be defined too.
            signing_redirect_url: The URL you want signers redirected to after they successfully sign.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request will not be legally binding if set to ``true``.
                Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            use_text_tags: Send with a value of ``true`` if you wish to enable `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ parsing in your document. Defaults
                to disabled, or ``false``.
            ignore_text_tags_extraction_errors: Sent with a value of ``true`` to ignore the validation errors from text
                tags extraction. Defaults to ``false``.
            expires_at: When the signature request will expire. Unsigned signatures will be moved to the expired status,
                and no longer signable. See `Signature Request Expiration Date
                <https://developers.hellosign.com/docs/signature-request/expiration/>`__ for details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.signature_request_send(
                files=files,
                file_urls=file_urls,
                signers=signers,
                grouped_signers=grouped_signers,
                allow_decline=allow_decline,
                allow_reassign=allow_reassign,
                attachments=attachments,
                cc_email_addresses=cc_email_addresses,
                client_id=client_id,
                custom_fields=custom_fields,
                field_options=field_options,
                form_field_groups=form_field_groups,
                form_field_rules=form_field_rules,
                form_fields_per_document=form_fields_per_document,
                hide_text_tags=hide_text_tags,
                is_eid=is_eid,
                message=message,
                metadata=metadata,
                signing_options=signing_options,
                signing_redirect_url=signing_redirect_url,
                subject=subject,
                test_mode=test_mode,
                title=title,
                use_text_tags=use_text_tags,
                ignore_text_tags_extraction_errors=ignore_text_tags_extraction_errors,
                expires_at=expires_at,
                request_options=request_options,
            ),
        )

    def signature_request_send_with_template(
        self,
        template_ids: list[str],
        signers: list[SubSignatureRequestTemplateSigner | SubSignatureRequestTemplateSignerDict],
        *,
        allow_decline: bool | None = False,
        ccs: list[SubCc | SubCcDict] | None = None,
        client_id: str | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        files: FileInput | None = None,
        file_urls: list[str] | None = None,
        is_eid: bool | None = False,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        signing_options: SubSigningOptions | SubSigningOptionsDict | None = None,
        signing_redirect_url: str | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        expires_at: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SignatureRequestGetResponse:
        """Creates and sends a new SignatureRequest based off of the Template(s) specified with the ``template_ids``
        parameter.

        Args:
            template_ids: Use ``template_ids`` to create a SignatureRequest from one or more templates, in the order in
                which the template will be used.
            signers: Add Signers to your Templated-based Signature Request.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            ccs: Add CC email recipients. Required when a CC role exists for the Template.
            client_id: Client id of the app to associate with the signature request. Used to apply the branding and
                callback url defined for the app.
            custom_fields: An array defining values and options for custom fields. Required when a custom field exists
                in the Template.
            files: Use ``files[]`` to indicate the uploaded file(s) to send for signature. This endpoint requires either
                **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            is_eid: Send with a value of ``true`` if you wish to enable `electronic identification (eID)
                <https://www.hellosign.com/features/electronic-id>`__, which requires the signer to verify their
                identity with an eID provider to sign a document.<br> **NOTE:** You need the eID add-on to use this
                feature. Please `contact sales <https://sign.dropbox.com/form/contact-sales>`__ for more information.
                Cannot be used in ``test_mode``. Only works on requests with one signer.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            signing_options: This allows the requester to specify the types allowed for creating a signature and specify
                another signing options. **NOTE:** If ``signing_options`` are not defined in the request, the allowed
                types will default to those specified in the account settings. **NOTE:** If
                ``force_advanced_signature_details`` is set, allowed types has to be defined too.
            signing_redirect_url: The URL you want signers redirected to after they successfully sign.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request will not be legally binding if set to ``true``.
                Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            expires_at: When the signature request will expire. Unsigned signatures will be moved to the expired status,
                and no longer signable. See `Signature Request Expiration Date
                <https://developers.hellosign.com/docs/signature-request/expiration/>`__ for details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.signature_request_send_with_template(
                template_ids,
                signers,
                allow_decline=allow_decline,
                ccs=ccs,
                client_id=client_id,
                custom_fields=custom_fields,
                files=files,
                file_urls=file_urls,
                is_eid=is_eid,
                message=message,
                metadata=metadata,
                signing_options=signing_options,
                signing_redirect_url=signing_redirect_url,
                subject=subject,
                test_mode=test_mode,
                title=title,
                expires_at=expires_at,
                request_options=request_options,
            ),
        )

    def signature_request_update(
        self,
        signature_request_id: str,
        body: SignatureRequestUpdateRequest | SignatureRequestUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SignatureRequestGetResponse:
        """Updates the email address and/or the name for a given signer on a signature request. You can listen for the
        ``signature_request_email_bounce`` event on your app or account to detect bounced emails, and respond with this
        method.

        Updating the email address of a signer will generate a new ``signature_id`` value.

        **NOTE:** This action cannot be performed on a signature request with an appended signature page.

        Args:
            signature_request_id: The id of the SignatureRequest to update.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.signature_request_update(
                signature_request_id, body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> SignatureRequestWithRawResponse:
        return self._with_raw_response


class AsyncSignatureRequest:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSignatureRequestWithRawResponse(client, server, auth)

    async def signature_request_bulk_create_embedded_with_template(
        self,
        template_ids: list[str],
        client_id: str,
        *,
        signer_file: AsyncFileInput | None = None,
        signer_list: list[SubBulkSignerList | SubBulkSignerListDict] | None = None,
        allow_decline: bool | None = False,
        ccs: list[SubCc | SubCcDict] | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        signing_redirect_url: str | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        expires_at: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkSendJobSendResponse:
        """Creates BulkSendJob which sends up to 250 SignatureRequests in bulk based off of the provided Template(s)
        specified with the ``template_ids`` parameter to be signed in an embedded iFrame. These embedded signature
        requests can only be signed in embedded iFrames whereas normal signature requests can only be signed on Dropbox
        Sign.

        **NOTE:** Only available for Standard plan and higher.

        Args:
            template_ids: Use ``template_ids`` to create a SignatureRequest from one or more templates, in the order in
                which the template will be used.
            client_id: Client id of the app you're using to create this embedded signature request. Used for security
                purposes.
            signer_file: ``signer_file`` is a CSV file defining values and options for signer fields. Required unless a
                ``signer_list`` is used, you may not use both. The CSV can have the following columns: - ``name``: the
                name of the signer filling the role of RoleName - ``email_address``: email address of the signer filling
                the role of RoleName - ``pin``: the 4- to 12-character access code that will secure this signer's
                signature page (optional) - ``sms_phone_number``: An E.164 formatted phone number that will receive a
                code via SMS to access this signer's signature page. (optional) By using the feature, you agree you are
                responsible for obtaining a signer's consent to receive text messages from Dropbox Sign related to this
                signature request and confirm you have obtained such consent from all signers prior to enabling SMS
                delivery for this signature request. `Learn more
                <https://faq.hellosign.com/hc/en-us/articles/15815316468877-Dropbox-Sign-SMS-tools-add-on>`__. **NOTE:**
                Not available in test mode and requires a Standard plan or higher. - ``*_field``: any column with a
                _field" suffix will be treated as a custom field (optional) You may only specify field values here, any
                other options should be set in the custom_fields request parameter. Example CSV: ``` name,
                email_address, pin, company_field George, george@example.com, d79a3td, ABC Corp Mary, mary@example.com,
                gd9as5b, 123 LLC ```
            signer_list: ``signer_list`` is an array defining values and options for signer fields. Required unless a
                ``signer_file`` is used, you may not use both.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            ccs: Add CC email recipients. Required when a CC role exists for the Template.
            custom_fields: When used together with merge fields, ``custom_fields`` allows users to add pre-filled data
                to their signature requests. Pre-filled data can be used with "send-once" signature requests by adding
                merge fields with ``form_fields_per_document`` or `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ while passing values back with
                ``custom_fields`` together in one API call. For using pre-filled on repeatable signature requests, merge
                fields are added to templates in the Dropbox Sign UI or by calling `/template/create_embedded_draft
                </api/reference/operation/templateCreateEmbeddedDraft>`__ and then passing ``custom_fields`` on
                subsequent signature requests referencing that template.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            signing_redirect_url: The URL you want signers redirected to after they successfully sign.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request will not be legally binding if set to ``true``.
                Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            expires_at: When the signature request will expire. Unsigned signatures will be moved to the expired status,
                and no longer signable. See `Signature Request Expiration Date
                <https://developers.hellosign.com/docs/signature-request/expiration/>`__ for details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.signature_request_bulk_create_embedded_with_template(
                template_ids,
                client_id,
                signer_file=signer_file,
                signer_list=signer_list,
                allow_decline=allow_decline,
                ccs=ccs,
                custom_fields=custom_fields,
                message=message,
                metadata=metadata,
                signing_redirect_url=signing_redirect_url,
                subject=subject,
                test_mode=test_mode,
                title=title,
                expires_at=expires_at,
                request_options=request_options,
            ),
        )

    async def signature_request_bulk_send_with_template(
        self,
        template_ids: list[str],
        *,
        signer_file: AsyncFileInput | None = None,
        signer_list: list[SubBulkSignerList | SubBulkSignerListDict] | None = None,
        allow_decline: bool | None = False,
        ccs: list[SubCc | SubCcDict] | None = None,
        client_id: str | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        signing_redirect_url: str | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        expires_at: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkSendJobSendResponse:
        """Creates BulkSendJob which sends up to 250 SignatureRequests in bulk based off of the provided Template(s)
        specified with the ``template_ids`` parameter.

        **NOTE:** Only available for Standard plan and higher.

        Args:
            template_ids: Use ``template_ids`` to create a SignatureRequest from one or more templates, in the order in
                which the template will be used.
            signer_file: ``signer_file`` is a CSV file defining values and options for signer fields. Required unless a
                ``signer_list`` is used, you may not use both. The CSV can have the following columns: - ``name``: the
                name of the signer filling the role of RoleName - ``email_address``: email address of the signer filling
                the role of RoleName - ``pin``: the 4- to 12-character access code that will secure this signer's
                signature page (optional) - ``sms_phone_number``: An E.164 formatted phone number that will receive a
                code via SMS to access this signer's signature page. (optional) By using the feature, you agree you are
                responsible for obtaining a signer's consent to receive text messages from Dropbox Sign related to this
                signature request and confirm you have obtained such consent from all signers prior to enabling SMS
                delivery for this signature request. `Learn more
                <https://faq.hellosign.com/hc/en-us/articles/15815316468877-Dropbox-Sign-SMS-tools-add-on>`__. **NOTE:**
                Not available in test mode and requires a Standard plan or higher. - ``*_field``: any column with a
                _field" suffix will be treated as a custom field (optional) You may only specify field values here, any
                other options should be set in the custom_fields request parameter. Example CSV: ``` name,
                email_address, pin, company_field George, george@example.com, d79a3td, ABC Corp Mary, mary@example.com,
                gd9as5b, 123 LLC ```
            signer_list: ``signer_list`` is an array defining values and options for signer fields. Required unless a
                ``signer_file`` is used, you may not use both.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            ccs: Add CC email recipients. Required when a CC role exists for the Template.
            client_id: The client id of the API App you want to associate with this request. Used to apply the branding
                and callback url defined for the app.
            custom_fields: When used together with merge fields, ``custom_fields`` allows users to add pre-filled data
                to their signature requests. Pre-filled data can be used with "send-once" signature requests by adding
                merge fields with ``form_fields_per_document`` or `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ while passing values back with
                ``custom_fields`` together in one API call. For using pre-filled on repeatable signature requests, merge
                fields are added to templates in the Dropbox Sign UI or by calling `/template/create_embedded_draft
                </api/reference/operation/templateCreateEmbeddedDraft>`__ and then passing ``custom_fields`` on
                subsequent signature requests referencing that template.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            signing_redirect_url: The URL you want signers redirected to after they successfully sign.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request will not be legally binding if set to ``true``.
                Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            expires_at: When the signature request will expire. Unsigned signatures will be moved to the expired status,
                and no longer signable. See `Signature Request Expiration Date
                <https://developers.hellosign.com/docs/signature-request/expiration/>`__ for details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.signature_request_bulk_send_with_template(
                template_ids,
                signer_file=signer_file,
                signer_list=signer_list,
                allow_decline=allow_decline,
                ccs=ccs,
                client_id=client_id,
                custom_fields=custom_fields,
                message=message,
                metadata=metadata,
                signing_redirect_url=signing_redirect_url,
                subject=subject,
                test_mode=test_mode,
                title=title,
                expires_at=expires_at,
                request_options=request_options,
            ),
        )

    async def signature_request_cancel(
        self, signature_request_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Any:
        """Cancels an incomplete signature request. This action is **not reversible**.

        The request will be canceled and signers will no longer be able to sign. If they try to access the signature
        request they will receive a HTTP 410 status code indicating that the resource has been deleted. Cancelation is
        asynchronous and a successful call to this endpoint will return an empty 200 OK response if the signature
        request is eligible to be canceled and has been successfully queued.

        This 200 OK response does not indicate a successful cancelation of the signature request itself. The cancelation
        is confirmed via the ``signature_request_canceled`` event. It is recommended that a `callback handler
        </api/reference/tag/Callbacks-and-Events>`__ be implemented to listen for the ``signature_request_canceled``
        event. This callback will be sent only when the cancelation has completed successfully. If a callback handler
        has been configured and the event has not been received within 60 minutes of making the call, check the status
        of the request in the `API Dashboard <https://app.hellosign.com/apidashboard>`__ and retry the cancelation if
        necessary.

        To be eligible for cancelation, a signature request must have been sent successfully, must not yet have been
        signed by all signers, and you must either be the sender or own the API app under which it was sent. A partially
        signed signature request can be canceled.

        **NOTE:** To remove your access to a completed signature request, use the endpoint: ``POST
        /signature_request/remove/[:signature_request_id]``.

        Args:
            signature_request_id: The id of the incomplete SignatureRequest to cancel.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.signature_request_cancel(
                signature_request_id, request_options=request_options
            ),
        )

    async def signature_request_create_embedded(
        self,
        client_id: str,
        *,
        files: AsyncFileInput | None = None,
        file_urls: list[str] | None = None,
        signers: list[SubSignatureRequestSigner | SubSignatureRequestSignerDict] | None = None,
        grouped_signers: list[SubSignatureRequestGroupedSigners | SubSignatureRequestGroupedSignersDict] | None = None,
        allow_decline: bool | None = False,
        allow_reassign: bool | None = False,
        attachments: list[SubAttachment | SubAttachmentDict] | None = None,
        cc_email_addresses: list[EmailStr] | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        field_options: SubFieldOptions | SubFieldOptionsDict | None = None,
        form_field_groups: list[SubFormFieldGroup | SubFormFieldGroupDict] | None = None,
        form_field_rules: list[SubFormFieldRule | SubFormFieldRuleDict] | None = None,
        form_fields_per_document: list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None = None,
        hide_text_tags: bool | None = False,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        signing_options: SubSigningOptions | SubSigningOptionsDict | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        use_text_tags: bool | None = False,
        ignore_text_tags_extraction_errors: bool | None = False,
        populate_auto_fill_fields: bool | None = False,
        expires_at: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SignatureRequestGetResponse:
        """Creates a new SignatureRequest with the submitted documents to be signed in an embedded iFrame. If
        form_fields_per_document is not specified, a signature page will be affixed where all signers will be required
        to add their signature, signifying their agreement to all contained documents. Note that embedded signature
        requests can only be signed in embedded iFrames whereas normal signature requests can only be signed on Dropbox
        Sign.

        Args:
            client_id: Client id of the app you're using to create this embedded signature request. Used for security
                purposes.
            files: Use ``files[]`` to indicate the uploaded file(s) to send for signature. This endpoint requires either
                **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            signers: Add Signers to your Signature Request. This endpoint requires either **signers** or
                **grouped_signers**, but not both.
            grouped_signers: Add Grouped Signers to your Signature Request. This endpoint requires either **signers** or
                **grouped_signers**, but not both.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            allow_reassign: Allows signers to reassign their signature requests to other signers if set to ``true``.
                Defaults to ``false``. **NOTE:** Only available for Premium plan.
            attachments: A list describing the attachments
            cc_email_addresses: The email addresses that should be CCed.
            custom_fields: When used together with merge fields, ``custom_fields`` allows users to add pre-filled data
                to their signature requests. Pre-filled data can be used with "send-once" signature requests by adding
                merge fields with ``form_fields_per_document`` or `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ while passing values back with
                ``custom_fields`` together in one API call. For using pre-filled on repeatable signature requests, merge
                fields are added to templates in the Dropbox Sign UI or by calling `/template/create_embedded_draft
                </api/reference/operation/templateCreateEmbeddedDraft>`__ and then passing ``custom_fields`` on
                subsequent signature requests referencing that template.
            field_options: This allows the requester to specify field options for a signature request.
            form_field_groups: Group information for fields defined in ``form_fields_per_document``. String-indexed JSON
                array with ``group_label`` and ``requirement`` keys. ``form_fields_per_document`` must contain fields
                referencing a group defined in ``form_field_groups``.
            form_field_rules: Conditional Logic rules for fields defined in ``form_fields_per_document``.
            form_fields_per_document: The fields that should appear on the document, expressed as an array of objects.
                (For more details you can read about it here: `Using Form Fields per Document
                </docs/openapi/form-fields-per-document>`__.) **NOTE:** Fields like **text**, **dropdown**,
                **checkbox**, **radio**, and **hyperlink** have additional required and optional parameters. Check out
                the list of `additional parameters </api/reference/constants/#form-fields-per-document>`__ for these
                field types. * Text Field use ``SubFormFieldsPerDocumentText`` * Dropdown Field use
                ``SubFormFieldsPerDocumentDropdown`` * Hyperlink Field use ``SubFormFieldsPerDocumentHyperlink`` *
                Checkbox Field use ``SubFormFieldsPerDocumentCheckbox`` * Radio Field use
                ``SubFormFieldsPerDocumentRadio`` * Signature Field use ``SubFormFieldsPerDocumentSignature`` * Date
                Signed Field use ``SubFormFieldsPerDocumentDateSigned`` * Initials Field use
                ``SubFormFieldsPerDocumentInitials`` * Text Merge Field use ``SubFormFieldsPerDocumentTextMerge`` *
                Checkbox Merge Field use ``SubFormFieldsPerDocumentCheckboxMerge``
            hide_text_tags: Enables automatic Text Tag removal when set to true. **NOTE:** Removing text tags this way
                can cause unwanted clipping. We recommend leaving this setting on ``false`` and instead hiding your text
                tags using white text or a similar approach. See the `Text Tags Walkthrough
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ for more information.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            signing_options: This allows the requester to specify the types allowed for creating a signature and specify
                another signing options. **NOTE:** If ``signing_options`` are not defined in the request, the allowed
                types will default to those specified in the account settings. **NOTE:** If
                ``force_advanced_signature_details`` is set, allowed types has to be defined too.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request will not be legally binding if set to ``true``.
                Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            use_text_tags: Send with a value of ``true`` if you wish to enable `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ parsing in your document. Defaults
                to disabled, or ``false``.
            ignore_text_tags_extraction_errors: Sent with a value of ``true`` to ignore the validation errors from text
                tags extraction. Defaults to ``false``.
            populate_auto_fill_fields: Controls whether `auto fill fields
                <https://faq.hellosign.com/hc/en-us/articles/360051467511-Auto-Fill-Fields>`__ can automatically
                populate a signer's information during signing. **NOTE:** Keep your signer's information safe by
                ensuring that the _signer on your signature request is the intended party_ before using this feature.
            expires_at: When the signature request will expire. Unsigned signatures will be moved to the expired status,
                and no longer signable. See `Signature Request Expiration Date
                <https://developers.hellosign.com/docs/signature-request/expiration/>`__ for details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.signature_request_create_embedded(
                client_id,
                files=files,
                file_urls=file_urls,
                signers=signers,
                grouped_signers=grouped_signers,
                allow_decline=allow_decline,
                allow_reassign=allow_reassign,
                attachments=attachments,
                cc_email_addresses=cc_email_addresses,
                custom_fields=custom_fields,
                field_options=field_options,
                form_field_groups=form_field_groups,
                form_field_rules=form_field_rules,
                form_fields_per_document=form_fields_per_document,
                hide_text_tags=hide_text_tags,
                message=message,
                metadata=metadata,
                signing_options=signing_options,
                subject=subject,
                test_mode=test_mode,
                title=title,
                use_text_tags=use_text_tags,
                ignore_text_tags_extraction_errors=ignore_text_tags_extraction_errors,
                populate_auto_fill_fields=populate_auto_fill_fields,
                expires_at=expires_at,
                request_options=request_options,
            ),
        )

    async def signature_request_create_embedded_with_template(
        self,
        template_ids: list[str],
        client_id: str,
        signers: list[SubSignatureRequestTemplateSigner | SubSignatureRequestTemplateSignerDict],
        *,
        allow_decline: bool | None = False,
        ccs: list[SubCc | SubCcDict] | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        files: AsyncFileInput | None = None,
        file_urls: list[str] | None = None,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        signing_options: SubSigningOptions | SubSigningOptionsDict | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        populate_auto_fill_fields: bool | None = False,
        expires_at: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SignatureRequestGetResponse:
        """Creates a new SignatureRequest based on the given Template(s) to be signed in an embedded iFrame. Note that
        embedded signature requests can only be signed in embedded iFrames whereas normal signature requests can only be
        signed on Dropbox Sign.

        Args:
            template_ids: Use ``template_ids`` to create a SignatureRequest from one or more templates, in the order in
                which the template will be used.
            client_id: Client id of the app you're using to create this embedded signature request. Used for security
                purposes.
            signers: Add Signers to your Templated-based Signature Request.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            ccs: Add CC email recipients. Required when a CC role exists for the Template.
            custom_fields: An array defining values and options for custom fields. Required when a custom field exists
                in the Template.
            files: Use ``files[]`` to indicate the uploaded file(s) to send for signature. This endpoint requires either
                **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            signing_options: This allows the requester to specify the types allowed for creating a signature and specify
                another signing options. **NOTE:** If ``signing_options`` are not defined in the request, the allowed
                types will default to those specified in the account settings. **NOTE:** If
                ``force_advanced_signature_details`` is set, allowed types has to be defined too.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request will not be legally binding if set to ``true``.
                Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            populate_auto_fill_fields: Controls whether `auto fill fields
                <https://faq.hellosign.com/hc/en-us/articles/360051467511-Auto-Fill-Fields>`__ can automatically
                populate a signer's information during signing. **NOTE:** Keep your signer's information safe by
                ensuring that the _signer on your signature request is the intended party_ before using this feature.
            expires_at: When the signature request will expire. Unsigned signatures will be moved to the expired status,
                and no longer signable. See `Signature Request Expiration Date
                <https://developers.hellosign.com/docs/signature-request/expiration/>`__ for details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.signature_request_create_embedded_with_template(
                template_ids,
                client_id,
                signers,
                allow_decline=allow_decline,
                ccs=ccs,
                custom_fields=custom_fields,
                files=files,
                file_urls=file_urls,
                message=message,
                metadata=metadata,
                signing_options=signing_options,
                subject=subject,
                test_mode=test_mode,
                title=title,
                populate_auto_fill_fields=populate_auto_fill_fields,
                expires_at=expires_at,
                request_options=request_options,
            ),
        )

    async def signature_request_edit(
        self,
        signature_request_id: str,
        *,
        files: AsyncFileInput | None = None,
        file_urls: list[str] | None = None,
        signers: list[SubSignatureRequestSigner | SubSignatureRequestSignerDict] | None = None,
        grouped_signers: list[SubSignatureRequestGroupedSigners | SubSignatureRequestGroupedSignersDict] | None = None,
        allow_decline: bool | None = False,
        allow_reassign: bool | None = False,
        attachments: list[SubAttachment | SubAttachmentDict] | None = None,
        cc_email_addresses: list[EmailStr] | None = None,
        client_id: str | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        field_options: SubFieldOptions | SubFieldOptionsDict | None = None,
        form_field_groups: list[SubFormFieldGroup | SubFormFieldGroupDict] | None = None,
        form_field_rules: list[SubFormFieldRule | SubFormFieldRuleDict] | None = None,
        form_fields_per_document: list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None = None,
        hide_text_tags: bool | None = False,
        is_eid: bool | None = False,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        signing_options: SubSigningOptions | SubSigningOptionsDict | None = None,
        signing_redirect_url: str | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        use_text_tags: bool | None = False,
        ignore_text_tags_extraction_errors: bool | None = False,
        expires_at: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SignatureRequestGetResponse:
        """Edits and sends a SignatureRequest with the submitted documents. If ``form_fields_per_document`` is not
        specified, a signature page will be affixed where all signers will be required to add their signature,
        signifying their agreement to all contained documents.

        **NOTE:** Edit and resend *will* deduct your signature request quota.

        Args:
            signature_request_id: The id of the SignatureRequest to edit.
            files: Use ``files[]`` to indicate the uploaded file(s) to send for signature. This endpoint requires either
                **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            signers: Add Signers to your Signature Request. This endpoint requires either **signers** or
                **grouped_signers**, but not both.
            grouped_signers: Add Grouped Signers to your Signature Request. This endpoint requires either **signers** or
                **grouped_signers**, but not both.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            allow_reassign: Allows signers to reassign their signature requests to other signers if set to ``true``.
                Defaults to ``false``. **NOTE:** Only available for Premium plan and higher.
            attachments: A list describing the attachments
            cc_email_addresses: The email addresses that should be CCed.
            client_id: The client id of the API App you want to associate with this request. Used to apply the branding
                and callback url defined for the app.
            custom_fields: When used together with merge fields, ``custom_fields`` allows users to add pre-filled data
                to their signature requests. Pre-filled data can be used with "send-once" signature requests by adding
                merge fields with ``form_fields_per_document`` or `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ while passing values back with
                ``custom_fields`` together in one API call. For using pre-filled on repeatable signature requests, merge
                fields are added to templates in the Dropbox Sign UI or by calling `/template/create_embedded_draft
                </api/reference/operation/templateCreateEmbeddedDraft>`__ and then passing ``custom_fields`` on
                subsequent signature requests referencing that template.
            field_options: This allows the requester to specify field options for a signature request.
            form_field_groups: Group information for fields defined in ``form_fields_per_document``. String-indexed JSON
                array with ``group_label`` and ``requirement`` keys. ``form_fields_per_document`` must contain fields
                referencing a group defined in ``form_field_groups``.
            form_field_rules: Conditional Logic rules for fields defined in ``form_fields_per_document``.
            form_fields_per_document: The fields that should appear on the document, expressed as an array of objects.
                (For more details you can read about it here: `Using Form Fields per Document
                </docs/openapi/form-fields-per-document>`__.) **NOTE:** Fields like **text**, **dropdown**,
                **checkbox**, **radio**, and **hyperlink** have additional required and optional parameters. Check out
                the list of `additional parameters </api/reference/constants/#form-fields-per-document>`__ for these
                field types. * Text Field use ``SubFormFieldsPerDocumentText`` * Dropdown Field use
                ``SubFormFieldsPerDocumentDropdown`` * Hyperlink Field use ``SubFormFieldsPerDocumentHyperlink`` *
                Checkbox Field use ``SubFormFieldsPerDocumentCheckbox`` * Radio Field use
                ``SubFormFieldsPerDocumentRadio`` * Signature Field use ``SubFormFieldsPerDocumentSignature`` * Date
                Signed Field use ``SubFormFieldsPerDocumentDateSigned`` * Initials Field use
                ``SubFormFieldsPerDocumentInitials`` * Text Merge Field use ``SubFormFieldsPerDocumentTextMerge`` *
                Checkbox Merge Field use ``SubFormFieldsPerDocumentCheckboxMerge``
            hide_text_tags: Enables automatic Text Tag removal when set to true. **NOTE:** Removing text tags this way
                can cause unwanted clipping. We recommend leaving this setting on ``false`` and instead hiding your text
                tags using white text or a similar approach. See the `Text Tags Walkthrough
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ for more information.
            is_eid: Send with a value of ``true`` if you wish to enable `electronic identification (eID)
                <https://www.hellosign.com/features/electronic-id>`__, which requires the signer to verify their
                identity with an eID provider to sign a document.<br> **NOTE:** You need the eID add-on to use this
                feature. Please `contact sales <https://sign.dropbox.com/form/contact-sales>`__ for more information.
                Cannot be used in ``test_mode``. Only works on requests with one signer.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            signing_options: This allows the requester to specify the types allowed for creating a signature and specify
                another signing options. **NOTE:** If ``signing_options`` are not defined in the request, the allowed
                types will default to those specified in the account settings. **NOTE:** If
                ``force_advanced_signature_details`` is set, allowed types has to be defined too.
            signing_redirect_url: The URL you want signers redirected to after they successfully sign.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request will not be legally binding if set to ``true``.
                Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            use_text_tags: Send with a value of ``true`` if you wish to enable `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ parsing in your document. Defaults
                to disabled, or ``false``.
            ignore_text_tags_extraction_errors: Sent with a value of ``true`` to ignore the validation errors from text
                tags extraction. Defaults to ``false``.
            expires_at: When the signature request will expire. Unsigned signatures will be moved to the expired status,
                and no longer signable. See `Signature Request Expiration Date
                <https://developers.hellosign.com/docs/signature-request/expiration/>`__ for details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.signature_request_edit(
                signature_request_id,
                files=files,
                file_urls=file_urls,
                signers=signers,
                grouped_signers=grouped_signers,
                allow_decline=allow_decline,
                allow_reassign=allow_reassign,
                attachments=attachments,
                cc_email_addresses=cc_email_addresses,
                client_id=client_id,
                custom_fields=custom_fields,
                field_options=field_options,
                form_field_groups=form_field_groups,
                form_field_rules=form_field_rules,
                form_fields_per_document=form_fields_per_document,
                hide_text_tags=hide_text_tags,
                is_eid=is_eid,
                message=message,
                metadata=metadata,
                signing_options=signing_options,
                signing_redirect_url=signing_redirect_url,
                subject=subject,
                test_mode=test_mode,
                title=title,
                use_text_tags=use_text_tags,
                ignore_text_tags_extraction_errors=ignore_text_tags_extraction_errors,
                expires_at=expires_at,
                request_options=request_options,
            ),
        )

    async def signature_request_edit_embedded(
        self,
        signature_request_id: str,
        client_id: str,
        *,
        files: AsyncFileInput | None = None,
        file_urls: list[str] | None = None,
        signers: list[SubSignatureRequestSigner | SubSignatureRequestSignerDict] | None = None,
        grouped_signers: list[SubSignatureRequestGroupedSigners | SubSignatureRequestGroupedSignersDict] | None = None,
        allow_decline: bool | None = False,
        allow_reassign: bool | None = False,
        attachments: list[SubAttachment | SubAttachmentDict] | None = None,
        cc_email_addresses: list[EmailStr] | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        field_options: SubFieldOptions | SubFieldOptionsDict | None = None,
        form_field_groups: list[SubFormFieldGroup | SubFormFieldGroupDict] | None = None,
        form_field_rules: list[SubFormFieldRule | SubFormFieldRuleDict] | None = None,
        form_fields_per_document: list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None = None,
        hide_text_tags: bool | None = False,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        signing_options: SubSigningOptions | SubSigningOptionsDict | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        use_text_tags: bool | None = False,
        ignore_text_tags_extraction_errors: bool | None = False,
        populate_auto_fill_fields: bool | None = False,
        expires_at: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SignatureRequestGetResponse:
        """Edits a SignatureRequest with the submitted documents to be signed in an embedded iFrame. If
        form_fields_per_document is not specified, a signature page will be affixed where all signers will be required
        to add their signature, signifying their agreement to all contained documents. Note that embedded signature
        requests can only be signed in embedded iFrames whereas normal signature requests can only be signed on Dropbox
        Sign.

        **NOTE:** Edit and resend *will* deduct your signature request quota.

        Args:
            signature_request_id: The id of the SignatureRequest to edit.
            client_id: Client id of the app you're using to create this embedded signature request. Used for security
                purposes.
            files: Use ``files[]`` to indicate the uploaded file(s) to send for signature. This endpoint requires either
                **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            signers: Add Signers to your Signature Request. This endpoint requires either **signers** or
                **grouped_signers**, but not both.
            grouped_signers: Add Grouped Signers to your Signature Request. This endpoint requires either **signers** or
                **grouped_signers**, but not both.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            allow_reassign: Allows signers to reassign their signature requests to other signers if set to ``true``.
                Defaults to ``false``. **NOTE:** Only available for Premium plan.
            attachments: A list describing the attachments
            cc_email_addresses: The email addresses that should be CCed.
            custom_fields: When used together with merge fields, ``custom_fields`` allows users to add pre-filled data
                to their signature requests. Pre-filled data can be used with "send-once" signature requests by adding
                merge fields with ``form_fields_per_document`` or `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ while passing values back with
                ``custom_fields`` together in one API call. For using pre-filled on repeatable signature requests, merge
                fields are added to templates in the Dropbox Sign UI or by calling `/template/create_embedded_draft
                </api/reference/operation/templateCreateEmbeddedDraft>`__ and then passing ``custom_fields`` on
                subsequent signature requests referencing that template.
            field_options: This allows the requester to specify field options for a signature request.
            form_field_groups: Group information for fields defined in ``form_fields_per_document``. String-indexed JSON
                array with ``group_label`` and ``requirement`` keys. ``form_fields_per_document`` must contain fields
                referencing a group defined in ``form_field_groups``.
            form_field_rules: Conditional Logic rules for fields defined in ``form_fields_per_document``.
            form_fields_per_document: The fields that should appear on the document, expressed as an array of objects.
                (For more details you can read about it here: `Using Form Fields per Document
                </docs/openapi/form-fields-per-document>`__.) **NOTE:** Fields like **text**, **dropdown**,
                **checkbox**, **radio**, and **hyperlink** have additional required and optional parameters. Check out
                the list of `additional parameters </api/reference/constants/#form-fields-per-document>`__ for these
                field types. * Text Field use ``SubFormFieldsPerDocumentText`` * Dropdown Field use
                ``SubFormFieldsPerDocumentDropdown`` * Hyperlink Field use ``SubFormFieldsPerDocumentHyperlink`` *
                Checkbox Field use ``SubFormFieldsPerDocumentCheckbox`` * Radio Field use
                ``SubFormFieldsPerDocumentRadio`` * Signature Field use ``SubFormFieldsPerDocumentSignature`` * Date
                Signed Field use ``SubFormFieldsPerDocumentDateSigned`` * Initials Field use
                ``SubFormFieldsPerDocumentInitials`` * Text Merge Field use ``SubFormFieldsPerDocumentTextMerge`` *
                Checkbox Merge Field use ``SubFormFieldsPerDocumentCheckboxMerge``
            hide_text_tags: Enables automatic Text Tag removal when set to true. **NOTE:** Removing text tags this way
                can cause unwanted clipping. We recommend leaving this setting on ``false`` and instead hiding your text
                tags using white text or a similar approach. See the `Text Tags Walkthrough
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ for more information.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            signing_options: This allows the requester to specify the types allowed for creating a signature and specify
                another signing options. **NOTE:** If ``signing_options`` are not defined in the request, the allowed
                types will default to those specified in the account settings. **NOTE:** If
                ``force_advanced_signature_details`` is set, allowed types has to be defined too.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request will not be legally binding if set to ``true``.
                Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            use_text_tags: Send with a value of ``true`` if you wish to enable `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ parsing in your document. Defaults
                to disabled, or ``false``.
            ignore_text_tags_extraction_errors: Sent with a value of ``true`` to ignore the validation errors from text
                tags extraction. Defaults to ``false``.
            populate_auto_fill_fields: Controls whether `auto fill fields
                <https://faq.hellosign.com/hc/en-us/articles/360051467511-Auto-Fill-Fields>`__ can automatically
                populate a signer's information during signing. **NOTE:** Keep your signer's information safe by
                ensuring that the _signer on your signature request is the intended party_ before using this feature.
            expires_at: When the signature request will expire. Unsigned signatures will be moved to the expired status,
                and no longer signable. See `Signature Request Expiration Date
                <https://developers.hellosign.com/docs/signature-request/expiration/>`__ for details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.signature_request_edit_embedded(
                signature_request_id,
                client_id,
                files=files,
                file_urls=file_urls,
                signers=signers,
                grouped_signers=grouped_signers,
                allow_decline=allow_decline,
                allow_reassign=allow_reassign,
                attachments=attachments,
                cc_email_addresses=cc_email_addresses,
                custom_fields=custom_fields,
                field_options=field_options,
                form_field_groups=form_field_groups,
                form_field_rules=form_field_rules,
                form_fields_per_document=form_fields_per_document,
                hide_text_tags=hide_text_tags,
                message=message,
                metadata=metadata,
                signing_options=signing_options,
                subject=subject,
                test_mode=test_mode,
                title=title,
                use_text_tags=use_text_tags,
                ignore_text_tags_extraction_errors=ignore_text_tags_extraction_errors,
                populate_auto_fill_fields=populate_auto_fill_fields,
                expires_at=expires_at,
                request_options=request_options,
            ),
        )

    async def signature_request_edit_embedded_with_template(
        self,
        signature_request_id: str,
        template_ids: list[str],
        client_id: str,
        signers: list[SubSignatureRequestTemplateSigner | SubSignatureRequestTemplateSignerDict],
        *,
        allow_decline: bool | None = False,
        ccs: list[SubCc | SubCcDict] | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        files: AsyncFileInput | None = None,
        file_urls: list[str] | None = None,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        signing_options: SubSigningOptions | SubSigningOptionsDict | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        populate_auto_fill_fields: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SignatureRequestGetResponse:
        """Edits a SignatureRequest based on the given Template(s) to be signed in an embedded iFrame. Note that
        embedded signature requests can only be signed in embedded iFrames whereas normal signature requests can only be
        signed on Dropbox Sign.

        **NOTE:** Edit and resend *will* deduct your signature request quota.

        Args:
            signature_request_id: The id of the SignatureRequest to edit.
            template_ids: Use ``template_ids`` to create a SignatureRequest from one or more templates, in the order in
                which the template will be used.
            client_id: Client id of the app you're using to create this embedded signature request. Used for security
                purposes.
            signers: Add Signers to your Templated-based Signature Request.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            ccs: Add CC email recipients. Required when a CC role exists for the Template.
            custom_fields: An array defining values and options for custom fields. Required when a custom field exists
                in the Template.
            files: Use ``files[]`` to indicate the uploaded file(s) to send for signature. This endpoint requires either
                **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            signing_options: This allows the requester to specify the types allowed for creating a signature and specify
                another signing options. **NOTE:** If ``signing_options`` are not defined in the request, the allowed
                types will default to those specified in the account settings. **NOTE:** If
                ``force_advanced_signature_details`` is set, allowed types has to be defined too.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request will not be legally binding if set to ``true``.
                Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            populate_auto_fill_fields: Controls whether `auto fill fields
                <https://faq.hellosign.com/hc/en-us/articles/360051467511-Auto-Fill-Fields>`__ can automatically
                populate a signer's information during signing. **NOTE:** Keep your signer's information safe by
                ensuring that the _signer on your signature request is the intended party_ before using this feature.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.signature_request_edit_embedded_with_template(
                signature_request_id,
                template_ids,
                client_id,
                signers,
                allow_decline=allow_decline,
                ccs=ccs,
                custom_fields=custom_fields,
                files=files,
                file_urls=file_urls,
                message=message,
                metadata=metadata,
                signing_options=signing_options,
                subject=subject,
                test_mode=test_mode,
                title=title,
                populate_auto_fill_fields=populate_auto_fill_fields,
                request_options=request_options,
            ),
        )

    async def signature_request_edit_with_template(
        self,
        signature_request_id: str,
        template_ids: list[str],
        signers: list[SubSignatureRequestTemplateSigner | SubSignatureRequestTemplateSignerDict],
        *,
        allow_decline: bool | None = False,
        ccs: list[SubCc | SubCcDict] | None = None,
        client_id: str | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        files: AsyncFileInput | None = None,
        file_urls: list[str] | None = None,
        is_eid: bool | None = False,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        signing_options: SubSigningOptions | SubSigningOptionsDict | None = None,
        signing_redirect_url: str | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SignatureRequestGetResponse:
        """Edits and sends a SignatureRequest based off of the Template(s) specified with the template_ids parameter.

        **NOTE:** Edit and resend *will* deduct your signature request quota.

        Args:
            signature_request_id: The id of the SignatureRequest to edit.
            template_ids: Use ``template_ids`` to create a SignatureRequest from one or more templates, in the order in
                which the template will be used.
            signers: Add Signers to your Templated-based Signature Request.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            ccs: Add CC email recipients. Required when a CC role exists for the Template.
            client_id: Client id of the app to associate with the signature request. Used to apply the branding and
                callback url defined for the app.
            custom_fields: An array defining values and options for custom fields. Required when a custom field exists
                in the Template.
            files: Use ``files[]`` to indicate the uploaded file(s) to send for signature. This endpoint requires either
                **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            is_eid: Send with a value of ``true`` if you wish to enable `electronic identification (eID)
                <https://www.hellosign.com/features/electronic-id>`__, which requires the signer to verify their
                identity with an eID provider to sign a document.<br> **NOTE:** You need the eID add-on to use this
                feature. Please `contact sales <https://sign.dropbox.com/form/contact-sales>`__ for more information.
                Cannot be used in ``test_mode``. Only works on requests with one signer.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            signing_options: This allows the requester to specify the types allowed for creating a signature and specify
                another signing options. **NOTE:** If ``signing_options`` are not defined in the request, the allowed
                types will default to those specified in the account settings. **NOTE:** If
                ``force_advanced_signature_details`` is set, allowed types has to be defined too.
            signing_redirect_url: The URL you want signers redirected to after they successfully sign.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request will not be legally binding if set to ``true``.
                Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.signature_request_edit_with_template(
                signature_request_id,
                template_ids,
                signers,
                allow_decline=allow_decline,
                ccs=ccs,
                client_id=client_id,
                custom_fields=custom_fields,
                files=files,
                file_urls=file_urls,
                is_eid=is_eid,
                message=message,
                metadata=metadata,
                signing_options=signing_options,
                signing_redirect_url=signing_redirect_url,
                subject=subject,
                test_mode=test_mode,
                title=title,
                request_options=request_options,
            ),
        )

    async def signature_request_files(
        self,
        signature_request_id: str,
        *,
        file_type: FileTypeOrStr | None = FileType.PDF,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Obtain a copy of the current documents specified by the ``signature_request_id`` parameter. Returns a PDF or
        ZIP file.

        If the files are currently being prepared, a status code of ``409`` will be returned instead.

        Args:
            signature_request_id: The id of the SignatureRequest to retrieve.
            file_type: Set to ``pdf`` for a single merged document or ``zip`` for a collection of individual documents.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.signature_request_files(
                signature_request_id, file_type=file_type, request_options=request_options
            ),
        )

    async def signature_request_files_as_data_uri(
        self, signature_request_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> FileResponseDataUri:
        """Obtain a copy of the current documents specified by the ``signature_request_id`` parameter. Returns a JSON
        object with a ``data_uri`` representing the base64 encoded file (PDFs only).

        If the files are currently being prepared, a status code of ``409`` will be returned instead.

        Args:
            signature_request_id: The id of the SignatureRequest to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.signature_request_files_as_data_uri(
                signature_request_id, request_options=request_options
            ),
        )

    async def signature_request_files_as_file_url(
        self,
        signature_request_id: str,
        *,
        force_download: int | None = 1,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FileResponseModel:
        """Obtain a copy of the current documents specified by the ``signature_request_id`` parameter. Returns a JSON
        object with a url to the file (PDFs only).

        If the files are currently being prepared, a status code of ``409`` will be returned instead.

        Args:
            signature_request_id: The id of the SignatureRequest to retrieve.
            force_download: By default when opening the ``file_url`` a browser will download the PDF and save it
                locally. When set to ``0`` the PDF file will be displayed in the browser.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.signature_request_files_as_file_url(
                signature_request_id, force_download=force_download, request_options=request_options
            ),
        )

    async def signature_request_get(
        self, signature_request_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SignatureRequestGetResponse:
        """Returns the status of the SignatureRequest specified by the ``signature_request_id`` parameter.

        Args:
            signature_request_id: The id of the SignatureRequest to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.signature_request_get(signature_request_id, request_options=request_options)
        )

    async def signature_request_list(
        self,
        *,
        account_id: str | None = None,
        page: int | None = 1,
        page_size: int | None = 20,
        query: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SignatureRequestListResponse:
        """Returns a list of SignatureRequests that you can access. This includes SignatureRequests you have sent as
        well as received, but not ones that you have been CCed on.

        Take a look at our `search guide </api/reference/search/>`__ to learn more about querying signature requests.

        Args:
            account_id: Which account to return SignatureRequests for. Must be a team member. Use ``all`` to indicate
                all team members. Defaults to your account.
            page: Which page number of the SignatureRequest List to return. Defaults to ``1``.
            page_size: Number of objects to be returned per page. Must be between ``1`` and ``100``. Default is ``20``.
            query: String that includes search terms and/or fields to be used to filter the SignatureRequest objects.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.signature_request_list(
                account_id=account_id, page=page, page_size=page_size, query=query, request_options=request_options
            ),
        )

    async def signature_request_release_hold(
        self, signature_request_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SignatureRequestGetResponse:
        """Releases a held SignatureRequest that was claimed and prepared from an `UnclaimedDraft
        </api/reference/tag/Unclaimed-Draft>`__. The owner of the Draft must indicate at Draft creation that the
        SignatureRequest created from the Draft should be held. Releasing the SignatureRequest will send requests to all
        signers.

        Args:
            signature_request_id: The id of the SignatureRequest to release.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.signature_request_release_hold(
                signature_request_id, request_options=request_options
            ),
        )

    async def signature_request_remind(
        self,
        signature_request_id: str,
        body: SignatureRequestRemindRequest | SignatureRequestRemindRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SignatureRequestGetResponse:
        """Sends an email to the signer reminding them to sign the signature request. You cannot send a reminder within
        1 hour of the last reminder that was sent. This includes manual AND automatic reminders.

        **NOTE:** This action can **not** be used with embedded signature requests.

        Args:
            signature_request_id: The id of the SignatureRequest to send a reminder for.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.signature_request_remind(
                signature_request_id, body, request_options=request_options
            ),
        )

    async def signature_request_remove(
        self, signature_request_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Any:
        """Removes your access to a completed signature request. This action is **not reversible**.

        The signature request must be fully executed by all parties (signed or declined to sign). Other parties will
        continue to maintain access to the completed signature request document(s).

        Unlike /signature_request/cancel, this endpoint is synchronous and your access will be immediately removed. Upon
        successful removal, this endpoint will return a 200 OK response.

        Args:
            signature_request_id: The id of the SignatureRequest to remove.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.signature_request_remove(
                signature_request_id, request_options=request_options
            ),
        )

    async def signature_request_send(
        self,
        *,
        files: AsyncFileInput | None = None,
        file_urls: list[str] | None = None,
        signers: list[SubSignatureRequestSigner | SubSignatureRequestSignerDict] | None = None,
        grouped_signers: list[SubSignatureRequestGroupedSigners | SubSignatureRequestGroupedSignersDict] | None = None,
        allow_decline: bool | None = False,
        allow_reassign: bool | None = False,
        attachments: list[SubAttachment | SubAttachmentDict] | None = None,
        cc_email_addresses: list[EmailStr] | None = None,
        client_id: str | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        field_options: SubFieldOptions | SubFieldOptionsDict | None = None,
        form_field_groups: list[SubFormFieldGroup | SubFormFieldGroupDict] | None = None,
        form_field_rules: list[SubFormFieldRule | SubFormFieldRuleDict] | None = None,
        form_fields_per_document: list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None = None,
        hide_text_tags: bool | None = False,
        is_eid: bool | None = False,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        signing_options: SubSigningOptions | SubSigningOptionsDict | None = None,
        signing_redirect_url: str | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        use_text_tags: bool | None = False,
        ignore_text_tags_extraction_errors: bool | None = False,
        expires_at: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SignatureRequestGetResponse:
        """Creates and sends a new SignatureRequest with the submitted documents. If ``form_fields_per_document`` is not
        specified, a signature page will be affixed where all signers will be required to add their signature,
        signifying their agreement to all contained documents.

        Args:
            files: Use ``files[]`` to indicate the uploaded file(s) to send for signature. This endpoint requires either
                **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            signers: Add Signers to your Signature Request. This endpoint requires either **signers** or
                **grouped_signers**, but not both.
            grouped_signers: Add Grouped Signers to your Signature Request. This endpoint requires either **signers** or
                **grouped_signers**, but not both.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            allow_reassign: Allows signers to reassign their signature requests to other signers if set to ``true``.
                Defaults to ``false``. **NOTE:** Only available for Premium plan and higher.
            attachments: A list describing the attachments
            cc_email_addresses: The email addresses that should be CCed.
            client_id: The client id of the API App you want to associate with this request. Used to apply the branding
                and callback url defined for the app.
            custom_fields: When used together with merge fields, ``custom_fields`` allows users to add pre-filled data
                to their signature requests. Pre-filled data can be used with "send-once" signature requests by adding
                merge fields with ``form_fields_per_document`` or `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ while passing values back with
                ``custom_fields`` together in one API call. For using pre-filled on repeatable signature requests, merge
                fields are added to templates in the Dropbox Sign UI or by calling `/template/create_embedded_draft
                </api/reference/operation/templateCreateEmbeddedDraft>`__ and then passing ``custom_fields`` on
                subsequent signature requests referencing that template.
            field_options: This allows the requester to specify field options for a signature request.
            form_field_groups: Group information for fields defined in ``form_fields_per_document``. String-indexed JSON
                array with ``group_label`` and ``requirement`` keys. ``form_fields_per_document`` must contain fields
                referencing a group defined in ``form_field_groups``.
            form_field_rules: Conditional Logic rules for fields defined in ``form_fields_per_document``.
            form_fields_per_document: The fields that should appear on the document, expressed as an array of objects.
                (For more details you can read about it here: `Using Form Fields per Document
                </docs/openapi/form-fields-per-document>`__.) **NOTE:** Fields like **text**, **dropdown**,
                **checkbox**, **radio**, and **hyperlink** have additional required and optional parameters. Check out
                the list of `additional parameters </api/reference/constants/#form-fields-per-document>`__ for these
                field types. * Text Field use ``SubFormFieldsPerDocumentText`` * Dropdown Field use
                ``SubFormFieldsPerDocumentDropdown`` * Hyperlink Field use ``SubFormFieldsPerDocumentHyperlink`` *
                Checkbox Field use ``SubFormFieldsPerDocumentCheckbox`` * Radio Field use
                ``SubFormFieldsPerDocumentRadio`` * Signature Field use ``SubFormFieldsPerDocumentSignature`` * Date
                Signed Field use ``SubFormFieldsPerDocumentDateSigned`` * Initials Field use
                ``SubFormFieldsPerDocumentInitials`` * Text Merge Field use ``SubFormFieldsPerDocumentTextMerge`` *
                Checkbox Merge Field use ``SubFormFieldsPerDocumentCheckboxMerge``
            hide_text_tags: Enables automatic Text Tag removal when set to true. **NOTE:** Removing text tags this way
                can cause unwanted clipping. We recommend leaving this setting on ``false`` and instead hiding your text
                tags using white text or a similar approach. See the `Text Tags Walkthrough
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ for more information.
            is_eid: Send with a value of ``true`` if you wish to enable `electronic identification (eID)
                <https://www.hellosign.com/features/electronic-id>`__, which requires the signer to verify their
                identity with an eID provider to sign a document.<br> **NOTE:** You need the eID add-on to use this
                feature. Please `contact sales <https://sign.dropbox.com/form/contact-sales>`__ for more information.
                Cannot be used in ``test_mode``. Only works on requests with one signer.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            signing_options: This allows the requester to specify the types allowed for creating a signature and specify
                another signing options. **NOTE:** If ``signing_options`` are not defined in the request, the allowed
                types will default to those specified in the account settings. **NOTE:** If
                ``force_advanced_signature_details`` is set, allowed types has to be defined too.
            signing_redirect_url: The URL you want signers redirected to after they successfully sign.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request will not be legally binding if set to ``true``.
                Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            use_text_tags: Send with a value of ``true`` if you wish to enable `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ parsing in your document. Defaults
                to disabled, or ``false``.
            ignore_text_tags_extraction_errors: Sent with a value of ``true`` to ignore the validation errors from text
                tags extraction. Defaults to ``false``.
            expires_at: When the signature request will expire. Unsigned signatures will be moved to the expired status,
                and no longer signable. See `Signature Request Expiration Date
                <https://developers.hellosign.com/docs/signature-request/expiration/>`__ for details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.signature_request_send(
                files=files,
                file_urls=file_urls,
                signers=signers,
                grouped_signers=grouped_signers,
                allow_decline=allow_decline,
                allow_reassign=allow_reassign,
                attachments=attachments,
                cc_email_addresses=cc_email_addresses,
                client_id=client_id,
                custom_fields=custom_fields,
                field_options=field_options,
                form_field_groups=form_field_groups,
                form_field_rules=form_field_rules,
                form_fields_per_document=form_fields_per_document,
                hide_text_tags=hide_text_tags,
                is_eid=is_eid,
                message=message,
                metadata=metadata,
                signing_options=signing_options,
                signing_redirect_url=signing_redirect_url,
                subject=subject,
                test_mode=test_mode,
                title=title,
                use_text_tags=use_text_tags,
                ignore_text_tags_extraction_errors=ignore_text_tags_extraction_errors,
                expires_at=expires_at,
                request_options=request_options,
            ),
        )

    async def signature_request_send_with_template(
        self,
        template_ids: list[str],
        signers: list[SubSignatureRequestTemplateSigner | SubSignatureRequestTemplateSignerDict],
        *,
        allow_decline: bool | None = False,
        ccs: list[SubCc | SubCcDict] | None = None,
        client_id: str | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        files: AsyncFileInput | None = None,
        file_urls: list[str] | None = None,
        is_eid: bool | None = False,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        signing_options: SubSigningOptions | SubSigningOptionsDict | None = None,
        signing_redirect_url: str | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        expires_at: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SignatureRequestGetResponse:
        """Creates and sends a new SignatureRequest based off of the Template(s) specified with the ``template_ids``
        parameter.

        Args:
            template_ids: Use ``template_ids`` to create a SignatureRequest from one or more templates, in the order in
                which the template will be used.
            signers: Add Signers to your Templated-based Signature Request.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            ccs: Add CC email recipients. Required when a CC role exists for the Template.
            client_id: Client id of the app to associate with the signature request. Used to apply the branding and
                callback url defined for the app.
            custom_fields: An array defining values and options for custom fields. Required when a custom field exists
                in the Template.
            files: Use ``files[]`` to indicate the uploaded file(s) to send for signature. This endpoint requires either
                **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            is_eid: Send with a value of ``true`` if you wish to enable `electronic identification (eID)
                <https://www.hellosign.com/features/electronic-id>`__, which requires the signer to verify their
                identity with an eID provider to sign a document.<br> **NOTE:** You need the eID add-on to use this
                feature. Please `contact sales <https://sign.dropbox.com/form/contact-sales>`__ for more information.
                Cannot be used in ``test_mode``. Only works on requests with one signer.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            signing_options: This allows the requester to specify the types allowed for creating a signature and specify
                another signing options. **NOTE:** If ``signing_options`` are not defined in the request, the allowed
                types will default to those specified in the account settings. **NOTE:** If
                ``force_advanced_signature_details`` is set, allowed types has to be defined too.
            signing_redirect_url: The URL you want signers redirected to after they successfully sign.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request will not be legally binding if set to ``true``.
                Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            expires_at: When the signature request will expire. Unsigned signatures will be moved to the expired status,
                and no longer signable. See `Signature Request Expiration Date
                <https://developers.hellosign.com/docs/signature-request/expiration/>`__ for details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.signature_request_send_with_template(
                template_ids,
                signers,
                allow_decline=allow_decline,
                ccs=ccs,
                client_id=client_id,
                custom_fields=custom_fields,
                files=files,
                file_urls=file_urls,
                is_eid=is_eid,
                message=message,
                metadata=metadata,
                signing_options=signing_options,
                signing_redirect_url=signing_redirect_url,
                subject=subject,
                test_mode=test_mode,
                title=title,
                expires_at=expires_at,
                request_options=request_options,
            ),
        )

    async def signature_request_update(
        self,
        signature_request_id: str,
        body: SignatureRequestUpdateRequest | SignatureRequestUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SignatureRequestGetResponse:
        """Updates the email address and/or the name for a given signer on a signature request. You can listen for the
        ``signature_request_email_bounce`` event on your app or account to detect bounced emails, and respond with this
        method.

        Updating the email address of a signer will generate a new ``signature_id`` value.

        **NOTE:** This action cannot be performed on a signature request with an appended signature page.

        Args:
            signature_request_id: The id of the SignatureRequest to update.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.signature_request_update(
                signature_request_id, body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncSignatureRequestWithRawResponse:
        return self._with_raw_response


class SignatureRequestWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def signature_request_bulk_create_embedded_with_template(
        self,
        template_ids: list[str],
        client_id: str,
        *,
        signer_file: FileInput | None = None,
        signer_list: list[SubBulkSignerList | SubBulkSignerListDict] | None = None,
        allow_decline: bool | None = False,
        ccs: list[SubCc | SubCcDict] | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        signing_redirect_url: str | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        expires_at: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkSendJobSendResponse, SignatureRequestBulkCreateEmbeddedWithTemplateErrorBody]:
        """Creates BulkSendJob which sends up to 250 SignatureRequests in bulk based off of the provided Template(s)
        specified with the ``template_ids`` parameter to be signed in an embedded iFrame. These embedded signature
        requests can only be signed in embedded iFrames whereas normal signature requests can only be signed on Dropbox
        Sign.

        **NOTE:** Only available for Standard plan and higher.

        Args:
            template_ids: Use ``template_ids`` to create a SignatureRequest from one or more templates, in the order in
                which the template will be used.
            client_id: Client id of the app you're using to create this embedded signature request. Used for security
                purposes.
            signer_file: ``signer_file`` is a CSV file defining values and options for signer fields. Required unless a
                ``signer_list`` is used, you may not use both. The CSV can have the following columns: - ``name``: the
                name of the signer filling the role of RoleName - ``email_address``: email address of the signer filling
                the role of RoleName - ``pin``: the 4- to 12-character access code that will secure this signer's
                signature page (optional) - ``sms_phone_number``: An E.164 formatted phone number that will receive a
                code via SMS to access this signer's signature page. (optional) By using the feature, you agree you are
                responsible for obtaining a signer's consent to receive text messages from Dropbox Sign related to this
                signature request and confirm you have obtained such consent from all signers prior to enabling SMS
                delivery for this signature request. `Learn more
                <https://faq.hellosign.com/hc/en-us/articles/15815316468877-Dropbox-Sign-SMS-tools-add-on>`__. **NOTE:**
                Not available in test mode and requires a Standard plan or higher. - ``*_field``: any column with a
                _field" suffix will be treated as a custom field (optional) You may only specify field values here, any
                other options should be set in the custom_fields request parameter. Example CSV: ``` name,
                email_address, pin, company_field George, george@example.com, d79a3td, ABC Corp Mary, mary@example.com,
                gd9as5b, 123 LLC ```
            signer_list: ``signer_list`` is an array defining values and options for signer fields. Required unless a
                ``signer_file`` is used, you may not use both.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            ccs: Add CC email recipients. Required when a CC role exists for the Template.
            custom_fields: When used together with merge fields, ``custom_fields`` allows users to add pre-filled data
                to their signature requests. Pre-filled data can be used with "send-once" signature requests by adding
                merge fields with ``form_fields_per_document`` or `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ while passing values back with
                ``custom_fields`` together in one API call. For using pre-filled on repeatable signature requests, merge
                fields are added to templates in the Dropbox Sign UI or by calling `/template/create_embedded_draft
                </api/reference/operation/templateCreateEmbeddedDraft>`__ and then passing ``custom_fields`` on
                subsequent signature requests referencing that template.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            signing_redirect_url: The URL you want signers redirected to after they successfully sign.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request will not be legally binding if set to ``true``.
                Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            expires_at: When the signature request will expire. Unsigned signatures will be moved to the expired status,
                and no longer signable. See `Signature Request Expiration Date
                <https://developers.hellosign.com/docs/signature-request/expiration/>`__ for details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/signature_request/bulk_create_embedded_with_template"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(
                param[list[str]]("template_ids", template_ids),
                param[str]("client_id", client_id),
                file_part("signer_file", signer_file) if signer_file is not None else None,
                param[list[SubBulkSignerList | SubBulkSignerListDict] | None]("signer_list", signer_list),
                param[bool | None]("allow_decline", allow_decline),
                param[list[SubCc | SubCcDict] | None]("ccs", ccs),
                param[list[SubCustomField | SubCustomFieldDict] | None]("custom_fields", custom_fields),
                param[str | None]("message", message),
                param[dict[str, Any] | None]("metadata", metadata),
                param[str | None]("signing_redirect_url", signing_redirect_url),
                param[str | None]("subject", subject),
                param[bool | None]("test_mode", test_mode),
                param[str | None]("title", title),
                param[int | None]("expires_at", expires_at),
            ),
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[BulkSendJobSendResponse],
            error_mapper=signature_request_bulk_create_embedded_with_template_error_mapper,
            request_options=request_options,
        )

    def signature_request_bulk_send_with_template(
        self,
        template_ids: list[str],
        *,
        signer_file: FileInput | None = None,
        signer_list: list[SubBulkSignerList | SubBulkSignerListDict] | None = None,
        allow_decline: bool | None = False,
        ccs: list[SubCc | SubCcDict] | None = None,
        client_id: str | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        signing_redirect_url: str | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        expires_at: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkSendJobSendResponse, SignatureRequestBulkSendWithTemplateErrorBody]:
        """Creates BulkSendJob which sends up to 250 SignatureRequests in bulk based off of the provided Template(s)
        specified with the ``template_ids`` parameter.

        **NOTE:** Only available for Standard plan and higher.

        Args:
            template_ids: Use ``template_ids`` to create a SignatureRequest from one or more templates, in the order in
                which the template will be used.
            signer_file: ``signer_file`` is a CSV file defining values and options for signer fields. Required unless a
                ``signer_list`` is used, you may not use both. The CSV can have the following columns: - ``name``: the
                name of the signer filling the role of RoleName - ``email_address``: email address of the signer filling
                the role of RoleName - ``pin``: the 4- to 12-character access code that will secure this signer's
                signature page (optional) - ``sms_phone_number``: An E.164 formatted phone number that will receive a
                code via SMS to access this signer's signature page. (optional) By using the feature, you agree you are
                responsible for obtaining a signer's consent to receive text messages from Dropbox Sign related to this
                signature request and confirm you have obtained such consent from all signers prior to enabling SMS
                delivery for this signature request. `Learn more
                <https://faq.hellosign.com/hc/en-us/articles/15815316468877-Dropbox-Sign-SMS-tools-add-on>`__. **NOTE:**
                Not available in test mode and requires a Standard plan or higher. - ``*_field``: any column with a
                _field" suffix will be treated as a custom field (optional) You may only specify field values here, any
                other options should be set in the custom_fields request parameter. Example CSV: ``` name,
                email_address, pin, company_field George, george@example.com, d79a3td, ABC Corp Mary, mary@example.com,
                gd9as5b, 123 LLC ```
            signer_list: ``signer_list`` is an array defining values and options for signer fields. Required unless a
                ``signer_file`` is used, you may not use both.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            ccs: Add CC email recipients. Required when a CC role exists for the Template.
            client_id: The client id of the API App you want to associate with this request. Used to apply the branding
                and callback url defined for the app.
            custom_fields: When used together with merge fields, ``custom_fields`` allows users to add pre-filled data
                to their signature requests. Pre-filled data can be used with "send-once" signature requests by adding
                merge fields with ``form_fields_per_document`` or `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ while passing values back with
                ``custom_fields`` together in one API call. For using pre-filled on repeatable signature requests, merge
                fields are added to templates in the Dropbox Sign UI or by calling `/template/create_embedded_draft
                </api/reference/operation/templateCreateEmbeddedDraft>`__ and then passing ``custom_fields`` on
                subsequent signature requests referencing that template.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            signing_redirect_url: The URL you want signers redirected to after they successfully sign.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request will not be legally binding if set to ``true``.
                Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            expires_at: When the signature request will expire. Unsigned signatures will be moved to the expired status,
                and no longer signable. See `Signature Request Expiration Date
                <https://developers.hellosign.com/docs/signature-request/expiration/>`__ for details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/signature_request/bulk_send_with_template"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(
                param[list[str]]("template_ids", template_ids),
                file_part("signer_file", signer_file) if signer_file is not None else None,
                param[list[SubBulkSignerList | SubBulkSignerListDict] | None]("signer_list", signer_list),
                param[bool | None]("allow_decline", allow_decline),
                param[list[SubCc | SubCcDict] | None]("ccs", ccs),
                param[str | None]("client_id", client_id),
                param[list[SubCustomField | SubCustomFieldDict] | None]("custom_fields", custom_fields),
                param[str | None]("message", message),
                param[dict[str, Any] | None]("metadata", metadata),
                param[str | None]("signing_redirect_url", signing_redirect_url),
                param[str | None]("subject", subject),
                param[bool | None]("test_mode", test_mode),
                param[str | None]("title", title),
                param[int | None]("expires_at", expires_at),
            ),
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[BulkSendJobSendResponse],
            error_mapper=signature_request_bulk_send_with_template_error_mapper,
            request_options=request_options,
        )

    def signature_request_cancel(
        self, signature_request_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, SignatureRequestCancelErrorBody]:
        """Cancels an incomplete signature request. This action is **not reversible**.

        The request will be canceled and signers will no longer be able to sign. If they try to access the signature
        request they will receive a HTTP 410 status code indicating that the resource has been deleted. Cancelation is
        asynchronous and a successful call to this endpoint will return an empty 200 OK response if the signature
        request is eligible to be canceled and has been successfully queued.

        This 200 OK response does not indicate a successful cancelation of the signature request itself. The cancelation
        is confirmed via the ``signature_request_canceled`` event. It is recommended that a `callback handler
        </api/reference/tag/Callbacks-and-Events>`__ be implemented to listen for the ``signature_request_canceled``
        event. This callback will be sent only when the cancelation has completed successfully. If a callback handler
        has been configured and the event has not been received within 60 minutes of making the call, check the status
        of the request in the `API Dashboard <https://app.hellosign.com/apidashboard>`__ and retry the cancelation if
        necessary.

        To be eligible for cancelation, a signature request must have been sent successfully, must not yet have been
        signed by all signers, and you must either be the sender or own the API app under which it was sent. A partially
        signed signature request can be canceled.

        **NOTE:** To remove your access to a completed signature request, use the endpoint: ``POST
        /signature_request/remove/[:signature_request_id]``.

        Args:
            signature_request_id: The id of the incomplete SignatureRequest to cancel.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/signature_request/cancel/{signature_request_id}"),
            path_params=[param[str]("signature_request_id", signature_request_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[Any],
            error_mapper=signature_request_cancel_error_mapper,
            request_options=request_options,
        )

    def signature_request_create_embedded(
        self,
        client_id: str,
        *,
        files: FileInput | None = None,
        file_urls: list[str] | None = None,
        signers: list[SubSignatureRequestSigner | SubSignatureRequestSignerDict] | None = None,
        grouped_signers: list[SubSignatureRequestGroupedSigners | SubSignatureRequestGroupedSignersDict] | None = None,
        allow_decline: bool | None = False,
        allow_reassign: bool | None = False,
        attachments: list[SubAttachment | SubAttachmentDict] | None = None,
        cc_email_addresses: list[EmailStr] | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        field_options: SubFieldOptions | SubFieldOptionsDict | None = None,
        form_field_groups: list[SubFormFieldGroup | SubFormFieldGroupDict] | None = None,
        form_field_rules: list[SubFormFieldRule | SubFormFieldRuleDict] | None = None,
        form_fields_per_document: list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None = None,
        hide_text_tags: bool | None = False,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        signing_options: SubSigningOptions | SubSigningOptionsDict | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        use_text_tags: bool | None = False,
        ignore_text_tags_extraction_errors: bool | None = False,
        populate_auto_fill_fields: bool | None = False,
        expires_at: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SignatureRequestGetResponse, SignatureRequestCreateEmbeddedErrorBody]:
        """Creates a new SignatureRequest with the submitted documents to be signed in an embedded iFrame. If
        form_fields_per_document is not specified, a signature page will be affixed where all signers will be required
        to add their signature, signifying their agreement to all contained documents. Note that embedded signature
        requests can only be signed in embedded iFrames whereas normal signature requests can only be signed on Dropbox
        Sign.

        Args:
            client_id: Client id of the app you're using to create this embedded signature request. Used for security
                purposes.
            files: Use ``files[]`` to indicate the uploaded file(s) to send for signature. This endpoint requires either
                **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            signers: Add Signers to your Signature Request. This endpoint requires either **signers** or
                **grouped_signers**, but not both.
            grouped_signers: Add Grouped Signers to your Signature Request. This endpoint requires either **signers** or
                **grouped_signers**, but not both.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            allow_reassign: Allows signers to reassign their signature requests to other signers if set to ``true``.
                Defaults to ``false``. **NOTE:** Only available for Premium plan.
            attachments: A list describing the attachments
            cc_email_addresses: The email addresses that should be CCed.
            custom_fields: When used together with merge fields, ``custom_fields`` allows users to add pre-filled data
                to their signature requests. Pre-filled data can be used with "send-once" signature requests by adding
                merge fields with ``form_fields_per_document`` or `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ while passing values back with
                ``custom_fields`` together in one API call. For using pre-filled on repeatable signature requests, merge
                fields are added to templates in the Dropbox Sign UI or by calling `/template/create_embedded_draft
                </api/reference/operation/templateCreateEmbeddedDraft>`__ and then passing ``custom_fields`` on
                subsequent signature requests referencing that template.
            field_options: This allows the requester to specify field options for a signature request.
            form_field_groups: Group information for fields defined in ``form_fields_per_document``. String-indexed JSON
                array with ``group_label`` and ``requirement`` keys. ``form_fields_per_document`` must contain fields
                referencing a group defined in ``form_field_groups``.
            form_field_rules: Conditional Logic rules for fields defined in ``form_fields_per_document``.
            form_fields_per_document: The fields that should appear on the document, expressed as an array of objects.
                (For more details you can read about it here: `Using Form Fields per Document
                </docs/openapi/form-fields-per-document>`__.) **NOTE:** Fields like **text**, **dropdown**,
                **checkbox**, **radio**, and **hyperlink** have additional required and optional parameters. Check out
                the list of `additional parameters </api/reference/constants/#form-fields-per-document>`__ for these
                field types. * Text Field use ``SubFormFieldsPerDocumentText`` * Dropdown Field use
                ``SubFormFieldsPerDocumentDropdown`` * Hyperlink Field use ``SubFormFieldsPerDocumentHyperlink`` *
                Checkbox Field use ``SubFormFieldsPerDocumentCheckbox`` * Radio Field use
                ``SubFormFieldsPerDocumentRadio`` * Signature Field use ``SubFormFieldsPerDocumentSignature`` * Date
                Signed Field use ``SubFormFieldsPerDocumentDateSigned`` * Initials Field use
                ``SubFormFieldsPerDocumentInitials`` * Text Merge Field use ``SubFormFieldsPerDocumentTextMerge`` *
                Checkbox Merge Field use ``SubFormFieldsPerDocumentCheckboxMerge``
            hide_text_tags: Enables automatic Text Tag removal when set to true. **NOTE:** Removing text tags this way
                can cause unwanted clipping. We recommend leaving this setting on ``false`` and instead hiding your text
                tags using white text or a similar approach. See the `Text Tags Walkthrough
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ for more information.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            signing_options: This allows the requester to specify the types allowed for creating a signature and specify
                another signing options. **NOTE:** If ``signing_options`` are not defined in the request, the allowed
                types will default to those specified in the account settings. **NOTE:** If
                ``force_advanced_signature_details`` is set, allowed types has to be defined too.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request will not be legally binding if set to ``true``.
                Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            use_text_tags: Send with a value of ``true`` if you wish to enable `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ parsing in your document. Defaults
                to disabled, or ``false``.
            ignore_text_tags_extraction_errors: Sent with a value of ``true`` to ignore the validation errors from text
                tags extraction. Defaults to ``false``.
            populate_auto_fill_fields: Controls whether `auto fill fields
                <https://faq.hellosign.com/hc/en-us/articles/360051467511-Auto-Fill-Fields>`__ can automatically
                populate a signer's information during signing. **NOTE:** Keep your signer's information safe by
                ensuring that the _signer on your signature request is the intended party_ before using this feature.
            expires_at: When the signature request will expire. Unsigned signatures will be moved to the expired status,
                and no longer signable. See `Signature Request Expiration Date
                <https://developers.hellosign.com/docs/signature-request/expiration/>`__ for details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/signature_request/create_embedded"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(
                param[str]("client_id", client_id),
                file_part("files", files) if files is not None else None,
                param[list[str] | None]("file_urls", file_urls),
                param[list[SubSignatureRequestSigner | SubSignatureRequestSignerDict] | None]("signers", signers),
                param[list[SubSignatureRequestGroupedSigners | SubSignatureRequestGroupedSignersDict] | None](
                    "grouped_signers", grouped_signers
                ),
                param[bool | None]("allow_decline", allow_decline),
                param[bool | None]("allow_reassign", allow_reassign),
                param[list[SubAttachment | SubAttachmentDict] | None]("attachments", attachments),
                param[list[EmailStr] | None]("cc_email_addresses", cc_email_addresses),
                param[list[SubCustomField | SubCustomFieldDict] | None]("custom_fields", custom_fields),
                param[SubFieldOptions | SubFieldOptionsDict | None]("field_options", field_options),
                param[list[SubFormFieldGroup | SubFormFieldGroupDict] | None]("form_field_groups", form_field_groups),
                param[list[SubFormFieldRule | SubFormFieldRuleDict] | None]("form_field_rules", form_field_rules),
                param[list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None](
                    "form_fields_per_document", form_fields_per_document
                ),
                param[bool | None]("hide_text_tags", hide_text_tags),
                param[str | None]("message", message),
                param[dict[str, Any] | None]("metadata", metadata),
                param[SubSigningOptions | SubSigningOptionsDict | None]("signing_options", signing_options),
                param[str | None]("subject", subject),
                param[bool | None]("test_mode", test_mode),
                param[str | None]("title", title),
                param[bool | None]("use_text_tags", use_text_tags),
                param[bool | None]("ignore_text_tags_extraction_errors", ignore_text_tags_extraction_errors),
                param[bool | None]("populate_auto_fill_fields", populate_auto_fill_fields),
                param[int | None]("expires_at", expires_at),
            ),
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[SignatureRequestGetResponse],
            error_mapper=signature_request_create_embedded_error_mapper,
            request_options=request_options,
        )

    def signature_request_create_embedded_with_template(
        self,
        template_ids: list[str],
        client_id: str,
        signers: list[SubSignatureRequestTemplateSigner | SubSignatureRequestTemplateSignerDict],
        *,
        allow_decline: bool | None = False,
        ccs: list[SubCc | SubCcDict] | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        files: FileInput | None = None,
        file_urls: list[str] | None = None,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        signing_options: SubSigningOptions | SubSigningOptionsDict | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        populate_auto_fill_fields: bool | None = False,
        expires_at: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SignatureRequestGetResponse, SignatureRequestCreateEmbeddedWithTemplateErrorBody]:
        """Creates a new SignatureRequest based on the given Template(s) to be signed in an embedded iFrame. Note that
        embedded signature requests can only be signed in embedded iFrames whereas normal signature requests can only be
        signed on Dropbox Sign.

        Args:
            template_ids: Use ``template_ids`` to create a SignatureRequest from one or more templates, in the order in
                which the template will be used.
            client_id: Client id of the app you're using to create this embedded signature request. Used for security
                purposes.
            signers: Add Signers to your Templated-based Signature Request.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            ccs: Add CC email recipients. Required when a CC role exists for the Template.
            custom_fields: An array defining values and options for custom fields. Required when a custom field exists
                in the Template.
            files: Use ``files[]`` to indicate the uploaded file(s) to send for signature. This endpoint requires either
                **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            signing_options: This allows the requester to specify the types allowed for creating a signature and specify
                another signing options. **NOTE:** If ``signing_options`` are not defined in the request, the allowed
                types will default to those specified in the account settings. **NOTE:** If
                ``force_advanced_signature_details`` is set, allowed types has to be defined too.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request will not be legally binding if set to ``true``.
                Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            populate_auto_fill_fields: Controls whether `auto fill fields
                <https://faq.hellosign.com/hc/en-us/articles/360051467511-Auto-Fill-Fields>`__ can automatically
                populate a signer's information during signing. **NOTE:** Keep your signer's information safe by
                ensuring that the _signer on your signature request is the intended party_ before using this feature.
            expires_at: When the signature request will expire. Unsigned signatures will be moved to the expired status,
                and no longer signable. See `Signature Request Expiration Date
                <https://developers.hellosign.com/docs/signature-request/expiration/>`__ for details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/signature_request/create_embedded_with_template"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(
                param[list[str]]("template_ids", template_ids),
                param[str]("client_id", client_id),
                param[list[SubSignatureRequestTemplateSigner | SubSignatureRequestTemplateSignerDict]](
                    "signers", signers
                ),
                param[bool | None]("allow_decline", allow_decline),
                param[list[SubCc | SubCcDict] | None]("ccs", ccs),
                param[list[SubCustomField | SubCustomFieldDict] | None]("custom_fields", custom_fields),
                file_part("files", files) if files is not None else None,
                param[list[str] | None]("file_urls", file_urls),
                param[str | None]("message", message),
                param[dict[str, Any] | None]("metadata", metadata),
                param[SubSigningOptions | SubSigningOptionsDict | None]("signing_options", signing_options),
                param[str | None]("subject", subject),
                param[bool | None]("test_mode", test_mode),
                param[str | None]("title", title),
                param[bool | None]("populate_auto_fill_fields", populate_auto_fill_fields),
                param[int | None]("expires_at", expires_at),
            ),
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[SignatureRequestGetResponse],
            error_mapper=signature_request_create_embedded_with_template_error_mapper,
            request_options=request_options,
        )

    def signature_request_edit(
        self,
        signature_request_id: str,
        *,
        files: FileInput | None = None,
        file_urls: list[str] | None = None,
        signers: list[SubSignatureRequestSigner | SubSignatureRequestSignerDict] | None = None,
        grouped_signers: list[SubSignatureRequestGroupedSigners | SubSignatureRequestGroupedSignersDict] | None = None,
        allow_decline: bool | None = False,
        allow_reassign: bool | None = False,
        attachments: list[SubAttachment | SubAttachmentDict] | None = None,
        cc_email_addresses: list[EmailStr] | None = None,
        client_id: str | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        field_options: SubFieldOptions | SubFieldOptionsDict | None = None,
        form_field_groups: list[SubFormFieldGroup | SubFormFieldGroupDict] | None = None,
        form_field_rules: list[SubFormFieldRule | SubFormFieldRuleDict] | None = None,
        form_fields_per_document: list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None = None,
        hide_text_tags: bool | None = False,
        is_eid: bool | None = False,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        signing_options: SubSigningOptions | SubSigningOptionsDict | None = None,
        signing_redirect_url: str | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        use_text_tags: bool | None = False,
        ignore_text_tags_extraction_errors: bool | None = False,
        expires_at: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SignatureRequestGetResponse, SignatureRequestEditErrorBody]:
        """Edits and sends a SignatureRequest with the submitted documents. If ``form_fields_per_document`` is not
        specified, a signature page will be affixed where all signers will be required to add their signature,
        signifying their agreement to all contained documents.

        **NOTE:** Edit and resend *will* deduct your signature request quota.

        Args:
            signature_request_id: The id of the SignatureRequest to edit.
            files: Use ``files[]`` to indicate the uploaded file(s) to send for signature. This endpoint requires either
                **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            signers: Add Signers to your Signature Request. This endpoint requires either **signers** or
                **grouped_signers**, but not both.
            grouped_signers: Add Grouped Signers to your Signature Request. This endpoint requires either **signers** or
                **grouped_signers**, but not both.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            allow_reassign: Allows signers to reassign their signature requests to other signers if set to ``true``.
                Defaults to ``false``. **NOTE:** Only available for Premium plan and higher.
            attachments: A list describing the attachments
            cc_email_addresses: The email addresses that should be CCed.
            client_id: The client id of the API App you want to associate with this request. Used to apply the branding
                and callback url defined for the app.
            custom_fields: When used together with merge fields, ``custom_fields`` allows users to add pre-filled data
                to their signature requests. Pre-filled data can be used with "send-once" signature requests by adding
                merge fields with ``form_fields_per_document`` or `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ while passing values back with
                ``custom_fields`` together in one API call. For using pre-filled on repeatable signature requests, merge
                fields are added to templates in the Dropbox Sign UI or by calling `/template/create_embedded_draft
                </api/reference/operation/templateCreateEmbeddedDraft>`__ and then passing ``custom_fields`` on
                subsequent signature requests referencing that template.
            field_options: This allows the requester to specify field options for a signature request.
            form_field_groups: Group information for fields defined in ``form_fields_per_document``. String-indexed JSON
                array with ``group_label`` and ``requirement`` keys. ``form_fields_per_document`` must contain fields
                referencing a group defined in ``form_field_groups``.
            form_field_rules: Conditional Logic rules for fields defined in ``form_fields_per_document``.
            form_fields_per_document: The fields that should appear on the document, expressed as an array of objects.
                (For more details you can read about it here: `Using Form Fields per Document
                </docs/openapi/form-fields-per-document>`__.) **NOTE:** Fields like **text**, **dropdown**,
                **checkbox**, **radio**, and **hyperlink** have additional required and optional parameters. Check out
                the list of `additional parameters </api/reference/constants/#form-fields-per-document>`__ for these
                field types. * Text Field use ``SubFormFieldsPerDocumentText`` * Dropdown Field use
                ``SubFormFieldsPerDocumentDropdown`` * Hyperlink Field use ``SubFormFieldsPerDocumentHyperlink`` *
                Checkbox Field use ``SubFormFieldsPerDocumentCheckbox`` * Radio Field use
                ``SubFormFieldsPerDocumentRadio`` * Signature Field use ``SubFormFieldsPerDocumentSignature`` * Date
                Signed Field use ``SubFormFieldsPerDocumentDateSigned`` * Initials Field use
                ``SubFormFieldsPerDocumentInitials`` * Text Merge Field use ``SubFormFieldsPerDocumentTextMerge`` *
                Checkbox Merge Field use ``SubFormFieldsPerDocumentCheckboxMerge``
            hide_text_tags: Enables automatic Text Tag removal when set to true. **NOTE:** Removing text tags this way
                can cause unwanted clipping. We recommend leaving this setting on ``false`` and instead hiding your text
                tags using white text or a similar approach. See the `Text Tags Walkthrough
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ for more information.
            is_eid: Send with a value of ``true`` if you wish to enable `electronic identification (eID)
                <https://www.hellosign.com/features/electronic-id>`__, which requires the signer to verify their
                identity with an eID provider to sign a document.<br> **NOTE:** You need the eID add-on to use this
                feature. Please `contact sales <https://sign.dropbox.com/form/contact-sales>`__ for more information.
                Cannot be used in ``test_mode``. Only works on requests with one signer.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            signing_options: This allows the requester to specify the types allowed for creating a signature and specify
                another signing options. **NOTE:** If ``signing_options`` are not defined in the request, the allowed
                types will default to those specified in the account settings. **NOTE:** If
                ``force_advanced_signature_details`` is set, allowed types has to be defined too.
            signing_redirect_url: The URL you want signers redirected to after they successfully sign.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request will not be legally binding if set to ``true``.
                Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            use_text_tags: Send with a value of ``true`` if you wish to enable `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ parsing in your document. Defaults
                to disabled, or ``false``.
            ignore_text_tags_extraction_errors: Sent with a value of ``true`` to ignore the validation errors from text
                tags extraction. Defaults to ``false``.
            expires_at: When the signature request will expire. Unsigned signatures will be moved to the expired status,
                and no longer signable. See `Signature Request Expiration Date
                <https://developers.hellosign.com/docs/signature-request/expiration/>`__ for details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/signature_request/edit/{signature_request_id}"),
            path_params=[param[str]("signature_request_id", signature_request_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(
                file_part("files", files) if files is not None else None,
                param[list[str] | None]("file_urls", file_urls),
                param[list[SubSignatureRequestSigner | SubSignatureRequestSignerDict] | None]("signers", signers),
                param[list[SubSignatureRequestGroupedSigners | SubSignatureRequestGroupedSignersDict] | None](
                    "grouped_signers", grouped_signers
                ),
                param[bool | None]("allow_decline", allow_decline),
                param[bool | None]("allow_reassign", allow_reassign),
                param[list[SubAttachment | SubAttachmentDict] | None]("attachments", attachments),
                param[list[EmailStr] | None]("cc_email_addresses", cc_email_addresses),
                param[str | None]("client_id", client_id),
                param[list[SubCustomField | SubCustomFieldDict] | None]("custom_fields", custom_fields),
                param[SubFieldOptions | SubFieldOptionsDict | None]("field_options", field_options),
                param[list[SubFormFieldGroup | SubFormFieldGroupDict] | None]("form_field_groups", form_field_groups),
                param[list[SubFormFieldRule | SubFormFieldRuleDict] | None]("form_field_rules", form_field_rules),
                param[list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None](
                    "form_fields_per_document", form_fields_per_document
                ),
                param[bool | None]("hide_text_tags", hide_text_tags),
                param[bool | None]("is_eid", is_eid),
                param[str | None]("message", message),
                param[dict[str, Any] | None]("metadata", metadata),
                param[SubSigningOptions | SubSigningOptionsDict | None]("signing_options", signing_options),
                param[str | None]("signing_redirect_url", signing_redirect_url),
                param[str | None]("subject", subject),
                param[bool | None]("test_mode", test_mode),
                param[str | None]("title", title),
                param[bool | None]("use_text_tags", use_text_tags),
                param[bool | None]("ignore_text_tags_extraction_errors", ignore_text_tags_extraction_errors),
                param[int | None]("expires_at", expires_at),
            ),
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[SignatureRequestGetResponse],
            error_mapper=signature_request_edit_error_mapper,
            request_options=request_options,
        )

    def signature_request_edit_embedded(
        self,
        signature_request_id: str,
        client_id: str,
        *,
        files: FileInput | None = None,
        file_urls: list[str] | None = None,
        signers: list[SubSignatureRequestSigner | SubSignatureRequestSignerDict] | None = None,
        grouped_signers: list[SubSignatureRequestGroupedSigners | SubSignatureRequestGroupedSignersDict] | None = None,
        allow_decline: bool | None = False,
        allow_reassign: bool | None = False,
        attachments: list[SubAttachment | SubAttachmentDict] | None = None,
        cc_email_addresses: list[EmailStr] | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        field_options: SubFieldOptions | SubFieldOptionsDict | None = None,
        form_field_groups: list[SubFormFieldGroup | SubFormFieldGroupDict] | None = None,
        form_field_rules: list[SubFormFieldRule | SubFormFieldRuleDict] | None = None,
        form_fields_per_document: list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None = None,
        hide_text_tags: bool | None = False,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        signing_options: SubSigningOptions | SubSigningOptionsDict | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        use_text_tags: bool | None = False,
        ignore_text_tags_extraction_errors: bool | None = False,
        populate_auto_fill_fields: bool | None = False,
        expires_at: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SignatureRequestGetResponse, SignatureRequestEditEmbeddedErrorBody]:
        """Edits a SignatureRequest with the submitted documents to be signed in an embedded iFrame. If
        form_fields_per_document is not specified, a signature page will be affixed where all signers will be required
        to add their signature, signifying their agreement to all contained documents. Note that embedded signature
        requests can only be signed in embedded iFrames whereas normal signature requests can only be signed on Dropbox
        Sign.

        **NOTE:** Edit and resend *will* deduct your signature request quota.

        Args:
            signature_request_id: The id of the SignatureRequest to edit.
            client_id: Client id of the app you're using to create this embedded signature request. Used for security
                purposes.
            files: Use ``files[]`` to indicate the uploaded file(s) to send for signature. This endpoint requires either
                **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            signers: Add Signers to your Signature Request. This endpoint requires either **signers** or
                **grouped_signers**, but not both.
            grouped_signers: Add Grouped Signers to your Signature Request. This endpoint requires either **signers** or
                **grouped_signers**, but not both.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            allow_reassign: Allows signers to reassign their signature requests to other signers if set to ``true``.
                Defaults to ``false``. **NOTE:** Only available for Premium plan.
            attachments: A list describing the attachments
            cc_email_addresses: The email addresses that should be CCed.
            custom_fields: When used together with merge fields, ``custom_fields`` allows users to add pre-filled data
                to their signature requests. Pre-filled data can be used with "send-once" signature requests by adding
                merge fields with ``form_fields_per_document`` or `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ while passing values back with
                ``custom_fields`` together in one API call. For using pre-filled on repeatable signature requests, merge
                fields are added to templates in the Dropbox Sign UI or by calling `/template/create_embedded_draft
                </api/reference/operation/templateCreateEmbeddedDraft>`__ and then passing ``custom_fields`` on
                subsequent signature requests referencing that template.
            field_options: This allows the requester to specify field options for a signature request.
            form_field_groups: Group information for fields defined in ``form_fields_per_document``. String-indexed JSON
                array with ``group_label`` and ``requirement`` keys. ``form_fields_per_document`` must contain fields
                referencing a group defined in ``form_field_groups``.
            form_field_rules: Conditional Logic rules for fields defined in ``form_fields_per_document``.
            form_fields_per_document: The fields that should appear on the document, expressed as an array of objects.
                (For more details you can read about it here: `Using Form Fields per Document
                </docs/openapi/form-fields-per-document>`__.) **NOTE:** Fields like **text**, **dropdown**,
                **checkbox**, **radio**, and **hyperlink** have additional required and optional parameters. Check out
                the list of `additional parameters </api/reference/constants/#form-fields-per-document>`__ for these
                field types. * Text Field use ``SubFormFieldsPerDocumentText`` * Dropdown Field use
                ``SubFormFieldsPerDocumentDropdown`` * Hyperlink Field use ``SubFormFieldsPerDocumentHyperlink`` *
                Checkbox Field use ``SubFormFieldsPerDocumentCheckbox`` * Radio Field use
                ``SubFormFieldsPerDocumentRadio`` * Signature Field use ``SubFormFieldsPerDocumentSignature`` * Date
                Signed Field use ``SubFormFieldsPerDocumentDateSigned`` * Initials Field use
                ``SubFormFieldsPerDocumentInitials`` * Text Merge Field use ``SubFormFieldsPerDocumentTextMerge`` *
                Checkbox Merge Field use ``SubFormFieldsPerDocumentCheckboxMerge``
            hide_text_tags: Enables automatic Text Tag removal when set to true. **NOTE:** Removing text tags this way
                can cause unwanted clipping. We recommend leaving this setting on ``false`` and instead hiding your text
                tags using white text or a similar approach. See the `Text Tags Walkthrough
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ for more information.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            signing_options: This allows the requester to specify the types allowed for creating a signature and specify
                another signing options. **NOTE:** If ``signing_options`` are not defined in the request, the allowed
                types will default to those specified in the account settings. **NOTE:** If
                ``force_advanced_signature_details`` is set, allowed types has to be defined too.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request will not be legally binding if set to ``true``.
                Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            use_text_tags: Send with a value of ``true`` if you wish to enable `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ parsing in your document. Defaults
                to disabled, or ``false``.
            ignore_text_tags_extraction_errors: Sent with a value of ``true`` to ignore the validation errors from text
                tags extraction. Defaults to ``false``.
            populate_auto_fill_fields: Controls whether `auto fill fields
                <https://faq.hellosign.com/hc/en-us/articles/360051467511-Auto-Fill-Fields>`__ can automatically
                populate a signer's information during signing. **NOTE:** Keep your signer's information safe by
                ensuring that the _signer on your signature request is the intended party_ before using this feature.
            expires_at: When the signature request will expire. Unsigned signatures will be moved to the expired status,
                and no longer signable. See `Signature Request Expiration Date
                <https://developers.hellosign.com/docs/signature-request/expiration/>`__ for details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/signature_request/edit_embedded/{signature_request_id}"),
            path_params=[param[str]("signature_request_id", signature_request_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(
                param[str]("client_id", client_id),
                file_part("files", files) if files is not None else None,
                param[list[str] | None]("file_urls", file_urls),
                param[list[SubSignatureRequestSigner | SubSignatureRequestSignerDict] | None]("signers", signers),
                param[list[SubSignatureRequestGroupedSigners | SubSignatureRequestGroupedSignersDict] | None](
                    "grouped_signers", grouped_signers
                ),
                param[bool | None]("allow_decline", allow_decline),
                param[bool | None]("allow_reassign", allow_reassign),
                param[list[SubAttachment | SubAttachmentDict] | None]("attachments", attachments),
                param[list[EmailStr] | None]("cc_email_addresses", cc_email_addresses),
                param[list[SubCustomField | SubCustomFieldDict] | None]("custom_fields", custom_fields),
                param[SubFieldOptions | SubFieldOptionsDict | None]("field_options", field_options),
                param[list[SubFormFieldGroup | SubFormFieldGroupDict] | None]("form_field_groups", form_field_groups),
                param[list[SubFormFieldRule | SubFormFieldRuleDict] | None]("form_field_rules", form_field_rules),
                param[list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None](
                    "form_fields_per_document", form_fields_per_document
                ),
                param[bool | None]("hide_text_tags", hide_text_tags),
                param[str | None]("message", message),
                param[dict[str, Any] | None]("metadata", metadata),
                param[SubSigningOptions | SubSigningOptionsDict | None]("signing_options", signing_options),
                param[str | None]("subject", subject),
                param[bool | None]("test_mode", test_mode),
                param[str | None]("title", title),
                param[bool | None]("use_text_tags", use_text_tags),
                param[bool | None]("ignore_text_tags_extraction_errors", ignore_text_tags_extraction_errors),
                param[bool | None]("populate_auto_fill_fields", populate_auto_fill_fields),
                param[int | None]("expires_at", expires_at),
            ),
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[SignatureRequestGetResponse],
            error_mapper=signature_request_edit_embedded_error_mapper,
            request_options=request_options,
        )

    def signature_request_edit_embedded_with_template(
        self,
        signature_request_id: str,
        template_ids: list[str],
        client_id: str,
        signers: list[SubSignatureRequestTemplateSigner | SubSignatureRequestTemplateSignerDict],
        *,
        allow_decline: bool | None = False,
        ccs: list[SubCc | SubCcDict] | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        files: FileInput | None = None,
        file_urls: list[str] | None = None,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        signing_options: SubSigningOptions | SubSigningOptionsDict | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        populate_auto_fill_fields: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SignatureRequestGetResponse, SignatureRequestEditEmbeddedWithTemplateErrorBody]:
        """Edits a SignatureRequest based on the given Template(s) to be signed in an embedded iFrame. Note that
        embedded signature requests can only be signed in embedded iFrames whereas normal signature requests can only be
        signed on Dropbox Sign.

        **NOTE:** Edit and resend *will* deduct your signature request quota.

        Args:
            signature_request_id: The id of the SignatureRequest to edit.
            template_ids: Use ``template_ids`` to create a SignatureRequest from one or more templates, in the order in
                which the template will be used.
            client_id: Client id of the app you're using to create this embedded signature request. Used for security
                purposes.
            signers: Add Signers to your Templated-based Signature Request.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            ccs: Add CC email recipients. Required when a CC role exists for the Template.
            custom_fields: An array defining values and options for custom fields. Required when a custom field exists
                in the Template.
            files: Use ``files[]`` to indicate the uploaded file(s) to send for signature. This endpoint requires either
                **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            signing_options: This allows the requester to specify the types allowed for creating a signature and specify
                another signing options. **NOTE:** If ``signing_options`` are not defined in the request, the allowed
                types will default to those specified in the account settings. **NOTE:** If
                ``force_advanced_signature_details`` is set, allowed types has to be defined too.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request will not be legally binding if set to ``true``.
                Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            populate_auto_fill_fields: Controls whether `auto fill fields
                <https://faq.hellosign.com/hc/en-us/articles/360051467511-Auto-Fill-Fields>`__ can automatically
                populate a signer's information during signing. **NOTE:** Keep your signer's information safe by
                ensuring that the _signer on your signature request is the intended party_ before using this feature.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/signature_request/edit_embedded_with_template/{signature_request_id}"),
            path_params=[param[str]("signature_request_id", signature_request_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(
                param[list[str]]("template_ids", template_ids),
                param[str]("client_id", client_id),
                param[list[SubSignatureRequestTemplateSigner | SubSignatureRequestTemplateSignerDict]](
                    "signers", signers
                ),
                param[bool | None]("allow_decline", allow_decline),
                param[list[SubCc | SubCcDict] | None]("ccs", ccs),
                param[list[SubCustomField | SubCustomFieldDict] | None]("custom_fields", custom_fields),
                file_part("files", files) if files is not None else None,
                param[list[str] | None]("file_urls", file_urls),
                param[str | None]("message", message),
                param[dict[str, Any] | None]("metadata", metadata),
                param[SubSigningOptions | SubSigningOptionsDict | None]("signing_options", signing_options),
                param[str | None]("subject", subject),
                param[bool | None]("test_mode", test_mode),
                param[str | None]("title", title),
                param[bool | None]("populate_auto_fill_fields", populate_auto_fill_fields),
            ),
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[SignatureRequestGetResponse],
            error_mapper=signature_request_edit_embedded_with_template_error_mapper,
            request_options=request_options,
        )

    def signature_request_edit_with_template(
        self,
        signature_request_id: str,
        template_ids: list[str],
        signers: list[SubSignatureRequestTemplateSigner | SubSignatureRequestTemplateSignerDict],
        *,
        allow_decline: bool | None = False,
        ccs: list[SubCc | SubCcDict] | None = None,
        client_id: str | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        files: FileInput | None = None,
        file_urls: list[str] | None = None,
        is_eid: bool | None = False,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        signing_options: SubSigningOptions | SubSigningOptionsDict | None = None,
        signing_redirect_url: str | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SignatureRequestGetResponse, SignatureRequestEditWithTemplateErrorBody]:
        """Edits and sends a SignatureRequest based off of the Template(s) specified with the template_ids parameter.

        **NOTE:** Edit and resend *will* deduct your signature request quota.

        Args:
            signature_request_id: The id of the SignatureRequest to edit.
            template_ids: Use ``template_ids`` to create a SignatureRequest from one or more templates, in the order in
                which the template will be used.
            signers: Add Signers to your Templated-based Signature Request.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            ccs: Add CC email recipients. Required when a CC role exists for the Template.
            client_id: Client id of the app to associate with the signature request. Used to apply the branding and
                callback url defined for the app.
            custom_fields: An array defining values and options for custom fields. Required when a custom field exists
                in the Template.
            files: Use ``files[]`` to indicate the uploaded file(s) to send for signature. This endpoint requires either
                **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            is_eid: Send with a value of ``true`` if you wish to enable `electronic identification (eID)
                <https://www.hellosign.com/features/electronic-id>`__, which requires the signer to verify their
                identity with an eID provider to sign a document.<br> **NOTE:** You need the eID add-on to use this
                feature. Please `contact sales <https://sign.dropbox.com/form/contact-sales>`__ for more information.
                Cannot be used in ``test_mode``. Only works on requests with one signer.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            signing_options: This allows the requester to specify the types allowed for creating a signature and specify
                another signing options. **NOTE:** If ``signing_options`` are not defined in the request, the allowed
                types will default to those specified in the account settings. **NOTE:** If
                ``force_advanced_signature_details`` is set, allowed types has to be defined too.
            signing_redirect_url: The URL you want signers redirected to after they successfully sign.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request will not be legally binding if set to ``true``.
                Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/signature_request/edit_with_template/{signature_request_id}"),
            path_params=[param[str]("signature_request_id", signature_request_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(
                param[list[str]]("template_ids", template_ids),
                param[list[SubSignatureRequestTemplateSigner | SubSignatureRequestTemplateSignerDict]](
                    "signers", signers
                ),
                param[bool | None]("allow_decline", allow_decline),
                param[list[SubCc | SubCcDict] | None]("ccs", ccs),
                param[str | None]("client_id", client_id),
                param[list[SubCustomField | SubCustomFieldDict] | None]("custom_fields", custom_fields),
                file_part("files", files) if files is not None else None,
                param[list[str] | None]("file_urls", file_urls),
                param[bool | None]("is_eid", is_eid),
                param[str | None]("message", message),
                param[dict[str, Any] | None]("metadata", metadata),
                param[SubSigningOptions | SubSigningOptionsDict | None]("signing_options", signing_options),
                param[str | None]("signing_redirect_url", signing_redirect_url),
                param[str | None]("subject", subject),
                param[bool | None]("test_mode", test_mode),
                param[str | None]("title", title),
            ),
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[SignatureRequestGetResponse],
            error_mapper=signature_request_edit_with_template_error_mapper,
            request_options=request_options,
        )

    def signature_request_files(
        self,
        signature_request_id: str,
        *,
        file_type: FileTypeOrStr | None = FileType.PDF,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, SignatureRequestFilesErrorBody]:
        """Obtain a copy of the current documents specified by the ``signature_request_id`` parameter. Returns a PDF or
        ZIP file.

        If the files are currently being prepared, a status code of ``409`` will be returned instead.

        Args:
            signature_request_id: The id of the SignatureRequest to retrieve.
            file_type: Set to ``pdf`` for a single merged document or ``zip`` for a collection of individual documents.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/signature_request/files/{signature_request_id}"),
            path_params=[param[str]("signature_request_id", signature_request_id)],
            query_params=[param[FileTypeOrStr | None]("file_type", file_type)],
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=empty_response,
            error_mapper=signature_request_files_error_mapper,
            request_options=request_options,
        )

    def signature_request_files_as_data_uri(
        self, signature_request_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FileResponseDataUri, SignatureRequestFilesAsDataUriErrorBody]:
        """Obtain a copy of the current documents specified by the ``signature_request_id`` parameter. Returns a JSON
        object with a ``data_uri`` representing the base64 encoded file (PDFs only).

        If the files are currently being prepared, a status code of ``409`` will be returned instead.

        Args:
            signature_request_id: The id of the SignatureRequest to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/signature_request/files_as_data_uri/{signature_request_id}"),
            path_params=[param[str]("signature_request_id", signature_request_id)],
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[FileResponseDataUri],
            error_mapper=signature_request_files_as_data_uri_error_mapper,
            request_options=request_options,
        )

    def signature_request_files_as_file_url(
        self,
        signature_request_id: str,
        *,
        force_download: int | None = 1,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FileResponseModel, SignatureRequestFilesAsFileUrlErrorBody]:
        """Obtain a copy of the current documents specified by the ``signature_request_id`` parameter. Returns a JSON
        object with a url to the file (PDFs only).

        If the files are currently being prepared, a status code of ``409`` will be returned instead.

        Args:
            signature_request_id: The id of the SignatureRequest to retrieve.
            force_download: By default when opening the ``file_url`` a browser will download the PDF and save it
                locally. When set to ``0`` the PDF file will be displayed in the browser.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/signature_request/files_as_file_url/{signature_request_id}"),
            path_params=[param[str]("signature_request_id", signature_request_id)],
            query_params=[param[int | None]("force_download", force_download)],
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[FileResponseModel],
            error_mapper=signature_request_files_as_file_url_error_mapper,
            request_options=request_options,
        )

    def signature_request_get(
        self, signature_request_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SignatureRequestGetResponse, SignatureRequestGetErrorBody]:
        """Returns the status of the SignatureRequest specified by the ``signature_request_id`` parameter.

        Args:
            signature_request_id: The id of the SignatureRequest to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/signature_request/{signature_request_id}"),
            path_params=[param[str]("signature_request_id", signature_request_id)],
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[SignatureRequestGetResponse],
            error_mapper=signature_request_get_error_mapper,
            request_options=request_options,
        )

    def signature_request_list(
        self,
        *,
        account_id: str | None = None,
        page: int | None = 1,
        page_size: int | None = 20,
        query: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SignatureRequestListResponse, SignatureRequestListErrorBody]:
        """Returns a list of SignatureRequests that you can access. This includes SignatureRequests you have sent as
        well as received, but not ones that you have been CCed on.

        Take a look at our `search guide </api/reference/search/>`__ to learn more about querying signature requests.

        Args:
            account_id: Which account to return SignatureRequests for. Must be a team member. Use ``all`` to indicate
                all team members. Defaults to your account.
            page: Which page number of the SignatureRequest List to return. Defaults to ``1``.
            page_size: Number of objects to be returned per page. Must be between ``1`` and ``100``. Default is ``20``.
            query: String that includes search terms and/or fields to be used to filter the SignatureRequest objects.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/signature_request/list"),
            query_params=[
                param[str | None]("account_id", account_id),
                param[int | None]("page", page),
                param[int | None]("page_size", page_size),
                param[str | None]("query", query),
            ],
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[SignatureRequestListResponse],
            error_mapper=signature_request_list_error_mapper,
            request_options=request_options,
        )

    def signature_request_release_hold(
        self, signature_request_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SignatureRequestGetResponse, SignatureRequestReleaseHoldErrorBody]:
        """Releases a held SignatureRequest that was claimed and prepared from an `UnclaimedDraft
        </api/reference/tag/Unclaimed-Draft>`__. The owner of the Draft must indicate at Draft creation that the
        SignatureRequest created from the Draft should be held. Releasing the SignatureRequest will send requests to all
        signers.

        Args:
            signature_request_id: The id of the SignatureRequest to release.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/signature_request/release_hold/{signature_request_id}"),
            path_params=[param[str]("signature_request_id", signature_request_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[SignatureRequestGetResponse],
            error_mapper=signature_request_release_hold_error_mapper,
            request_options=request_options,
        )

    def signature_request_remind(
        self,
        signature_request_id: str,
        body: SignatureRequestRemindRequest | SignatureRequestRemindRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SignatureRequestGetResponse, SignatureRequestRemindErrorBody]:
        """Sends an email to the signer reminding them to sign the signature request. You cannot send a reminder within
        1 hour of the last reminder that was sent. This includes manual AND automatic reminders.

        **NOTE:** This action can **not** be used with embedded signature requests.

        Args:
            signature_request_id: The id of the SignatureRequest to send a reminder for.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/signature_request/remind/{signature_request_id}"),
            path_params=[param[str]("signature_request_id", signature_request_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SignatureRequestRemindRequest | SignatureRequestRemindRequestDict](body),
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[SignatureRequestGetResponse],
            error_mapper=signature_request_remind_error_mapper,
            request_options=request_options,
        )

    def signature_request_remove(
        self, signature_request_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, SignatureRequestRemoveErrorBody]:
        """Removes your access to a completed signature request. This action is **not reversible**.

        The signature request must be fully executed by all parties (signed or declined to sign). Other parties will
        continue to maintain access to the completed signature request document(s).

        Unlike /signature_request/cancel, this endpoint is synchronous and your access will be immediately removed. Upon
        successful removal, this endpoint will return a 200 OK response.

        Args:
            signature_request_id: The id of the SignatureRequest to remove.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/signature_request/remove/{signature_request_id}"),
            path_params=[param[str]("signature_request_id", signature_request_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[Any],
            error_mapper=signature_request_remove_error_mapper,
            request_options=request_options,
        )

    def signature_request_send(
        self,
        *,
        files: FileInput | None = None,
        file_urls: list[str] | None = None,
        signers: list[SubSignatureRequestSigner | SubSignatureRequestSignerDict] | None = None,
        grouped_signers: list[SubSignatureRequestGroupedSigners | SubSignatureRequestGroupedSignersDict] | None = None,
        allow_decline: bool | None = False,
        allow_reassign: bool | None = False,
        attachments: list[SubAttachment | SubAttachmentDict] | None = None,
        cc_email_addresses: list[EmailStr] | None = None,
        client_id: str | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        field_options: SubFieldOptions | SubFieldOptionsDict | None = None,
        form_field_groups: list[SubFormFieldGroup | SubFormFieldGroupDict] | None = None,
        form_field_rules: list[SubFormFieldRule | SubFormFieldRuleDict] | None = None,
        form_fields_per_document: list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None = None,
        hide_text_tags: bool | None = False,
        is_eid: bool | None = False,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        signing_options: SubSigningOptions | SubSigningOptionsDict | None = None,
        signing_redirect_url: str | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        use_text_tags: bool | None = False,
        ignore_text_tags_extraction_errors: bool | None = False,
        expires_at: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SignatureRequestGetResponse, SignatureRequestSendErrorBody]:
        """Creates and sends a new SignatureRequest with the submitted documents. If ``form_fields_per_document`` is not
        specified, a signature page will be affixed where all signers will be required to add their signature,
        signifying their agreement to all contained documents.

        Args:
            files: Use ``files[]`` to indicate the uploaded file(s) to send for signature. This endpoint requires either
                **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            signers: Add Signers to your Signature Request. This endpoint requires either **signers** or
                **grouped_signers**, but not both.
            grouped_signers: Add Grouped Signers to your Signature Request. This endpoint requires either **signers** or
                **grouped_signers**, but not both.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            allow_reassign: Allows signers to reassign their signature requests to other signers if set to ``true``.
                Defaults to ``false``. **NOTE:** Only available for Premium plan and higher.
            attachments: A list describing the attachments
            cc_email_addresses: The email addresses that should be CCed.
            client_id: The client id of the API App you want to associate with this request. Used to apply the branding
                and callback url defined for the app.
            custom_fields: When used together with merge fields, ``custom_fields`` allows users to add pre-filled data
                to their signature requests. Pre-filled data can be used with "send-once" signature requests by adding
                merge fields with ``form_fields_per_document`` or `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ while passing values back with
                ``custom_fields`` together in one API call. For using pre-filled on repeatable signature requests, merge
                fields are added to templates in the Dropbox Sign UI or by calling `/template/create_embedded_draft
                </api/reference/operation/templateCreateEmbeddedDraft>`__ and then passing ``custom_fields`` on
                subsequent signature requests referencing that template.
            field_options: This allows the requester to specify field options for a signature request.
            form_field_groups: Group information for fields defined in ``form_fields_per_document``. String-indexed JSON
                array with ``group_label`` and ``requirement`` keys. ``form_fields_per_document`` must contain fields
                referencing a group defined in ``form_field_groups``.
            form_field_rules: Conditional Logic rules for fields defined in ``form_fields_per_document``.
            form_fields_per_document: The fields that should appear on the document, expressed as an array of objects.
                (For more details you can read about it here: `Using Form Fields per Document
                </docs/openapi/form-fields-per-document>`__.) **NOTE:** Fields like **text**, **dropdown**,
                **checkbox**, **radio**, and **hyperlink** have additional required and optional parameters. Check out
                the list of `additional parameters </api/reference/constants/#form-fields-per-document>`__ for these
                field types. * Text Field use ``SubFormFieldsPerDocumentText`` * Dropdown Field use
                ``SubFormFieldsPerDocumentDropdown`` * Hyperlink Field use ``SubFormFieldsPerDocumentHyperlink`` *
                Checkbox Field use ``SubFormFieldsPerDocumentCheckbox`` * Radio Field use
                ``SubFormFieldsPerDocumentRadio`` * Signature Field use ``SubFormFieldsPerDocumentSignature`` * Date
                Signed Field use ``SubFormFieldsPerDocumentDateSigned`` * Initials Field use
                ``SubFormFieldsPerDocumentInitials`` * Text Merge Field use ``SubFormFieldsPerDocumentTextMerge`` *
                Checkbox Merge Field use ``SubFormFieldsPerDocumentCheckboxMerge``
            hide_text_tags: Enables automatic Text Tag removal when set to true. **NOTE:** Removing text tags this way
                can cause unwanted clipping. We recommend leaving this setting on ``false`` and instead hiding your text
                tags using white text or a similar approach. See the `Text Tags Walkthrough
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ for more information.
            is_eid: Send with a value of ``true`` if you wish to enable `electronic identification (eID)
                <https://www.hellosign.com/features/electronic-id>`__, which requires the signer to verify their
                identity with an eID provider to sign a document.<br> **NOTE:** You need the eID add-on to use this
                feature. Please `contact sales <https://sign.dropbox.com/form/contact-sales>`__ for more information.
                Cannot be used in ``test_mode``. Only works on requests with one signer.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            signing_options: This allows the requester to specify the types allowed for creating a signature and specify
                another signing options. **NOTE:** If ``signing_options`` are not defined in the request, the allowed
                types will default to those specified in the account settings. **NOTE:** If
                ``force_advanced_signature_details`` is set, allowed types has to be defined too.
            signing_redirect_url: The URL you want signers redirected to after they successfully sign.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request will not be legally binding if set to ``true``.
                Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            use_text_tags: Send with a value of ``true`` if you wish to enable `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ parsing in your document. Defaults
                to disabled, or ``false``.
            ignore_text_tags_extraction_errors: Sent with a value of ``true`` to ignore the validation errors from text
                tags extraction. Defaults to ``false``.
            expires_at: When the signature request will expire. Unsigned signatures will be moved to the expired status,
                and no longer signable. See `Signature Request Expiration Date
                <https://developers.hellosign.com/docs/signature-request/expiration/>`__ for details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/signature_request/send"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(
                file_part("files", files) if files is not None else None,
                param[list[str] | None]("file_urls", file_urls),
                param[list[SubSignatureRequestSigner | SubSignatureRequestSignerDict] | None]("signers", signers),
                param[list[SubSignatureRequestGroupedSigners | SubSignatureRequestGroupedSignersDict] | None](
                    "grouped_signers", grouped_signers
                ),
                param[bool | None]("allow_decline", allow_decline),
                param[bool | None]("allow_reassign", allow_reassign),
                param[list[SubAttachment | SubAttachmentDict] | None]("attachments", attachments),
                param[list[EmailStr] | None]("cc_email_addresses", cc_email_addresses),
                param[str | None]("client_id", client_id),
                param[list[SubCustomField | SubCustomFieldDict] | None]("custom_fields", custom_fields),
                param[SubFieldOptions | SubFieldOptionsDict | None]("field_options", field_options),
                param[list[SubFormFieldGroup | SubFormFieldGroupDict] | None]("form_field_groups", form_field_groups),
                param[list[SubFormFieldRule | SubFormFieldRuleDict] | None]("form_field_rules", form_field_rules),
                param[list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None](
                    "form_fields_per_document", form_fields_per_document
                ),
                param[bool | None]("hide_text_tags", hide_text_tags),
                param[bool | None]("is_eid", is_eid),
                param[str | None]("message", message),
                param[dict[str, Any] | None]("metadata", metadata),
                param[SubSigningOptions | SubSigningOptionsDict | None]("signing_options", signing_options),
                param[str | None]("signing_redirect_url", signing_redirect_url),
                param[str | None]("subject", subject),
                param[bool | None]("test_mode", test_mode),
                param[str | None]("title", title),
                param[bool | None]("use_text_tags", use_text_tags),
                param[bool | None]("ignore_text_tags_extraction_errors", ignore_text_tags_extraction_errors),
                param[int | None]("expires_at", expires_at),
            ),
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[SignatureRequestGetResponse],
            error_mapper=signature_request_send_error_mapper,
            request_options=request_options,
        )

    def signature_request_send_with_template(
        self,
        template_ids: list[str],
        signers: list[SubSignatureRequestTemplateSigner | SubSignatureRequestTemplateSignerDict],
        *,
        allow_decline: bool | None = False,
        ccs: list[SubCc | SubCcDict] | None = None,
        client_id: str | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        files: FileInput | None = None,
        file_urls: list[str] | None = None,
        is_eid: bool | None = False,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        signing_options: SubSigningOptions | SubSigningOptionsDict | None = None,
        signing_redirect_url: str | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        expires_at: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SignatureRequestGetResponse, SignatureRequestSendWithTemplateErrorBody]:
        """Creates and sends a new SignatureRequest based off of the Template(s) specified with the ``template_ids``
        parameter.

        Args:
            template_ids: Use ``template_ids`` to create a SignatureRequest from one or more templates, in the order in
                which the template will be used.
            signers: Add Signers to your Templated-based Signature Request.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            ccs: Add CC email recipients. Required when a CC role exists for the Template.
            client_id: Client id of the app to associate with the signature request. Used to apply the branding and
                callback url defined for the app.
            custom_fields: An array defining values and options for custom fields. Required when a custom field exists
                in the Template.
            files: Use ``files[]`` to indicate the uploaded file(s) to send for signature. This endpoint requires either
                **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            is_eid: Send with a value of ``true`` if you wish to enable `electronic identification (eID)
                <https://www.hellosign.com/features/electronic-id>`__, which requires the signer to verify their
                identity with an eID provider to sign a document.<br> **NOTE:** You need the eID add-on to use this
                feature. Please `contact sales <https://sign.dropbox.com/form/contact-sales>`__ for more information.
                Cannot be used in ``test_mode``. Only works on requests with one signer.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            signing_options: This allows the requester to specify the types allowed for creating a signature and specify
                another signing options. **NOTE:** If ``signing_options`` are not defined in the request, the allowed
                types will default to those specified in the account settings. **NOTE:** If
                ``force_advanced_signature_details`` is set, allowed types has to be defined too.
            signing_redirect_url: The URL you want signers redirected to after they successfully sign.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request will not be legally binding if set to ``true``.
                Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            expires_at: When the signature request will expire. Unsigned signatures will be moved to the expired status,
                and no longer signable. See `Signature Request Expiration Date
                <https://developers.hellosign.com/docs/signature-request/expiration/>`__ for details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/signature_request/send_with_template"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(
                param[list[str]]("template_ids", template_ids),
                param[list[SubSignatureRequestTemplateSigner | SubSignatureRequestTemplateSignerDict]](
                    "signers", signers
                ),
                param[bool | None]("allow_decline", allow_decline),
                param[list[SubCc | SubCcDict] | None]("ccs", ccs),
                param[str | None]("client_id", client_id),
                param[list[SubCustomField | SubCustomFieldDict] | None]("custom_fields", custom_fields),
                file_part("files", files) if files is not None else None,
                param[list[str] | None]("file_urls", file_urls),
                param[bool | None]("is_eid", is_eid),
                param[str | None]("message", message),
                param[dict[str, Any] | None]("metadata", metadata),
                param[SubSigningOptions | SubSigningOptionsDict | None]("signing_options", signing_options),
                param[str | None]("signing_redirect_url", signing_redirect_url),
                param[str | None]("subject", subject),
                param[bool | None]("test_mode", test_mode),
                param[str | None]("title", title),
                param[int | None]("expires_at", expires_at),
            ),
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[SignatureRequestGetResponse],
            error_mapper=signature_request_send_with_template_error_mapper,
            request_options=request_options,
        )

    def signature_request_update(
        self,
        signature_request_id: str,
        body: SignatureRequestUpdateRequest | SignatureRequestUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SignatureRequestGetResponse, SignatureRequestUpdateErrorBody]:
        """Updates the email address and/or the name for a given signer on a signature request. You can listen for the
        ``signature_request_email_bounce`` event on your app or account to detect bounced emails, and respond with this
        method.

        Updating the email address of a signer will generate a new ``signature_id`` value.

        **NOTE:** This action cannot be performed on a signature request with an appended signature page.

        Args:
            signature_request_id: The id of the SignatureRequest to update.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/signature_request/update/{signature_request_id}"),
            path_params=[param[str]("signature_request_id", signature_request_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SignatureRequestUpdateRequest | SignatureRequestUpdateRequestDict](body),
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[SignatureRequestGetResponse],
            error_mapper=signature_request_update_error_mapper,
            request_options=request_options,
        )


class AsyncSignatureRequestWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def signature_request_bulk_create_embedded_with_template(
        self,
        template_ids: list[str],
        client_id: str,
        *,
        signer_file: AsyncFileInput | None = None,
        signer_list: list[SubBulkSignerList | SubBulkSignerListDict] | None = None,
        allow_decline: bool | None = False,
        ccs: list[SubCc | SubCcDict] | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        signing_redirect_url: str | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        expires_at: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkSendJobSendResponse, SignatureRequestBulkCreateEmbeddedWithTemplateErrorBody]:
        """Creates BulkSendJob which sends up to 250 SignatureRequests in bulk based off of the provided Template(s)
        specified with the ``template_ids`` parameter to be signed in an embedded iFrame. These embedded signature
        requests can only be signed in embedded iFrames whereas normal signature requests can only be signed on Dropbox
        Sign.

        **NOTE:** Only available for Standard plan and higher.

        Args:
            template_ids: Use ``template_ids`` to create a SignatureRequest from one or more templates, in the order in
                which the template will be used.
            client_id: Client id of the app you're using to create this embedded signature request. Used for security
                purposes.
            signer_file: ``signer_file`` is a CSV file defining values and options for signer fields. Required unless a
                ``signer_list`` is used, you may not use both. The CSV can have the following columns: - ``name``: the
                name of the signer filling the role of RoleName - ``email_address``: email address of the signer filling
                the role of RoleName - ``pin``: the 4- to 12-character access code that will secure this signer's
                signature page (optional) - ``sms_phone_number``: An E.164 formatted phone number that will receive a
                code via SMS to access this signer's signature page. (optional) By using the feature, you agree you are
                responsible for obtaining a signer's consent to receive text messages from Dropbox Sign related to this
                signature request and confirm you have obtained such consent from all signers prior to enabling SMS
                delivery for this signature request. `Learn more
                <https://faq.hellosign.com/hc/en-us/articles/15815316468877-Dropbox-Sign-SMS-tools-add-on>`__. **NOTE:**
                Not available in test mode and requires a Standard plan or higher. - ``*_field``: any column with a
                _field" suffix will be treated as a custom field (optional) You may only specify field values here, any
                other options should be set in the custom_fields request parameter. Example CSV: ``` name,
                email_address, pin, company_field George, george@example.com, d79a3td, ABC Corp Mary, mary@example.com,
                gd9as5b, 123 LLC ```
            signer_list: ``signer_list`` is an array defining values and options for signer fields. Required unless a
                ``signer_file`` is used, you may not use both.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            ccs: Add CC email recipients. Required when a CC role exists for the Template.
            custom_fields: When used together with merge fields, ``custom_fields`` allows users to add pre-filled data
                to their signature requests. Pre-filled data can be used with "send-once" signature requests by adding
                merge fields with ``form_fields_per_document`` or `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ while passing values back with
                ``custom_fields`` together in one API call. For using pre-filled on repeatable signature requests, merge
                fields are added to templates in the Dropbox Sign UI or by calling `/template/create_embedded_draft
                </api/reference/operation/templateCreateEmbeddedDraft>`__ and then passing ``custom_fields`` on
                subsequent signature requests referencing that template.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            signing_redirect_url: The URL you want signers redirected to after they successfully sign.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request will not be legally binding if set to ``true``.
                Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            expires_at: When the signature request will expire. Unsigned signatures will be moved to the expired status,
                and no longer signable. See `Signature Request Expiration Date
                <https://developers.hellosign.com/docs/signature-request/expiration/>`__ for details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/signature_request/bulk_create_embedded_with_template"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(
                param[list[str]]("template_ids", template_ids),
                param[str]("client_id", client_id),
                file_part("signer_file", signer_file) if signer_file is not None else None,
                param[list[SubBulkSignerList | SubBulkSignerListDict] | None]("signer_list", signer_list),
                param[bool | None]("allow_decline", allow_decline),
                param[list[SubCc | SubCcDict] | None]("ccs", ccs),
                param[list[SubCustomField | SubCustomFieldDict] | None]("custom_fields", custom_fields),
                param[str | None]("message", message),
                param[dict[str, Any] | None]("metadata", metadata),
                param[str | None]("signing_redirect_url", signing_redirect_url),
                param[str | None]("subject", subject),
                param[bool | None]("test_mode", test_mode),
                param[str | None]("title", title),
                param[int | None]("expires_at", expires_at),
            ),
            auth_scheme=self._auth.api_key,
            decoder=async_json_decoder[BulkSendJobSendResponse],
            error_mapper=signature_request_bulk_create_embedded_with_template_error_mapper,
            request_options=request_options,
        )

    async def signature_request_bulk_send_with_template(
        self,
        template_ids: list[str],
        *,
        signer_file: AsyncFileInput | None = None,
        signer_list: list[SubBulkSignerList | SubBulkSignerListDict] | None = None,
        allow_decline: bool | None = False,
        ccs: list[SubCc | SubCcDict] | None = None,
        client_id: str | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        signing_redirect_url: str | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        expires_at: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkSendJobSendResponse, SignatureRequestBulkSendWithTemplateErrorBody]:
        """Creates BulkSendJob which sends up to 250 SignatureRequests in bulk based off of the provided Template(s)
        specified with the ``template_ids`` parameter.

        **NOTE:** Only available for Standard plan and higher.

        Args:
            template_ids: Use ``template_ids`` to create a SignatureRequest from one or more templates, in the order in
                which the template will be used.
            signer_file: ``signer_file`` is a CSV file defining values and options for signer fields. Required unless a
                ``signer_list`` is used, you may not use both. The CSV can have the following columns: - ``name``: the
                name of the signer filling the role of RoleName - ``email_address``: email address of the signer filling
                the role of RoleName - ``pin``: the 4- to 12-character access code that will secure this signer's
                signature page (optional) - ``sms_phone_number``: An E.164 formatted phone number that will receive a
                code via SMS to access this signer's signature page. (optional) By using the feature, you agree you are
                responsible for obtaining a signer's consent to receive text messages from Dropbox Sign related to this
                signature request and confirm you have obtained such consent from all signers prior to enabling SMS
                delivery for this signature request. `Learn more
                <https://faq.hellosign.com/hc/en-us/articles/15815316468877-Dropbox-Sign-SMS-tools-add-on>`__. **NOTE:**
                Not available in test mode and requires a Standard plan or higher. - ``*_field``: any column with a
                _field" suffix will be treated as a custom field (optional) You may only specify field values here, any
                other options should be set in the custom_fields request parameter. Example CSV: ``` name,
                email_address, pin, company_field George, george@example.com, d79a3td, ABC Corp Mary, mary@example.com,
                gd9as5b, 123 LLC ```
            signer_list: ``signer_list`` is an array defining values and options for signer fields. Required unless a
                ``signer_file`` is used, you may not use both.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            ccs: Add CC email recipients. Required when a CC role exists for the Template.
            client_id: The client id of the API App you want to associate with this request. Used to apply the branding
                and callback url defined for the app.
            custom_fields: When used together with merge fields, ``custom_fields`` allows users to add pre-filled data
                to their signature requests. Pre-filled data can be used with "send-once" signature requests by adding
                merge fields with ``form_fields_per_document`` or `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ while passing values back with
                ``custom_fields`` together in one API call. For using pre-filled on repeatable signature requests, merge
                fields are added to templates in the Dropbox Sign UI or by calling `/template/create_embedded_draft
                </api/reference/operation/templateCreateEmbeddedDraft>`__ and then passing ``custom_fields`` on
                subsequent signature requests referencing that template.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            signing_redirect_url: The URL you want signers redirected to after they successfully sign.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request will not be legally binding if set to ``true``.
                Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            expires_at: When the signature request will expire. Unsigned signatures will be moved to the expired status,
                and no longer signable. See `Signature Request Expiration Date
                <https://developers.hellosign.com/docs/signature-request/expiration/>`__ for details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/signature_request/bulk_send_with_template"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(
                param[list[str]]("template_ids", template_ids),
                file_part("signer_file", signer_file) if signer_file is not None else None,
                param[list[SubBulkSignerList | SubBulkSignerListDict] | None]("signer_list", signer_list),
                param[bool | None]("allow_decline", allow_decline),
                param[list[SubCc | SubCcDict] | None]("ccs", ccs),
                param[str | None]("client_id", client_id),
                param[list[SubCustomField | SubCustomFieldDict] | None]("custom_fields", custom_fields),
                param[str | None]("message", message),
                param[dict[str, Any] | None]("metadata", metadata),
                param[str | None]("signing_redirect_url", signing_redirect_url),
                param[str | None]("subject", subject),
                param[bool | None]("test_mode", test_mode),
                param[str | None]("title", title),
                param[int | None]("expires_at", expires_at),
            ),
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[BulkSendJobSendResponse],
            error_mapper=signature_request_bulk_send_with_template_error_mapper,
            request_options=request_options,
        )

    async def signature_request_cancel(
        self, signature_request_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, SignatureRequestCancelErrorBody]:
        """Cancels an incomplete signature request. This action is **not reversible**.

        The request will be canceled and signers will no longer be able to sign. If they try to access the signature
        request they will receive a HTTP 410 status code indicating that the resource has been deleted. Cancelation is
        asynchronous and a successful call to this endpoint will return an empty 200 OK response if the signature
        request is eligible to be canceled and has been successfully queued.

        This 200 OK response does not indicate a successful cancelation of the signature request itself. The cancelation
        is confirmed via the ``signature_request_canceled`` event. It is recommended that a `callback handler
        </api/reference/tag/Callbacks-and-Events>`__ be implemented to listen for the ``signature_request_canceled``
        event. This callback will be sent only when the cancelation has completed successfully. If a callback handler
        has been configured and the event has not been received within 60 minutes of making the call, check the status
        of the request in the `API Dashboard <https://app.hellosign.com/apidashboard>`__ and retry the cancelation if
        necessary.

        To be eligible for cancelation, a signature request must have been sent successfully, must not yet have been
        signed by all signers, and you must either be the sender or own the API app under which it was sent. A partially
        signed signature request can be canceled.

        **NOTE:** To remove your access to a completed signature request, use the endpoint: ``POST
        /signature_request/remove/[:signature_request_id]``.

        Args:
            signature_request_id: The id of the incomplete SignatureRequest to cancel.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/signature_request/cancel/{signature_request_id}"),
            path_params=[param[str]("signature_request_id", signature_request_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[Any],
            error_mapper=signature_request_cancel_error_mapper,
            request_options=request_options,
        )

    async def signature_request_create_embedded(
        self,
        client_id: str,
        *,
        files: AsyncFileInput | None = None,
        file_urls: list[str] | None = None,
        signers: list[SubSignatureRequestSigner | SubSignatureRequestSignerDict] | None = None,
        grouped_signers: list[SubSignatureRequestGroupedSigners | SubSignatureRequestGroupedSignersDict] | None = None,
        allow_decline: bool | None = False,
        allow_reassign: bool | None = False,
        attachments: list[SubAttachment | SubAttachmentDict] | None = None,
        cc_email_addresses: list[EmailStr] | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        field_options: SubFieldOptions | SubFieldOptionsDict | None = None,
        form_field_groups: list[SubFormFieldGroup | SubFormFieldGroupDict] | None = None,
        form_field_rules: list[SubFormFieldRule | SubFormFieldRuleDict] | None = None,
        form_fields_per_document: list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None = None,
        hide_text_tags: bool | None = False,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        signing_options: SubSigningOptions | SubSigningOptionsDict | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        use_text_tags: bool | None = False,
        ignore_text_tags_extraction_errors: bool | None = False,
        populate_auto_fill_fields: bool | None = False,
        expires_at: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SignatureRequestGetResponse, SignatureRequestCreateEmbeddedErrorBody]:
        """Creates a new SignatureRequest with the submitted documents to be signed in an embedded iFrame. If
        form_fields_per_document is not specified, a signature page will be affixed where all signers will be required
        to add their signature, signifying their agreement to all contained documents. Note that embedded signature
        requests can only be signed in embedded iFrames whereas normal signature requests can only be signed on Dropbox
        Sign.

        Args:
            client_id: Client id of the app you're using to create this embedded signature request. Used for security
                purposes.
            files: Use ``files[]`` to indicate the uploaded file(s) to send for signature. This endpoint requires either
                **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            signers: Add Signers to your Signature Request. This endpoint requires either **signers** or
                **grouped_signers**, but not both.
            grouped_signers: Add Grouped Signers to your Signature Request. This endpoint requires either **signers** or
                **grouped_signers**, but not both.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            allow_reassign: Allows signers to reassign their signature requests to other signers if set to ``true``.
                Defaults to ``false``. **NOTE:** Only available for Premium plan.
            attachments: A list describing the attachments
            cc_email_addresses: The email addresses that should be CCed.
            custom_fields: When used together with merge fields, ``custom_fields`` allows users to add pre-filled data
                to their signature requests. Pre-filled data can be used with "send-once" signature requests by adding
                merge fields with ``form_fields_per_document`` or `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ while passing values back with
                ``custom_fields`` together in one API call. For using pre-filled on repeatable signature requests, merge
                fields are added to templates in the Dropbox Sign UI or by calling `/template/create_embedded_draft
                </api/reference/operation/templateCreateEmbeddedDraft>`__ and then passing ``custom_fields`` on
                subsequent signature requests referencing that template.
            field_options: This allows the requester to specify field options for a signature request.
            form_field_groups: Group information for fields defined in ``form_fields_per_document``. String-indexed JSON
                array with ``group_label`` and ``requirement`` keys. ``form_fields_per_document`` must contain fields
                referencing a group defined in ``form_field_groups``.
            form_field_rules: Conditional Logic rules for fields defined in ``form_fields_per_document``.
            form_fields_per_document: The fields that should appear on the document, expressed as an array of objects.
                (For more details you can read about it here: `Using Form Fields per Document
                </docs/openapi/form-fields-per-document>`__.) **NOTE:** Fields like **text**, **dropdown**,
                **checkbox**, **radio**, and **hyperlink** have additional required and optional parameters. Check out
                the list of `additional parameters </api/reference/constants/#form-fields-per-document>`__ for these
                field types. * Text Field use ``SubFormFieldsPerDocumentText`` * Dropdown Field use
                ``SubFormFieldsPerDocumentDropdown`` * Hyperlink Field use ``SubFormFieldsPerDocumentHyperlink`` *
                Checkbox Field use ``SubFormFieldsPerDocumentCheckbox`` * Radio Field use
                ``SubFormFieldsPerDocumentRadio`` * Signature Field use ``SubFormFieldsPerDocumentSignature`` * Date
                Signed Field use ``SubFormFieldsPerDocumentDateSigned`` * Initials Field use
                ``SubFormFieldsPerDocumentInitials`` * Text Merge Field use ``SubFormFieldsPerDocumentTextMerge`` *
                Checkbox Merge Field use ``SubFormFieldsPerDocumentCheckboxMerge``
            hide_text_tags: Enables automatic Text Tag removal when set to true. **NOTE:** Removing text tags this way
                can cause unwanted clipping. We recommend leaving this setting on ``false`` and instead hiding your text
                tags using white text or a similar approach. See the `Text Tags Walkthrough
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ for more information.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            signing_options: This allows the requester to specify the types allowed for creating a signature and specify
                another signing options. **NOTE:** If ``signing_options`` are not defined in the request, the allowed
                types will default to those specified in the account settings. **NOTE:** If
                ``force_advanced_signature_details`` is set, allowed types has to be defined too.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request will not be legally binding if set to ``true``.
                Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            use_text_tags: Send with a value of ``true`` if you wish to enable `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ parsing in your document. Defaults
                to disabled, or ``false``.
            ignore_text_tags_extraction_errors: Sent with a value of ``true`` to ignore the validation errors from text
                tags extraction. Defaults to ``false``.
            populate_auto_fill_fields: Controls whether `auto fill fields
                <https://faq.hellosign.com/hc/en-us/articles/360051467511-Auto-Fill-Fields>`__ can automatically
                populate a signer's information during signing. **NOTE:** Keep your signer's information safe by
                ensuring that the _signer on your signature request is the intended party_ before using this feature.
            expires_at: When the signature request will expire. Unsigned signatures will be moved to the expired status,
                and no longer signable. See `Signature Request Expiration Date
                <https://developers.hellosign.com/docs/signature-request/expiration/>`__ for details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/signature_request/create_embedded"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(
                param[str]("client_id", client_id),
                file_part("files", files) if files is not None else None,
                param[list[str] | None]("file_urls", file_urls),
                param[list[SubSignatureRequestSigner | SubSignatureRequestSignerDict] | None]("signers", signers),
                param[list[SubSignatureRequestGroupedSigners | SubSignatureRequestGroupedSignersDict] | None](
                    "grouped_signers", grouped_signers
                ),
                param[bool | None]("allow_decline", allow_decline),
                param[bool | None]("allow_reassign", allow_reassign),
                param[list[SubAttachment | SubAttachmentDict] | None]("attachments", attachments),
                param[list[EmailStr] | None]("cc_email_addresses", cc_email_addresses),
                param[list[SubCustomField | SubCustomFieldDict] | None]("custom_fields", custom_fields),
                param[SubFieldOptions | SubFieldOptionsDict | None]("field_options", field_options),
                param[list[SubFormFieldGroup | SubFormFieldGroupDict] | None]("form_field_groups", form_field_groups),
                param[list[SubFormFieldRule | SubFormFieldRuleDict] | None]("form_field_rules", form_field_rules),
                param[list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None](
                    "form_fields_per_document", form_fields_per_document
                ),
                param[bool | None]("hide_text_tags", hide_text_tags),
                param[str | None]("message", message),
                param[dict[str, Any] | None]("metadata", metadata),
                param[SubSigningOptions | SubSigningOptionsDict | None]("signing_options", signing_options),
                param[str | None]("subject", subject),
                param[bool | None]("test_mode", test_mode),
                param[str | None]("title", title),
                param[bool | None]("use_text_tags", use_text_tags),
                param[bool | None]("ignore_text_tags_extraction_errors", ignore_text_tags_extraction_errors),
                param[bool | None]("populate_auto_fill_fields", populate_auto_fill_fields),
                param[int | None]("expires_at", expires_at),
            ),
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[SignatureRequestGetResponse],
            error_mapper=signature_request_create_embedded_error_mapper,
            request_options=request_options,
        )

    async def signature_request_create_embedded_with_template(
        self,
        template_ids: list[str],
        client_id: str,
        signers: list[SubSignatureRequestTemplateSigner | SubSignatureRequestTemplateSignerDict],
        *,
        allow_decline: bool | None = False,
        ccs: list[SubCc | SubCcDict] | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        files: AsyncFileInput | None = None,
        file_urls: list[str] | None = None,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        signing_options: SubSigningOptions | SubSigningOptionsDict | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        populate_auto_fill_fields: bool | None = False,
        expires_at: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SignatureRequestGetResponse, SignatureRequestCreateEmbeddedWithTemplateErrorBody]:
        """Creates a new SignatureRequest based on the given Template(s) to be signed in an embedded iFrame. Note that
        embedded signature requests can only be signed in embedded iFrames whereas normal signature requests can only be
        signed on Dropbox Sign.

        Args:
            template_ids: Use ``template_ids`` to create a SignatureRequest from one or more templates, in the order in
                which the template will be used.
            client_id: Client id of the app you're using to create this embedded signature request. Used for security
                purposes.
            signers: Add Signers to your Templated-based Signature Request.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            ccs: Add CC email recipients. Required when a CC role exists for the Template.
            custom_fields: An array defining values and options for custom fields. Required when a custom field exists
                in the Template.
            files: Use ``files[]`` to indicate the uploaded file(s) to send for signature. This endpoint requires either
                **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            signing_options: This allows the requester to specify the types allowed for creating a signature and specify
                another signing options. **NOTE:** If ``signing_options`` are not defined in the request, the allowed
                types will default to those specified in the account settings. **NOTE:** If
                ``force_advanced_signature_details`` is set, allowed types has to be defined too.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request will not be legally binding if set to ``true``.
                Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            populate_auto_fill_fields: Controls whether `auto fill fields
                <https://faq.hellosign.com/hc/en-us/articles/360051467511-Auto-Fill-Fields>`__ can automatically
                populate a signer's information during signing. **NOTE:** Keep your signer's information safe by
                ensuring that the _signer on your signature request is the intended party_ before using this feature.
            expires_at: When the signature request will expire. Unsigned signatures will be moved to the expired status,
                and no longer signable. See `Signature Request Expiration Date
                <https://developers.hellosign.com/docs/signature-request/expiration/>`__ for details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/signature_request/create_embedded_with_template"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(
                param[list[str]]("template_ids", template_ids),
                param[str]("client_id", client_id),
                param[list[SubSignatureRequestTemplateSigner | SubSignatureRequestTemplateSignerDict]](
                    "signers", signers
                ),
                param[bool | None]("allow_decline", allow_decline),
                param[list[SubCc | SubCcDict] | None]("ccs", ccs),
                param[list[SubCustomField | SubCustomFieldDict] | None]("custom_fields", custom_fields),
                file_part("files", files) if files is not None else None,
                param[list[str] | None]("file_urls", file_urls),
                param[str | None]("message", message),
                param[dict[str, Any] | None]("metadata", metadata),
                param[SubSigningOptions | SubSigningOptionsDict | None]("signing_options", signing_options),
                param[str | None]("subject", subject),
                param[bool | None]("test_mode", test_mode),
                param[str | None]("title", title),
                param[bool | None]("populate_auto_fill_fields", populate_auto_fill_fields),
                param[int | None]("expires_at", expires_at),
            ),
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[SignatureRequestGetResponse],
            error_mapper=signature_request_create_embedded_with_template_error_mapper,
            request_options=request_options,
        )

    async def signature_request_edit(
        self,
        signature_request_id: str,
        *,
        files: AsyncFileInput | None = None,
        file_urls: list[str] | None = None,
        signers: list[SubSignatureRequestSigner | SubSignatureRequestSignerDict] | None = None,
        grouped_signers: list[SubSignatureRequestGroupedSigners | SubSignatureRequestGroupedSignersDict] | None = None,
        allow_decline: bool | None = False,
        allow_reassign: bool | None = False,
        attachments: list[SubAttachment | SubAttachmentDict] | None = None,
        cc_email_addresses: list[EmailStr] | None = None,
        client_id: str | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        field_options: SubFieldOptions | SubFieldOptionsDict | None = None,
        form_field_groups: list[SubFormFieldGroup | SubFormFieldGroupDict] | None = None,
        form_field_rules: list[SubFormFieldRule | SubFormFieldRuleDict] | None = None,
        form_fields_per_document: list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None = None,
        hide_text_tags: bool | None = False,
        is_eid: bool | None = False,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        signing_options: SubSigningOptions | SubSigningOptionsDict | None = None,
        signing_redirect_url: str | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        use_text_tags: bool | None = False,
        ignore_text_tags_extraction_errors: bool | None = False,
        expires_at: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SignatureRequestGetResponse, SignatureRequestEditErrorBody]:
        """Edits and sends a SignatureRequest with the submitted documents. If ``form_fields_per_document`` is not
        specified, a signature page will be affixed where all signers will be required to add their signature,
        signifying their agreement to all contained documents.

        **NOTE:** Edit and resend *will* deduct your signature request quota.

        Args:
            signature_request_id: The id of the SignatureRequest to edit.
            files: Use ``files[]`` to indicate the uploaded file(s) to send for signature. This endpoint requires either
                **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            signers: Add Signers to your Signature Request. This endpoint requires either **signers** or
                **grouped_signers**, but not both.
            grouped_signers: Add Grouped Signers to your Signature Request. This endpoint requires either **signers** or
                **grouped_signers**, but not both.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            allow_reassign: Allows signers to reassign their signature requests to other signers if set to ``true``.
                Defaults to ``false``. **NOTE:** Only available for Premium plan and higher.
            attachments: A list describing the attachments
            cc_email_addresses: The email addresses that should be CCed.
            client_id: The client id of the API App you want to associate with this request. Used to apply the branding
                and callback url defined for the app.
            custom_fields: When used together with merge fields, ``custom_fields`` allows users to add pre-filled data
                to their signature requests. Pre-filled data can be used with "send-once" signature requests by adding
                merge fields with ``form_fields_per_document`` or `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ while passing values back with
                ``custom_fields`` together in one API call. For using pre-filled on repeatable signature requests, merge
                fields are added to templates in the Dropbox Sign UI or by calling `/template/create_embedded_draft
                </api/reference/operation/templateCreateEmbeddedDraft>`__ and then passing ``custom_fields`` on
                subsequent signature requests referencing that template.
            field_options: This allows the requester to specify field options for a signature request.
            form_field_groups: Group information for fields defined in ``form_fields_per_document``. String-indexed JSON
                array with ``group_label`` and ``requirement`` keys. ``form_fields_per_document`` must contain fields
                referencing a group defined in ``form_field_groups``.
            form_field_rules: Conditional Logic rules for fields defined in ``form_fields_per_document``.
            form_fields_per_document: The fields that should appear on the document, expressed as an array of objects.
                (For more details you can read about it here: `Using Form Fields per Document
                </docs/openapi/form-fields-per-document>`__.) **NOTE:** Fields like **text**, **dropdown**,
                **checkbox**, **radio**, and **hyperlink** have additional required and optional parameters. Check out
                the list of `additional parameters </api/reference/constants/#form-fields-per-document>`__ for these
                field types. * Text Field use ``SubFormFieldsPerDocumentText`` * Dropdown Field use
                ``SubFormFieldsPerDocumentDropdown`` * Hyperlink Field use ``SubFormFieldsPerDocumentHyperlink`` *
                Checkbox Field use ``SubFormFieldsPerDocumentCheckbox`` * Radio Field use
                ``SubFormFieldsPerDocumentRadio`` * Signature Field use ``SubFormFieldsPerDocumentSignature`` * Date
                Signed Field use ``SubFormFieldsPerDocumentDateSigned`` * Initials Field use
                ``SubFormFieldsPerDocumentInitials`` * Text Merge Field use ``SubFormFieldsPerDocumentTextMerge`` *
                Checkbox Merge Field use ``SubFormFieldsPerDocumentCheckboxMerge``
            hide_text_tags: Enables automatic Text Tag removal when set to true. **NOTE:** Removing text tags this way
                can cause unwanted clipping. We recommend leaving this setting on ``false`` and instead hiding your text
                tags using white text or a similar approach. See the `Text Tags Walkthrough
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ for more information.
            is_eid: Send with a value of ``true`` if you wish to enable `electronic identification (eID)
                <https://www.hellosign.com/features/electronic-id>`__, which requires the signer to verify their
                identity with an eID provider to sign a document.<br> **NOTE:** You need the eID add-on to use this
                feature. Please `contact sales <https://sign.dropbox.com/form/contact-sales>`__ for more information.
                Cannot be used in ``test_mode``. Only works on requests with one signer.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            signing_options: This allows the requester to specify the types allowed for creating a signature and specify
                another signing options. **NOTE:** If ``signing_options`` are not defined in the request, the allowed
                types will default to those specified in the account settings. **NOTE:** If
                ``force_advanced_signature_details`` is set, allowed types has to be defined too.
            signing_redirect_url: The URL you want signers redirected to after they successfully sign.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request will not be legally binding if set to ``true``.
                Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            use_text_tags: Send with a value of ``true`` if you wish to enable `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ parsing in your document. Defaults
                to disabled, or ``false``.
            ignore_text_tags_extraction_errors: Sent with a value of ``true`` to ignore the validation errors from text
                tags extraction. Defaults to ``false``.
            expires_at: When the signature request will expire. Unsigned signatures will be moved to the expired status,
                and no longer signable. See `Signature Request Expiration Date
                <https://developers.hellosign.com/docs/signature-request/expiration/>`__ for details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/signature_request/edit/{signature_request_id}"),
            path_params=[param[str]("signature_request_id", signature_request_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(
                file_part("files", files) if files is not None else None,
                param[list[str] | None]("file_urls", file_urls),
                param[list[SubSignatureRequestSigner | SubSignatureRequestSignerDict] | None]("signers", signers),
                param[list[SubSignatureRequestGroupedSigners | SubSignatureRequestGroupedSignersDict] | None](
                    "grouped_signers", grouped_signers
                ),
                param[bool | None]("allow_decline", allow_decline),
                param[bool | None]("allow_reassign", allow_reassign),
                param[list[SubAttachment | SubAttachmentDict] | None]("attachments", attachments),
                param[list[EmailStr] | None]("cc_email_addresses", cc_email_addresses),
                param[str | None]("client_id", client_id),
                param[list[SubCustomField | SubCustomFieldDict] | None]("custom_fields", custom_fields),
                param[SubFieldOptions | SubFieldOptionsDict | None]("field_options", field_options),
                param[list[SubFormFieldGroup | SubFormFieldGroupDict] | None]("form_field_groups", form_field_groups),
                param[list[SubFormFieldRule | SubFormFieldRuleDict] | None]("form_field_rules", form_field_rules),
                param[list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None](
                    "form_fields_per_document", form_fields_per_document
                ),
                param[bool | None]("hide_text_tags", hide_text_tags),
                param[bool | None]("is_eid", is_eid),
                param[str | None]("message", message),
                param[dict[str, Any] | None]("metadata", metadata),
                param[SubSigningOptions | SubSigningOptionsDict | None]("signing_options", signing_options),
                param[str | None]("signing_redirect_url", signing_redirect_url),
                param[str | None]("subject", subject),
                param[bool | None]("test_mode", test_mode),
                param[str | None]("title", title),
                param[bool | None]("use_text_tags", use_text_tags),
                param[bool | None]("ignore_text_tags_extraction_errors", ignore_text_tags_extraction_errors),
                param[int | None]("expires_at", expires_at),
            ),
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[SignatureRequestGetResponse],
            error_mapper=signature_request_edit_error_mapper,
            request_options=request_options,
        )

    async def signature_request_edit_embedded(
        self,
        signature_request_id: str,
        client_id: str,
        *,
        files: AsyncFileInput | None = None,
        file_urls: list[str] | None = None,
        signers: list[SubSignatureRequestSigner | SubSignatureRequestSignerDict] | None = None,
        grouped_signers: list[SubSignatureRequestGroupedSigners | SubSignatureRequestGroupedSignersDict] | None = None,
        allow_decline: bool | None = False,
        allow_reassign: bool | None = False,
        attachments: list[SubAttachment | SubAttachmentDict] | None = None,
        cc_email_addresses: list[EmailStr] | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        field_options: SubFieldOptions | SubFieldOptionsDict | None = None,
        form_field_groups: list[SubFormFieldGroup | SubFormFieldGroupDict] | None = None,
        form_field_rules: list[SubFormFieldRule | SubFormFieldRuleDict] | None = None,
        form_fields_per_document: list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None = None,
        hide_text_tags: bool | None = False,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        signing_options: SubSigningOptions | SubSigningOptionsDict | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        use_text_tags: bool | None = False,
        ignore_text_tags_extraction_errors: bool | None = False,
        populate_auto_fill_fields: bool | None = False,
        expires_at: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SignatureRequestGetResponse, SignatureRequestEditEmbeddedErrorBody]:
        """Edits a SignatureRequest with the submitted documents to be signed in an embedded iFrame. If
        form_fields_per_document is not specified, a signature page will be affixed where all signers will be required
        to add their signature, signifying their agreement to all contained documents. Note that embedded signature
        requests can only be signed in embedded iFrames whereas normal signature requests can only be signed on Dropbox
        Sign.

        **NOTE:** Edit and resend *will* deduct your signature request quota.

        Args:
            signature_request_id: The id of the SignatureRequest to edit.
            client_id: Client id of the app you're using to create this embedded signature request. Used for security
                purposes.
            files: Use ``files[]`` to indicate the uploaded file(s) to send for signature. This endpoint requires either
                **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            signers: Add Signers to your Signature Request. This endpoint requires either **signers** or
                **grouped_signers**, but not both.
            grouped_signers: Add Grouped Signers to your Signature Request. This endpoint requires either **signers** or
                **grouped_signers**, but not both.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            allow_reassign: Allows signers to reassign their signature requests to other signers if set to ``true``.
                Defaults to ``false``. **NOTE:** Only available for Premium plan.
            attachments: A list describing the attachments
            cc_email_addresses: The email addresses that should be CCed.
            custom_fields: When used together with merge fields, ``custom_fields`` allows users to add pre-filled data
                to their signature requests. Pre-filled data can be used with "send-once" signature requests by adding
                merge fields with ``form_fields_per_document`` or `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ while passing values back with
                ``custom_fields`` together in one API call. For using pre-filled on repeatable signature requests, merge
                fields are added to templates in the Dropbox Sign UI or by calling `/template/create_embedded_draft
                </api/reference/operation/templateCreateEmbeddedDraft>`__ and then passing ``custom_fields`` on
                subsequent signature requests referencing that template.
            field_options: This allows the requester to specify field options for a signature request.
            form_field_groups: Group information for fields defined in ``form_fields_per_document``. String-indexed JSON
                array with ``group_label`` and ``requirement`` keys. ``form_fields_per_document`` must contain fields
                referencing a group defined in ``form_field_groups``.
            form_field_rules: Conditional Logic rules for fields defined in ``form_fields_per_document``.
            form_fields_per_document: The fields that should appear on the document, expressed as an array of objects.
                (For more details you can read about it here: `Using Form Fields per Document
                </docs/openapi/form-fields-per-document>`__.) **NOTE:** Fields like **text**, **dropdown**,
                **checkbox**, **radio**, and **hyperlink** have additional required and optional parameters. Check out
                the list of `additional parameters </api/reference/constants/#form-fields-per-document>`__ for these
                field types. * Text Field use ``SubFormFieldsPerDocumentText`` * Dropdown Field use
                ``SubFormFieldsPerDocumentDropdown`` * Hyperlink Field use ``SubFormFieldsPerDocumentHyperlink`` *
                Checkbox Field use ``SubFormFieldsPerDocumentCheckbox`` * Radio Field use
                ``SubFormFieldsPerDocumentRadio`` * Signature Field use ``SubFormFieldsPerDocumentSignature`` * Date
                Signed Field use ``SubFormFieldsPerDocumentDateSigned`` * Initials Field use
                ``SubFormFieldsPerDocumentInitials`` * Text Merge Field use ``SubFormFieldsPerDocumentTextMerge`` *
                Checkbox Merge Field use ``SubFormFieldsPerDocumentCheckboxMerge``
            hide_text_tags: Enables automatic Text Tag removal when set to true. **NOTE:** Removing text tags this way
                can cause unwanted clipping. We recommend leaving this setting on ``false`` and instead hiding your text
                tags using white text or a similar approach. See the `Text Tags Walkthrough
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ for more information.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            signing_options: This allows the requester to specify the types allowed for creating a signature and specify
                another signing options. **NOTE:** If ``signing_options`` are not defined in the request, the allowed
                types will default to those specified in the account settings. **NOTE:** If
                ``force_advanced_signature_details`` is set, allowed types has to be defined too.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request will not be legally binding if set to ``true``.
                Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            use_text_tags: Send with a value of ``true`` if you wish to enable `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ parsing in your document. Defaults
                to disabled, or ``false``.
            ignore_text_tags_extraction_errors: Sent with a value of ``true`` to ignore the validation errors from text
                tags extraction. Defaults to ``false``.
            populate_auto_fill_fields: Controls whether `auto fill fields
                <https://faq.hellosign.com/hc/en-us/articles/360051467511-Auto-Fill-Fields>`__ can automatically
                populate a signer's information during signing. **NOTE:** Keep your signer's information safe by
                ensuring that the _signer on your signature request is the intended party_ before using this feature.
            expires_at: When the signature request will expire. Unsigned signatures will be moved to the expired status,
                and no longer signable. See `Signature Request Expiration Date
                <https://developers.hellosign.com/docs/signature-request/expiration/>`__ for details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/signature_request/edit_embedded/{signature_request_id}"),
            path_params=[param[str]("signature_request_id", signature_request_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(
                param[str]("client_id", client_id),
                file_part("files", files) if files is not None else None,
                param[list[str] | None]("file_urls", file_urls),
                param[list[SubSignatureRequestSigner | SubSignatureRequestSignerDict] | None]("signers", signers),
                param[list[SubSignatureRequestGroupedSigners | SubSignatureRequestGroupedSignersDict] | None](
                    "grouped_signers", grouped_signers
                ),
                param[bool | None]("allow_decline", allow_decline),
                param[bool | None]("allow_reassign", allow_reassign),
                param[list[SubAttachment | SubAttachmentDict] | None]("attachments", attachments),
                param[list[EmailStr] | None]("cc_email_addresses", cc_email_addresses),
                param[list[SubCustomField | SubCustomFieldDict] | None]("custom_fields", custom_fields),
                param[SubFieldOptions | SubFieldOptionsDict | None]("field_options", field_options),
                param[list[SubFormFieldGroup | SubFormFieldGroupDict] | None]("form_field_groups", form_field_groups),
                param[list[SubFormFieldRule | SubFormFieldRuleDict] | None]("form_field_rules", form_field_rules),
                param[list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None](
                    "form_fields_per_document", form_fields_per_document
                ),
                param[bool | None]("hide_text_tags", hide_text_tags),
                param[str | None]("message", message),
                param[dict[str, Any] | None]("metadata", metadata),
                param[SubSigningOptions | SubSigningOptionsDict | None]("signing_options", signing_options),
                param[str | None]("subject", subject),
                param[bool | None]("test_mode", test_mode),
                param[str | None]("title", title),
                param[bool | None]("use_text_tags", use_text_tags),
                param[bool | None]("ignore_text_tags_extraction_errors", ignore_text_tags_extraction_errors),
                param[bool | None]("populate_auto_fill_fields", populate_auto_fill_fields),
                param[int | None]("expires_at", expires_at),
            ),
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[SignatureRequestGetResponse],
            error_mapper=signature_request_edit_embedded_error_mapper,
            request_options=request_options,
        )

    async def signature_request_edit_embedded_with_template(
        self,
        signature_request_id: str,
        template_ids: list[str],
        client_id: str,
        signers: list[SubSignatureRequestTemplateSigner | SubSignatureRequestTemplateSignerDict],
        *,
        allow_decline: bool | None = False,
        ccs: list[SubCc | SubCcDict] | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        files: AsyncFileInput | None = None,
        file_urls: list[str] | None = None,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        signing_options: SubSigningOptions | SubSigningOptionsDict | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        populate_auto_fill_fields: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SignatureRequestGetResponse, SignatureRequestEditEmbeddedWithTemplateErrorBody]:
        """Edits a SignatureRequest based on the given Template(s) to be signed in an embedded iFrame. Note that
        embedded signature requests can only be signed in embedded iFrames whereas normal signature requests can only be
        signed on Dropbox Sign.

        **NOTE:** Edit and resend *will* deduct your signature request quota.

        Args:
            signature_request_id: The id of the SignatureRequest to edit.
            template_ids: Use ``template_ids`` to create a SignatureRequest from one or more templates, in the order in
                which the template will be used.
            client_id: Client id of the app you're using to create this embedded signature request. Used for security
                purposes.
            signers: Add Signers to your Templated-based Signature Request.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            ccs: Add CC email recipients. Required when a CC role exists for the Template.
            custom_fields: An array defining values and options for custom fields. Required when a custom field exists
                in the Template.
            files: Use ``files[]`` to indicate the uploaded file(s) to send for signature. This endpoint requires either
                **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            signing_options: This allows the requester to specify the types allowed for creating a signature and specify
                another signing options. **NOTE:** If ``signing_options`` are not defined in the request, the allowed
                types will default to those specified in the account settings. **NOTE:** If
                ``force_advanced_signature_details`` is set, allowed types has to be defined too.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request will not be legally binding if set to ``true``.
                Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            populate_auto_fill_fields: Controls whether `auto fill fields
                <https://faq.hellosign.com/hc/en-us/articles/360051467511-Auto-Fill-Fields>`__ can automatically
                populate a signer's information during signing. **NOTE:** Keep your signer's information safe by
                ensuring that the _signer on your signature request is the intended party_ before using this feature.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/signature_request/edit_embedded_with_template/{signature_request_id}"),
            path_params=[param[str]("signature_request_id", signature_request_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(
                param[list[str]]("template_ids", template_ids),
                param[str]("client_id", client_id),
                param[list[SubSignatureRequestTemplateSigner | SubSignatureRequestTemplateSignerDict]](
                    "signers", signers
                ),
                param[bool | None]("allow_decline", allow_decline),
                param[list[SubCc | SubCcDict] | None]("ccs", ccs),
                param[list[SubCustomField | SubCustomFieldDict] | None]("custom_fields", custom_fields),
                file_part("files", files) if files is not None else None,
                param[list[str] | None]("file_urls", file_urls),
                param[str | None]("message", message),
                param[dict[str, Any] | None]("metadata", metadata),
                param[SubSigningOptions | SubSigningOptionsDict | None]("signing_options", signing_options),
                param[str | None]("subject", subject),
                param[bool | None]("test_mode", test_mode),
                param[str | None]("title", title),
                param[bool | None]("populate_auto_fill_fields", populate_auto_fill_fields),
            ),
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[SignatureRequestGetResponse],
            error_mapper=signature_request_edit_embedded_with_template_error_mapper,
            request_options=request_options,
        )

    async def signature_request_edit_with_template(
        self,
        signature_request_id: str,
        template_ids: list[str],
        signers: list[SubSignatureRequestTemplateSigner | SubSignatureRequestTemplateSignerDict],
        *,
        allow_decline: bool | None = False,
        ccs: list[SubCc | SubCcDict] | None = None,
        client_id: str | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        files: AsyncFileInput | None = None,
        file_urls: list[str] | None = None,
        is_eid: bool | None = False,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        signing_options: SubSigningOptions | SubSigningOptionsDict | None = None,
        signing_redirect_url: str | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SignatureRequestGetResponse, SignatureRequestEditWithTemplateErrorBody]:
        """Edits and sends a SignatureRequest based off of the Template(s) specified with the template_ids parameter.

        **NOTE:** Edit and resend *will* deduct your signature request quota.

        Args:
            signature_request_id: The id of the SignatureRequest to edit.
            template_ids: Use ``template_ids`` to create a SignatureRequest from one or more templates, in the order in
                which the template will be used.
            signers: Add Signers to your Templated-based Signature Request.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            ccs: Add CC email recipients. Required when a CC role exists for the Template.
            client_id: Client id of the app to associate with the signature request. Used to apply the branding and
                callback url defined for the app.
            custom_fields: An array defining values and options for custom fields. Required when a custom field exists
                in the Template.
            files: Use ``files[]`` to indicate the uploaded file(s) to send for signature. This endpoint requires either
                **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            is_eid: Send with a value of ``true`` if you wish to enable `electronic identification (eID)
                <https://www.hellosign.com/features/electronic-id>`__, which requires the signer to verify their
                identity with an eID provider to sign a document.<br> **NOTE:** You need the eID add-on to use this
                feature. Please `contact sales <https://sign.dropbox.com/form/contact-sales>`__ for more information.
                Cannot be used in ``test_mode``. Only works on requests with one signer.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            signing_options: This allows the requester to specify the types allowed for creating a signature and specify
                another signing options. **NOTE:** If ``signing_options`` are not defined in the request, the allowed
                types will default to those specified in the account settings. **NOTE:** If
                ``force_advanced_signature_details`` is set, allowed types has to be defined too.
            signing_redirect_url: The URL you want signers redirected to after they successfully sign.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request will not be legally binding if set to ``true``.
                Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/signature_request/edit_with_template/{signature_request_id}"),
            path_params=[param[str]("signature_request_id", signature_request_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(
                param[list[str]]("template_ids", template_ids),
                param[list[SubSignatureRequestTemplateSigner | SubSignatureRequestTemplateSignerDict]](
                    "signers", signers
                ),
                param[bool | None]("allow_decline", allow_decline),
                param[list[SubCc | SubCcDict] | None]("ccs", ccs),
                param[str | None]("client_id", client_id),
                param[list[SubCustomField | SubCustomFieldDict] | None]("custom_fields", custom_fields),
                file_part("files", files) if files is not None else None,
                param[list[str] | None]("file_urls", file_urls),
                param[bool | None]("is_eid", is_eid),
                param[str | None]("message", message),
                param[dict[str, Any] | None]("metadata", metadata),
                param[SubSigningOptions | SubSigningOptionsDict | None]("signing_options", signing_options),
                param[str | None]("signing_redirect_url", signing_redirect_url),
                param[str | None]("subject", subject),
                param[bool | None]("test_mode", test_mode),
                param[str | None]("title", title),
            ),
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[SignatureRequestGetResponse],
            error_mapper=signature_request_edit_with_template_error_mapper,
            request_options=request_options,
        )

    async def signature_request_files(
        self,
        signature_request_id: str,
        *,
        file_type: FileTypeOrStr | None = FileType.PDF,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, SignatureRequestFilesErrorBody]:
        """Obtain a copy of the current documents specified by the ``signature_request_id`` parameter. Returns a PDF or
        ZIP file.

        If the files are currently being prepared, a status code of ``409`` will be returned instead.

        Args:
            signature_request_id: The id of the SignatureRequest to retrieve.
            file_type: Set to ``pdf`` for a single merged document or ``zip`` for a collection of individual documents.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/signature_request/files/{signature_request_id}"),
            path_params=[param[str]("signature_request_id", signature_request_id)],
            query_params=[param[FileTypeOrStr | None]("file_type", file_type)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_empty_response,
            error_mapper=signature_request_files_error_mapper,
            request_options=request_options,
        )

    async def signature_request_files_as_data_uri(
        self, signature_request_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FileResponseDataUri, SignatureRequestFilesAsDataUriErrorBody]:
        """Obtain a copy of the current documents specified by the ``signature_request_id`` parameter. Returns a JSON
        object with a ``data_uri`` representing the base64 encoded file (PDFs only).

        If the files are currently being prepared, a status code of ``409`` will be returned instead.

        Args:
            signature_request_id: The id of the SignatureRequest to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/signature_request/files_as_data_uri/{signature_request_id}"),
            path_params=[param[str]("signature_request_id", signature_request_id)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[FileResponseDataUri],
            error_mapper=signature_request_files_as_data_uri_error_mapper,
            request_options=request_options,
        )

    async def signature_request_files_as_file_url(
        self,
        signature_request_id: str,
        *,
        force_download: int | None = 1,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FileResponseModel, SignatureRequestFilesAsFileUrlErrorBody]:
        """Obtain a copy of the current documents specified by the ``signature_request_id`` parameter. Returns a JSON
        object with a url to the file (PDFs only).

        If the files are currently being prepared, a status code of ``409`` will be returned instead.

        Args:
            signature_request_id: The id of the SignatureRequest to retrieve.
            force_download: By default when opening the ``file_url`` a browser will download the PDF and save it
                locally. When set to ``0`` the PDF file will be displayed in the browser.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/signature_request/files_as_file_url/{signature_request_id}"),
            path_params=[param[str]("signature_request_id", signature_request_id)],
            query_params=[param[int | None]("force_download", force_download)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[FileResponseModel],
            error_mapper=signature_request_files_as_file_url_error_mapper,
            request_options=request_options,
        )

    async def signature_request_get(
        self, signature_request_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SignatureRequestGetResponse, SignatureRequestGetErrorBody]:
        """Returns the status of the SignatureRequest specified by the ``signature_request_id`` parameter.

        Args:
            signature_request_id: The id of the SignatureRequest to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/signature_request/{signature_request_id}"),
            path_params=[param[str]("signature_request_id", signature_request_id)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[SignatureRequestGetResponse],
            error_mapper=signature_request_get_error_mapper,
            request_options=request_options,
        )

    async def signature_request_list(
        self,
        *,
        account_id: str | None = None,
        page: int | None = 1,
        page_size: int | None = 20,
        query: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SignatureRequestListResponse, SignatureRequestListErrorBody]:
        """Returns a list of SignatureRequests that you can access. This includes SignatureRequests you have sent as
        well as received, but not ones that you have been CCed on.

        Take a look at our `search guide </api/reference/search/>`__ to learn more about querying signature requests.

        Args:
            account_id: Which account to return SignatureRequests for. Must be a team member. Use ``all`` to indicate
                all team members. Defaults to your account.
            page: Which page number of the SignatureRequest List to return. Defaults to ``1``.
            page_size: Number of objects to be returned per page. Must be between ``1`` and ``100``. Default is ``20``.
            query: String that includes search terms and/or fields to be used to filter the SignatureRequest objects.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/signature_request/list"),
            query_params=[
                param[str | None]("account_id", account_id),
                param[int | None]("page", page),
                param[int | None]("page_size", page_size),
                param[str | None]("query", query),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[SignatureRequestListResponse],
            error_mapper=signature_request_list_error_mapper,
            request_options=request_options,
        )

    async def signature_request_release_hold(
        self, signature_request_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SignatureRequestGetResponse, SignatureRequestReleaseHoldErrorBody]:
        """Releases a held SignatureRequest that was claimed and prepared from an `UnclaimedDraft
        </api/reference/tag/Unclaimed-Draft>`__. The owner of the Draft must indicate at Draft creation that the
        SignatureRequest created from the Draft should be held. Releasing the SignatureRequest will send requests to all
        signers.

        Args:
            signature_request_id: The id of the SignatureRequest to release.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/signature_request/release_hold/{signature_request_id}"),
            path_params=[param[str]("signature_request_id", signature_request_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[SignatureRequestGetResponse],
            error_mapper=signature_request_release_hold_error_mapper,
            request_options=request_options,
        )

    async def signature_request_remind(
        self,
        signature_request_id: str,
        body: SignatureRequestRemindRequest | SignatureRequestRemindRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SignatureRequestGetResponse, SignatureRequestRemindErrorBody]:
        """Sends an email to the signer reminding them to sign the signature request. You cannot send a reminder within
        1 hour of the last reminder that was sent. This includes manual AND automatic reminders.

        **NOTE:** This action can **not** be used with embedded signature requests.

        Args:
            signature_request_id: The id of the SignatureRequest to send a reminder for.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/signature_request/remind/{signature_request_id}"),
            path_params=[param[str]("signature_request_id", signature_request_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SignatureRequestRemindRequest | SignatureRequestRemindRequestDict](body),
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[SignatureRequestGetResponse],
            error_mapper=signature_request_remind_error_mapper,
            request_options=request_options,
        )

    async def signature_request_remove(
        self, signature_request_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, SignatureRequestRemoveErrorBody]:
        """Removes your access to a completed signature request. This action is **not reversible**.

        The signature request must be fully executed by all parties (signed or declined to sign). Other parties will
        continue to maintain access to the completed signature request document(s).

        Unlike /signature_request/cancel, this endpoint is synchronous and your access will be immediately removed. Upon
        successful removal, this endpoint will return a 200 OK response.

        Args:
            signature_request_id: The id of the SignatureRequest to remove.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/signature_request/remove/{signature_request_id}"),
            path_params=[param[str]("signature_request_id", signature_request_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key,
            decoder=async_json_decoder[Any],
            error_mapper=signature_request_remove_error_mapper,
            request_options=request_options,
        )

    async def signature_request_send(
        self,
        *,
        files: AsyncFileInput | None = None,
        file_urls: list[str] | None = None,
        signers: list[SubSignatureRequestSigner | SubSignatureRequestSignerDict] | None = None,
        grouped_signers: list[SubSignatureRequestGroupedSigners | SubSignatureRequestGroupedSignersDict] | None = None,
        allow_decline: bool | None = False,
        allow_reassign: bool | None = False,
        attachments: list[SubAttachment | SubAttachmentDict] | None = None,
        cc_email_addresses: list[EmailStr] | None = None,
        client_id: str | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        field_options: SubFieldOptions | SubFieldOptionsDict | None = None,
        form_field_groups: list[SubFormFieldGroup | SubFormFieldGroupDict] | None = None,
        form_field_rules: list[SubFormFieldRule | SubFormFieldRuleDict] | None = None,
        form_fields_per_document: list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None = None,
        hide_text_tags: bool | None = False,
        is_eid: bool | None = False,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        signing_options: SubSigningOptions | SubSigningOptionsDict | None = None,
        signing_redirect_url: str | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        use_text_tags: bool | None = False,
        ignore_text_tags_extraction_errors: bool | None = False,
        expires_at: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SignatureRequestGetResponse, SignatureRequestSendErrorBody]:
        """Creates and sends a new SignatureRequest with the submitted documents. If ``form_fields_per_document`` is not
        specified, a signature page will be affixed where all signers will be required to add their signature,
        signifying their agreement to all contained documents.

        Args:
            files: Use ``files[]`` to indicate the uploaded file(s) to send for signature. This endpoint requires either
                **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            signers: Add Signers to your Signature Request. This endpoint requires either **signers** or
                **grouped_signers**, but not both.
            grouped_signers: Add Grouped Signers to your Signature Request. This endpoint requires either **signers** or
                **grouped_signers**, but not both.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            allow_reassign: Allows signers to reassign their signature requests to other signers if set to ``true``.
                Defaults to ``false``. **NOTE:** Only available for Premium plan and higher.
            attachments: A list describing the attachments
            cc_email_addresses: The email addresses that should be CCed.
            client_id: The client id of the API App you want to associate with this request. Used to apply the branding
                and callback url defined for the app.
            custom_fields: When used together with merge fields, ``custom_fields`` allows users to add pre-filled data
                to their signature requests. Pre-filled data can be used with "send-once" signature requests by adding
                merge fields with ``form_fields_per_document`` or `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ while passing values back with
                ``custom_fields`` together in one API call. For using pre-filled on repeatable signature requests, merge
                fields are added to templates in the Dropbox Sign UI or by calling `/template/create_embedded_draft
                </api/reference/operation/templateCreateEmbeddedDraft>`__ and then passing ``custom_fields`` on
                subsequent signature requests referencing that template.
            field_options: This allows the requester to specify field options for a signature request.
            form_field_groups: Group information for fields defined in ``form_fields_per_document``. String-indexed JSON
                array with ``group_label`` and ``requirement`` keys. ``form_fields_per_document`` must contain fields
                referencing a group defined in ``form_field_groups``.
            form_field_rules: Conditional Logic rules for fields defined in ``form_fields_per_document``.
            form_fields_per_document: The fields that should appear on the document, expressed as an array of objects.
                (For more details you can read about it here: `Using Form Fields per Document
                </docs/openapi/form-fields-per-document>`__.) **NOTE:** Fields like **text**, **dropdown**,
                **checkbox**, **radio**, and **hyperlink** have additional required and optional parameters. Check out
                the list of `additional parameters </api/reference/constants/#form-fields-per-document>`__ for these
                field types. * Text Field use ``SubFormFieldsPerDocumentText`` * Dropdown Field use
                ``SubFormFieldsPerDocumentDropdown`` * Hyperlink Field use ``SubFormFieldsPerDocumentHyperlink`` *
                Checkbox Field use ``SubFormFieldsPerDocumentCheckbox`` * Radio Field use
                ``SubFormFieldsPerDocumentRadio`` * Signature Field use ``SubFormFieldsPerDocumentSignature`` * Date
                Signed Field use ``SubFormFieldsPerDocumentDateSigned`` * Initials Field use
                ``SubFormFieldsPerDocumentInitials`` * Text Merge Field use ``SubFormFieldsPerDocumentTextMerge`` *
                Checkbox Merge Field use ``SubFormFieldsPerDocumentCheckboxMerge``
            hide_text_tags: Enables automatic Text Tag removal when set to true. **NOTE:** Removing text tags this way
                can cause unwanted clipping. We recommend leaving this setting on ``false`` and instead hiding your text
                tags using white text or a similar approach. See the `Text Tags Walkthrough
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ for more information.
            is_eid: Send with a value of ``true`` if you wish to enable `electronic identification (eID)
                <https://www.hellosign.com/features/electronic-id>`__, which requires the signer to verify their
                identity with an eID provider to sign a document.<br> **NOTE:** You need the eID add-on to use this
                feature. Please `contact sales <https://sign.dropbox.com/form/contact-sales>`__ for more information.
                Cannot be used in ``test_mode``. Only works on requests with one signer.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            signing_options: This allows the requester to specify the types allowed for creating a signature and specify
                another signing options. **NOTE:** If ``signing_options`` are not defined in the request, the allowed
                types will default to those specified in the account settings. **NOTE:** If
                ``force_advanced_signature_details`` is set, allowed types has to be defined too.
            signing_redirect_url: The URL you want signers redirected to after they successfully sign.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request will not be legally binding if set to ``true``.
                Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            use_text_tags: Send with a value of ``true`` if you wish to enable `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ parsing in your document. Defaults
                to disabled, or ``false``.
            ignore_text_tags_extraction_errors: Sent with a value of ``true`` to ignore the validation errors from text
                tags extraction. Defaults to ``false``.
            expires_at: When the signature request will expire. Unsigned signatures will be moved to the expired status,
                and no longer signable. See `Signature Request Expiration Date
                <https://developers.hellosign.com/docs/signature-request/expiration/>`__ for details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/signature_request/send"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(
                file_part("files", files) if files is not None else None,
                param[list[str] | None]("file_urls", file_urls),
                param[list[SubSignatureRequestSigner | SubSignatureRequestSignerDict] | None]("signers", signers),
                param[list[SubSignatureRequestGroupedSigners | SubSignatureRequestGroupedSignersDict] | None](
                    "grouped_signers", grouped_signers
                ),
                param[bool | None]("allow_decline", allow_decline),
                param[bool | None]("allow_reassign", allow_reassign),
                param[list[SubAttachment | SubAttachmentDict] | None]("attachments", attachments),
                param[list[EmailStr] | None]("cc_email_addresses", cc_email_addresses),
                param[str | None]("client_id", client_id),
                param[list[SubCustomField | SubCustomFieldDict] | None]("custom_fields", custom_fields),
                param[SubFieldOptions | SubFieldOptionsDict | None]("field_options", field_options),
                param[list[SubFormFieldGroup | SubFormFieldGroupDict] | None]("form_field_groups", form_field_groups),
                param[list[SubFormFieldRule | SubFormFieldRuleDict] | None]("form_field_rules", form_field_rules),
                param[list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None](
                    "form_fields_per_document", form_fields_per_document
                ),
                param[bool | None]("hide_text_tags", hide_text_tags),
                param[bool | None]("is_eid", is_eid),
                param[str | None]("message", message),
                param[dict[str, Any] | None]("metadata", metadata),
                param[SubSigningOptions | SubSigningOptionsDict | None]("signing_options", signing_options),
                param[str | None]("signing_redirect_url", signing_redirect_url),
                param[str | None]("subject", subject),
                param[bool | None]("test_mode", test_mode),
                param[str | None]("title", title),
                param[bool | None]("use_text_tags", use_text_tags),
                param[bool | None]("ignore_text_tags_extraction_errors", ignore_text_tags_extraction_errors),
                param[int | None]("expires_at", expires_at),
            ),
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[SignatureRequestGetResponse],
            error_mapper=signature_request_send_error_mapper,
            request_options=request_options,
        )

    async def signature_request_send_with_template(
        self,
        template_ids: list[str],
        signers: list[SubSignatureRequestTemplateSigner | SubSignatureRequestTemplateSignerDict],
        *,
        allow_decline: bool | None = False,
        ccs: list[SubCc | SubCcDict] | None = None,
        client_id: str | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        files: AsyncFileInput | None = None,
        file_urls: list[str] | None = None,
        is_eid: bool | None = False,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        signing_options: SubSigningOptions | SubSigningOptionsDict | None = None,
        signing_redirect_url: str | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        expires_at: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SignatureRequestGetResponse, SignatureRequestSendWithTemplateErrorBody]:
        """Creates and sends a new SignatureRequest based off of the Template(s) specified with the ``template_ids``
        parameter.

        Args:
            template_ids: Use ``template_ids`` to create a SignatureRequest from one or more templates, in the order in
                which the template will be used.
            signers: Add Signers to your Templated-based Signature Request.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            ccs: Add CC email recipients. Required when a CC role exists for the Template.
            client_id: Client id of the app to associate with the signature request. Used to apply the branding and
                callback url defined for the app.
            custom_fields: An array defining values and options for custom fields. Required when a custom field exists
                in the Template.
            files: Use ``files[]`` to indicate the uploaded file(s) to send for signature. This endpoint requires either
                **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            is_eid: Send with a value of ``true`` if you wish to enable `electronic identification (eID)
                <https://www.hellosign.com/features/electronic-id>`__, which requires the signer to verify their
                identity with an eID provider to sign a document.<br> **NOTE:** You need the eID add-on to use this
                feature. Please `contact sales <https://sign.dropbox.com/form/contact-sales>`__ for more information.
                Cannot be used in ``test_mode``. Only works on requests with one signer.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            signing_options: This allows the requester to specify the types allowed for creating a signature and specify
                another signing options. **NOTE:** If ``signing_options`` are not defined in the request, the allowed
                types will default to those specified in the account settings. **NOTE:** If
                ``force_advanced_signature_details`` is set, allowed types has to be defined too.
            signing_redirect_url: The URL you want signers redirected to after they successfully sign.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request will not be legally binding if set to ``true``.
                Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            expires_at: When the signature request will expire. Unsigned signatures will be moved to the expired status,
                and no longer signable. See `Signature Request Expiration Date
                <https://developers.hellosign.com/docs/signature-request/expiration/>`__ for details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/signature_request/send_with_template"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(
                param[list[str]]("template_ids", template_ids),
                param[list[SubSignatureRequestTemplateSigner | SubSignatureRequestTemplateSignerDict]](
                    "signers", signers
                ),
                param[bool | None]("allow_decline", allow_decline),
                param[list[SubCc | SubCcDict] | None]("ccs", ccs),
                param[str | None]("client_id", client_id),
                param[list[SubCustomField | SubCustomFieldDict] | None]("custom_fields", custom_fields),
                file_part("files", files) if files is not None else None,
                param[list[str] | None]("file_urls", file_urls),
                param[bool | None]("is_eid", is_eid),
                param[str | None]("message", message),
                param[dict[str, Any] | None]("metadata", metadata),
                param[SubSigningOptions | SubSigningOptionsDict | None]("signing_options", signing_options),
                param[str | None]("signing_redirect_url", signing_redirect_url),
                param[str | None]("subject", subject),
                param[bool | None]("test_mode", test_mode),
                param[str | None]("title", title),
                param[int | None]("expires_at", expires_at),
            ),
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[SignatureRequestGetResponse],
            error_mapper=signature_request_send_with_template_error_mapper,
            request_options=request_options,
        )

    async def signature_request_update(
        self,
        signature_request_id: str,
        body: SignatureRequestUpdateRequest | SignatureRequestUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SignatureRequestGetResponse, SignatureRequestUpdateErrorBody]:
        """Updates the email address and/or the name for a given signer on a signature request. You can listen for the
        ``signature_request_email_bounce`` event on your app or account to detect bounced emails, and respond with this
        method.

        Updating the email address of a signer will generate a new ``signature_id`` value.

        **NOTE:** This action cannot be performed on a signature request with an appended signature page.

        Args:
            signature_request_id: The id of the SignatureRequest to update.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/signature_request/update/{signature_request_id}"),
            path_params=[param[str]("signature_request_id", signature_request_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SignatureRequestUpdateRequest | SignatureRequestUpdateRequestDict](body),
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[SignatureRequestGetResponse],
            error_mapper=signature_request_update_error_mapper,
            request_options=request_options,
        )
