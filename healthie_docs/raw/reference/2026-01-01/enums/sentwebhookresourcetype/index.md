---
title: SentWebhookResourceType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/sentwebhookresourcetype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/sentwebhookresourcetype/index.md
---

Types of resources that can trigger webhooks

## Used By

[`Query.sentWebhooks`](/reference/2026-01-01/queries/sentwebhooks)

## Definition

```
"""
Types of resources that can trigger webhooks
"""
enum SentWebhookResourceType {
  """
  AcceptedInsurancePlan
  """
  ACCEPTED_INSURANCE_PLAN


  """
  AllergySensitivity
  """
  ALLERGY_SENSITIVITY


  """
  AppliedTag
  """
  APPLIED_TAG


  """
  Appointment
  """
  APPOINTMENT


  """
  AppointmentFormAnswerGroupConnection
  """
  APPOINTMENT_FORM_ANSWER_GROUP_CONNECTION


  """
  Availability
  """
  AVAILABILITY


  """
  BillingItem
  """
  BILLING_ITEM


  """
  CarePlan
  """
  CARE_PLAN


  """
  ChargeBack
  """
  CHARGE_BACK


  """
  ChartingNoteAddendum
  """
  CHARTING_NOTE_ADDENDUM


  """
  ClaimSubmission
  """
  CLAIM_SUBMISSION


  """
  Cms1500
  """
  CMS1500


  """
  Comment
  """
  COMMENT


  """
  CompletedOnboardingItem
  """
  COMPLETED_ONBOARDING_ITEM


  """
  Conversation
  """
  CONVERSATION


  """
  ConversationMembership
  """
  CONVERSATION_MEMBERSHIP


  """
  CourseMembership
  """
  COURSE_MEMBERSHIP


  """
  CustomModule
  """
  CUSTOM_MODULE


  """
  CustomModuleForm
  """
  CUSTOM_MODULE_FORM


  """
  Diagnosis
  """
  DIAGNOSIS


  """
  Document
  """
  DOCUMENT


  """
  Entry
  """
  ENTRY


  """
  ExternalCalendar
  """
  EXTERNAL_CALENDAR


  """
  FamilyHistoryCondition
  """
  FAMILY_HISTORY_CONDITION


  """
  FeatureToggle
  """
  FEATURE_TOGGLE


  """
  FolderSharing
  """
  FOLDER_SHARING


  """
  FormAnswerGroup
  """
  FORM_ANSWER_GROUP


  """
  GeneratedFormAnswerGroup
  """
  GENERATED_FORM_ANSWER_GROUP


  """
  Goal
  """
  GOAL


  """
  GoalHistory
  """
  GOAL_HISTORY


  """
  GoalTemplate
  """
  GOAL_TEMPLATE


  """
  GroupCarePlanUserConnection
  """
  GROUP_CARE_PLAN_USER_CONNECTION


  """
  InsuranceAuthorization
  """
  INSURANCE_AUTHORIZATION


  """
  LabOrder
  """
  LAB_ORDER


  """
  LabResult
  """
  LAB_RESULT


  """
  Location
  """
  LOCATION


  """
  Medication
  """
  MEDICATION


  """
  Note
  """
  NOTE


  """
  NoteScheduler
  """
  NOTE_SCHEDULER


  """
  NotificationContact
  """
  NOTIFICATION_CONTACT


  """
  NotificationSetting
  """
  NOTIFICATION_SETTING


  """
  OrganizationInfo
  """
  ORGANIZATION_INFO


  """
  OrganizationMember
  """
  ORGANIZATION_MEMBER


  """
  OrganizationMembership
  """
  ORGANIZATION_MEMBERSHIP


  """
  OtherIdNumber
  """
  OTHER_ID_NUMBER


  """
  PatientEducationalResource
  """
  PATIENT_EDUCATIONAL_RESOURCE


  """
  Policy
  """
  POLICY


  """
  Prescription
  """
  PRESCRIPTION


  """
  ReceivedDirectMessage
  """
  RECEIVED_DIRECT_MESSAGE


  """
  ReceivedFax
  """
  RECEIVED_FAX


  """
  RecurringPayment
  """
  RECURRING_PAYMENT


  """
  Referral
  """
  REFERRAL


  """
  ReferringPhysician
  """
  REFERRING_PHYSICIAN


  """
  RequestedFormCompletion
  """
  REQUESTED_FORM_COMPLETION


  """
  RequestedPayment
  """
  REQUESTED_PAYMENT


  """
  SentFax
  """
  SENT_FAX


  """
  SentNotificationRecord
  """
  SENT_NOTIFICATION_RECORD


  """
  StripeCustomerDetail
  """
  STRIPE_CUSTOMER_DETAIL


  """
  SuperBill
  """
  SUPER_BILL


  """
  Task
  """
  TASK


  """
  User
  """
  USER
}
```
