---
title: API Changelog | Healthie API Docs
description: Detailed history of non-breaking changes to the Healthie GraphQL
  API baseline schema
source_url:
  html: https://docs.gethealthie.com/guides/api-concepts/changelog/index
  md: https://docs.gethealthie.com/guides/api-concepts/changelog/index.md
---

This changelog documents all non-breaking changes to the Healthie **GraphQL schema**. These changes follow the API accretion model and are immediately available in every API version without requiring any version upgrades in your client code.

## What’s Included

This changelog tracks:

* **New fields** - Added to existing types
* **New types** - Objects, inputs, enums, unions, and scalars
* **New arguments** - Optional arguments added to fields
* **New enum values** - Additional values for existing enums
* **Deprecations** - Fields and arguments marked for future removal
* **Other schema updates** - Additional non-breaking modifications to the API

Related Documentation

* **[Version History](/guides/api-concepts/versioning#version-history-breaking-changes)** - Breaking changes that require version upgrades
* **[API Deprecations](/guides/api-concepts/deprecations)** - Types and operations scheduled for removal

***

## Changelog Entries

### 2026-05-08

* Type `CustomModuleEdge` was added
* Type `CustomModulePaginationConnection` was added
* Type `NarxCheck` was added
* Type `PauseCourseMembershipInput` was added
* Type `PauseCourseMembershipPayload` was added
* Type `ResumeCourseMembershipInput` was added
* Type `ResumeCourseMembershipPayload` was added
* Field `organization_id` was added to object type `AppointmentType`
* Field `is_paused` was added to object type `CourseMembership`
* Field `paused_at` was added to object type `CourseMembership`
* Field `total_paused_duration` was added to object type `CourseMembership`
* Input field `share_with_all_clients` of type `Boolean` was added to input object type `CreateSharingsInput`
* Field `unshared_patients_count` was added to object type `Document`
* Field `unshared_patients_count` was added to object type `Folder`
* Field `form_answer_group_prescriptions` was added to object type `FormAnswerGroup`
* Field `narx_checks` was added to object type `FormAnswerGroup`
* Field `pauseCourseMembership` was added to object type `Mutation`
* Field `resumeCourseMembership` was added to object type `Mutation`
* Field `only_active_standard` was added to object type `Organization`
* Field `only_active_standard_count` was added to object type `Organization`
* Field `can_manage_others_availability` was added to object type `OrganizationMembership`
* Field `can_manage_others_blocks` was added to object type `OrganizationMembership`
* Field `can_manage_own_availability` was added to object type `OrganizationMembership`
* Field `can_manage_own_blocks` was added to object type `OrganizationMembership`
* Field `can_autogenerate_charting_notes_from_zoom_calls` was added to object type `PermissionTemplateType`
* Field `can_manage_others_availability` was added to object type `PermissionTemplateType`
* Field `can_manage_others_blocks` was added to object type `PermissionTemplateType`
* Field `can_manage_own_availability` was added to object type `PermissionTemplateType`
* Field `can_manage_own_blocks` was added to object type `PermissionTemplateType`
* Field `customModules` was added to object type `Query`
* Field `User.has_ach` is deprecated
* Field `User.has_ach` has deprecation reason `Client ACH via this feature is no longer supported. This field is always false.`
* Input field `can_manage_own_availability` of type `Boolean` was added to input object type `createPermissionTemplateInput`
* Input field `can_manage_own_blocks` of type `Boolean` was added to input object type `createPermissionTemplateInput`
* Input field `can_manage_others_availability` of type `Boolean` was added to input object type `createPermissionTemplateInput`
* Input field `can_manage_others_blocks` of type `Boolean` was added to input object type `createPermissionTemplateInput`
* Input field `can_manage_own_availability` of type `Boolean` was added to input object type `updateOrganizationMembershipInput`
* Input field `can_manage_own_blocks` of type `Boolean` was added to input object type `updateOrganizationMembershipInput`
* Input field `can_manage_others_availability` of type `Boolean` was added to input object type `updateOrganizationMembershipInput`
* Input field `can_manage_others_blocks` of type `Boolean` was added to input object type `updateOrganizationMembershipInput`
* Input field `can_manage_own_availability` of type `Boolean` was added to input object type `updatePermissionTemplateInput`
* Input field `can_manage_own_blocks` of type `Boolean` was added to input object type `updatePermissionTemplateInput`
* Input field `can_manage_others_availability` of type `Boolean` was added to input object type `updatePermissionTemplateInput`
* Input field `can_manage_others_blocks` of type `Boolean` was added to input object type `updatePermissionTemplateInput`

### 2026-04-24

* Enum value `REVIEWING_PROVIDER_LAST_NAME_ASC` was added to enum `LabOrderOrderKeys`
* Enum value `REVIEWING_PROVIDER_LAST_NAME_DESC` was added to enum `LabOrderOrderKeys`
* Enum value `NORMALIZED_STATUS_ASC` was added to enum `LabOrderOrderKeys`
* Enum value `NORMALIZED_STATUS_DESC` was added to enum `LabOrderOrderKeys`
* Enum value `INTERPRETATION_ASC` was added to enum `LabOrderOrderKeys`
* Enum value `INTERPRETATION_DESC` was added to enum `LabOrderOrderKeys`
* Field `created_at` was added to object type `Policy`
* Argument `provider_ids: [String]` added to field `Query.appointmentTypes`
* Argument `provider_ids: [String]` added to field `Query.appointmentTypesCount`
* Field `Query.prescriptions` is deprecated
* Field `Query.prescriptions` has deprecation reason `Use `prescriptionMedications` instead`
* Enum value `incomplete` was added to enum `TranscriptStatusEnum`
* Field `current_provider_has_access` was added to object type `parseCcdaDocumentPayload`
* Field `is_new_patient` was added to object type `parseCcdaDocumentPayload`

### 2026-04-17

* Type `Claim` was added
* Type `ClaimCobOverridesInput` was added
* Type `ClaimCptCode` was added
* Type `ClaimDiagnosis` was added
* Type `ClaimEdge` was added
* Type `ClaimIcdCode` was added
* Type `ClaimInsurancePlan` was added
* Type `ClaimLineCobOverridesInput` was added
* Type `ClaimLocation` was added
* Type `ClaimOtherIdNumber` was added
* Type `ClaimPaginationConnection` was added
* Type `ClaimPatient` was added
* Type `ClaimPlaceOfService` was added
* Type `ClaimPolicy` was added
* Type `ClaimPolicyHolder` was added
* Type `ClaimPolicyPriority` was added
* Type `ClaimProvider` was added
* Type `ClaimReferralInfo` was added
* Type `ClaimReferringPhysician` was added
* Type `ClaimServiceLine` was added
* Type `ClaimSubmissionEdge` was added
* Type `ClaimSubmissionPaginationConnection` was added
* Type `CobAdjustment` was added
* Type `CobAdjustmentInput` was added
* Type `CobServiceLineAdjustment` was added
* Type `ConversationMembershipsAllCounts` was added
* Type `CoordinationOfBenefits` was added
* Type `CreateSecondaryClaimInput` was added
* Type `CreateSecondaryClaimPayload` was added
* Type `HolderRelationship` was added
* Type `PayerOrder` was added
* Type `SubmitSecondaryClaimInput` was added
* Type `SubmitSecondaryClaimPayload` was added
* Type `UpdateSecondaryClaimInput` was added
* Type `UpdateSecondaryClaimPayload` was added
* Type `ZoomCoHostLink` was added
* Field `zoom_co_host_links` was added to object type `Appointment`
* Field `createSecondaryClaim` was added to object type `Mutation`
* Field `submitSecondaryClaim` was added to object type `Mutation`
* Field `updateSecondaryClaim` was added to object type `Mutation`
* Field `conversationMembershipsAllCounts` was added to object type `Query`
* Argument `include_inactive: Boolean` (with default value) added to field `Query.entries`
* Field `hide_apple_calendar` was added to object type `WhitelabelSetting`
* Directive `deprecated` was added to input field `clients_in_a_month` in input object `createPersonalizationQuestionnaireInput`

### 2026-04-10

* Type `GeneratedFormAnswerGroupRejectionReasonEnum` was added
* Field `rejection_reason` was added to object type `GeneratedFormAnswerGroupType`
* Input field `outside_party_payer_id` of type `ID` was added to input object type `completeCheckoutInput`
* Input field `invoice_id` of type `ID` was added to input object type `completeCheckoutInput`
* Input field `feedback` of type `String` was added to input object type `rejectGeneratedFormAnswerGroupInput`
* Input field `rejection_reason` of type `[GeneratedFormAnswerGroupRejectionReasonEnum!]` was added to input object type `rejectGeneratedFormAnswerGroupInput`

### 2026-04-03

* Field `cancelled_at` was added to object type `AppointmentInclusionType`
* Field `cancelled_by` was added to object type `AppointmentInclusionType`
* Field `cancelled_by_id` was added to object type `AppointmentInclusionType`
* Argument `exclude_provider_ids: [ID]` added to field `Query.availableSlotsForRange`
* Argument `exclude_provider_ids: [ID]` added to field `Query.daysAvailableForRange`

### 2026-03-27

* Enum value `TASK` was added to enum `AuditEventResourceName`
* Field `has_autoscored_calculator` was added to object type `AutoscoredSectionType`
* Field `timezone` was added to object type `Availability`
* Field `metadata` was added to object type `Conversation`
* Field `require_insurance_card_upload` was added to object type `Organization`
* Field `can_unlock_charting_notes` was added to object type `PermissionTemplateType`
* Input field `metadata` of type `JSON` was added to input object type `createConversationInput`
* Input field `can_unlock_charting_notes` of type `Boolean` was added to input object type `createPermissionTemplateInput`
* Input field `metadata` of type `JSON` was added to input object type `updateConversationInput`
* Input field `can_unlock_charting_notes` of type `Boolean` was added to input object type `updatePermissionTemplateInput`

### 2026-03-20

* Type `CreateInternalCommentInput` was added
* Type `CreateInternalCommentPayload` was added
* Type `DestroyInternalCommentInput` was added
* Type `DestroyInternalCommentPayload` was added
* Type `InternalComment` was added
* Type `InternalCommentEdge` was added
* Type `InternalCommentPaginationConnection` was added
* Type `InternalCommentable` was added
* Type `InternalCommentsOrderKeys` was added
* Type `UpdateInternalCommentInput` was added
* Type `UpdateInternalCommentPayload` was added
* Field `createInternalComment` was added to object type `Mutation`
* Field `destroyInternalComment` was added to object type `Mutation`
* Field `updateInternalComment` was added to object type `Mutation`
* Field `can_link_labs_to_chart_notes` was added to object type `Organization`
* Field `comments` was added to object type `Task`

### 2026-03-13

* Field `Course.use_category` is deprecated
* Field `Course.use_category` has deprecation reason `This field is no longer used`
* Field `CourseItem.category` is deprecated
* Field `CourseItem.category` has deprecation reason `This field is no longer used`
* Field `created_user` was added to object type `Goal`
* Enum value `CREATED_BY_ASC` was added to enum `GoalOrderKeys`
* Enum value `CREATED_BY_DESC` was added to enum `GoalOrderKeys`
* Enum value `HEALTHIE_APP` was added to enum `PartnerType`
* Enum value `HEALTHIE_INTEGRATION` was added to enum `PartnerType`
* Field `anticipated_number_of_providers` was added to object type `User`
* Field `any_incomplete_requested_form_completions` was added to object type `User`

### 2026-03-06

* Type `CancelMobileHealthDataSnapshotInput` was added
* Type `CancelMobileHealthDataSnapshotPayload` was added
* Type `CreateMobileHealthDataSnapshotInput` was added
* Type `CreateMobileHealthDataSnapshotPayload` was added
* Type `MobileHealthDataSnapshot` was added
* Type `MobileHealthDataSnapshotIntegrationType` was added
* Type `MobileHealthDataSnapshotStatus` was added
* Type `ProcessMobileHealthDataSnapshotInput` was added
* Type `ProcessMobileHealthDataSnapshotPayload` was added
* Field `lab_orders` was added to object type `FormAnswerGroup`
* Field `form_answer_group` was added to object type `LabOrder`
* Field `latest_result_received_at` was added to object type `LabOrder`
* Field `cancelMobileHealthDataSnapshot` was added to object type `Mutation`
* Field `createMobileHealthDataSnapshot` was added to object type `Mutation`
* Field `processMobileHealthDataSnapshot` was added to object type `Mutation`
* Field `embeddedZoomJwt` was added to object type `Query`
* Argument `form_answer_group_id: ID` added to field `Query.dosespot_ui_link`
* Argument `use_for_charting: Boolean` (with default value) added to field `Query.formAnswerGroups`
* Input field `form_answer_group_id` of type `ID` was added to input object type `SubmissionInput`
* Field `metadata` was added to object type `Task`
* Input field `metadata` of type `JSON` was added to input object type `createTaskInput`
* Input field `metadata` of type `JSON` was added to input object type `updateTaskInput`

### 2026-02-27

* Type `GoalHistoryActionTypeEnum` was added
* Field `use_embedded_zoom` was added to object type `Appointment`
* Field `send_embeddable_appt_creator_email` was added to object type `AppointmentSetting`
* Field `zoom_open_preference` was added to object type `AppointmentSetting`
* Input field `send_embeddable_appt_creator_email` of type `Boolean` was added to input object type `AppointmentTypeAppointmentSettingInput`
* Field `insurance_billing_enabled` was added to object type `AutomatedInsuranceBillingSetting`
* Input field `custom_module_form_id` of type `ID` was added to input object type `CustomMetricInput`
* Field `appointment` was added to object type `GeneratedFormAnswerGroupType`
* Field `appointment_id` was added to object type `GeneratedFormAnswerGroupType`
* Field `action` was added to object type `GoalHistory`
* Field `can_delete_automations` was added to object type `OrganizationMembership`
* Field `can_edit_automations` was added to object type `OrganizationMembership`
* Field `can_view_automations` was added to object type `OrganizationMembership`
* Field `is_in_other_orgs` was added to object type `OrganizationMembership`
* Field `organization` was added to object type `OrganizationMembership`
* Field `can_delete_automations` was added to object type `PermissionTemplateType`
* Field `can_edit_automations` was added to object type `PermissionTemplateType`
* Field `can_view_automations` was added to object type `PermissionTemplateType`
* Enum value `RECEIVED_DIRECT_MESSAGE` was added to enum `SentWebhookResourceType`
* Field `SubscriptionInstance.month_total` is deprecated
* Field `SubscriptionInstance.month_total` has deprecation reason `This field is no longer supported and always returns null. Use monthly_cost_of_base_plan instead.`
* Input field `send_embeddable_appt_creator_email` of type `Boolean` was added to input object type `createAppointmentSettingInput`
* Input field `insurance_billing_enabled` of type `Boolean` was added to input object type `createAutomatedInsuranceBillingSettingInput`
* Input field `action` of type `GoalHistoryActionTypeEnum` was added to input object type `createGoalHistoryInput`
* Input field `zoom_open_preference` of type `String` was added to input object type `updateAppointmentSettingInput`
* Input field `send_embeddable_appt_creator_email` of type `Boolean` was added to input object type `updateAppointmentSettingInput`
* Input field `insurance_billing_enabled` of type `Boolean` was added to input object type `updateAutomatedInsuranceBillingSettingInput`
* Input field `can_delete_automations` of type `Boolean` was added to input object type `updateOrganizationMembershipInput`
* Input field `can_edit_automations` of type `Boolean` was added to input object type `updateOrganizationMembershipInput`
* Input field `can_view_automations` of type `Boolean` was added to input object type `updateOrganizationMembershipInput`
* Input field `can_delete_automations` of type `Boolean` was added to input object type `updatePermissionTemplateInput`
* Input field `can_edit_automations` of type `Boolean` was added to input object type `updatePermissionTemplateInput`
* Input field `can_view_automations` of type `Boolean` was added to input object type `updatePermissionTemplateInput`

### 2026-02-20

* Input field `initiated_by` of type `CancellationReasonTypeEnum` was added to input object type `CancellationReasonOptionInput`
* Field `append_current_user_id` was added to object type `CustomSidebarOverride`
* Field `can_link_prescriptions_to_chart_notes` was added to object type `Organization`
* Field `clinic_id` was added to object type `Prescription`
* Field `dispensable_drug_id` was added to object type `Prescription`
* Field `dispense_unit_id` was added to object type `Prescription`
* Field `display_name` was added to object type `Prescription`
* Field `eligibility_id` was added to object type `Prescription`
* Field `error_ignored` was added to object type `Prescription`
* Field `formulary` was added to object type `Prescription`
* Field `free_text_type` was added to object type `Prescription`
* Field `is_rx_renewal` was added to object type `Prescription`
* Field `medication_status` was added to object type `Prescription`
* Field `non_dose_spot_prescription_id` was added to object type `Prescription`
* Field `patient_medication_id` was added to object type `Prescription`
* Field `prescriber_agent_id` was added to object type `Prescription`
* Field `prescriber_id` was added to object type `Prescription`
* Field `rx_renewal_note` was added to object type `Prescription`
* Field `supervisor_id` was added to object type `Prescription`
* Field `supply_id` was added to object type `Prescription`
* Field `type` was added to object type `Prescription`
* Input field `suppress_webhook_notifications` of type `Boolean` was added to input object type `createAppointmentInput`
* Input field `suppress_webhook_notifications` of type `Boolean` was added to input object type `deleteAppointmentInput`
* Input field `suppress_webhook_notifications` of type `Boolean` was added to input object type `updateAppointmentInput`

### 2026-02-13

* Type `ResetMfaInput` was added
* Type `ResetMfaPayload` was added
* Field `file_attachment` was added to object type `CustomModule`
* Field `resetMfa` was added to object type `Mutation`
* Field `paginated_users` was added to object type `Organization`
* Field `organization_id` was added to object type `User`
* Field `User.can_link_labs_to_chart_notes` is deprecated
* Field `User.can_link_labs_to_chart_notes` has deprecation reason `Use `OrganizationType.can\_link\_labs\_to\_chart\_notes` instead`

### 2026-02-06

* Type `CreateSharingsInput` was added
* Type `DestroySharingsInput` was added
* Type `SentWebhookResourceType` was added
* Type `Shareable` was added
* Type `ShareableType` was added
* Type `UserGroupEdge` was added
* Type `UserGroupPaginationConnection` was added
* Field `custom_module_form` was added to object type `CustomMetric`
* Field `custom_module_form_id` was added to object type `CustomMetric`
* Field `deleted_at` was added to object type `CustomModuleForm`
* Field `shareable_org_members` was added to object type `Document`
* Field `shareable_patients` was added to object type `Document`
* Field `shareable_user_groups` was added to object type `Document`
* Field `linked_to_autoscored_form` was added to object type `Entry`
* Field `record_created_at` was added to object type `Entry`
* Field `shareable_org_members` was added to object type `Folder`
* Field `shareable_patients` was added to object type `Folder`
* Field `shareable_user_groups` was added to object type `Folder`
* Field `createSharings` was added to object type `Mutation`
* Field `deleteSharings` was added to object type `Mutation`
* Field `shareable` was added to object type `Query`
* Argument `resource_id: ID` added to field `Query.sentWebhooks`
* Argument `resource_type: SentWebhookResourceType` added to field `Query.sentWebhooks`
* Argument `failed: Boolean` added to field `Query.sentWebhooks`
* Argument `resource_id: ID` added to field `Query.sentWebhooksCount`
* Argument `resource_type: SentWebhookResourceType` added to field `Query.sentWebhooksCount`
* Argument `http_response_status: String` added to field `Query.sentWebhooksCount`

### 2026-01-30

* Field `cancellation_reason` was added to object type `Appointment`
* Field `other_cancellation_reason` was added to object type `Appointment`
* Enum value `USER_NOTIFICATIONS_COUNT` was added to enum `SignedStreamName`
* Field `can_link_labs_to_chart_notes` was added to object type `User`
* Input field `cancellation_reason_id` of type `ID` was added to input object type `updateAppointmentInput`
* Input field `cancellation_initiated_by` of type `String` was added to input object type `updateAppointmentInput`
* Input field `other_cancellation_reason` of type `String` was added to input object type `updateAppointmentInput`

### 2026-01-23

* Type `InsurancePayment` was added
* Type `InsurancePaymentConnection` was added
* Type `InsurancePaymentEdge` was added
* Type `InsurancePaymentsDepositStatusEnum` was added
* Type `InsurancePaymentsOrderKeys` was added
* Type `asyncBulkCreateOrganizationMembershipsInput` was added
* Type `asyncBulkCreateOrganizationMembershipsPayload` was added
* Type `createInsurancePaymentInput` was added
* Type `createInsurancePaymentPayload` was added
* Type `deleteManualInsurancePaymentInput` was added
* Type `deleteManualInsurancePaymentPayload` was added
* Type `updateInsurancePaymentDepositStatusInput` was added
* Type `updateInsurancePaymentDepositStatusPayload` was added
* Type `updateManualInsurancePaymentInput` was added
* Type `updateManualInsurancePaymentPayload` was added
* Field `asyncBulkCreateOrganizationMemberships` was added to object type `Mutation`
* Field `createInsurancePayment` was added to object type `Mutation`
* Field `deleteManualInsurancePayment` was added to object type `Mutation`
* Field `updateInsurancePaymentDepositStatus` was added to object type `Mutation`
* Field `updateManualInsurancePayment` was added to object type `Mutation`
* Field `id` was added to object type `PatientEncounter`
* Field `insurancePayments` was added to object type `Query`

### 2026-01-16

* Type `SmsTemplateWarning` was added
* Type `bulkCreateOrganizationMembershipsInput` was added
* Type `bulkCreateOrganizationMembershipsPayload` was added
* Field `client_cancel_reason_required` was added to object type `AppointmentSetting`
* Field `provider_cancel_reason_required` was added to object type `AppointmentSetting`
* Field `bulkCreateOrganizationMemberships` was added to object type `Mutation`
* Input field `client_cancel_reason_required` of type `Boolean` was added to input object type `createAppointmentSettingInput`
* Input field `provider_cancel_reason_required` of type `Boolean` was added to input object type `createAppointmentSettingInput`
* Input field `custom_text_reminder_body` of type `String` was added to input object type `createAppointmentTypeInput`
* Field `sms_template_warning` was added to object type `createAppointmentTypePayload`
* Input field `client_cancel_reason_required` of type `Boolean` was added to input object type `updateAppointmentSettingInput`
* Input field `provider_cancel_reason_required` of type `Boolean` was added to input object type `updateAppointmentSettingInput`
* Field `sms_template_warning` was added to object type `updateAppointmentTypePayload`

### 2026-01-09

* Type `CancellationReasonTypeEnum` was added
* Type `CreateMobileHealthDataIntegrationInput` was added
* Type `CreateMobileHealthDataIntegrationPayload` was added
* Type `DeleteMobileHealthDataIntegrationInput` was added
* Type `DeleteMobileHealthDataIntegrationPayload` was added
* Type `HttpHeader` was added
* Type `MobileHealthDataIntegration` was added
* Type `MobileHealthDataIntegrationType` was added
* Type `createFormAnswerFileAttachmentInput` was added
* Type `createFormAnswerFileAttachmentPayload` was added
* Type `createFormAnswerFileAttachmentUploadUrlInput` was added
* Type `createFormAnswerFileAttachmentUploadUrlPayload` was added
* Type `deleteFormAnswerFileAttachmentInput` was added
* Type `deleteFormAnswerFileAttachmentPayload` was added
* Field `reason_type` was added to object type `CancellationReason`
* Field `allow_google_health_connect_sync` was added to object type `FeatureToggle`
* Field `createFormAnswerFileAttachment` was added to object type `Mutation`
* Field `createFormAnswerFileAttachmentUploadUrl` was added to object type `Mutation`
* Field `createMobileHealthDataIntegration` was added to object type `Mutation`
* Field `deleteFormAnswerFileAttachment` was added to object type `Mutation`
* Field `deleteMobileHealthDataIntegration` was added to object type `Mutation`
* Argument `reason_type: CancellationReasonTypeEnum` (with default value) added to field `Organization.cancellation_reasons`
* Field `mobile_health_integrations` was added to object type `User`
* Field `most_important_features` was added to object type `User`
* Field `profession` was added to object type `User`
* Argument `active: Boolean` added to field `User.policies`
* Input field `allow_google_health_connect_sync` of type `Boolean` was added to input object type `createFeatureToggleInput`
* Input field `allow_google_health_connect_sync` of type `Boolean` was added to input object type `updateFeatureToggleInput`

### 2025-12-19

* Type `AppointmentEdge` was added
* Type `AppointmentPaginationConnection` was added
* Type `TagEdge` was added
* Type `TagPaginationConnection` was added
* Field `will_be_scribed` was added to object type `Appointment`
* Field `recurringAppointment` was added to object type `Query`
* Field `tagsPaginated` was added to object type `Query`
* Argument `primary_payer_ids: [ID!]` (with default value) added to field `Query.chartNotes`
* Argument `tag_ids: [ID!]` (with default value) added to field `Query.chartNotes`
* Argument `primary_payer_ids: [ID!]` (with default value) added to field `Query.chartNotesCount`
* Argument `tag_ids: [ID!]` (with default value) added to field `Query.chartNotesCount`
* Field `appointments` was added to object type `RecurringAppointment`
* Field `patients_tagged_count` was added to object type `Tag`
* Field `providers_tagged_count` was added to object type `Tag`
* Field `primary_insurance_policy` was added to object type `User`

### 2025-12-05

* Type `BulkDeleteAvailabilityInput` was added
* Type `BulkDeleteAvailabilityPayload` was added
* Type `CreateCustomModuleFileAttachmentInput` was added
* Type `CreateCustomModuleFileAttachmentPayload` was added
* Type `DeleteTranscriptInput` was added
* Type `DeleteTranscriptPayload` was added
* Type `RelatedObjectUnion` was added
* Type `deleteZoomRecordingFileInput` was added
* Type `deleteZoomRecordingFilePayload` was added
* Field `cpt_code` was added to object type `AppointmentPricingInfoType`
* Field `created_at` was added to object type `Availability`
* Field `updated_at` was added to object type `Availability`
* Field `related_object` was added to object type `FormAnswerGroupAuditEvent`
* Field `bulkDeleteAvailability` was added to object type `Mutation`
* Field `createCustomModuleFileAttachment` was added to object type `Mutation`
* Field `deleteTranscript` was added to object type `Mutation`
* Field `deleteZoomRecordingFile` was added to object type `Mutation`
* Field `can_delete_recordings` was added to object type `OrganizationMembership`
* Field `can_unlink_chart_note_from_appointment` was added to object type `OrganizationMembership`
* Field `can_view_recordings` was added to object type `OrganizationMembership`
* Field `can_delete_recordings` was added to object type `PermissionTemplateType`
* Field `can_unlink_chart_note_from_appointment` was added to object type `PermissionTemplateType`
* Field `can_view_recordings` was added to object type `PermissionTemplateType`
* Argument `accepts_insurance_plan_id: ID` added to field `Query.availableSlotsForRange`
* Argument `accepts_insurance_plan_id: ID` added to field `Query.daysAvailableForRange`
* Argument `accepts_insurance_plan_id: ID` added to field `Query.nextAvailableSlot`
* Input field `can_delete_recordings` of type `Boolean` was added to input object type `createPermissionTemplateInput`
* Input field `can_unlink_chart_note_from_appointment` of type `Boolean` was added to input object type `createPermissionTemplateInput`
* Input field `can_view_recordings` of type `Boolean` was added to input object type `createPermissionTemplateInput`
* Input field `most_important_features` of type `[String]` was added to input object type `createPersonalizationQuestionnaireInput`
* Input field `remove_async_if_needed` of type `Boolean` was added to input object type `deleteTagInput`
* Field `removing_async` was added to object type `deleteTagPayload`
* Input field `can_delete_recordings` of type `Boolean` was added to input object type `updateOrganizationMembershipInput`
* Input field `can_unlink_chart_note_from_appointment` of type `Boolean` was added to input object type `updateOrganizationMembershipInput`
* Input field `can_view_recordings` of type `Boolean` was added to input object type `updateOrganizationMembershipInput`
* Input field `can_delete_recordings` of type `Boolean` was added to input object type `updatePermissionTemplateInput`
* Input field `can_unlink_chart_note_from_appointment` of type `Boolean` was added to input object type `updatePermissionTemplateInput`
* Input field `can_view_recordings` of type `Boolean` was added to input object type `updatePermissionTemplateInput`

### 2025-11-21

* Type `TranscriptStatusEnum` was added
* Field `generated_form_answer_group` was added to object type `Appointment`
* Argument `status: [TranscriptStatusEnum]` added to field `Appointment.transcripts`
* Field `client_display_description` was added to object type `AppointmentType`
* Field `client_facing_display_name` was added to object type `AppointmentType`
* Field `metadata` was added to object type `Benefit`
* Input field `metadata` of type `JSON` was added to input object type `BenefitInput`
* Enum value `ClaimMdRejectionMessagesInfo.CLAIM_MD_REJECTION_MESSAGES_NOT_AVAILABLE` was deprecated with reason `This value is no longer returned. The cms1500s-rejection-reason feature flag has been permanently enabled.`
* Directive `deprecated` was added to enum value `ClaimMdRejectionMessagesInfo.CLAIM_MD_REJECTION_MESSAGES_NOT_AVAILABLE`
* Input field `metadata` of type `JSON` was added to input object type `ClientInsurancePlanInput`
* Input field `metadata` of type `JSON` was added to input object type `ClientPolicyInput`
* Field `custom_module_form` was added to object type `GeneratedFormAnswerGroupType`
* Field `form_answer_group` was added to object type `GeneratedFormAnswerGroupType`
* Field `metadata` was added to object type `InsurancePlan`
* Input field `metadata` of type `JSON` was added to input object type `InsurancePlanInput`
* Field `metadata` was added to object type `Policy`
* Input field `metadata` of type `JSON` was added to input object type `PolicyInput`
* Field `Query.surescriptsReportedMedicationHistory` is deprecated
* Field `Query.surescriptsReportedMedicationHistory` has deprecation reason `Use API version 2025-11-30 or later to return MedicationHistoryType connection`
* Field `metadata` was added to object type `RequestedPayment`
* Field `status` was added to object type `Transcript`
* Input field `metadata` of type `JSON` was added to input object type `UserPolicyInput`
* Input field `client_display_description` of type `String` was added to input object type `createAppointmentTypeInput`
* Input field `ssn` of type `String` was added to input object type `createClientInput`
* Input field `metadata` of type `JSON` was added to input object type `createInsurancePlanInput`
* Input field `metadata` of type `JSON` was added to input object type `createRequestedPaymentInput`
* Input field `client_display_description` of type `String` was added to input object type `updateAppointmentTypeInput`
* Input field `ssn` of type `String` was added to input object type `updateClientInput`
* Input field `metadata` of type `JSON` was added to input object type `updateInsurancePlanInput`
* Input field `metadata` of type `JSON` was added to input object type `updatePolicyMutationInput`
* Input field `metadata` of type `JSON` was added to input object type `updateRequestedPaymentInput`

### 2025-11-07

* Type `ApiKeyEdge` was added
* Type `ApiKeyPaginationConnection` was added
* Type `InsurancePlanEdge` was added
* Type `InsurancePlanPaginationConnection` was added
* Type `ProviderBio` was added
* Type `ProviderBioInput` was added
* Field `branded_name` was added to object type `AssumedBrand`
* Field `amount_paid_string` was added to object type `BillingItem`
* Enum value `CORE` was added to enum `IntegrationPlanTiersType`
* Field `provider_insurance_plans` was added to object type `Organization`
* Field `sentNotificationRecord` was added to object type `Query`
* Field `api_keys` was added to object type `User`
* Field `has_ai_summaries` was added to object type `User`
* Field `provider_bio` was added to object type `User`
* Directive `deprecated` was added to input field `organization_id` in input object `updateOrganizationCptCodeInput`
* Input field `provider_bio` of type `ProviderBioInput` was added to input object type `updateOrganizationMemberInput`
* Input field `bypass_api_key_warning` of type `Boolean` was added to input object type `updateOrganizationMembershipInput`

### 2025-10-24

* Type `EpisodeOfCareConnection` was added
* Type `EpisodeOfCareEdge` was added
* Type `FileAttachment` was added
* Type `IntegrationButtonConfig` was added
* Type `PrescriptionMedication` was added
* Type `PrescriptionMedicationConnection` was added
* Type `PrescriptionMedicationEdge` was added
* Type `PrescriptionMedicationOrderBy` was added
* Type `PrescriptionMedicationQueryFiltersInput` was added
* Type `PrescriptionMedicationStatus` was added
* Type `PrescriptionMedicationTypeEnum` was added
* Argument `transcript_type: TranscriptTypeEnum` added to field `Appointment.transcripts`
* Field `closed_at` was added to object type `AppointmentRequestType`
* Field `closed_by` was added to object type `AppointmentRequestType`
* Field `first_appointment` was added to object type `AppointmentRequestType`
* Enum value `CARE_PLAN` was added to enum `AuditEventResourceName`
* Enum value `GOAL` was added to enum `AuditEventResourceName`
* Field `favorite_saved_filter_id` was added to object type `CalendarViewSetting`
* Field `view_medications` was added to object type `FeatureToggle`
* Field `file_attachments` was added to object type `FormAnswer`
* Field `extra_info` was added to object type `IntegrationDetailsType`
* Field `IntegrationDetailsType.formatted_description` is deprecated
* Field `IntegrationDetailsType.formatted_description` has deprecation reason `This field is being deprecated in favor of structured jsonb data in integration_option`
* Field `button_not_connected` was added to object type `IntegrationOptionType`
* Field `normalized_status` was added to object type `MedicationType`
* Field `Mutation.healthAssessmentServiceSignup` is deprecated
* Field `Mutation.healthAssessmentServiceSignup` has deprecation reason `Deprecated, do not use`
* Field `Mutation.sendSpeakToTrainerNotification` is deprecated
* Field `Mutation.sendSpeakToTrainerNotification` has deprecation reason `Deprecated, do not use`
* Field `Mutation.updateCalorieLevel` is deprecated
* Field `Mutation.updateCalorieLevel` has deprecation reason `Deprecated, do not use`
* Field `Mutation.updateMacronutrientSplit` is deprecated
* Field `Mutation.updateMacronutrientSplit` has deprecation reason `Deprecated, do not use`
* Field `send_email_on_appointment_reschedule` was added to object type `NotificationSetting`
* Argument `active: Boolean` added to field `Organization.organization_memberships`
* Argument `exclude_org_ids: [ID!]` (with default value) added to field `Organization.organization_memberships`
* Argument `active: Boolean` added to field `Organization.organization_memberships_count`
* Argument `exclude_org_ids: [ID!]` (with default value) added to field `Organization.organization_memberships_count`
* Field `normalized_status` was added to object type `Prescription`
* Field `episodesOfCare` was added to object type `Query`
* Field `patientEncounter` was added to object type `Query`
* Field `prescriptionMedications` was added to object type `Query`
* Argument `current_statuses: [AppointmentRequestStatus!]` (with default value) added to field `Query.appointmentRequests`
* Default value for argument `use_provider_inclusions` on field `Query.appointments` changed from `false` to `true`
* Default value for argument `use_provider_inclusions` on field `Query.appointmentsCount` changed from `false` to `true`
* Field `Query.healthAssessment` is deprecated
* Field `Query.healthAssessment` has deprecation reason `Deprecated, do not use`
* Argument `assignees: [ID]` added to field `Query.tasks`
* Argument `assignees: [ID]` added to field `Query.tasksCount`
* Field `previous_recurring_appointment_id` was added to object type `RecurringAppointment`
* Field `open_balance_due_count` was added to object type `User`
* Field `signup_completed` was added to object type `User`
* Argument `include_suborg_patients: Boolean` (with default value) added to field `User.active_patients_count`
* Input field `view_medications` of type `Boolean` was added to input object type `createFeatureToggleInput`
* Input field `favorite_saved_filter_id` of type `ID` was added to input object type `updateCalendarViewSettingInput`
* Input field `view_medications` of type `Boolean` was added to input object type `updateFeatureToggleInput`
* Input field `recurring_payment_reminder_emails` of type `Boolean` was added to input object type `updateNotificationSettingInput`
* Input field `send_email_on_appointment_reschedule` of type `Boolean` was added to input object type `updateNotificationSettingInput`
* Directive `deprecated` was added to input field `send_recurring_payment_reminder_emails` in input object `updateNotificationSettingInput`

### 2025-09-12

* Type `AppointmentRequestStatus` was added
* Field `appointment_request_id` was added to object type `Appointment`
* Field `current_status` was added to object type `AppointmentRequestType`
* Enum value `TEN_MINUTES` was added to enum `BaseCalendarInterval`
* Argument `custom_module_ids: [ID]` added to field `FormAnswerGroup.form_answers`
* Field `send_recurring_payment_reminder_emails` was added to object type `NotificationSetting`
* Field `automated_insurance_billing_setting` was added to object type `Organization`
* Argument `current_status: AppointmentRequestStatus` (with default value) added to field `Query.appointmentRequests`
* Argument `custom_module_ids: [ID]` added to field `Query.formAnswerGroupsCount`
* Field `completed_by` was added to object type `Task`
* Input field `appointment_request_id` of type `ID` was added to input object type `createAppointmentInput`
* Input field `status` of type `AppointmentRequestStatus` was added to input object type `updateAppointmentRequestInput`
* Directive `deprecated` was added to input field `id` in input object `updateAutomatedInsuranceBillingSettingInput`
* Input field `send_recurring_payment_reminder_emails` of type `Boolean` was added to input object type `updateNotificationSettingInput`

### 2025-08-29

* Type `PartnerType` was added
* Field `user_avatar_url` was added to object type `FormAnswerGroupSigning`
* Field `user_full_legal_name` was added to object type `FormAnswerGroupSigning`
* Field `user_qualifications` was added to object type `FormAnswerGroupSigning`
* Field `partner_type` was added to object type `IntegrationOptionType`
* Field `credit_balance` was added to object type `SubscriptionInstance`

### 2025-08-15

* Type `AppointmentPricingMethod` was added
* Type `BaseCalendarInterval` was added
* Type `RequestIntegrationInput` was added
* Type `RequestIntegrationPayload` was added
* Field `effective_pricing_method` was added to object type `Appointment`
* Field `base_calendar_interval` was added to object type `AppointmentSetting`
* Field `requestIntegration` was added to object type `Mutation`
* Argument `exclude_ids: [ID!]` (with default value) added to field `Organization.providers`
* Argument `order_by: UserOrderKeys` added to field `Organization.providers`
* Argument `page_size: Int` (with default value) added to field `Organization.providers`
* Argument `active_status: String` added to field `Organization.providers_count`
* Argument `exclude_ids: [ID!]` (with default value) added to field `Organization.providers_count`
* Argument `keywords: String` added to field `Organization.providers_count`
* Argument `licensed_in_state: String` added to field `Organization.providers_count`
* Argument `provider_ids: [ID]` (with default value) added to field `Organization.providers_count`
* Argument `with_private_notes_for_id: String` added to field `Organization.providers_count`
* Argument `with_tag_ids: [ID]` added to field `Organization.providers_count`
* Field `paid_for_group` was added to object type `SubscriptionInstance`
* Field `trial_end_at` was added to object type `SubscriptionInstance`
* Input field `base_calendar_interval` of type `BaseCalendarInterval` was added to input object type `createAppointmentSettingInput`
* Input field `billing_address` of type `BillingAddressInput` was added to input object type `createPersonalizationQuestionnaireInput`
* Input field `base_calendar_interval` of type `BaseCalendarInterval` was added to input object type `updateAppointmentSettingInput`
* Input field `stripe_plan` of type `String` was added to input object type `updateSubscriptionInput`

### 2025-08-01

* Type `OrganizationSettingsInput` was added
* Type `TranscriptTypeEnum` was added
* Field `appointment_category` was added to object type `AppointmentWorkflowStatusAppointmentType`
* Input field `organization_settings` of type `OrganizationSettingsInput` was added to input object type `SubOrganizationInfoInput`
* Field `transcript_end` was added to object type `Transcript`
* Field `transcript_type` was added to object type `Transcript`
* Enum value `shared_screen_with_speaker_view_cc` was added to enum `ZoomRecordingTypeEnum`

### 2025-07-18

* Type `CarePlanRecommendationCategory` was added
* Type `Transcript` was added
* Type `createCarePlanRecommendationCategoryInput` was added
* Type `createCarePlanRecommendationCategoryPayload` was added
* Type `deleteCarePlanRecommendationCategoryInput` was added
* Type `deleteCarePlanRecommendationCategoryPayload` was added
* Type `updateCarePlanRecommendationCategoryInput` was added
* Type `updateCarePlanRecommendationCategoryPayload` was added
* Field `transcripts` was added to object type `Appointment`
* Field `createCarePlanRecommendationCategory` was added to object type `Mutation`
* Field `deleteCarePlanRecommendationCategory` was added to object type `Mutation`
* Field `updateCarePlanRecommendationCategory` was added to object type `Mutation`
* Field `care_plan_recommendation_categories` was added to object type `Organization`
* Field `fee_per_unit_cents` was added to object type `OrganizationFeeScheduleCptCodeType`
* Field `OrganizationFeeScheduleCptCodeType.fee_per_unit` is deprecated
* Field `OrganizationFeeScheduleCptCodeType.fee_per_unit` has deprecation reason `Use `fee\_per\_unit\_cents` instead`
* Argument `range_end: ISO8601Date` added to field `Query.appointmentRequests`
* Argument `range_start: ISO8601Date` added to field `Query.appointmentRequests`
* Field `care_plan_recommendation_category` was added to object type `Recommendation`
* Enum value `UPDATED_AT_ASC` was added to enum `RequestedPaymentOrderKeys`
* Enum value `UPDATED_AT_DESC` was added to enum `RequestedPaymentOrderKeys`
* Input field `suppress_patient_updated_webhooks` of type `Boolean` was added to input object type `bulkUpdateClientsInput`
* Input field `care_plan_recommendation_category_id` of type `ID` was added to input object type `createRecommendationInput`
* Directive `deprecated` was added to input field `recommendation_type` in input object `createRecommendationInput`
* Input field `care_plan_recommendation_category_id` of type `ID` was added to input object type `updateRecommendationInput`
* Directive `deprecated` was added to input field `recommendation_type` in input object `updateRecommendationInput`

### 2025-07-04

* Type `AdjustmentGroup` was added
* Type `EpisodeOfCare` was added
* Type `IntegrationDetailsType` was added
* Type `IntegrationPlanTiersType` was added
* Type `LinkUnlinkEncounterToEpisodeOfCare` was added
* Type `PatientEncounter` was added
* Type `createEpisodeOfCareInput` was added
* Type `createEpisodeOfCarePayload` was added
* Type `deleteEpisodeOfCareInput` was added
* Type `deleteEpisodeOfCarePayload` was added
* Type `linkEncounterToEpisodeOfCareInput` was added
* Type `linkEncounterToEpisodeOfCarePayload` was added
* Type `unlinkEncounterToEpisodeOfCareInput` was added
* Type `unlinkEncounterToEpisodeOfCarePayload` was added
* Type `updateEpisodeOfCareInput` was added
* Type `updateEpisodeOfCarePayload` was added
* Field `checked_in` was added to object type `AppointmentFrequencyDataType`
* Enum value `requested_date_asc` was added to enum `AppointmentRequestOrderKeys`
* Enum value `requested_date_desc` was added to enum `AppointmentRequestOrderKeys`
* Field `enable_checked_in_status` was added to object type `AppointmentSetting`
* Field `enable_late_cancellation_status` was added to object type `AppointmentSetting`
* Field `era_service_lines` was added to object type `Era`
* Field `adjustment_group` was added to object type `EraAdjustment`
* Field `integration_details` was added to object type `IntegrationOptionType`
* Field `createEpisodeOfCare` was added to object type `Mutation`
* Field `deleteEpisodeOfCare` was added to object type `Mutation`
* Field `linkEncounterToEpisodeOfCare` was added to object type `Mutation`
* Field `unlinkEncounterToEpisodeOfCare` was added to object type `Mutation`
* Field `updateEpisodeOfCare` was added to object type `Mutation`
* Enum value `OTHER` was added to enum `PdfLetterheadTemplateAddressSource`
* Argument `appointment_location_ids: [ID!]` added to field `Query.appointmentRequests`
* Argument `custom_module_form_ids: [ID!]` (with default value) added to field `Query.chartNotes`
* Argument `exclude_requested_and_intake_flow_forms: Boolean` (with default value) added to field `Query.chartNotes`
* Argument `custom_module_form_ids: [ID!]` (with default value) added to field `Query.chartNotesCount`
* Argument `exclude_requested_and_intake_flow_forms: Boolean` (with default value) added to field `Query.chartNotesCount`
* Field `has_invalid_characters` was added to object type `User`
* Input field `enable_checked_in_status` of type `Boolean` was added to input object type `createAppointmentSettingInput`
* Input field `enable_late_cancellation_status` of type `Boolean` was added to input object type `createAppointmentSettingInput`
* Input field `include_letterhead` of type `Boolean` was added to input object type `createSentFaxInput`
* Input field `enable_checked_in_status` of type `Boolean` was added to input object type `updateAppointmentSettingInput`
* Input field `enable_late_cancellation_status` of type `Boolean` was added to input object type `updateAppointmentSettingInput`

### 2025-06-20

* Type `AcceptedInsurancePlanConnection` was added
* Type `AcceptedInsurancePlanEdge` was added
* Type `ActiveCareTeamMemberOrderKeys` was added
* Type `CalendarStatus` was added
* Type `CalendarType` was added
* Type `ExternalCalendarConnection` was added
* Type `ExternalCalendarEdge` was added
* Field `insurance_plan_ids_filter` was added to object type `CalendarViewSetting`
* Field `user_id` was added to object type `ExternalCalendar`
* Field `accepted_insurance_plans` was added to object type `Organization`
* Field `insurance_plans_used_by_organization_providers` was added to object type `Organization`
* Argument `order_by: ActiveCareTeamMemberOrderKeys` added to field `Organization.active_care_team_members`
* Argument `selected_insurance_plan_id: ID` added to field `Organization.active_care_team_members`
* Field `externalCalendars` was added to object type `Query`
* Argument `insurance_plan_ids: [ID]` added to field `Query.appointments`
* Argument `insurance_plan_ids: [ID]` added to field `Query.appointmentsCount`
* Argument `insurance_plan_ids: [ID]` added to field `Query.availabilities`
* Argument `include_header_on_every_page: Boolean` (with default value) added to field `Query.shareNotePreview`
* Argument `pdf_letterhead_template_id: ID` added to field `Query.shareNotePreview`
* Input field `include_header_on_every_page` of type `Boolean` was added to input object type `shareAnswersAsDocumentInput`
* Input field `pdf_letterhead_template_id` of type `ID` was added to input object type `shareAnswersAsDocumentInput`
* Input field `insurance_plan_ids_filter` of type `[ID!]` was added to input object type `updateCalendarViewSettingInput`

### 2025-06-06

* Type `Era` was added
* Type `EraAdjustment` was added
* Type `EraConnection` was added
* Type `EraEdge` was added
* Type `EraServiceLine` was added
* Type `EraServiceLineConnection` was added
* Type `EraServiceLineEdge` was added
* Type `createProviderAcceptedInsurancePlansInput` was added
* Type `createProviderAcceptedInsurancePlansPayload` was added
* Type `createSetupIntentInput` was added
* Type `createSetupIntentPayload` was added
* Field `alt_branded_logo_url` was added to object type `AssumedBrand`
* Field `pcn` was added to object type `ClaimSubmission`
* Field `eras` was added to object type `Cms1500`
* Field `has_been_submitted` was added to object type `Cms1500`
* Field `createProviderAcceptedInsurancePlans` was added to object type `Mutation`
* Field `createSetupIntent` was added to object type `Mutation`
* Field `sender_id` was added to object type `SentDirectMessage`
* Field `created_at` was added to object type `StripeCustomerDetail`
* Field `additional_quick_profile_items` was added to object type `User`
* Field `hide_bac_entry_actions` was added to object type `User`
* Input field `assignee_ids` of type `[ID!]` was added to input object type `createTaskInput`
* Directive `deprecated` was added to input field `user_id` in input object `createTaskInput`
* Input field `assignee_ids` of type `[ID!]` was added to input object type `updateTaskInput`
* Directive `deprecated` was added to input field `user_id` in input object `updateTaskInput`

### 2025-05-23

* Type `ProviderAcceptedInsurancePlanType` was added
* Type `VisualizeDashboardType` was added
* Type `deleteProviderAcceptedInsurancePlanInput` was added
* Type `deleteProviderAcceptedInsurancePlanPayload` was added
* Field `is_custom` was added to object type `InsurancePlan`
* Field `deleteProviderAcceptedInsurancePlan` was added to object type `Mutation`
* Field `scheduled_conversation_id` was added to object type `Note`
* Field `providerAcceptedInsurancePlan` was added to object type `Query`
* Field `providerAcceptedInsurancePlans` was added to object type `Query`
* Field `visualizeDashboard` was added to object type `Query`
* Argument `sent_after: ISO8601DateTime` added to field `Query.sentWebhooks`
* Argument `sent_before: ISO8601DateTime` added to field `Query.sentWebhooks`
* Enum value `BALANCE_DUE_ASC` was added to enum `RequestedPaymentOrderKeys`
* Enum value `BALANCE_DUE_DESC` was added to enum `RequestedPaymentOrderKeys`
* Enum value `SERVICE_DATE_ASC` was added to enum `RequestedPaymentOrderKeys`
* Enum value `SERVICE_DATE_DESC` was added to enum `RequestedPaymentOrderKeys`

### 2025-05-09

* Type `PrescriptionDiagnosis` was added
* Field `insurance_specific_cpt_code_pricing` was added to object type `AppointmentSetting`
* Field `invitees` was added to object type `NoteScheduler`
* Field `NoteScheduler.first_four_invitees` changed type from `[User!]` to `[User!]!`
* Field `first_prescription_diagnosis` was added to object type `Prescription`
* Field `second_prescription_diagnosis` was added to object type `Prescription`
* Field `unread_notifications_count` was added to object type `User`
* Input field `insurance_specific_cpt_code_pricing` of type `Boolean` was added to input object type `createAppointmentSettingInput`
* Input field `insurance_specific_cpt_code_pricing` of type `Boolean` was added to input object type `updateAppointmentSettingInput`

### 2025-04-25

* Type `AppointmentRequestOrderKeys` was added
* Type `AppointmentRequestSlotInput` was added
* Type `AppointmentRequestSlotType` was added
* Type `AppointmentRequestType` was added
* Type `AppointmentRequestTypeConnection` was added
* Type `AppointmentRequestTypeEdge` was added
* Type `PdfLetterheadTemplate` was added
* Type `PdfLetterheadTemplateAddressSource` was added
* Type `PdfLetterheadTemplateBrandLogoSource` was added
* Type `PdfLetterheadTemplateEmailSource` was added
* Type `PdfLetterheadTemplatePhoneNumberSource` was added
* Type `PdfLetterheadTemplateTeamMemberNameSource` was added
* Type `UserConnection` was added
* Type `UserEdge` was added
* Type `createAppointmentRequestInput` was added
* Type `createAppointmentRequestPayload` was added
* Type `createPdfLetterheadTemplateInput` was added
* Type `createPdfLetterheadTemplatePayload` was added
* Type `deleteAppointmentRequestInput` was added
* Type `deleteAppointmentRequestPayload` was added
* Type `destroyPdfLetterheadTemplateInput` was added
* Type `destroyPdfLetterheadTemplatePayload` was added
* Type `resetDefaultPdfLetterheadTemplateInput` was added
* Type `resetDefaultPdfLetterheadTemplatePayload` was added
* Type `setDefaultPdfLetterheadTemplateInput` was added
* Type `setDefaultPdfLetterheadTemplatePayload` was added
* Type `updateAppointmentRequestInput` was added
* Type `updateAppointmentRequestPayload` was added
* Type `updatePdfLetterheadTemplateInput` was added
* Type `updatePdfLetterheadTemplatePayload` was added
* Field `appointment_setting_id` was added to object type `AppointmentLocation`
* Input field `send_appointment_update_email` of type `Boolean` was added to input object type `AppointmentTypeAppointmentSettingInput`
* Enum value `ORGANIZATION` was added to enum `AuditEventResourceName`
* Enum value `ORGANIZATION_INFO` was added to enum `AuditEventResourceName`
* Enum value `ORGANIZATION_MEMBERSHIP` was added to enum `AuditEventResourceName`
* Field `createAppointmentRequest` was added to object type `Mutation`
* Field `createPdfLetterheadTemplate` was added to object type `Mutation`
* Field `deleteAppointmentRequest` was added to object type `Mutation`
* Field `destroyPdfLetterheadTemplate` was added to object type `Mutation`
* Field `resetDefaultPdfLetterheadTemplate` was added to object type `Mutation`
* Field `setDefaultPdfLetterheadTemplate` was added to object type `Mutation`
* Field `updateAppointmentRequest` was added to object type `Mutation`
* Field `updatePdfLetterheadTemplate` was added to object type `Mutation`
* Field `default_pdf_letterhead_template` was added to object type `Organization`
* Field `is_using_system_default_pdf_letterhead_template` was added to object type `Organization`
* Field `pdf_letterhead_templates` was added to object type `Organization`
* Field `hide_calendar_tab` was added to object type `OrganizationMembership`
* Field `appointmentRequest` was added to object type `Query`
* Field `appointmentRequests` was added to object type `Query`
* Field `pdfLetterheadTemplate` was added to object type `Query`
* Field `pdfLetterheadTemplatePreview` was added to object type `Query`
* Argument `organization_id: ID` added to field `Query.availabilitySummaryJson`
* Field `assignees` was added to object type `Task`
* Input field `enforce_availability` of type `Boolean` was added to input object type `createAppointmentInput`
* Input field `pdf_letterhead_template_id` of type `ID` was added to input object type `createSentFaxInput`
* Input field `pdf_letterhead_template_id` of type `ID` was added to input object type `generateChartingPdfInput`
* Input field `enforce_availability` of type `Boolean` was added to input object type `updateAppointmentInput`
* Input field `hide_calendar_tab` of type `Boolean` was added to input object type `updateOrganizationMembershipInput`

### 2025-04-11

* Type `AuditEvent` was added
* Type `AuditEventOrderKeys` was added
* Type `AuditEventResourceChange` was added
* Type `AuditEventResourceName` was added
* Type `AuditEventType` was added
* Type `SdDeleteClaimMdAccountInput` was added
* Type `SdDeleteClaimMdAccountPayload` was added
* Type `SdEnableClaimMdAccountInput` was added
* Type `SdEnableClaimMdAccountPayload` was added
* Type `SdGenerateInactiveProvidersReportInput` was added
* Type `SdGenerateInactiveProvidersReportPayload` was added
* Type `SdUpdateClaimMdAccountInput` was added
* Type `SdUpdateClaimMdAccountPayload` was added
* Type `ZoomCloudRecordingFile` was added
* Type `ZoomRecordingFileTypeEnum` was added
* Type `ZoomRecordingStatusEnum` was added
* Type `ZoomRecordingTypeEnum` was added
* Field `zoom_cloud_recording_files` was added to object type `Appointment`
* Field `form_answer_groups` was added to object type `Document`
* Field `documents` was added to object type `FormAnswerGroup`
* Field `deleteClaimMdAccount` was added to object type `Mutation`
* Field `enableClaimMdAccount` was added to object type `Mutation`
* Field `generateInactiveProvidersReport` was added to object type `Mutation`
* Field `updateClaimMdAccount` was added to object type `Mutation`
* Field `can_restrict_clients` was added to object type `OrganizationMembership`
* Field `can_restrict_clients` was added to object type `PermissionTemplateType`
* Field `auditLog` was added to object type `Query`
* Field `macro_micro_nutrients` was added to object type `ServingSize`
* Field `can_see_audit_log_ui` was added to object type `User`
* Input field `appointment_id` of type `ID` was added to input object type `createCms1500Input`
* Input field `can_restrict_clients` of type `Boolean` was added to input object type `createPermissionTemplateInput`
* Input field `can_restrict_clients` of type `Boolean` was added to input object type `updateOrganizationMembershipInput`
* Input field `can_restrict_clients` of type `Boolean` was added to input object type `updatePermissionTemplateInput`

### 2025-03-28

* Type `ChargeDisputeStatus` was added
* Type `ChargeDisputeType` was added
* Type `ChargeDisputeTypeConnection` was added
* Type `ChargeDisputeTypeEdge` was added
* Type `ChartNoteStatus` was added
* Type `Cms1500Status` was added
* Type `LabOrderInterpretation` was added
* Type `OrganizationFeeScheduleCptCodeType` was added
* Type `OrganizationFeeScheduleCptCodeTypeConnection` was added
* Type `OrganizationFeeScheduleCptCodeTypeEdge` was added
* Type `RequestedPaymentStatus` was added
* Type `SdDeleteChangeHealthAccountInput` was added
* Type `SdDeleteChangeHealthAccountPayload` was added
* Type `SdEnableScribeOrgInput` was added
* Type `SdEnableScribeOrgPayload` was added
* Type `SdUpdateChangeHealthAccountInput` was added
* Type `SdUpdateChangeHealthAccountPayload` was added
* Field `enable_appointment_requests` was added to object type `AppointmentSetting`
* Input field `enable_appointment_requests` of type `Boolean` was added to input object type `AppointmentTypeAppointmentSettingInput`
* Input field `send_appointment_cancellation_email` of type `Boolean` was added to input object type `AppointmentTypeAppointmentSettingInput`
* Field `chart_note_status` was added to object type `FormAnswerGroup`
* Field `requested_form_completion` was added to object type `FormAnswerGroup`
* Field `reviewing_providers` was added to object type `LabFiltersDataType`
* Field `interpretation` was added to object type `LabObservationResult`
* Field `interpretation` was added to object type `LabOrder`
* Field `reviewing_provider` was added to object type `LabOrder`
* Field `interpretation` was added to object type `LabResult`
* Field `deleteChangeAccount` was added to object type `Mutation`
* Field `enableScribe` was added to object type `Mutation`
* Field `updateChangeAccount` was added to object type `Mutation`
* Field `send_email_on_appt_request_for_anyone` was added to object type `NotificationSetting`
* Field `send_email_on_appt_request_for_you` was added to object type `NotificationSetting`
* Argument `include_suborg_providers: Boolean` added to field `Organization.providers`
* Argument `include_suborg_providers: Boolean` added to field `Organization.providers_count`
* Field `can_access_zus` was added to object type `OrganizationMembership`
* Field `chargeDisputes` was added to object type `Query`
* Field `chartNotes` was added to object type `Query`
* Field `chartNotesCount` was added to object type `Query`
* Field `organizationFeeScheduleCptCode` was added to object type `Query`
* Field `organizationFeeScheduleCptCodes` was added to object type `Query`
* Argument `chart_note_statuses: [AppointmentWorkflowChartNoteStatus]` (with default value) added to field `Query.appointmentWorkflowStatuses`
* Argument `client_id: ID` added to field `Query.appointmentWorkflowStatuses`
* Argument `cms1500_statuses: [Cms1500Status]` (with default value) added to field `Query.appointmentWorkflowStatuses`
* Argument `invoice_statuses: [RequestedPaymentStatus]` (with default value) added to field `Query.appointmentWorkflowStatuses`
* Argument `provider_ids: [ID!]` (with default value) added to field `Query.appointmentWorkflowStatuses`
* Argument `organization_id: ID` added to field `Query.appointments`
* Argument `organization_id: ID` added to field `Query.appointmentsCount`
* Argument `include_suborganizations: Boolean` (with default value) added to field `Query.availabilities`
* Argument `organization_id: ID` added to field `Query.availabilities`
* Argument `orderer_filter: String` added to field `Query.labOrders`
* Argument `reviewing_provider_filter: String` added to field `Query.labOrders`
* Argument `orderer_filter: String` added to field `Query.labOrdersCount`
* Argument `reviewing_provider_filter: String` added to field `Query.labOrdersCount`
* Argument `assigned_to_user: Boolean` added to field `Query.tasks`
* Argument `smart: Boolean` added to field `Query.tasks`
* Argument `assigned_to_user: Boolean` added to field `Query.tasksCount`
* Argument `client_id: String` added to field `Query.tasksCount`
* Argument `smart: Boolean` added to field `Query.tasksCount`
* Field `created_at` was added to object type `RequestedPayment`
* Field `updated_at` was added to object type `RequestedPayment`
* Field `attachments` was added to object type `SentDirectMessage`
* Field `has_binary_attachment` was added to object type `SentDirectMessage`
* Argument `keywords: String` added to field `User.active_patients_count`
* Input field `is_adding_credit_card` of type `Boolean` was added to input object type `completeCheckoutInput`
* Input field `enable_appointment_requests` of type `Boolean` was added to input object type `createAppointmentSettingInput`
* Directive `deprecated` was added to input field `use_cpt_codes_units_and_fees_with_appointment_types` in input object `createAutomatedInsuranceBillingSettingInput`
* Input field `metadata` of type `String` was added to input object type `createBillingItemInput`
* Input field `can_access_zus` of type `Boolean` was added to input object type `createPermissionTemplateInput`
* Input field `enable_appointment_requests` of type `Boolean` was added to input object type `updateAppointmentSettingInput`
* Directive `deprecated` was added to input field `use_cpt_codes_units_and_fees_with_appointment_types` in input object `updateAutomatedInsuranceBillingSettingInput`
* Input field `metadata` of type `String` was added to input object type `updateBillingItemInput`
* Input field `send_email_on_appt_request_for_anyone` of type `Boolean` was added to input object type `updateNotificationSettingInput`
* Input field `send_email_on_appt_request_for_you` of type `Boolean` was added to input object type `updateNotificationSettingInput`
* Input field `can_access_zus` of type `Boolean` was added to input object type `updateOrganizationMembershipInput`
* Input field `can_access_zus` of type `Boolean` was added to input object type `updatePermissionTemplateInput`

### 2025-03-14

* Type `AppointmentWorkflowChartNoteStatus` was added
* Type `AppointmentWorkflowStatus` was added
* Type `AppointmentWorkflowStatusAppointmentType` was added
* Type `AppointmentWorkflowStatusChartNoteType` was added
* Type `AppointmentWorkflowStatusClientType` was added
* Type `AppointmentWorkflowStatusCms1500Type` was added
* Type `AppointmentWorkflowStatusConnection` was added
* Type `AppointmentWorkflowStatusEdge` was added
* Type `AppointmentWorkflowStatusInvoiceType` was added
* Type `AppointmentWorkflowStatusProviderType` was added
* Type `ClaimMdMessage` was added
* Type `ClaimMdRejectionMessagesInfo` was added
* Type `PageInfo` was added
* Type `enableClaimMdAcctInput` was added
* Type `enableClaimMdAcctPayload` was added
* Type `updateStripeSubscriptionInput` was added
* Type `updateStripeSubscriptionPayload` was added
* Field `require_cc_at_booking` was added to object type `AppointmentType`
* Field `claim_md_rejection_messages` was added to object type `Cms1500`
* Field `claim_md_rejection_messages_info` was added to object type `Cms1500`
* Field `enableClaimMdAcct` was added to object type `Mutation`
* Field `updateStripeSubscription` was added to object type `Mutation`
* Field `appointmentWorkflowStatuses` was added to object type `Query`
* Argument `include_suborg_patients: Boolean` (with default value) added to field `Query.users`
* Argument `include_suborg_patients: Boolean` (with default value) added to field `Query.usersCount`
* Argument `show_all_by_default: Boolean` (with default value) added to field `Query.usersCount`
* Argument `include_suborg_patients: Boolean` (with default value) added to field `User.active_patients`
* Input field `require_cc_at_booking` of type `Boolean` was added to input object type `createAppointmentTypeInput`
* Input field `restricted` of type `Boolean` was added to input object type `createClientInput`
* Input field `require_cc_at_booking` of type `Boolean` was added to input object type `updateAppointmentTypeInput`
* Input field `restricted` of type `Boolean` was added to input object type `updateClientInput`

### 2025-02-28

* Type `ISO8601Date` was added
* Type `LabOrderLabVendor` was added
* Type `ingestMedicationsFromSurescriptsInput` was added
* Type `ingestMedicationsFromSurescriptsPayload` was added
* Field `theme_background_sidebar` was added to object type `Brand`
* Field `theme_text_sidebar` was added to object type `Brand`
* Field `theme_text_sidebar_active` was added to object type `Brand`
* Field `theme_text_sidebar_tab_bar` was added to object type `Brand`
* Field `lab_vendors` was added to object type `ELabsSettings`
* Field `ingestMedicationsFromSurescripts` was added to object type `Mutation`
* Argument `custom_sign_in_path: String` added to field `Query.assumedBrand`
* Argument `partner_name: String` added to field `Query.assumedBrand`
* Argument `current_only: Boolean` (with default value) added to field `Query.prescriptions`
* Argument `make_unique: Boolean` (with default value) added to field `Query.prescriptions`
* Input field `theme_background_sidebar` of type `HexColor` was added to input object type `updateBrandInput`
* Input field `theme_text_sidebar` of type `HexColor` was added to input object type `updateBrandInput`
* Input field `theme_text_sidebar_active` of type `HexColor` was added to input object type `updateBrandInput`
* Input field `theme_text_sidebar_tab_bar` of type `HexColor` was added to input object type `updateBrandInput`

### 2025-02-14

* Type `AssumedBrand` was added
* Type `ClientRestrictionAuthorization` was added
* Type `EnablePushToMainCalendarInput` was added
* Type `EnablePushToMainCalendarPayload` was added
* Type `HexColor` was added
* Type `createClientRestrictionAuthorizationInput` was added
* Type `createClientRestrictionAuthorizationPayload` was added
* Type `deleteClientRestrictionAuthorizationInput` was added
* Type `deleteClientRestrictionAuthorizationPayload` was added
* Field `auto_charge_enabled` was added to object type `AppointmentSetting`
* Field `theme_accent_primary` was added to object type `Brand`
* Field `theme_accent_primary_hover` was added to object type `Brand`
* Field `theme_background_hover` was added to object type `Brand`
* Field `theme_background_input` was added to object type `Brand`
* Field `theme_background_primary` was added to object type `Brand`
* Field `theme_background_secondary` was added to object type `Brand`
* Field `theme_border_input` was added to object type `Brand`
* Field `theme_border_primary` was added to object type `Brand`
* Field `metadata` was added to object type `FormAnswer`
* Field `is_locked` was added to object type `FormAnswerGroup`
* Input field `metadata` of type `String` was added to input object type `FormAnswerInput`
* Field `createClientRestrictionAuthorization` was added to object type `Mutation`
* Field `deleteClientRestrictionAuthorization` was added to object type `Mutation`
* Field `enablePushToMainCalendar` was added to object type `Mutation`
* Field `assumedBrand` was added to object type `Query`
* Field `canInvoiceSenderSeeRecipient` was added to object type `Query`
* Argument `attendee_ids: [ID]` added to field `Query.appointmentsCount`
* Argument `colorSchemeId: String` added to field `Query.appointmentsCount`
* Argument `filter_by_appointment_statuses: [String]` added to field `Query.appointmentsCount`
* Argument `filter_by_client_confirmed: Boolean` added to field `Query.appointmentsCount`
* Argument `filter_by_contact_types: String` added to field `Query.appointmentsCount`
* Argument `filter_by_provider_confirmed: Boolean` added to field `Query.appointmentsCount`
* Argument `order_by: AppointmentOrderKeys` added to field `Query.appointmentsCount`
* Argument `should_paginate: Boolean` (with default value) added to field `Query.appointmentsCount`
* Argument `sort_by: String` added to field `Query.appointmentsCount`
* Argument `state_license: String` added to field `Query.appointmentsCount`
* Argument `tag_ids: [ID]` added to field `Query.appointmentsCount`
* Argument `use_provider_inclusions: Boolean` (with default value) added to field `Query.appointmentsCount`
* Argument `search_string: String` added to field `Query.labOptions`
* Input field `icd_code_ids` of type `[ID]` was added to input object type `SubmissionInput`
* Input field `lab_option_ids` of type `[ID]` was added to input object type `SubmissionInput`
* Input field `SubmissionInput.tests` changed type from `[TestInput]!` to `[TestInput]`
* Directive `deprecated` was added to input field `tests` in input object `SubmissionInput`
* Field `client_restriction_authorizations` was added to object type `User`
* Field `provider_restriction_authorizations` was added to object type `User`
* Field `restricted` was added to object type `User`
* Field `User.in_org` is deprecated
* Field `User.in_org` has deprecation reason `As of Jan 2025, this is always true as users are always in an organization`
* Input field `theme_accent_primary` of type `HexColor` was added to input object type `updateBrandInput`
* Input field `theme_accent_primary_hover` of type `HexColor` was added to input object type `updateBrandInput`
* Input field `theme_background_hover` of type `HexColor` was added to input object type `updateBrandInput`
* Input field `theme_background_input` of type `HexColor` was added to input object type `updateBrandInput`
* Input field `theme_background_primary` of type `HexColor` was added to input object type `updateBrandInput`
* Input field `theme_background_secondary` of type `HexColor` was added to input object type `updateBrandInput`
* Input field `theme_border_input` of type `HexColor` was added to input object type `updateBrandInput`
* Input field `theme_border_primary` of type `HexColor` was added to input object type `updateBrandInput`
* Directive `feature` was added

### 2025-01-31

* Type `ELabsSettings` was added
* Type `cancelRecurringPaymentInput` was added
* Type `cancelRecurringPaymentPayload` was added
* Field `is_in_fee_schedules` was added to object type `InsurancePlan`
* Field `cancelRecurringPayment` was added to object type `Mutation`
* Field `e_labs_settings` was added to object type `Organization`

### 2025-01-17

* Type `OrgDataExport` was added
* Type `createFaxAcctInput` was added
* Type `createFaxAcctPayload` was added
* Type `deleteFormAnswerGroupSigningInput` was added
* Type `deleteFormAnswerGroupSigningPayload` was added
* Type `deleteWriteOffInput` was added
* Type `deleteWriteOffPayload` was added
* Type `destroyFaxAcctInput` was added
* Type `destroyFaxAcctPayload` was added
* Type `logMedicationHistoryConsentInput` was added
* Type `logMedicationHistoryConsentPayload` was added
* Type `orgDataExportInput` was added
* Type `orgDataExportPayload` was added
* Type `updateFaxAcctInput` was added
* Type `updateFaxAcctPayload` was added
* Enum value `REMOVE_SIGNATURE` was added to enum `Action`
* Field `potential_filtered_provider_ids` was added to object type `CalendarViewSetting`
* Field `display_name` was added to object type `Diagnosis`
* Field `is_abnormal` was added to object type `LabObservationResult`
* Field `created_at` was added to object type `LabResult`
* Field `createFaxAcct` was added to object type `Mutation`
* Field `deleteFaxAcct` was added to object type `Mutation`
* Field `deleteFormAnswerGroupSigning` was added to object type `Mutation`
* Field `deleteWriteOff` was added to object type `Mutation`
* Field `logMedicationHistoryConsent` was added to object type `Mutation`
* Field `orgDataExport` was added to object type `Mutation`
* Field `updateFaxAcct` was added to object type `Mutation`
* Argument `active_status: String` added to field `Organization.providers`
* Field `can_remove_org_member_signatures` was added to object type `OrganizationMembership`
* Field `can_remove_org_member_signatures` was added to object type `PermissionTemplateType`
* Field `surescriptsReportedMedicationHistory` was added to object type `Query`
* Argument `unreconciled_from_ccda_ingest: Boolean` (with default value) added to field `User.diagnoses`
* Input field `can_remove_org_member_signatures` of type `Boolean` was added to input object type `createPermissionTemplateInput`
* Input field `can_remove_org_member_signatures` of type `Boolean` was added to input object type `updateOrganizationMembershipInput`
* Input field `can_remove_org_member_signatures` of type `Boolean` was added to input object type `updatePermissionTemplateInput`
