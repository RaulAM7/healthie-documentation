---
title: WebhookEventType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/webhookeventtype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/webhookeventtype/index.md
---

Types of webhook events that can be triggered

## Used By

[`SentWebhook.event_type`](/reference/2026-01-01/objects/sentwebhook)

[`Webhook.event_type`](/reference/2026-01-01/objects/webhook)

[`WebhookEvent.event_type`](/reference/2026-01-01/objects/webhookevent)

[`WebhookEventInput.event_type`](/reference/2026-01-01/input-objects/webhookeventinput)

[`createWebhookInput.event_type`](/reference/2026-01-01/input-objects/createwebhookinput)

[`updateWebhookInput.event_type`](/reference/2026-01-01/input-objects/updatewebhookinput)

## Definition

```
"""
Types of webhook events that can be triggered
"""
enum WebhookEventType {
  """
  accepted_insurance_plan.created
  """
  ACCEPTED_INSURANCE_PLAN_CREATED


  """
  accepted_insurance_plan.deleted
  """
  ACCEPTED_INSURANCE_PLAN_DELETED


  """
  allergy_sensitivity.created
  """
  ALLERGY_SENSITIVITY_CREATED


  """
  allergy_sensitivity.deleted
  """
  ALLERGY_SENSITIVITY_DELETED


  """
  allergy_sensitivity.updated
  """
  ALLERGY_SENSITIVITY_UPDATED


  """
  applied_tag.created
  """
  APPLIED_TAG_CREATED


  """
  applied_tag.deleted
  """
  APPLIED_TAG_DELETED


  """
  appointment.created
  """
  APPOINTMENT_CREATED


  """
  appointment.deleted
  """
  APPOINTMENT_DELETED


  """
  appointment.participant_joined
  """
  APPOINTMENT_PARTICIPANT_JOINED


  """
  appointment.participant_left
  """
  APPOINTMENT_PARTICIPANT_LEFT


  """
  appointment.patient_added
  """
  APPOINTMENT_PATIENT_ADDED


  """
  appointment.patient_removed
  """
  APPOINTMENT_PATIENT_REMOVED


  """
  appointment.recording_completed
  """
  APPOINTMENT_RECORDING_COMPLETED


  """
  appointment.recording_started
  """
  APPOINTMENT_RECORDING_STARTED


  """
  appointment.recording_stopped
  """
  APPOINTMENT_RECORDING_STOPPED


  """
  appointment.transcript_available
  """
  APPOINTMENT_TRANSCRIPT_AVAILABLE


  """
  appointment.transcript_failed
  """
  APPOINTMENT_TRANSCRIPT_FAILED


  """
  appointment.transcript_started
  """
  APPOINTMENT_TRANSCRIPT_STARTED


  """
  appointment.updated
  """
  APPOINTMENT_UPDATED


  """
  appointment_form_answer_group_connection.created
  """
  APPOINTMENT_FORM_ANSWER_GROUP_CONNECTION_CREATED


  """
  appointment_form_answer_group_connection.deleted
  """
  APPOINTMENT_FORM_ANSWER_GROUP_CONNECTION_DELETED


  """
  appointment_form_answer_group_connection.updated
  """
  APPOINTMENT_FORM_ANSWER_GROUP_CONNECTION_UPDATED


  """
  availability.created
  """
  AVAILABILITY_CREATED


  """
  availability.deleted
  """
  AVAILABILITY_DELETED


  """
  availability.updated
  """
  AVAILABILITY_UPDATED


  """
  billing_item.created
  """
  BILLING_ITEM_CREATED


  """
  billing_item.deleted
  """
  BILLING_ITEM_DELETED


  """
  billing_item.updated
  """
  BILLING_ITEM_UPDATED


  """
  care_plan.activated
  """
  CARE_PLAN_ACTIVATED


  """
  care_plan.created
  """
  CARE_PLAN_CREATED


  """
  care_plan.deactivated
  """
  CARE_PLAN_DEACTIVATED


  """
  care_plan.deleted
  """
  CARE_PLAN_DELETED


  """
  care_plan.updated
  """
  CARE_PLAN_UPDATED


  """
  charge_back.created
  """
  CHARGE_BACK_CREATED


  """
  charge_back.deleted
  """
  CHARGE_BACK_DELETED


  """
  charge_back.updated
  """
  CHARGE_BACK_UPDATED


  """
  charting_note_addendum.created
  """
  CHARTING_NOTE_ADDENDUM_CREATED


  """
  charting_note_addendum.deleted
  """
  CHARTING_NOTE_ADDENDUM_DELETED


  """
  charting_note_addendum.updated
  """
  CHARTING_NOTE_ADDENDUM_UPDATED


  """
  claim_submission.created
  """
  CLAIM_SUBMISSION_CREATED


  """
  claim_submission.deleted
  """
  CLAIM_SUBMISSION_DELETED


  """
  claim_submission.updated
  """
  CLAIM_SUBMISSION_UPDATED


  """
  cms1500.created
  """
  CMS1500_CREATED


  """
  cms1500.deleted
  """
  CMS1500_DELETED


  """
  cms1500.updated
  """
  CMS1500_UPDATED


  """
  comment.created
  """
  COMMENT_CREATED


  """
  comment.deleted
  """
  COMMENT_DELETED


  """
  comment.updated
  """
  COMMENT_UPDATED


  """
  completed_onboarding_item.created
  """
  COMPLETED_ONBOARDING_ITEM_CREATED


  """
  completed_onboarding_item.deleted
  """
  COMPLETED_ONBOARDING_ITEM_DELETED


  """
  completed_onboarding_item.updated
  """
  COMPLETED_ONBOARDING_ITEM_UPDATED


  """
  conversation.created
  """
  CONVERSATION_CREATED


  """
  conversation.updated
  """
  CONVERSATION_UPDATED


  """
  conversation_membership.created
  """
  CONVERSATION_MEMBERSHIP_CREATED


  """
  conversation_membership.deleted
  """
  CONVERSATION_MEMBERSHIP_DELETED


  """
  conversation_membership.viewed
  """
  CONVERSATION_MEMBERSHIP_VIEWED


  """
  course_membership.created
  """
  COURSE_MEMBERSHIP_CREATED


  """
  course_membership.deleted
  """
  COURSE_MEMBERSHIP_DELETED


  """
  course_membership.updated
  """
  COURSE_MEMBERSHIP_UPDATED


  """
  custom_module.created
  """
  CUSTOM_MODULE_CREATED


  """
  custom_module.deleted
  """
  CUSTOM_MODULE_DELETED


  """
  custom_module.updated
  """
  CUSTOM_MODULE_UPDATED


  """
  custom_module_form.created
  """
  CUSTOM_MODULE_FORM_CREATED


  """
  custom_module_form.deleted
  """
  CUSTOM_MODULE_FORM_DELETED


  """
  custom_module_form.updated
  """
  CUSTOM_MODULE_FORM_UPDATED


  """
  diagnosis.created
  """
  DIAGNOSIS_CREATED


  """
  diagnosis.deleted
  """
  DIAGNOSIS_DELETED


  """
  diagnosis.updated
  """
  DIAGNOSIS_UPDATED


  """
  document.created
  """
  DOCUMENT_CREATED


  """
  document.deleted
  """
  DOCUMENT_DELETED


  """
  document.updated
  """
  DOCUMENT_UPDATED


  """
  dosespot_notification.created
  """
  DOSESPOT_NOTIFICATION_CREATED


  """
  entry.created
  """
  ENTRY_CREATED


  """
  entry.deleted
  """
  ENTRY_DELETED


  """
  entry.updated
  """
  ENTRY_UPDATED


  """
  external_calendar.authorization_error
  """
  EXTERNAL_CALENDAR_AUTHORIZATION_ERROR


  """
  family_history_condition.created
  """
  FAMILY_HISTORY_CONDITION_CREATED


  """
  family_history_condition.deleted
  """
  FAMILY_HISTORY_CONDITION_DELETED


  """
  family_history_condition.updated
  """
  FAMILY_HISTORY_CONDITION_UPDATED


  """
  feature_toggle.created
  """
  FEATURE_TOGGLE_CREATED


  """
  feature_toggle.deleted
  """
  FEATURE_TOGGLE_DELETED


  """
  feature_toggle.updated
  """
  FEATURE_TOGGLE_UPDATED


  """
  folder_sharing.created
  """
  FOLDER_SHARING_CREATED


  """
  folder_sharing.deleted
  """
  FOLDER_SHARING_DELETED


  """
  form_answer_group.created
  """
  FORM_ANSWER_GROUP_CREATED


  """
  form_answer_group.deleted
  """
  FORM_ANSWER_GROUP_DELETED


  """
  form_answer_group.locked
  """
  FORM_ANSWER_GROUP_LOCKED


  """
  form_answer_group.signed
  """
  FORM_ANSWER_GROUP_SIGNED


  """
  form_answer_group.unlocked
  """
  FORM_ANSWER_GROUP_UNLOCKED


  """
  generated_form_answer_group.converted
  """
  GENERATED_FORM_ANSWER_GROUP_CONVERTED


  """
  generated_form_answer_group.created
  """
  GENERATED_FORM_ANSWER_GROUP_CREATED


  """
  generated_form_answer_group.deleted
  """
  GENERATED_FORM_ANSWER_GROUP_DELETED


  """
  generated_form_answer_group.rejected
  """
  GENERATED_FORM_ANSWER_GROUP_REJECTED


  """
  generated_form_answer_group.updated
  """
  GENERATED_FORM_ANSWER_GROUP_UPDATED


  """
  goal.created
  """
  GOAL_CREATED


  """
  goal.deleted
  """
  GOAL_DELETED


  """
  goal.updated
  """
  GOAL_UPDATED


  """
  goal_history.created
  """
  GOAL_HISTORY_CREATED


  """
  goal_history.deleted
  """
  GOAL_HISTORY_DELETED


  """
  goal_template.created
  """
  GOAL_TEMPLATE_CREATED


  """
  goal_template.deleted
  """
  GOAL_TEMPLATE_DELETED


  """
  goal_template.updated
  """
  GOAL_TEMPLATE_UPDATED


  """
  insurance_authorization.created
  """
  INSURANCE_AUTHORIZATION_CREATED


  """
  insurance_authorization.deleted
  """
  INSURANCE_AUTHORIZATION_DELETED


  """
  insurance_authorization.updated
  """
  INSURANCE_AUTHORIZATION_UPDATED


  """
  lab_order.created
  """
  LAB_ORDER_CREATED


  """
  lab_order.updated
  """
  LAB_ORDER_UPDATED


  """
  lab_result.created
  """
  LAB_RESULT_CREATED


  """
  lab_result.updated
  """
  LAB_RESULT_UPDATED


  """
  location.created
  """
  LOCATION_CREATED


  """
  location.deleted
  """
  LOCATION_DELETED


  """
  location.updated
  """
  LOCATION_UPDATED


  """
  medication.created
  """
  MEDICATION_CREATED


  """
  medication.deleted
  """
  MEDICATION_DELETED


  """
  medication.updated
  """
  MEDICATION_UPDATED


  """
  message.created
  """
  MESSAGE_CREATED


  """
  message.deleted
  """
  MESSAGE_DELETED


  """
  metric_entry.created
  """
  METRIC_ENTRY_CREATED


  """
  metric_entry.deleted
  """
  METRIC_ENTRY_DELETED


  """
  metric_entry.updated
  """
  METRIC_ENTRY_UPDATED


  """
  notification_contact.created
  """
  NOTIFICATION_CONTACT_CREATED


  """
  notification_contact.deleted
  """
  NOTIFICATION_CONTACT_DELETED


  """
  notification_contact.updated
  """
  NOTIFICATION_CONTACT_UPDATED


  """
  notification_setting.created
  """
  NOTIFICATION_SETTING_CREATED


  """
  notification_setting.deleted
  """
  NOTIFICATION_SETTING_DELETED


  """
  notification_setting.updated
  """
  NOTIFICATION_SETTING_UPDATED


  """
  organization_info.created
  """
  ORGANIZATION_INFO_CREATED


  """
  organization_info.deleted
  """
  ORGANIZATION_INFO_DELETED


  """
  organization_info.updated
  """
  ORGANIZATION_INFO_UPDATED


  """
  organization_member.updated
  """
  ORGANIZATION_MEMBER_UPDATED


  """
  organization_membership.created
  """
  ORGANIZATION_MEMBERSHIP_CREATED


  """
  organization_membership.updated
  """
  ORGANIZATION_MEMBERSHIP_UPDATED


  """
  other_id_number.created
  """
  OTHER_ID_NUMBER_CREATED


  """
  other_id_number.deleted
  """
  OTHER_ID_NUMBER_DELETED


  """
  other_id_number.updated
  """
  OTHER_ID_NUMBER_UPDATED


  """
  patient.created
  """
  PATIENT_CREATED


  """
  patient.merged
  """
  PATIENT_MERGED


  """
  patient.updated
  """
  PATIENT_UPDATED


  """
  patient_educational_resource.created
  """
  PATIENT_EDUCATIONAL_RESOURCE_CREATED


  """
  patient_educational_resource.deleted
  """
  PATIENT_EDUCATIONAL_RESOURCE_DELETED


  """
  patient_educational_resource.updated
  """
  PATIENT_EDUCATIONAL_RESOURCE_UPDATED


  """
  policy.created
  """
  POLICY_CREATED


  """
  policy.deleted
  """
  POLICY_DELETED


  """
  policy.updated
  """
  POLICY_UPDATED


  """
  prescription.medication_status_updated
  """
  PRESCRIPTION_MEDICATION_STATUS_UPDATED


  """
  prescription.updated
  """
  PRESCRIPTION_UPDATED


  """
  received_direct_message.created
  """
  RECEIVED_DIRECT_MESSAGE_CREATED


  """
  received_fax.created
  """
  RECEIVED_FAX_CREATED


  """
  recurring_payment.created
  """
  RECURRING_PAYMENT_CREATED


  """
  recurring_payment.updated
  """
  RECURRING_PAYMENT_UPDATED


  """
  referral.created
  """
  REFERRAL_CREATED


  """
  referral.deleted
  """
  REFERRAL_DELETED


  """
  referral.updated
  """
  REFERRAL_UPDATED


  """
  referring_physician.created
  """
  REFERRING_PHYSICIAN_CREATED


  """
  referring_physician.deleted
  """
  REFERRING_PHYSICIAN_DELETED


  """
  referring_physician.updated
  """
  REFERRING_PHYSICIAN_UPDATED


  """
  requested_form_completion.created
  """
  REQUESTED_FORM_COMPLETION_CREATED


  """
  requested_form_completion.deleted
  """
  REQUESTED_FORM_COMPLETION_DELETED


  """
  requested_form_completion.updated
  """
  REQUESTED_FORM_COMPLETION_UPDATED


  """
  requested_payment.created
  """
  REQUESTED_PAYMENT_CREATED


  """
  requested_payment.deleted
  """
  REQUESTED_PAYMENT_DELETED


  """
  requested_payment.updated
  """
  REQUESTED_PAYMENT_UPDATED


  """
  scheduled_message.sent
  """
  SCHEDULED_MESSAGE_SENT


  """
  sent_fax.created
  """
  SENT_FAX_CREATED


  """
  sent_fax.status_changed
  """
  SENT_FAX_STATUS_CHANGED


  """
  sent_fax.updated
  """
  SENT_FAX_UPDATED


  """
  sent_notification_record.created
  """
  SENT_NOTIFICATION_RECORD_CREATED


  """
  sent_notification_record.updated
  """
  SENT_NOTIFICATION_RECORD_UPDATED


  """
  stripe_customer_detail.created
  """
  STRIPE_CUSTOMER_DETAIL_CREATED


  """
  stripe_customer_detail.deleted
  """
  STRIPE_CUSTOMER_DETAIL_DELETED


  """
  stripe_customer_detail.updated
  """
  STRIPE_CUSTOMER_DETAIL_UPDATED


  """
  super_bill.created
  """
  SUPER_BILL_CREATED


  """
  super_bill.deleted
  """
  SUPER_BILL_DELETED


  """
  super_bill.updated
  """
  SUPER_BILL_UPDATED


  """
  task.created
  """
  TASK_CREATED


  """
  task.deleted
  """
  TASK_DELETED


  """
  task.updated
  """
  TASK_UPDATED


  """
  test.created
  """
  TEST_CREATED
}
```
