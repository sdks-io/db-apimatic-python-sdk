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
    async_json_decoder,
    file_part,
    json_body,
    json_decoder,
    multipart_body,
    param,
    unwrap,
)
from ..errors.unclaimed_draft_create_embedded_error import (
    UnclaimedDraftCreateEmbeddedErrorBody,
    unclaimed_draft_create_embedded_error_mapper,
)
from ..errors.unclaimed_draft_create_embedded_with_template_error import (
    UnclaimedDraftCreateEmbeddedWithTemplateErrorBody,
    unclaimed_draft_create_embedded_with_template_error_mapper,
)
from ..errors.unclaimed_draft_create_error import UnclaimedDraftCreateErrorBody, unclaimed_draft_create_error_mapper
from ..errors.unclaimed_draft_edit_and_resend_error import (
    UnclaimedDraftEditAndResendErrorBody,
    unclaimed_draft_edit_and_resend_error_mapper,
)
from ..models.enums.type2 import Type2OrStr
from ..models.enums.type3 import Type3, Type3OrStr
from ..models.sub_attachment import SubAttachment, SubAttachmentDict
from ..models.sub_cc import SubCc, SubCcDict
from ..models.sub_custom_field import SubCustomField, SubCustomFieldDict
from ..models.sub_editor_options import SubEditorOptions, SubEditorOptionsDict
from ..models.sub_field_options import SubFieldOptions, SubFieldOptionsDict
from ..models.sub_form_field_group import SubFormFieldGroup, SubFormFieldGroupDict
from ..models.sub_form_field_rule import SubFormFieldRule, SubFormFieldRuleDict
from ..models.sub_signing_options import SubSigningOptions, SubSigningOptionsDict
from ..models.sub_unclaimed_draft_signer import SubUnclaimedDraftSigner, SubUnclaimedDraftSignerDict
from ..models.sub_unclaimed_draft_template_signer import (
    SubUnclaimedDraftTemplateSigner,
    SubUnclaimedDraftTemplateSignerDict,
)
from ..models.unclaimed_draft_create_response import UnclaimedDraftCreateResponse
from ..models.unclaimed_draft_edit_and_resend_request import (
    UnclaimedDraftEditAndResendRequest,
    UnclaimedDraftEditAndResendRequestDict,
)
from ..models.unions.sub_form_fields_per_document_base import (
    SubFormFieldsPerDocumentBase,
    SubFormFieldsPerDocumentBaseDict,
)
from ..server.server import Server


class UnclaimedDraft:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = UnclaimedDraftWithRawResponse(client, server, auth)

    def unclaimed_draft_create(
        self,
        type_: Type2OrStr,
        *,
        files: FileInput | None = None,
        file_urls: list[str] | None = None,
        allow_decline: bool | None = False,
        attachments: list[SubAttachment | SubAttachmentDict] | None = None,
        cc_email_addresses: list[EmailStr] | None = None,
        client_id: str | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        field_options: SubFieldOptions | SubFieldOptionsDict | None = None,
        form_field_groups: list[SubFormFieldGroup | SubFormFieldGroupDict] | None = None,
        form_field_rules: list[SubFormFieldRule | SubFormFieldRuleDict] | None = None,
        form_fields_per_document: list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None = None,
        hide_text_tags: bool | None = False,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        show_progress_stepper: bool | None = True,
        signers: list[SubUnclaimedDraftSigner | SubUnclaimedDraftSignerDict] | None = None,
        signing_options: SubSigningOptions | SubSigningOptionsDict | None = None,
        signing_redirect_url: str | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        use_preexisting_fields: bool | None = False,
        use_text_tags: bool | None = False,
        ignore_text_tags_extraction_errors: bool | None = False,
        expires_at: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UnclaimedDraftCreateResponse:
        """Creates a new Draft that can be claimed using the claim URL. The first authenticated user to access the URL
        will claim the Draft and will be shown either the "Sign and send" or the "Request signature" page with the Draft
        loaded. Subsequent access to the claim URL will result in a 404.

        Args:
            type_: The type of unclaimed draft to create. Use ``send_document`` to create a claimable file, and
                ``request_signature`` for a claimable signature request. If the type is ``request_signature`` then
                signers name and email_address are not optional.
            files: Use ``files[]`` to indicate the uploaded file(s) to send for signature. This endpoint requires either
                **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            attachments: A list describing the attachments
            cc_email_addresses: The email addresses that should be CCed.
            client_id: Client id of the app used to create the draft. Used to apply the branding and callback url
                defined for the app.
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
            hide_text_tags: Send with a value of ``true`` if you wish to enable automatic Text Tag removal. Defaults to
                ``false``. When using Text Tags it is preferred that you set this to ``false`` and hide your tags with
                white text or something similar because the automatic removal system can cause unwanted clipping. See
                the `Text Tags <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ walkthrough for more
                details.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            show_progress_stepper: When only one step remains in the signature request process and this parameter is set
                to ``false`` then the progress stepper will be hidden.
            signers: Add Signers to your Unclaimed Draft Signature Request.
            signing_options: This allows the requester to specify the types allowed for creating a signature and specify
                another signing options. **NOTE:** If ``signing_options`` are not defined in the request, the allowed
                types will default to those specified in the account settings. **NOTE:** If
                ``force_advanced_signature_details`` is set, allowed types has to be defined too.
            signing_redirect_url: The URL you want signers redirected to after they successfully sign.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request created from this draft will not be legally binding
                if set to ``true``. Defaults to ``false``.
            use_preexisting_fields: Set ``use_text_tags`` to ``true`` to enable `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ parsing in your document (defaults
                to disabled, or ``false``). Alternatively, if your PDF contains pre-defined fields, enable the detection
                of these fields by setting the ``use_preexisting_fields`` to ``true`` (defaults to disabled, or
                ``false``). Currently we only support use of either ``use_text_tags`` or ``use_preexisting_fields``
                parameter, not both.
            use_text_tags: Set ``use_text_tags`` to ``true`` to enable `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ parsing in your document (defaults
                to disabled, or ``false``). Alternatively, if your PDF contains pre-defined fields, enable the detection
                of these fields by setting the ``use_preexisting_fields`` to ``true`` (defaults to disabled, or
                ``false``). Currently we only support use of either ``use_text_tags`` or ``use_preexisting_fields``
                parameter, not both.
            ignore_text_tags_extraction_errors: Sent with a value of ``true`` to ignore the validation errors from text
                tags extraction. Defaults to ``false``.
            expires_at: When the signature request will expire. Unsigned signatures will be moved to the expired status,
                and no longer signable. See `Signature Request Expiration Date
                <https://developers.hellosign.com/docs/signature-request/expiration/>`__ for details. **NOTE:** This
                does not correspond to the **expires_at** returned in the response.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.unclaimed_draft_create(
                type_,
                files=files,
                file_urls=file_urls,
                allow_decline=allow_decline,
                attachments=attachments,
                cc_email_addresses=cc_email_addresses,
                client_id=client_id,
                custom_fields=custom_fields,
                field_options=field_options,
                form_field_groups=form_field_groups,
                form_field_rules=form_field_rules,
                form_fields_per_document=form_fields_per_document,
                hide_text_tags=hide_text_tags,
                message=message,
                metadata=metadata,
                show_progress_stepper=show_progress_stepper,
                signers=signers,
                signing_options=signing_options,
                signing_redirect_url=signing_redirect_url,
                subject=subject,
                test_mode=test_mode,
                use_preexisting_fields=use_preexisting_fields,
                use_text_tags=use_text_tags,
                ignore_text_tags_extraction_errors=ignore_text_tags_extraction_errors,
                expires_at=expires_at,
                request_options=request_options,
            ),
        )

    def unclaimed_draft_create_embedded(
        self,
        client_id: str,
        requester_email_address: EmailStr,
        *,
        files: FileInput | None = None,
        file_urls: list[str] | None = None,
        allow_ccs: bool | None = True,
        allow_decline: bool | None = False,
        allow_reassign: bool | None = False,
        attachments: list[SubAttachment | SubAttachmentDict] | None = None,
        cc_email_addresses: list[EmailStr] | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        editor_options: SubEditorOptions | SubEditorOptionsDict | None = None,
        field_options: SubFieldOptions | SubFieldOptionsDict | None = None,
        force_signer_page: bool | None = False,
        force_subject_message: bool | None = False,
        form_field_groups: list[SubFormFieldGroup | SubFormFieldGroupDict] | None = None,
        form_field_rules: list[SubFormFieldRule | SubFormFieldRuleDict] | None = None,
        form_fields_per_document: list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None = None,
        hide_text_tags: bool | None = False,
        hold_request: bool | None = False,
        is_for_embedded_signing: bool | None = False,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        requesting_redirect_url: str | None = None,
        show_preview: bool | None = None,
        show_progress_stepper: bool | None = True,
        signers: list[SubUnclaimedDraftSigner | SubUnclaimedDraftSignerDict] | None = None,
        signing_options: SubSigningOptions | SubSigningOptionsDict | None = None,
        signing_redirect_url: str | None = None,
        skip_me_now: bool | None = False,
        subject: str | None = None,
        test_mode: bool | None = False,
        type_: Type3OrStr | None = Type3.REQUEST_SIGNATURE,
        use_preexisting_fields: bool | None = False,
        use_text_tags: bool | None = False,
        ignore_text_tags_extraction_errors: bool | None = False,
        populate_auto_fill_fields: bool | None = False,
        expires_at: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UnclaimedDraftCreateResponse:
        """Creates a new Draft that can be claimed and used in an embedded iFrame. The first authenticated user to
        access the URL will claim the Draft and will be shown the "Request signature" page with the Draft loaded.
        Subsequent access to the claim URL will result in a ``404``. For this embedded endpoint the
        ``requester_email_address`` parameter is required.

        **NOTE:** Embedded unclaimed drafts can only be accessed in embedded iFrames whereas normal drafts can be used
        and accessed on Dropbox Sign.

        Args:
            client_id: Client id of the app used to create the draft. Used to apply the branding and callback url
                defined for the app.
            requester_email_address: The email address of the user that should be designated as the requester of this
                draft, if the draft type is ``request_signature``.
            files: Use ``files[]`` to indicate the uploaded file(s) to send for signature. This endpoint requires either
                **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            allow_ccs: This allows the requester to specify whether the user is allowed to provide email addresses to CC
                when claiming the draft.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            allow_reassign: Allows signers to reassign their signature requests to other signers if set to ``true``.
                Defaults to ``false``. **NOTE:** Only available for Premium plan and higher.
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
            editor_options: This allows the requester to specify editor options when a preparing a document
            field_options: This allows the requester to specify field options for a signature request.
            force_signer_page: Provide users the ability to review/edit the signers.
            force_subject_message: Provide users the ability to review/edit the subject and message.
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
            hide_text_tags: Send with a value of ``true`` if you wish to enable automatic Text Tag removal. Defaults to
                ``false``. When using Text Tags it is preferred that you set this to ``false`` and hide your tags with
                white text or something similar because the automatic removal system can cause unwanted clipping. See
                the `Text Tags <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ walkthrough for more
                details.
            hold_request: The request from this draft will not automatically send to signers post-claim if set to
                ``true``. Requester must `release </api/reference/operation/signatureRequestReleaseHold/>`__ the request
                from hold when ready to send. Defaults to ``false``.
            is_for_embedded_signing: The request created from this draft will also be signable in embedded mode if set
                to ``true``. Defaults to ``false``.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            requesting_redirect_url: The URL you want signers redirected to after they successfully request a signature.
            show_preview: This allows the requester to enable the editor/preview experience. - ``show_preview=true``:
                Allows requesters to enable the editor/preview experience. - ``show_preview=false``: Allows requesters
                to disable the editor/preview experience.
            show_progress_stepper: When only one step remains in the signature request process and this parameter is set
                to ``false`` then the progress stepper will be hidden.
            signers: Add Signers to your Unclaimed Draft Signature Request.
            signing_options: This allows the requester to specify the types allowed for creating a signature and specify
                another signing options. **NOTE:** If ``signing_options`` are not defined in the request, the allowed
                types will default to those specified in the account settings. **NOTE:** If
                ``force_advanced_signature_details`` is set, allowed types has to be defined too.
            signing_redirect_url: The URL you want signers redirected to after they successfully sign.
            skip_me_now: Disables the "Me (Now)" option for the person preparing the document. Does not work with type
                ``send_document``. Defaults to ``false``.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request created from this draft will not be legally binding
                if set to ``true``. Defaults to ``false``.
            type_: The type of the draft. By default this is ``request_signature``, but you can set it to
                ``send_document`` if you want to self sign a document and download it.
            use_preexisting_fields: Set ``use_text_tags`` to ``true`` to enable `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ parsing in your document (defaults
                to disabled, or ``false``). Alternatively, if your PDF contains pre-defined fields, enable the detection
                of these fields by setting the ``use_preexisting_fields`` to ``true`` (defaults to disabled, or
                ``false``). Currently we only support use of either ``use_text_tags`` or ``use_preexisting_fields``
                parameter, not both.
            use_text_tags: Set ``use_text_tags`` to ``true`` to enable `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ parsing in your document (defaults
                to disabled, or ``false``). Alternatively, if your PDF contains pre-defined fields, enable the detection
                of these fields by setting the ``use_preexisting_fields`` to ``true`` (defaults to disabled, or
                ``false``). Currently we only support use of either ``use_text_tags`` or ``use_preexisting_fields``
                parameter, not both.
            ignore_text_tags_extraction_errors: Sent with a value of ``true`` to ignore the validation errors from text
                tags extraction. Defaults to ``false``.
            populate_auto_fill_fields: Controls whether `auto fill fields
                <https://faq.hellosign.com/hc/en-us/articles/360051467511-Auto-Fill-Fields>`__ can automatically
                populate a signer's information during signing. **NOTE:** Keep your signer's information safe by
                ensuring that the _signer on your signature request is the intended party_ before using this feature.
            expires_at: When the signature request will expire. Unsigned signatures will be moved to the expired status,
                and no longer signable. See `Signature Request Expiration Date
                <https://developers.hellosign.com/docs/signature-request/expiration/>`__ for details. **NOTE:** This
                does not correspond to the **expires_at** returned in the response.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.unclaimed_draft_create_embedded(
                client_id,
                requester_email_address,
                files=files,
                file_urls=file_urls,
                allow_ccs=allow_ccs,
                allow_decline=allow_decline,
                allow_reassign=allow_reassign,
                attachments=attachments,
                cc_email_addresses=cc_email_addresses,
                custom_fields=custom_fields,
                editor_options=editor_options,
                field_options=field_options,
                force_signer_page=force_signer_page,
                force_subject_message=force_subject_message,
                form_field_groups=form_field_groups,
                form_field_rules=form_field_rules,
                form_fields_per_document=form_fields_per_document,
                hide_text_tags=hide_text_tags,
                hold_request=hold_request,
                is_for_embedded_signing=is_for_embedded_signing,
                message=message,
                metadata=metadata,
                requesting_redirect_url=requesting_redirect_url,
                show_preview=show_preview,
                show_progress_stepper=show_progress_stepper,
                signers=signers,
                signing_options=signing_options,
                signing_redirect_url=signing_redirect_url,
                skip_me_now=skip_me_now,
                subject=subject,
                test_mode=test_mode,
                type_=type_,
                use_preexisting_fields=use_preexisting_fields,
                use_text_tags=use_text_tags,
                ignore_text_tags_extraction_errors=ignore_text_tags_extraction_errors,
                populate_auto_fill_fields=populate_auto_fill_fields,
                expires_at=expires_at,
                request_options=request_options,
            ),
        )

    def unclaimed_draft_create_embedded_with_template(
        self,
        client_id: str,
        requester_email_address: EmailStr,
        template_ids: list[str],
        *,
        allow_decline: bool | None = False,
        allow_reassign: bool | None = False,
        ccs: list[SubCc | SubCcDict] | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        editor_options: SubEditorOptions | SubEditorOptionsDict | None = None,
        field_options: SubFieldOptions | SubFieldOptionsDict | None = None,
        files: FileInput | None = None,
        file_urls: list[str] | None = None,
        force_signer_roles: bool | None = False,
        force_subject_message: bool | None = False,
        hold_request: bool | None = False,
        is_for_embedded_signing: bool | None = False,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        preview_only: bool | None = False,
        requesting_redirect_url: str | None = None,
        show_preview: bool | None = False,
        show_progress_stepper: bool | None = True,
        signers: list[SubUnclaimedDraftTemplateSigner | SubUnclaimedDraftTemplateSignerDict] | None = None,
        signing_options: SubSigningOptions | SubSigningOptionsDict | None = None,
        signing_redirect_url: str | None = None,
        skip_me_now: bool | None = False,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        populate_auto_fill_fields: bool | None = False,
        allow_ccs: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UnclaimedDraftCreateResponse:
        """Creates a new Draft with a previously saved template(s) that can be claimed and used in an embedded iFrame.
        The first authenticated user to access the URL will claim the Draft and will be shown the "Request signature"
        page with the Draft loaded. Subsequent access to the claim URL will result in a ``404``. For this embedded
        endpoint the ``requester_email_address`` parameter is required.

        **NOTE:** Embedded unclaimed drafts can only be accessed in embedded iFrames whereas normal drafts can be used
        and accessed on Dropbox Sign.

        Args:
            client_id: Client id of the app used to create the draft. Used to apply the branding and callback url
                defined for the app.
            requester_email_address: The email address of the user that should be designated as the requester of this
                draft.
            template_ids: Use ``template_ids`` to create a SignatureRequest from one or more templates, in the order in
                which the templates will be used.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            allow_reassign: Allows signers to reassign their signature requests to other signers if set to ``true``.
                Defaults to ``false``. **NOTE:** Only available for Premium plan and higher.
            ccs: Add CC email recipients. Required when a CC role exists for the Template.
            custom_fields: An array defining values and options for custom fields. Required when a custom field exists
                in the Template.
            editor_options: This allows the requester to specify editor options when a preparing a document
            field_options: This allows the requester to specify field options for a signature request.
            files: Use ``files[]`` to append additional files to the signature request being created from the template.
                Dropbox Sign will parse the files for `text tags <https://app.hellosign.com/api/textTagsWalkthrough>`__
                and append it to the signature request. Text tags for signers not on the template(s) will be ignored.
                **files** or **file_urls[]** is required, but not both.
            file_urls: Use file_urls[] to append additional files to the signature request being created from the
                template. Dropbox Sign will download the file, then parse it for `text tags
                <https://app.hellosign.com/api/textTagsWalkthrough>`__, and append to the signature request. Text tags
                for signers not on the template(s) will be ignored. **files** or **file_urls[]** is required, but not
                both.
            force_signer_roles: Provide users the ability to review/edit the template signer roles.
            force_subject_message: Provide users the ability to review/edit the template subject and message.
            hold_request: The request from this draft will not automatically send to signers post-claim if set to 1.
                Requester must `release </api/reference/operation/signatureRequestReleaseHold/>`__ the request from hold
                when ready to send. Defaults to ``false``.
            is_for_embedded_signing: The request created from this draft will also be signable in embedded mode if set
                to ``true``. Defaults to ``false``.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            preview_only: This allows the requester to enable the preview experience (i.e. does not allow the
                requester's end user to add any additional fields via the editor). - ``preview_only=true``: Allows
                requesters to enable the preview only experience. - ``preview_only=false``: Allows requesters to disable
                the preview only experience. **NOTE:** This parameter overwrites ``show_preview=1`` (if set).
            requesting_redirect_url: The URL you want signers redirected to after they successfully request a signature.
            show_preview: This allows the requester to enable the editor/preview experience. - ``show_preview=true``:
                Allows requesters to enable the editor/preview experience. - ``show_preview=false``: Allows requesters
                to disable the editor/preview experience.
            show_progress_stepper: When only one step remains in the signature request process and this parameter is set
                to ``false`` then the progress stepper will be hidden.
            signers: Add Signers to your Templated-based Signature Request.
            signing_options: This allows the requester to specify the types allowed for creating a signature and specify
                another signing options. **NOTE:** If ``signing_options`` are not defined in the request, the allowed
                types will default to those specified in the account settings. **NOTE:** If
                ``force_advanced_signature_details`` is set, allowed types has to be defined too.
            signing_redirect_url: The URL you want signers redirected to after they successfully sign.
            skip_me_now: Disables the "Me (Now)" option for the person preparing the document. Does not work with type
                ``send_document``. Defaults to ``false``.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request created from this draft will not be legally binding
                if set to ``true``. Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            populate_auto_fill_fields: Controls whether `auto fill fields
                <https://faq.hellosign.com/hc/en-us/articles/360051467511-Auto-Fill-Fields>`__ can automatically
                populate a signer's information during signing. **NOTE:** Keep your signer's information safe by
                ensuring that the _signer on your signature request is the intended party_ before using this feature.
            allow_ccs: This allows the requester to specify whether the user is allowed to provide email addresses to CC
                when claiming the draft.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.unclaimed_draft_create_embedded_with_template(
                client_id,
                requester_email_address,
                template_ids,
                allow_decline=allow_decline,
                allow_reassign=allow_reassign,
                ccs=ccs,
                custom_fields=custom_fields,
                editor_options=editor_options,
                field_options=field_options,
                files=files,
                file_urls=file_urls,
                force_signer_roles=force_signer_roles,
                force_subject_message=force_subject_message,
                hold_request=hold_request,
                is_for_embedded_signing=is_for_embedded_signing,
                message=message,
                metadata=metadata,
                preview_only=preview_only,
                requesting_redirect_url=requesting_redirect_url,
                show_preview=show_preview,
                show_progress_stepper=show_progress_stepper,
                signers=signers,
                signing_options=signing_options,
                signing_redirect_url=signing_redirect_url,
                skip_me_now=skip_me_now,
                subject=subject,
                test_mode=test_mode,
                title=title,
                populate_auto_fill_fields=populate_auto_fill_fields,
                allow_ccs=allow_ccs,
                request_options=request_options,
            ),
        )

    def unclaimed_draft_edit_and_resend(
        self,
        signature_request_id: str,
        body: UnclaimedDraftEditAndResendRequest | UnclaimedDraftEditAndResendRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UnclaimedDraftCreateResponse:
        """Creates a new signature request from an embedded request that can be edited prior to being sent to the
        recipients. Parameter ``test_mode`` can be edited prior to request. Signers can be edited in embedded editor.
        Requester's email address will remain unchanged if ``requester_email_address`` parameter is not set.

        **NOTE:** Embedded unclaimed drafts can only be accessed in embedded iFrames whereas normal drafts can be used
        and accessed on Dropbox Sign.

        Args:
            signature_request_id: The ID of the signature request to edit and resend.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.unclaimed_draft_edit_and_resend(
                signature_request_id, body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> UnclaimedDraftWithRawResponse:
        return self._with_raw_response


class AsyncUnclaimedDraft:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncUnclaimedDraftWithRawResponse(client, server, auth)

    async def unclaimed_draft_create(
        self,
        type_: Type2OrStr,
        *,
        files: AsyncFileInput | None = None,
        file_urls: list[str] | None = None,
        allow_decline: bool | None = False,
        attachments: list[SubAttachment | SubAttachmentDict] | None = None,
        cc_email_addresses: list[EmailStr] | None = None,
        client_id: str | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        field_options: SubFieldOptions | SubFieldOptionsDict | None = None,
        form_field_groups: list[SubFormFieldGroup | SubFormFieldGroupDict] | None = None,
        form_field_rules: list[SubFormFieldRule | SubFormFieldRuleDict] | None = None,
        form_fields_per_document: list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None = None,
        hide_text_tags: bool | None = False,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        show_progress_stepper: bool | None = True,
        signers: list[SubUnclaimedDraftSigner | SubUnclaimedDraftSignerDict] | None = None,
        signing_options: SubSigningOptions | SubSigningOptionsDict | None = None,
        signing_redirect_url: str | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        use_preexisting_fields: bool | None = False,
        use_text_tags: bool | None = False,
        ignore_text_tags_extraction_errors: bool | None = False,
        expires_at: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UnclaimedDraftCreateResponse:
        """Creates a new Draft that can be claimed using the claim URL. The first authenticated user to access the URL
        will claim the Draft and will be shown either the "Sign and send" or the "Request signature" page with the Draft
        loaded. Subsequent access to the claim URL will result in a 404.

        Args:
            type_: The type of unclaimed draft to create. Use ``send_document`` to create a claimable file, and
                ``request_signature`` for a claimable signature request. If the type is ``request_signature`` then
                signers name and email_address are not optional.
            files: Use ``files[]`` to indicate the uploaded file(s) to send for signature. This endpoint requires either
                **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            attachments: A list describing the attachments
            cc_email_addresses: The email addresses that should be CCed.
            client_id: Client id of the app used to create the draft. Used to apply the branding and callback url
                defined for the app.
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
            hide_text_tags: Send with a value of ``true`` if you wish to enable automatic Text Tag removal. Defaults to
                ``false``. When using Text Tags it is preferred that you set this to ``false`` and hide your tags with
                white text or something similar because the automatic removal system can cause unwanted clipping. See
                the `Text Tags <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ walkthrough for more
                details.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            show_progress_stepper: When only one step remains in the signature request process and this parameter is set
                to ``false`` then the progress stepper will be hidden.
            signers: Add Signers to your Unclaimed Draft Signature Request.
            signing_options: This allows the requester to specify the types allowed for creating a signature and specify
                another signing options. **NOTE:** If ``signing_options`` are not defined in the request, the allowed
                types will default to those specified in the account settings. **NOTE:** If
                ``force_advanced_signature_details`` is set, allowed types has to be defined too.
            signing_redirect_url: The URL you want signers redirected to after they successfully sign.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request created from this draft will not be legally binding
                if set to ``true``. Defaults to ``false``.
            use_preexisting_fields: Set ``use_text_tags`` to ``true`` to enable `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ parsing in your document (defaults
                to disabled, or ``false``). Alternatively, if your PDF contains pre-defined fields, enable the detection
                of these fields by setting the ``use_preexisting_fields`` to ``true`` (defaults to disabled, or
                ``false``). Currently we only support use of either ``use_text_tags`` or ``use_preexisting_fields``
                parameter, not both.
            use_text_tags: Set ``use_text_tags`` to ``true`` to enable `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ parsing in your document (defaults
                to disabled, or ``false``). Alternatively, if your PDF contains pre-defined fields, enable the detection
                of these fields by setting the ``use_preexisting_fields`` to ``true`` (defaults to disabled, or
                ``false``). Currently we only support use of either ``use_text_tags`` or ``use_preexisting_fields``
                parameter, not both.
            ignore_text_tags_extraction_errors: Sent with a value of ``true`` to ignore the validation errors from text
                tags extraction. Defaults to ``false``.
            expires_at: When the signature request will expire. Unsigned signatures will be moved to the expired status,
                and no longer signable. See `Signature Request Expiration Date
                <https://developers.hellosign.com/docs/signature-request/expiration/>`__ for details. **NOTE:** This
                does not correspond to the **expires_at** returned in the response.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.unclaimed_draft_create(
                type_,
                files=files,
                file_urls=file_urls,
                allow_decline=allow_decline,
                attachments=attachments,
                cc_email_addresses=cc_email_addresses,
                client_id=client_id,
                custom_fields=custom_fields,
                field_options=field_options,
                form_field_groups=form_field_groups,
                form_field_rules=form_field_rules,
                form_fields_per_document=form_fields_per_document,
                hide_text_tags=hide_text_tags,
                message=message,
                metadata=metadata,
                show_progress_stepper=show_progress_stepper,
                signers=signers,
                signing_options=signing_options,
                signing_redirect_url=signing_redirect_url,
                subject=subject,
                test_mode=test_mode,
                use_preexisting_fields=use_preexisting_fields,
                use_text_tags=use_text_tags,
                ignore_text_tags_extraction_errors=ignore_text_tags_extraction_errors,
                expires_at=expires_at,
                request_options=request_options,
            ),
        )

    async def unclaimed_draft_create_embedded(
        self,
        client_id: str,
        requester_email_address: EmailStr,
        *,
        files: AsyncFileInput | None = None,
        file_urls: list[str] | None = None,
        allow_ccs: bool | None = True,
        allow_decline: bool | None = False,
        allow_reassign: bool | None = False,
        attachments: list[SubAttachment | SubAttachmentDict] | None = None,
        cc_email_addresses: list[EmailStr] | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        editor_options: SubEditorOptions | SubEditorOptionsDict | None = None,
        field_options: SubFieldOptions | SubFieldOptionsDict | None = None,
        force_signer_page: bool | None = False,
        force_subject_message: bool | None = False,
        form_field_groups: list[SubFormFieldGroup | SubFormFieldGroupDict] | None = None,
        form_field_rules: list[SubFormFieldRule | SubFormFieldRuleDict] | None = None,
        form_fields_per_document: list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None = None,
        hide_text_tags: bool | None = False,
        hold_request: bool | None = False,
        is_for_embedded_signing: bool | None = False,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        requesting_redirect_url: str | None = None,
        show_preview: bool | None = None,
        show_progress_stepper: bool | None = True,
        signers: list[SubUnclaimedDraftSigner | SubUnclaimedDraftSignerDict] | None = None,
        signing_options: SubSigningOptions | SubSigningOptionsDict | None = None,
        signing_redirect_url: str | None = None,
        skip_me_now: bool | None = False,
        subject: str | None = None,
        test_mode: bool | None = False,
        type_: Type3OrStr | None = Type3.REQUEST_SIGNATURE,
        use_preexisting_fields: bool | None = False,
        use_text_tags: bool | None = False,
        ignore_text_tags_extraction_errors: bool | None = False,
        populate_auto_fill_fields: bool | None = False,
        expires_at: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UnclaimedDraftCreateResponse:
        """Creates a new Draft that can be claimed and used in an embedded iFrame. The first authenticated user to
        access the URL will claim the Draft and will be shown the "Request signature" page with the Draft loaded.
        Subsequent access to the claim URL will result in a ``404``. For this embedded endpoint the
        ``requester_email_address`` parameter is required.

        **NOTE:** Embedded unclaimed drafts can only be accessed in embedded iFrames whereas normal drafts can be used
        and accessed on Dropbox Sign.

        Args:
            client_id: Client id of the app used to create the draft. Used to apply the branding and callback url
                defined for the app.
            requester_email_address: The email address of the user that should be designated as the requester of this
                draft, if the draft type is ``request_signature``.
            files: Use ``files[]`` to indicate the uploaded file(s) to send for signature. This endpoint requires either
                **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            allow_ccs: This allows the requester to specify whether the user is allowed to provide email addresses to CC
                when claiming the draft.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            allow_reassign: Allows signers to reassign their signature requests to other signers if set to ``true``.
                Defaults to ``false``. **NOTE:** Only available for Premium plan and higher.
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
            editor_options: This allows the requester to specify editor options when a preparing a document
            field_options: This allows the requester to specify field options for a signature request.
            force_signer_page: Provide users the ability to review/edit the signers.
            force_subject_message: Provide users the ability to review/edit the subject and message.
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
            hide_text_tags: Send with a value of ``true`` if you wish to enable automatic Text Tag removal. Defaults to
                ``false``. When using Text Tags it is preferred that you set this to ``false`` and hide your tags with
                white text or something similar because the automatic removal system can cause unwanted clipping. See
                the `Text Tags <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ walkthrough for more
                details.
            hold_request: The request from this draft will not automatically send to signers post-claim if set to
                ``true``. Requester must `release </api/reference/operation/signatureRequestReleaseHold/>`__ the request
                from hold when ready to send. Defaults to ``false``.
            is_for_embedded_signing: The request created from this draft will also be signable in embedded mode if set
                to ``true``. Defaults to ``false``.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            requesting_redirect_url: The URL you want signers redirected to after they successfully request a signature.
            show_preview: This allows the requester to enable the editor/preview experience. - ``show_preview=true``:
                Allows requesters to enable the editor/preview experience. - ``show_preview=false``: Allows requesters
                to disable the editor/preview experience.
            show_progress_stepper: When only one step remains in the signature request process and this parameter is set
                to ``false`` then the progress stepper will be hidden.
            signers: Add Signers to your Unclaimed Draft Signature Request.
            signing_options: This allows the requester to specify the types allowed for creating a signature and specify
                another signing options. **NOTE:** If ``signing_options`` are not defined in the request, the allowed
                types will default to those specified in the account settings. **NOTE:** If
                ``force_advanced_signature_details`` is set, allowed types has to be defined too.
            signing_redirect_url: The URL you want signers redirected to after they successfully sign.
            skip_me_now: Disables the "Me (Now)" option for the person preparing the document. Does not work with type
                ``send_document``. Defaults to ``false``.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request created from this draft will not be legally binding
                if set to ``true``. Defaults to ``false``.
            type_: The type of the draft. By default this is ``request_signature``, but you can set it to
                ``send_document`` if you want to self sign a document and download it.
            use_preexisting_fields: Set ``use_text_tags`` to ``true`` to enable `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ parsing in your document (defaults
                to disabled, or ``false``). Alternatively, if your PDF contains pre-defined fields, enable the detection
                of these fields by setting the ``use_preexisting_fields`` to ``true`` (defaults to disabled, or
                ``false``). Currently we only support use of either ``use_text_tags`` or ``use_preexisting_fields``
                parameter, not both.
            use_text_tags: Set ``use_text_tags`` to ``true`` to enable `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ parsing in your document (defaults
                to disabled, or ``false``). Alternatively, if your PDF contains pre-defined fields, enable the detection
                of these fields by setting the ``use_preexisting_fields`` to ``true`` (defaults to disabled, or
                ``false``). Currently we only support use of either ``use_text_tags`` or ``use_preexisting_fields``
                parameter, not both.
            ignore_text_tags_extraction_errors: Sent with a value of ``true`` to ignore the validation errors from text
                tags extraction. Defaults to ``false``.
            populate_auto_fill_fields: Controls whether `auto fill fields
                <https://faq.hellosign.com/hc/en-us/articles/360051467511-Auto-Fill-Fields>`__ can automatically
                populate a signer's information during signing. **NOTE:** Keep your signer's information safe by
                ensuring that the _signer on your signature request is the intended party_ before using this feature.
            expires_at: When the signature request will expire. Unsigned signatures will be moved to the expired status,
                and no longer signable. See `Signature Request Expiration Date
                <https://developers.hellosign.com/docs/signature-request/expiration/>`__ for details. **NOTE:** This
                does not correspond to the **expires_at** returned in the response.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.unclaimed_draft_create_embedded(
                client_id,
                requester_email_address,
                files=files,
                file_urls=file_urls,
                allow_ccs=allow_ccs,
                allow_decline=allow_decline,
                allow_reassign=allow_reassign,
                attachments=attachments,
                cc_email_addresses=cc_email_addresses,
                custom_fields=custom_fields,
                editor_options=editor_options,
                field_options=field_options,
                force_signer_page=force_signer_page,
                force_subject_message=force_subject_message,
                form_field_groups=form_field_groups,
                form_field_rules=form_field_rules,
                form_fields_per_document=form_fields_per_document,
                hide_text_tags=hide_text_tags,
                hold_request=hold_request,
                is_for_embedded_signing=is_for_embedded_signing,
                message=message,
                metadata=metadata,
                requesting_redirect_url=requesting_redirect_url,
                show_preview=show_preview,
                show_progress_stepper=show_progress_stepper,
                signers=signers,
                signing_options=signing_options,
                signing_redirect_url=signing_redirect_url,
                skip_me_now=skip_me_now,
                subject=subject,
                test_mode=test_mode,
                type_=type_,
                use_preexisting_fields=use_preexisting_fields,
                use_text_tags=use_text_tags,
                ignore_text_tags_extraction_errors=ignore_text_tags_extraction_errors,
                populate_auto_fill_fields=populate_auto_fill_fields,
                expires_at=expires_at,
                request_options=request_options,
            ),
        )

    async def unclaimed_draft_create_embedded_with_template(
        self,
        client_id: str,
        requester_email_address: EmailStr,
        template_ids: list[str],
        *,
        allow_decline: bool | None = False,
        allow_reassign: bool | None = False,
        ccs: list[SubCc | SubCcDict] | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        editor_options: SubEditorOptions | SubEditorOptionsDict | None = None,
        field_options: SubFieldOptions | SubFieldOptionsDict | None = None,
        files: AsyncFileInput | None = None,
        file_urls: list[str] | None = None,
        force_signer_roles: bool | None = False,
        force_subject_message: bool | None = False,
        hold_request: bool | None = False,
        is_for_embedded_signing: bool | None = False,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        preview_only: bool | None = False,
        requesting_redirect_url: str | None = None,
        show_preview: bool | None = False,
        show_progress_stepper: bool | None = True,
        signers: list[SubUnclaimedDraftTemplateSigner | SubUnclaimedDraftTemplateSignerDict] | None = None,
        signing_options: SubSigningOptions | SubSigningOptionsDict | None = None,
        signing_redirect_url: str | None = None,
        skip_me_now: bool | None = False,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        populate_auto_fill_fields: bool | None = False,
        allow_ccs: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UnclaimedDraftCreateResponse:
        """Creates a new Draft with a previously saved template(s) that can be claimed and used in an embedded iFrame.
        The first authenticated user to access the URL will claim the Draft and will be shown the "Request signature"
        page with the Draft loaded. Subsequent access to the claim URL will result in a ``404``. For this embedded
        endpoint the ``requester_email_address`` parameter is required.

        **NOTE:** Embedded unclaimed drafts can only be accessed in embedded iFrames whereas normal drafts can be used
        and accessed on Dropbox Sign.

        Args:
            client_id: Client id of the app used to create the draft. Used to apply the branding and callback url
                defined for the app.
            requester_email_address: The email address of the user that should be designated as the requester of this
                draft.
            template_ids: Use ``template_ids`` to create a SignatureRequest from one or more templates, in the order in
                which the templates will be used.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            allow_reassign: Allows signers to reassign their signature requests to other signers if set to ``true``.
                Defaults to ``false``. **NOTE:** Only available for Premium plan and higher.
            ccs: Add CC email recipients. Required when a CC role exists for the Template.
            custom_fields: An array defining values and options for custom fields. Required when a custom field exists
                in the Template.
            editor_options: This allows the requester to specify editor options when a preparing a document
            field_options: This allows the requester to specify field options for a signature request.
            files: Use ``files[]`` to append additional files to the signature request being created from the template.
                Dropbox Sign will parse the files for `text tags <https://app.hellosign.com/api/textTagsWalkthrough>`__
                and append it to the signature request. Text tags for signers not on the template(s) will be ignored.
                **files** or **file_urls[]** is required, but not both.
            file_urls: Use file_urls[] to append additional files to the signature request being created from the
                template. Dropbox Sign will download the file, then parse it for `text tags
                <https://app.hellosign.com/api/textTagsWalkthrough>`__, and append to the signature request. Text tags
                for signers not on the template(s) will be ignored. **files** or **file_urls[]** is required, but not
                both.
            force_signer_roles: Provide users the ability to review/edit the template signer roles.
            force_subject_message: Provide users the ability to review/edit the template subject and message.
            hold_request: The request from this draft will not automatically send to signers post-claim if set to 1.
                Requester must `release </api/reference/operation/signatureRequestReleaseHold/>`__ the request from hold
                when ready to send. Defaults to ``false``.
            is_for_embedded_signing: The request created from this draft will also be signable in embedded mode if set
                to ``true``. Defaults to ``false``.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            preview_only: This allows the requester to enable the preview experience (i.e. does not allow the
                requester's end user to add any additional fields via the editor). - ``preview_only=true``: Allows
                requesters to enable the preview only experience. - ``preview_only=false``: Allows requesters to disable
                the preview only experience. **NOTE:** This parameter overwrites ``show_preview=1`` (if set).
            requesting_redirect_url: The URL you want signers redirected to after they successfully request a signature.
            show_preview: This allows the requester to enable the editor/preview experience. - ``show_preview=true``:
                Allows requesters to enable the editor/preview experience. - ``show_preview=false``: Allows requesters
                to disable the editor/preview experience.
            show_progress_stepper: When only one step remains in the signature request process and this parameter is set
                to ``false`` then the progress stepper will be hidden.
            signers: Add Signers to your Templated-based Signature Request.
            signing_options: This allows the requester to specify the types allowed for creating a signature and specify
                another signing options. **NOTE:** If ``signing_options`` are not defined in the request, the allowed
                types will default to those specified in the account settings. **NOTE:** If
                ``force_advanced_signature_details`` is set, allowed types has to be defined too.
            signing_redirect_url: The URL you want signers redirected to after they successfully sign.
            skip_me_now: Disables the "Me (Now)" option for the person preparing the document. Does not work with type
                ``send_document``. Defaults to ``false``.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request created from this draft will not be legally binding
                if set to ``true``. Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            populate_auto_fill_fields: Controls whether `auto fill fields
                <https://faq.hellosign.com/hc/en-us/articles/360051467511-Auto-Fill-Fields>`__ can automatically
                populate a signer's information during signing. **NOTE:** Keep your signer's information safe by
                ensuring that the _signer on your signature request is the intended party_ before using this feature.
            allow_ccs: This allows the requester to specify whether the user is allowed to provide email addresses to CC
                when claiming the draft.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.unclaimed_draft_create_embedded_with_template(
                client_id,
                requester_email_address,
                template_ids,
                allow_decline=allow_decline,
                allow_reassign=allow_reassign,
                ccs=ccs,
                custom_fields=custom_fields,
                editor_options=editor_options,
                field_options=field_options,
                files=files,
                file_urls=file_urls,
                force_signer_roles=force_signer_roles,
                force_subject_message=force_subject_message,
                hold_request=hold_request,
                is_for_embedded_signing=is_for_embedded_signing,
                message=message,
                metadata=metadata,
                preview_only=preview_only,
                requesting_redirect_url=requesting_redirect_url,
                show_preview=show_preview,
                show_progress_stepper=show_progress_stepper,
                signers=signers,
                signing_options=signing_options,
                signing_redirect_url=signing_redirect_url,
                skip_me_now=skip_me_now,
                subject=subject,
                test_mode=test_mode,
                title=title,
                populate_auto_fill_fields=populate_auto_fill_fields,
                allow_ccs=allow_ccs,
                request_options=request_options,
            ),
        )

    async def unclaimed_draft_edit_and_resend(
        self,
        signature_request_id: str,
        body: UnclaimedDraftEditAndResendRequest | UnclaimedDraftEditAndResendRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UnclaimedDraftCreateResponse:
        """Creates a new signature request from an embedded request that can be edited prior to being sent to the
        recipients. Parameter ``test_mode`` can be edited prior to request. Signers can be edited in embedded editor.
        Requester's email address will remain unchanged if ``requester_email_address`` parameter is not set.

        **NOTE:** Embedded unclaimed drafts can only be accessed in embedded iFrames whereas normal drafts can be used
        and accessed on Dropbox Sign.

        Args:
            signature_request_id: The ID of the signature request to edit and resend.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.unclaimed_draft_edit_and_resend(
                signature_request_id, body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncUnclaimedDraftWithRawResponse:
        return self._with_raw_response


class UnclaimedDraftWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def unclaimed_draft_create(
        self,
        type_: Type2OrStr,
        *,
        files: FileInput | None = None,
        file_urls: list[str] | None = None,
        allow_decline: bool | None = False,
        attachments: list[SubAttachment | SubAttachmentDict] | None = None,
        cc_email_addresses: list[EmailStr] | None = None,
        client_id: str | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        field_options: SubFieldOptions | SubFieldOptionsDict | None = None,
        form_field_groups: list[SubFormFieldGroup | SubFormFieldGroupDict] | None = None,
        form_field_rules: list[SubFormFieldRule | SubFormFieldRuleDict] | None = None,
        form_fields_per_document: list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None = None,
        hide_text_tags: bool | None = False,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        show_progress_stepper: bool | None = True,
        signers: list[SubUnclaimedDraftSigner | SubUnclaimedDraftSignerDict] | None = None,
        signing_options: SubSigningOptions | SubSigningOptionsDict | None = None,
        signing_redirect_url: str | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        use_preexisting_fields: bool | None = False,
        use_text_tags: bool | None = False,
        ignore_text_tags_extraction_errors: bool | None = False,
        expires_at: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UnclaimedDraftCreateResponse, UnclaimedDraftCreateErrorBody]:
        """Creates a new Draft that can be claimed using the claim URL. The first authenticated user to access the URL
        will claim the Draft and will be shown either the "Sign and send" or the "Request signature" page with the Draft
        loaded. Subsequent access to the claim URL will result in a 404.

        Args:
            type_: The type of unclaimed draft to create. Use ``send_document`` to create a claimable file, and
                ``request_signature`` for a claimable signature request. If the type is ``request_signature`` then
                signers name and email_address are not optional.
            files: Use ``files[]`` to indicate the uploaded file(s) to send for signature. This endpoint requires either
                **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            attachments: A list describing the attachments
            cc_email_addresses: The email addresses that should be CCed.
            client_id: Client id of the app used to create the draft. Used to apply the branding and callback url
                defined for the app.
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
            hide_text_tags: Send with a value of ``true`` if you wish to enable automatic Text Tag removal. Defaults to
                ``false``. When using Text Tags it is preferred that you set this to ``false`` and hide your tags with
                white text or something similar because the automatic removal system can cause unwanted clipping. See
                the `Text Tags <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ walkthrough for more
                details.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            show_progress_stepper: When only one step remains in the signature request process and this parameter is set
                to ``false`` then the progress stepper will be hidden.
            signers: Add Signers to your Unclaimed Draft Signature Request.
            signing_options: This allows the requester to specify the types allowed for creating a signature and specify
                another signing options. **NOTE:** If ``signing_options`` are not defined in the request, the allowed
                types will default to those specified in the account settings. **NOTE:** If
                ``force_advanced_signature_details`` is set, allowed types has to be defined too.
            signing_redirect_url: The URL you want signers redirected to after they successfully sign.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request created from this draft will not be legally binding
                if set to ``true``. Defaults to ``false``.
            use_preexisting_fields: Set ``use_text_tags`` to ``true`` to enable `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ parsing in your document (defaults
                to disabled, or ``false``). Alternatively, if your PDF contains pre-defined fields, enable the detection
                of these fields by setting the ``use_preexisting_fields`` to ``true`` (defaults to disabled, or
                ``false``). Currently we only support use of either ``use_text_tags`` or ``use_preexisting_fields``
                parameter, not both.
            use_text_tags: Set ``use_text_tags`` to ``true`` to enable `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ parsing in your document (defaults
                to disabled, or ``false``). Alternatively, if your PDF contains pre-defined fields, enable the detection
                of these fields by setting the ``use_preexisting_fields`` to ``true`` (defaults to disabled, or
                ``false``). Currently we only support use of either ``use_text_tags`` or ``use_preexisting_fields``
                parameter, not both.
            ignore_text_tags_extraction_errors: Sent with a value of ``true`` to ignore the validation errors from text
                tags extraction. Defaults to ``false``.
            expires_at: When the signature request will expire. Unsigned signatures will be moved to the expired status,
                and no longer signable. See `Signature Request Expiration Date
                <https://developers.hellosign.com/docs/signature-request/expiration/>`__ for details. **NOTE:** This
                does not correspond to the **expires_at** returned in the response.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/unclaimed_draft/create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(
                param[Type2OrStr]("type", type_),
                file_part("files", files) if files is not None else None,
                param[list[str] | None]("file_urls", file_urls),
                param[bool | None]("allow_decline", allow_decline),
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
                param[str | None]("message", message),
                param[dict[str, Any] | None]("metadata", metadata),
                param[bool | None]("show_progress_stepper", show_progress_stepper),
                param[list[SubUnclaimedDraftSigner | SubUnclaimedDraftSignerDict] | None]("signers", signers),
                param[SubSigningOptions | SubSigningOptionsDict | None]("signing_options", signing_options),
                param[str | None]("signing_redirect_url", signing_redirect_url),
                param[str | None]("subject", subject),
                param[bool | None]("test_mode", test_mode),
                param[bool | None]("use_preexisting_fields", use_preexisting_fields),
                param[bool | None]("use_text_tags", use_text_tags),
                param[bool | None]("ignore_text_tags_extraction_errors", ignore_text_tags_extraction_errors),
                param[int | None]("expires_at", expires_at),
            ),
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[UnclaimedDraftCreateResponse],
            error_mapper=unclaimed_draft_create_error_mapper,
            request_options=request_options,
        )

    def unclaimed_draft_create_embedded(
        self,
        client_id: str,
        requester_email_address: EmailStr,
        *,
        files: FileInput | None = None,
        file_urls: list[str] | None = None,
        allow_ccs: bool | None = True,
        allow_decline: bool | None = False,
        allow_reassign: bool | None = False,
        attachments: list[SubAttachment | SubAttachmentDict] | None = None,
        cc_email_addresses: list[EmailStr] | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        editor_options: SubEditorOptions | SubEditorOptionsDict | None = None,
        field_options: SubFieldOptions | SubFieldOptionsDict | None = None,
        force_signer_page: bool | None = False,
        force_subject_message: bool | None = False,
        form_field_groups: list[SubFormFieldGroup | SubFormFieldGroupDict] | None = None,
        form_field_rules: list[SubFormFieldRule | SubFormFieldRuleDict] | None = None,
        form_fields_per_document: list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None = None,
        hide_text_tags: bool | None = False,
        hold_request: bool | None = False,
        is_for_embedded_signing: bool | None = False,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        requesting_redirect_url: str | None = None,
        show_preview: bool | None = None,
        show_progress_stepper: bool | None = True,
        signers: list[SubUnclaimedDraftSigner | SubUnclaimedDraftSignerDict] | None = None,
        signing_options: SubSigningOptions | SubSigningOptionsDict | None = None,
        signing_redirect_url: str | None = None,
        skip_me_now: bool | None = False,
        subject: str | None = None,
        test_mode: bool | None = False,
        type_: Type3OrStr | None = Type3.REQUEST_SIGNATURE,
        use_preexisting_fields: bool | None = False,
        use_text_tags: bool | None = False,
        ignore_text_tags_extraction_errors: bool | None = False,
        populate_auto_fill_fields: bool | None = False,
        expires_at: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UnclaimedDraftCreateResponse, UnclaimedDraftCreateEmbeddedErrorBody]:
        """Creates a new Draft that can be claimed and used in an embedded iFrame. The first authenticated user to
        access the URL will claim the Draft and will be shown the "Request signature" page with the Draft loaded.
        Subsequent access to the claim URL will result in a ``404``. For this embedded endpoint the
        ``requester_email_address`` parameter is required.

        **NOTE:** Embedded unclaimed drafts can only be accessed in embedded iFrames whereas normal drafts can be used
        and accessed on Dropbox Sign.

        Args:
            client_id: Client id of the app used to create the draft. Used to apply the branding and callback url
                defined for the app.
            requester_email_address: The email address of the user that should be designated as the requester of this
                draft, if the draft type is ``request_signature``.
            files: Use ``files[]`` to indicate the uploaded file(s) to send for signature. This endpoint requires either
                **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            allow_ccs: This allows the requester to specify whether the user is allowed to provide email addresses to CC
                when claiming the draft.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            allow_reassign: Allows signers to reassign their signature requests to other signers if set to ``true``.
                Defaults to ``false``. **NOTE:** Only available for Premium plan and higher.
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
            editor_options: This allows the requester to specify editor options when a preparing a document
            field_options: This allows the requester to specify field options for a signature request.
            force_signer_page: Provide users the ability to review/edit the signers.
            force_subject_message: Provide users the ability to review/edit the subject and message.
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
            hide_text_tags: Send with a value of ``true`` if you wish to enable automatic Text Tag removal. Defaults to
                ``false``. When using Text Tags it is preferred that you set this to ``false`` and hide your tags with
                white text or something similar because the automatic removal system can cause unwanted clipping. See
                the `Text Tags <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ walkthrough for more
                details.
            hold_request: The request from this draft will not automatically send to signers post-claim if set to
                ``true``. Requester must `release </api/reference/operation/signatureRequestReleaseHold/>`__ the request
                from hold when ready to send. Defaults to ``false``.
            is_for_embedded_signing: The request created from this draft will also be signable in embedded mode if set
                to ``true``. Defaults to ``false``.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            requesting_redirect_url: The URL you want signers redirected to after they successfully request a signature.
            show_preview: This allows the requester to enable the editor/preview experience. - ``show_preview=true``:
                Allows requesters to enable the editor/preview experience. - ``show_preview=false``: Allows requesters
                to disable the editor/preview experience.
            show_progress_stepper: When only one step remains in the signature request process and this parameter is set
                to ``false`` then the progress stepper will be hidden.
            signers: Add Signers to your Unclaimed Draft Signature Request.
            signing_options: This allows the requester to specify the types allowed for creating a signature and specify
                another signing options. **NOTE:** If ``signing_options`` are not defined in the request, the allowed
                types will default to those specified in the account settings. **NOTE:** If
                ``force_advanced_signature_details`` is set, allowed types has to be defined too.
            signing_redirect_url: The URL you want signers redirected to after they successfully sign.
            skip_me_now: Disables the "Me (Now)" option for the person preparing the document. Does not work with type
                ``send_document``. Defaults to ``false``.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request created from this draft will not be legally binding
                if set to ``true``. Defaults to ``false``.
            type_: The type of the draft. By default this is ``request_signature``, but you can set it to
                ``send_document`` if you want to self sign a document and download it.
            use_preexisting_fields: Set ``use_text_tags`` to ``true`` to enable `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ parsing in your document (defaults
                to disabled, or ``false``). Alternatively, if your PDF contains pre-defined fields, enable the detection
                of these fields by setting the ``use_preexisting_fields`` to ``true`` (defaults to disabled, or
                ``false``). Currently we only support use of either ``use_text_tags`` or ``use_preexisting_fields``
                parameter, not both.
            use_text_tags: Set ``use_text_tags`` to ``true`` to enable `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ parsing in your document (defaults
                to disabled, or ``false``). Alternatively, if your PDF contains pre-defined fields, enable the detection
                of these fields by setting the ``use_preexisting_fields`` to ``true`` (defaults to disabled, or
                ``false``). Currently we only support use of either ``use_text_tags`` or ``use_preexisting_fields``
                parameter, not both.
            ignore_text_tags_extraction_errors: Sent with a value of ``true`` to ignore the validation errors from text
                tags extraction. Defaults to ``false``.
            populate_auto_fill_fields: Controls whether `auto fill fields
                <https://faq.hellosign.com/hc/en-us/articles/360051467511-Auto-Fill-Fields>`__ can automatically
                populate a signer's information during signing. **NOTE:** Keep your signer's information safe by
                ensuring that the _signer on your signature request is the intended party_ before using this feature.
            expires_at: When the signature request will expire. Unsigned signatures will be moved to the expired status,
                and no longer signable. See `Signature Request Expiration Date
                <https://developers.hellosign.com/docs/signature-request/expiration/>`__ for details. **NOTE:** This
                does not correspond to the **expires_at** returned in the response.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/unclaimed_draft/create_embedded"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(
                param[str]("client_id", client_id),
                param[EmailStr]("requester_email_address", requester_email_address),
                file_part("files", files) if files is not None else None,
                param[list[str] | None]("file_urls", file_urls),
                param[bool | None]("allow_ccs", allow_ccs),
                param[bool | None]("allow_decline", allow_decline),
                param[bool | None]("allow_reassign", allow_reassign),
                param[list[SubAttachment | SubAttachmentDict] | None]("attachments", attachments),
                param[list[EmailStr] | None]("cc_email_addresses", cc_email_addresses),
                param[list[SubCustomField | SubCustomFieldDict] | None]("custom_fields", custom_fields),
                param[SubEditorOptions | SubEditorOptionsDict | None]("editor_options", editor_options),
                param[SubFieldOptions | SubFieldOptionsDict | None]("field_options", field_options),
                param[bool | None]("force_signer_page", force_signer_page),
                param[bool | None]("force_subject_message", force_subject_message),
                param[list[SubFormFieldGroup | SubFormFieldGroupDict] | None]("form_field_groups", form_field_groups),
                param[list[SubFormFieldRule | SubFormFieldRuleDict] | None]("form_field_rules", form_field_rules),
                param[list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None](
                    "form_fields_per_document", form_fields_per_document
                ),
                param[bool | None]("hide_text_tags", hide_text_tags),
                param[bool | None]("hold_request", hold_request),
                param[bool | None]("is_for_embedded_signing", is_for_embedded_signing),
                param[str | None]("message", message),
                param[dict[str, Any] | None]("metadata", metadata),
                param[str | None]("requesting_redirect_url", requesting_redirect_url),
                param[bool | None]("show_preview", show_preview),
                param[bool | None]("show_progress_stepper", show_progress_stepper),
                param[list[SubUnclaimedDraftSigner | SubUnclaimedDraftSignerDict] | None]("signers", signers),
                param[SubSigningOptions | SubSigningOptionsDict | None]("signing_options", signing_options),
                param[str | None]("signing_redirect_url", signing_redirect_url),
                param[bool | None]("skip_me_now", skip_me_now),
                param[str | None]("subject", subject),
                param[bool | None]("test_mode", test_mode),
                param[Type3OrStr | None]("type", type_),
                param[bool | None]("use_preexisting_fields", use_preexisting_fields),
                param[bool | None]("use_text_tags", use_text_tags),
                param[bool | None]("ignore_text_tags_extraction_errors", ignore_text_tags_extraction_errors),
                param[bool | None]("populate_auto_fill_fields", populate_auto_fill_fields),
                param[int | None]("expires_at", expires_at),
            ),
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[UnclaimedDraftCreateResponse],
            error_mapper=unclaimed_draft_create_embedded_error_mapper,
            request_options=request_options,
        )

    def unclaimed_draft_create_embedded_with_template(
        self,
        client_id: str,
        requester_email_address: EmailStr,
        template_ids: list[str],
        *,
        allow_decline: bool | None = False,
        allow_reassign: bool | None = False,
        ccs: list[SubCc | SubCcDict] | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        editor_options: SubEditorOptions | SubEditorOptionsDict | None = None,
        field_options: SubFieldOptions | SubFieldOptionsDict | None = None,
        files: FileInput | None = None,
        file_urls: list[str] | None = None,
        force_signer_roles: bool | None = False,
        force_subject_message: bool | None = False,
        hold_request: bool | None = False,
        is_for_embedded_signing: bool | None = False,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        preview_only: bool | None = False,
        requesting_redirect_url: str | None = None,
        show_preview: bool | None = False,
        show_progress_stepper: bool | None = True,
        signers: list[SubUnclaimedDraftTemplateSigner | SubUnclaimedDraftTemplateSignerDict] | None = None,
        signing_options: SubSigningOptions | SubSigningOptionsDict | None = None,
        signing_redirect_url: str | None = None,
        skip_me_now: bool | None = False,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        populate_auto_fill_fields: bool | None = False,
        allow_ccs: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UnclaimedDraftCreateResponse, UnclaimedDraftCreateEmbeddedWithTemplateErrorBody]:
        """Creates a new Draft with a previously saved template(s) that can be claimed and used in an embedded iFrame.
        The first authenticated user to access the URL will claim the Draft and will be shown the "Request signature"
        page with the Draft loaded. Subsequent access to the claim URL will result in a ``404``. For this embedded
        endpoint the ``requester_email_address`` parameter is required.

        **NOTE:** Embedded unclaimed drafts can only be accessed in embedded iFrames whereas normal drafts can be used
        and accessed on Dropbox Sign.

        Args:
            client_id: Client id of the app used to create the draft. Used to apply the branding and callback url
                defined for the app.
            requester_email_address: The email address of the user that should be designated as the requester of this
                draft.
            template_ids: Use ``template_ids`` to create a SignatureRequest from one or more templates, in the order in
                which the templates will be used.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            allow_reassign: Allows signers to reassign their signature requests to other signers if set to ``true``.
                Defaults to ``false``. **NOTE:** Only available for Premium plan and higher.
            ccs: Add CC email recipients. Required when a CC role exists for the Template.
            custom_fields: An array defining values and options for custom fields. Required when a custom field exists
                in the Template.
            editor_options: This allows the requester to specify editor options when a preparing a document
            field_options: This allows the requester to specify field options for a signature request.
            files: Use ``files[]`` to append additional files to the signature request being created from the template.
                Dropbox Sign will parse the files for `text tags <https://app.hellosign.com/api/textTagsWalkthrough>`__
                and append it to the signature request. Text tags for signers not on the template(s) will be ignored.
                **files** or **file_urls[]** is required, but not both.
            file_urls: Use file_urls[] to append additional files to the signature request being created from the
                template. Dropbox Sign will download the file, then parse it for `text tags
                <https://app.hellosign.com/api/textTagsWalkthrough>`__, and append to the signature request. Text tags
                for signers not on the template(s) will be ignored. **files** or **file_urls[]** is required, but not
                both.
            force_signer_roles: Provide users the ability to review/edit the template signer roles.
            force_subject_message: Provide users the ability to review/edit the template subject and message.
            hold_request: The request from this draft will not automatically send to signers post-claim if set to 1.
                Requester must `release </api/reference/operation/signatureRequestReleaseHold/>`__ the request from hold
                when ready to send. Defaults to ``false``.
            is_for_embedded_signing: The request created from this draft will also be signable in embedded mode if set
                to ``true``. Defaults to ``false``.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            preview_only: This allows the requester to enable the preview experience (i.e. does not allow the
                requester's end user to add any additional fields via the editor). - ``preview_only=true``: Allows
                requesters to enable the preview only experience. - ``preview_only=false``: Allows requesters to disable
                the preview only experience. **NOTE:** This parameter overwrites ``show_preview=1`` (if set).
            requesting_redirect_url: The URL you want signers redirected to after they successfully request a signature.
            show_preview: This allows the requester to enable the editor/preview experience. - ``show_preview=true``:
                Allows requesters to enable the editor/preview experience. - ``show_preview=false``: Allows requesters
                to disable the editor/preview experience.
            show_progress_stepper: When only one step remains in the signature request process and this parameter is set
                to ``false`` then the progress stepper will be hidden.
            signers: Add Signers to your Templated-based Signature Request.
            signing_options: This allows the requester to specify the types allowed for creating a signature and specify
                another signing options. **NOTE:** If ``signing_options`` are not defined in the request, the allowed
                types will default to those specified in the account settings. **NOTE:** If
                ``force_advanced_signature_details`` is set, allowed types has to be defined too.
            signing_redirect_url: The URL you want signers redirected to after they successfully sign.
            skip_me_now: Disables the "Me (Now)" option for the person preparing the document. Does not work with type
                ``send_document``. Defaults to ``false``.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request created from this draft will not be legally binding
                if set to ``true``. Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            populate_auto_fill_fields: Controls whether `auto fill fields
                <https://faq.hellosign.com/hc/en-us/articles/360051467511-Auto-Fill-Fields>`__ can automatically
                populate a signer's information during signing. **NOTE:** Keep your signer's information safe by
                ensuring that the _signer on your signature request is the intended party_ before using this feature.
            allow_ccs: This allows the requester to specify whether the user is allowed to provide email addresses to CC
                when claiming the draft.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/unclaimed_draft/create_embedded_with_template"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(
                param[str]("client_id", client_id),
                param[EmailStr]("requester_email_address", requester_email_address),
                param[list[str]]("template_ids", template_ids),
                param[bool | None]("allow_decline", allow_decline),
                param[bool | None]("allow_reassign", allow_reassign),
                param[list[SubCc | SubCcDict] | None]("ccs", ccs),
                param[list[SubCustomField | SubCustomFieldDict] | None]("custom_fields", custom_fields),
                param[SubEditorOptions | SubEditorOptionsDict | None]("editor_options", editor_options),
                param[SubFieldOptions | SubFieldOptionsDict | None]("field_options", field_options),
                file_part("files", files) if files is not None else None,
                param[list[str] | None]("file_urls", file_urls),
                param[bool | None]("force_signer_roles", force_signer_roles),
                param[bool | None]("force_subject_message", force_subject_message),
                param[bool | None]("hold_request", hold_request),
                param[bool | None]("is_for_embedded_signing", is_for_embedded_signing),
                param[str | None]("message", message),
                param[dict[str, Any] | None]("metadata", metadata),
                param[bool | None]("preview_only", preview_only),
                param[str | None]("requesting_redirect_url", requesting_redirect_url),
                param[bool | None]("show_preview", show_preview),
                param[bool | None]("show_progress_stepper", show_progress_stepper),
                param[list[SubUnclaimedDraftTemplateSigner | SubUnclaimedDraftTemplateSignerDict] | None](
                    "signers", signers
                ),
                param[SubSigningOptions | SubSigningOptionsDict | None]("signing_options", signing_options),
                param[str | None]("signing_redirect_url", signing_redirect_url),
                param[bool | None]("skip_me_now", skip_me_now),
                param[str | None]("subject", subject),
                param[bool | None]("test_mode", test_mode),
                param[str | None]("title", title),
                param[bool | None]("populate_auto_fill_fields", populate_auto_fill_fields),
                param[bool | None]("allow_ccs", allow_ccs),
            ),
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[UnclaimedDraftCreateResponse],
            error_mapper=unclaimed_draft_create_embedded_with_template_error_mapper,
            request_options=request_options,
        )

    def unclaimed_draft_edit_and_resend(
        self,
        signature_request_id: str,
        body: UnclaimedDraftEditAndResendRequest | UnclaimedDraftEditAndResendRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UnclaimedDraftCreateResponse, UnclaimedDraftEditAndResendErrorBody]:
        """Creates a new signature request from an embedded request that can be edited prior to being sent to the
        recipients. Parameter ``test_mode`` can be edited prior to request. Signers can be edited in embedded editor.
        Requester's email address will remain unchanged if ``requester_email_address`` parameter is not set.

        **NOTE:** Embedded unclaimed drafts can only be accessed in embedded iFrames whereas normal drafts can be used
        and accessed on Dropbox Sign.

        Args:
            signature_request_id: The ID of the signature request to edit and resend.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/unclaimed_draft/edit_and_resend/{signature_request_id}"),
            path_params=[param[str]("signature_request_id", signature_request_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UnclaimedDraftEditAndResendRequest | UnclaimedDraftEditAndResendRequestDict](body),
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[UnclaimedDraftCreateResponse],
            error_mapper=unclaimed_draft_edit_and_resend_error_mapper,
            request_options=request_options,
        )


class AsyncUnclaimedDraftWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def unclaimed_draft_create(
        self,
        type_: Type2OrStr,
        *,
        files: AsyncFileInput | None = None,
        file_urls: list[str] | None = None,
        allow_decline: bool | None = False,
        attachments: list[SubAttachment | SubAttachmentDict] | None = None,
        cc_email_addresses: list[EmailStr] | None = None,
        client_id: str | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        field_options: SubFieldOptions | SubFieldOptionsDict | None = None,
        form_field_groups: list[SubFormFieldGroup | SubFormFieldGroupDict] | None = None,
        form_field_rules: list[SubFormFieldRule | SubFormFieldRuleDict] | None = None,
        form_fields_per_document: list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None = None,
        hide_text_tags: bool | None = False,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        show_progress_stepper: bool | None = True,
        signers: list[SubUnclaimedDraftSigner | SubUnclaimedDraftSignerDict] | None = None,
        signing_options: SubSigningOptions | SubSigningOptionsDict | None = None,
        signing_redirect_url: str | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        use_preexisting_fields: bool | None = False,
        use_text_tags: bool | None = False,
        ignore_text_tags_extraction_errors: bool | None = False,
        expires_at: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UnclaimedDraftCreateResponse, UnclaimedDraftCreateErrorBody]:
        """Creates a new Draft that can be claimed using the claim URL. The first authenticated user to access the URL
        will claim the Draft and will be shown either the "Sign and send" or the "Request signature" page with the Draft
        loaded. Subsequent access to the claim URL will result in a 404.

        Args:
            type_: The type of unclaimed draft to create. Use ``send_document`` to create a claimable file, and
                ``request_signature`` for a claimable signature request. If the type is ``request_signature`` then
                signers name and email_address are not optional.
            files: Use ``files[]`` to indicate the uploaded file(s) to send for signature. This endpoint requires either
                **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            attachments: A list describing the attachments
            cc_email_addresses: The email addresses that should be CCed.
            client_id: Client id of the app used to create the draft. Used to apply the branding and callback url
                defined for the app.
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
            hide_text_tags: Send with a value of ``true`` if you wish to enable automatic Text Tag removal. Defaults to
                ``false``. When using Text Tags it is preferred that you set this to ``false`` and hide your tags with
                white text or something similar because the automatic removal system can cause unwanted clipping. See
                the `Text Tags <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ walkthrough for more
                details.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            show_progress_stepper: When only one step remains in the signature request process and this parameter is set
                to ``false`` then the progress stepper will be hidden.
            signers: Add Signers to your Unclaimed Draft Signature Request.
            signing_options: This allows the requester to specify the types allowed for creating a signature and specify
                another signing options. **NOTE:** If ``signing_options`` are not defined in the request, the allowed
                types will default to those specified in the account settings. **NOTE:** If
                ``force_advanced_signature_details`` is set, allowed types has to be defined too.
            signing_redirect_url: The URL you want signers redirected to after they successfully sign.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request created from this draft will not be legally binding
                if set to ``true``. Defaults to ``false``.
            use_preexisting_fields: Set ``use_text_tags`` to ``true`` to enable `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ parsing in your document (defaults
                to disabled, or ``false``). Alternatively, if your PDF contains pre-defined fields, enable the detection
                of these fields by setting the ``use_preexisting_fields`` to ``true`` (defaults to disabled, or
                ``false``). Currently we only support use of either ``use_text_tags`` or ``use_preexisting_fields``
                parameter, not both.
            use_text_tags: Set ``use_text_tags`` to ``true`` to enable `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ parsing in your document (defaults
                to disabled, or ``false``). Alternatively, if your PDF contains pre-defined fields, enable the detection
                of these fields by setting the ``use_preexisting_fields`` to ``true`` (defaults to disabled, or
                ``false``). Currently we only support use of either ``use_text_tags`` or ``use_preexisting_fields``
                parameter, not both.
            ignore_text_tags_extraction_errors: Sent with a value of ``true`` to ignore the validation errors from text
                tags extraction. Defaults to ``false``.
            expires_at: When the signature request will expire. Unsigned signatures will be moved to the expired status,
                and no longer signable. See `Signature Request Expiration Date
                <https://developers.hellosign.com/docs/signature-request/expiration/>`__ for details. **NOTE:** This
                does not correspond to the **expires_at** returned in the response.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/unclaimed_draft/create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(
                param[Type2OrStr]("type", type_),
                file_part("files", files) if files is not None else None,
                param[list[str] | None]("file_urls", file_urls),
                param[bool | None]("allow_decline", allow_decline),
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
                param[str | None]("message", message),
                param[dict[str, Any] | None]("metadata", metadata),
                param[bool | None]("show_progress_stepper", show_progress_stepper),
                param[list[SubUnclaimedDraftSigner | SubUnclaimedDraftSignerDict] | None]("signers", signers),
                param[SubSigningOptions | SubSigningOptionsDict | None]("signing_options", signing_options),
                param[str | None]("signing_redirect_url", signing_redirect_url),
                param[str | None]("subject", subject),
                param[bool | None]("test_mode", test_mode),
                param[bool | None]("use_preexisting_fields", use_preexisting_fields),
                param[bool | None]("use_text_tags", use_text_tags),
                param[bool | None]("ignore_text_tags_extraction_errors", ignore_text_tags_extraction_errors),
                param[int | None]("expires_at", expires_at),
            ),
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[UnclaimedDraftCreateResponse],
            error_mapper=unclaimed_draft_create_error_mapper,
            request_options=request_options,
        )

    async def unclaimed_draft_create_embedded(
        self,
        client_id: str,
        requester_email_address: EmailStr,
        *,
        files: AsyncFileInput | None = None,
        file_urls: list[str] | None = None,
        allow_ccs: bool | None = True,
        allow_decline: bool | None = False,
        allow_reassign: bool | None = False,
        attachments: list[SubAttachment | SubAttachmentDict] | None = None,
        cc_email_addresses: list[EmailStr] | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        editor_options: SubEditorOptions | SubEditorOptionsDict | None = None,
        field_options: SubFieldOptions | SubFieldOptionsDict | None = None,
        force_signer_page: bool | None = False,
        force_subject_message: bool | None = False,
        form_field_groups: list[SubFormFieldGroup | SubFormFieldGroupDict] | None = None,
        form_field_rules: list[SubFormFieldRule | SubFormFieldRuleDict] | None = None,
        form_fields_per_document: list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None = None,
        hide_text_tags: bool | None = False,
        hold_request: bool | None = False,
        is_for_embedded_signing: bool | None = False,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        requesting_redirect_url: str | None = None,
        show_preview: bool | None = None,
        show_progress_stepper: bool | None = True,
        signers: list[SubUnclaimedDraftSigner | SubUnclaimedDraftSignerDict] | None = None,
        signing_options: SubSigningOptions | SubSigningOptionsDict | None = None,
        signing_redirect_url: str | None = None,
        skip_me_now: bool | None = False,
        subject: str | None = None,
        test_mode: bool | None = False,
        type_: Type3OrStr | None = Type3.REQUEST_SIGNATURE,
        use_preexisting_fields: bool | None = False,
        use_text_tags: bool | None = False,
        ignore_text_tags_extraction_errors: bool | None = False,
        populate_auto_fill_fields: bool | None = False,
        expires_at: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UnclaimedDraftCreateResponse, UnclaimedDraftCreateEmbeddedErrorBody]:
        """Creates a new Draft that can be claimed and used in an embedded iFrame. The first authenticated user to
        access the URL will claim the Draft and will be shown the "Request signature" page with the Draft loaded.
        Subsequent access to the claim URL will result in a ``404``. For this embedded endpoint the
        ``requester_email_address`` parameter is required.

        **NOTE:** Embedded unclaimed drafts can only be accessed in embedded iFrames whereas normal drafts can be used
        and accessed on Dropbox Sign.

        Args:
            client_id: Client id of the app used to create the draft. Used to apply the branding and callback url
                defined for the app.
            requester_email_address: The email address of the user that should be designated as the requester of this
                draft, if the draft type is ``request_signature``.
            files: Use ``files[]`` to indicate the uploaded file(s) to send for signature. This endpoint requires either
                **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            allow_ccs: This allows the requester to specify whether the user is allowed to provide email addresses to CC
                when claiming the draft.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            allow_reassign: Allows signers to reassign their signature requests to other signers if set to ``true``.
                Defaults to ``false``. **NOTE:** Only available for Premium plan and higher.
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
            editor_options: This allows the requester to specify editor options when a preparing a document
            field_options: This allows the requester to specify field options for a signature request.
            force_signer_page: Provide users the ability to review/edit the signers.
            force_subject_message: Provide users the ability to review/edit the subject and message.
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
            hide_text_tags: Send with a value of ``true`` if you wish to enable automatic Text Tag removal. Defaults to
                ``false``. When using Text Tags it is preferred that you set this to ``false`` and hide your tags with
                white text or something similar because the automatic removal system can cause unwanted clipping. See
                the `Text Tags <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ walkthrough for more
                details.
            hold_request: The request from this draft will not automatically send to signers post-claim if set to
                ``true``. Requester must `release </api/reference/operation/signatureRequestReleaseHold/>`__ the request
                from hold when ready to send. Defaults to ``false``.
            is_for_embedded_signing: The request created from this draft will also be signable in embedded mode if set
                to ``true``. Defaults to ``false``.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            requesting_redirect_url: The URL you want signers redirected to after they successfully request a signature.
            show_preview: This allows the requester to enable the editor/preview experience. - ``show_preview=true``:
                Allows requesters to enable the editor/preview experience. - ``show_preview=false``: Allows requesters
                to disable the editor/preview experience.
            show_progress_stepper: When only one step remains in the signature request process and this parameter is set
                to ``false`` then the progress stepper will be hidden.
            signers: Add Signers to your Unclaimed Draft Signature Request.
            signing_options: This allows the requester to specify the types allowed for creating a signature and specify
                another signing options. **NOTE:** If ``signing_options`` are not defined in the request, the allowed
                types will default to those specified in the account settings. **NOTE:** If
                ``force_advanced_signature_details`` is set, allowed types has to be defined too.
            signing_redirect_url: The URL you want signers redirected to after they successfully sign.
            skip_me_now: Disables the "Me (Now)" option for the person preparing the document. Does not work with type
                ``send_document``. Defaults to ``false``.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request created from this draft will not be legally binding
                if set to ``true``. Defaults to ``false``.
            type_: The type of the draft. By default this is ``request_signature``, but you can set it to
                ``send_document`` if you want to self sign a document and download it.
            use_preexisting_fields: Set ``use_text_tags`` to ``true`` to enable `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ parsing in your document (defaults
                to disabled, or ``false``). Alternatively, if your PDF contains pre-defined fields, enable the detection
                of these fields by setting the ``use_preexisting_fields`` to ``true`` (defaults to disabled, or
                ``false``). Currently we only support use of either ``use_text_tags`` or ``use_preexisting_fields``
                parameter, not both.
            use_text_tags: Set ``use_text_tags`` to ``true`` to enable `Text Tags
                <https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro>`__ parsing in your document (defaults
                to disabled, or ``false``). Alternatively, if your PDF contains pre-defined fields, enable the detection
                of these fields by setting the ``use_preexisting_fields`` to ``true`` (defaults to disabled, or
                ``false``). Currently we only support use of either ``use_text_tags`` or ``use_preexisting_fields``
                parameter, not both.
            ignore_text_tags_extraction_errors: Sent with a value of ``true`` to ignore the validation errors from text
                tags extraction. Defaults to ``false``.
            populate_auto_fill_fields: Controls whether `auto fill fields
                <https://faq.hellosign.com/hc/en-us/articles/360051467511-Auto-Fill-Fields>`__ can automatically
                populate a signer's information during signing. **NOTE:** Keep your signer's information safe by
                ensuring that the _signer on your signature request is the intended party_ before using this feature.
            expires_at: When the signature request will expire. Unsigned signatures will be moved to the expired status,
                and no longer signable. See `Signature Request Expiration Date
                <https://developers.hellosign.com/docs/signature-request/expiration/>`__ for details. **NOTE:** This
                does not correspond to the **expires_at** returned in the response.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/unclaimed_draft/create_embedded"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(
                param[str]("client_id", client_id),
                param[EmailStr]("requester_email_address", requester_email_address),
                file_part("files", files) if files is not None else None,
                param[list[str] | None]("file_urls", file_urls),
                param[bool | None]("allow_ccs", allow_ccs),
                param[bool | None]("allow_decline", allow_decline),
                param[bool | None]("allow_reassign", allow_reassign),
                param[list[SubAttachment | SubAttachmentDict] | None]("attachments", attachments),
                param[list[EmailStr] | None]("cc_email_addresses", cc_email_addresses),
                param[list[SubCustomField | SubCustomFieldDict] | None]("custom_fields", custom_fields),
                param[SubEditorOptions | SubEditorOptionsDict | None]("editor_options", editor_options),
                param[SubFieldOptions | SubFieldOptionsDict | None]("field_options", field_options),
                param[bool | None]("force_signer_page", force_signer_page),
                param[bool | None]("force_subject_message", force_subject_message),
                param[list[SubFormFieldGroup | SubFormFieldGroupDict] | None]("form_field_groups", form_field_groups),
                param[list[SubFormFieldRule | SubFormFieldRuleDict] | None]("form_field_rules", form_field_rules),
                param[list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None](
                    "form_fields_per_document", form_fields_per_document
                ),
                param[bool | None]("hide_text_tags", hide_text_tags),
                param[bool | None]("hold_request", hold_request),
                param[bool | None]("is_for_embedded_signing", is_for_embedded_signing),
                param[str | None]("message", message),
                param[dict[str, Any] | None]("metadata", metadata),
                param[str | None]("requesting_redirect_url", requesting_redirect_url),
                param[bool | None]("show_preview", show_preview),
                param[bool | None]("show_progress_stepper", show_progress_stepper),
                param[list[SubUnclaimedDraftSigner | SubUnclaimedDraftSignerDict] | None]("signers", signers),
                param[SubSigningOptions | SubSigningOptionsDict | None]("signing_options", signing_options),
                param[str | None]("signing_redirect_url", signing_redirect_url),
                param[bool | None]("skip_me_now", skip_me_now),
                param[str | None]("subject", subject),
                param[bool | None]("test_mode", test_mode),
                param[Type3OrStr | None]("type", type_),
                param[bool | None]("use_preexisting_fields", use_preexisting_fields),
                param[bool | None]("use_text_tags", use_text_tags),
                param[bool | None]("ignore_text_tags_extraction_errors", ignore_text_tags_extraction_errors),
                param[bool | None]("populate_auto_fill_fields", populate_auto_fill_fields),
                param[int | None]("expires_at", expires_at),
            ),
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[UnclaimedDraftCreateResponse],
            error_mapper=unclaimed_draft_create_embedded_error_mapper,
            request_options=request_options,
        )

    async def unclaimed_draft_create_embedded_with_template(
        self,
        client_id: str,
        requester_email_address: EmailStr,
        template_ids: list[str],
        *,
        allow_decline: bool | None = False,
        allow_reassign: bool | None = False,
        ccs: list[SubCc | SubCcDict] | None = None,
        custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None,
        editor_options: SubEditorOptions | SubEditorOptionsDict | None = None,
        field_options: SubFieldOptions | SubFieldOptionsDict | None = None,
        files: AsyncFileInput | None = None,
        file_urls: list[str] | None = None,
        force_signer_roles: bool | None = False,
        force_subject_message: bool | None = False,
        hold_request: bool | None = False,
        is_for_embedded_signing: bool | None = False,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        preview_only: bool | None = False,
        requesting_redirect_url: str | None = None,
        show_preview: bool | None = False,
        show_progress_stepper: bool | None = True,
        signers: list[SubUnclaimedDraftTemplateSigner | SubUnclaimedDraftTemplateSignerDict] | None = None,
        signing_options: SubSigningOptions | SubSigningOptionsDict | None = None,
        signing_redirect_url: str | None = None,
        skip_me_now: bool | None = False,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        populate_auto_fill_fields: bool | None = False,
        allow_ccs: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UnclaimedDraftCreateResponse, UnclaimedDraftCreateEmbeddedWithTemplateErrorBody]:
        """Creates a new Draft with a previously saved template(s) that can be claimed and used in an embedded iFrame.
        The first authenticated user to access the URL will claim the Draft and will be shown the "Request signature"
        page with the Draft loaded. Subsequent access to the claim URL will result in a ``404``. For this embedded
        endpoint the ``requester_email_address`` parameter is required.

        **NOTE:** Embedded unclaimed drafts can only be accessed in embedded iFrames whereas normal drafts can be used
        and accessed on Dropbox Sign.

        Args:
            client_id: Client id of the app used to create the draft. Used to apply the branding and callback url
                defined for the app.
            requester_email_address: The email address of the user that should be designated as the requester of this
                draft.
            template_ids: Use ``template_ids`` to create a SignatureRequest from one or more templates, in the order in
                which the templates will be used.
            allow_decline: Allows signers to decline to sign a document if ``true``. Defaults to ``false``.
            allow_reassign: Allows signers to reassign their signature requests to other signers if set to ``true``.
                Defaults to ``false``. **NOTE:** Only available for Premium plan and higher.
            ccs: Add CC email recipients. Required when a CC role exists for the Template.
            custom_fields: An array defining values and options for custom fields. Required when a custom field exists
                in the Template.
            editor_options: This allows the requester to specify editor options when a preparing a document
            field_options: This allows the requester to specify field options for a signature request.
            files: Use ``files[]`` to append additional files to the signature request being created from the template.
                Dropbox Sign will parse the files for `text tags <https://app.hellosign.com/api/textTagsWalkthrough>`__
                and append it to the signature request. Text tags for signers not on the template(s) will be ignored.
                **files** or **file_urls[]** is required, but not both.
            file_urls: Use file_urls[] to append additional files to the signature request being created from the
                template. Dropbox Sign will download the file, then parse it for `text tags
                <https://app.hellosign.com/api/textTagsWalkthrough>`__, and append to the signature request. Text tags
                for signers not on the template(s) will be ignored. **files** or **file_urls[]** is required, but not
                both.
            force_signer_roles: Provide users the ability to review/edit the template signer roles.
            force_subject_message: Provide users the ability to review/edit the template subject and message.
            hold_request: The request from this draft will not automatically send to signers post-claim if set to 1.
                Requester must `release </api/reference/operation/signatureRequestReleaseHold/>`__ the request from hold
                when ready to send. Defaults to ``false``.
            is_for_embedded_signing: The request created from this draft will also be signable in embedded mode if set
                to ``true``. Defaults to ``false``.
            message: The custom message in the email that will be sent to the signers.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            preview_only: This allows the requester to enable the preview experience (i.e. does not allow the
                requester's end user to add any additional fields via the editor). - ``preview_only=true``: Allows
                requesters to enable the preview only experience. - ``preview_only=false``: Allows requesters to disable
                the preview only experience. **NOTE:** This parameter overwrites ``show_preview=1`` (if set).
            requesting_redirect_url: The URL you want signers redirected to after they successfully request a signature.
            show_preview: This allows the requester to enable the editor/preview experience. - ``show_preview=true``:
                Allows requesters to enable the editor/preview experience. - ``show_preview=false``: Allows requesters
                to disable the editor/preview experience.
            show_progress_stepper: When only one step remains in the signature request process and this parameter is set
                to ``false`` then the progress stepper will be hidden.
            signers: Add Signers to your Templated-based Signature Request.
            signing_options: This allows the requester to specify the types allowed for creating a signature and specify
                another signing options. **NOTE:** If ``signing_options`` are not defined in the request, the allowed
                types will default to those specified in the account settings. **NOTE:** If
                ``force_advanced_signature_details`` is set, allowed types has to be defined too.
            signing_redirect_url: The URL you want signers redirected to after they successfully sign.
            skip_me_now: Disables the "Me (Now)" option for the person preparing the document. Does not work with type
                ``send_document``. Defaults to ``false``.
            subject: The subject in the email that will be sent to the signers.
            test_mode: Whether this is a test, the signature request created from this draft will not be legally binding
                if set to ``true``. Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            populate_auto_fill_fields: Controls whether `auto fill fields
                <https://faq.hellosign.com/hc/en-us/articles/360051467511-Auto-Fill-Fields>`__ can automatically
                populate a signer's information during signing. **NOTE:** Keep your signer's information safe by
                ensuring that the _signer on your signature request is the intended party_ before using this feature.
            allow_ccs: This allows the requester to specify whether the user is allowed to provide email addresses to CC
                when claiming the draft.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/unclaimed_draft/create_embedded_with_template"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(
                param[str]("client_id", client_id),
                param[EmailStr]("requester_email_address", requester_email_address),
                param[list[str]]("template_ids", template_ids),
                param[bool | None]("allow_decline", allow_decline),
                param[bool | None]("allow_reassign", allow_reassign),
                param[list[SubCc | SubCcDict] | None]("ccs", ccs),
                param[list[SubCustomField | SubCustomFieldDict] | None]("custom_fields", custom_fields),
                param[SubEditorOptions | SubEditorOptionsDict | None]("editor_options", editor_options),
                param[SubFieldOptions | SubFieldOptionsDict | None]("field_options", field_options),
                file_part("files", files) if files is not None else None,
                param[list[str] | None]("file_urls", file_urls),
                param[bool | None]("force_signer_roles", force_signer_roles),
                param[bool | None]("force_subject_message", force_subject_message),
                param[bool | None]("hold_request", hold_request),
                param[bool | None]("is_for_embedded_signing", is_for_embedded_signing),
                param[str | None]("message", message),
                param[dict[str, Any] | None]("metadata", metadata),
                param[bool | None]("preview_only", preview_only),
                param[str | None]("requesting_redirect_url", requesting_redirect_url),
                param[bool | None]("show_preview", show_preview),
                param[bool | None]("show_progress_stepper", show_progress_stepper),
                param[list[SubUnclaimedDraftTemplateSigner | SubUnclaimedDraftTemplateSignerDict] | None](
                    "signers", signers
                ),
                param[SubSigningOptions | SubSigningOptionsDict | None]("signing_options", signing_options),
                param[str | None]("signing_redirect_url", signing_redirect_url),
                param[bool | None]("skip_me_now", skip_me_now),
                param[str | None]("subject", subject),
                param[bool | None]("test_mode", test_mode),
                param[str | None]("title", title),
                param[bool | None]("populate_auto_fill_fields", populate_auto_fill_fields),
                param[bool | None]("allow_ccs", allow_ccs),
            ),
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[UnclaimedDraftCreateResponse],
            error_mapper=unclaimed_draft_create_embedded_with_template_error_mapper,
            request_options=request_options,
        )

    async def unclaimed_draft_edit_and_resend(
        self,
        signature_request_id: str,
        body: UnclaimedDraftEditAndResendRequest | UnclaimedDraftEditAndResendRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UnclaimedDraftCreateResponse, UnclaimedDraftEditAndResendErrorBody]:
        """Creates a new signature request from an embedded request that can be edited prior to being sent to the
        recipients. Parameter ``test_mode`` can be edited prior to request. Signers can be edited in embedded editor.
        Requester's email address will remain unchanged if ``requester_email_address`` parameter is not set.

        **NOTE:** Embedded unclaimed drafts can only be accessed in embedded iFrames whereas normal drafts can be used
        and accessed on Dropbox Sign.

        Args:
            signature_request_id: The ID of the signature request to edit and resend.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/unclaimed_draft/edit_and_resend/{signature_request_id}"),
            path_params=[param[str]("signature_request_id", signature_request_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UnclaimedDraftEditAndResendRequest | UnclaimedDraftEditAndResendRequestDict](body),
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[UnclaimedDraftCreateResponse],
            error_mapper=unclaimed_draft_edit_and_resend_error_mapper,
            request_options=request_options,
        )
