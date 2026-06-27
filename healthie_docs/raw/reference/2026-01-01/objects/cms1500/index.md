---
title: Cms1500 | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/cms1500/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/cms1500/index.md
---

A CMS1500 claim

## Fields

[`accept_assignment` ](#field-accept-assignment)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The provider agrees to accept assignment

[`additional_text` ](#field-additional-text)· [`String` ](/reference/2026-01-01/scalars/string)· Notes

[`adjustment` ](#field-adjustment)· [`String` ](/reference/2026-01-01/scalars/string)· The insurance discount

[`amount_paid` ](#field-amount-paid)· [`String` ](/reference/2026-01-01/scalars/string)· The amount that the client paid towards the claim

[`amount_reimbursed` ](#field-amount-reimbursed)· [`String` ](/reference/2026-01-01/scalars/string)· The amount that the insurance company reimbursed

[`billing_provider` ](#field-billing-provider)· [`Organization` ](/reference/2026-01-01/objects/organization)· The billing provider for the CMS1500

[`billing_provider_id` ](#field-billing-provider-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the Billing Provider

[`check_numbers` ](#field-check-numbers)· [`[String]` ](/reference/2026-01-01/scalars/string)· Check numbers associated with a reimbursement from the claim. Imported via ERA

[`claim_md_rejection_messages` ](#field-claim-md-rejection-messages)· [`[ClaimMdMessage!]!` ](/reference/2026-01-01/objects/claimmdmessage)· required · Most recent Claim MD rejection messages for this CMS1500

[`claim_md_rejection_messages_info` ](#field-claim-md-rejection-messages-info)· [`ClaimMdRejectionMessagesInfo` ](/reference/2026-01-01/enums/claimmdrejectionmessagesinfo)· Info explaining why claim\_md\_rejection\_messages field is empty

[`claim_submissions` ](#field-claim-submissions)· [`[ClaimSubmission!]` ](/reference/2026-01-01/objects/claimsubmission)· (Must be admin to view) A record of submission of events for this claim to different clearinghouse/RCM integrations.

[`client_responsibility` ](#field-client-responsibility)· [`String` ](/reference/2026-01-01/scalars/string)· Amount the client owes

[`client_responsibility_removed` ](#field-client-responsibility-removed)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· True if the provider chose to remove client responsibility

[`client_sig_on_file` ](#field-client-sig-on-file)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· True if the client's signature is on file

[`cms1500_policies` ](#field-cms1500-policies)· [`[Cms1500Policy!]` ](/reference/2026-01-01/objects/cms1500policy)· Cms1500 policies in use for this claim

[`copay` ](#field-copay)· [`String` ](/reference/2026-01-01/scalars/string)· The client's copay for the claim

[`copay_still_owed` ](#field-copay-still-owed)· [`String` ](/reference/2026-01-01/scalars/string)· The amount of copay still owed

[`cpt_code_names` ](#field-cpt-code-names)· [`String` ](/reference/2026-01-01/scalars/string)· The comma separated list of cpt codes names

[`cpt_codes_cms1500s` ](#field-cpt-codes-cms1500s)· [`[CptCodesCms1500!]` ](/reference/2026-01-01/objects/cptcodescms1500)· CPT codes in use for this claim

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The creation date of the claim

[`date_of_service` ](#field-date-of-service)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The claim's date of service

[`dietitian_id` ](#field-dietitian-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the rendering provider

[`eras` ](#field-eras)· [`EraConnection!` ](/reference/2026-01-01/objects/eraconnection)· required

[`estimated_cpt_fees_for_user` ](#field-estimated-cpt-fees-for-user)· [`[CptCodesCms1500!]` ](/reference/2026-01-01/objects/cptcodescms1500)· Estimated fee for the specific cpt code based on previous use

deprecated

Use CptCodesCms1500.last\_fee\_amount

[`form_answer_group_id` ](#field-form-answer-group-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Chart Note ID, if CMS1500 was exported from a Chart Note

[`has_been_submitted` ](#field-has-been-submitted)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Are there any submissions for this claim

[`icd_codes_cms1500s` ](#field-icd-codes-cms1500s)· [`[IcdCodesCms1500!]` ](/reference/2026-01-01/objects/icdcodescms1500)· ICD codes in use for this claim

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The unique identifier of the CMS1500

[`include_referrer_information` ](#field-include-referrer-information)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, includes referrer information on the claim

[`insured_sig_on_file` ](#field-insured-sig-on-file)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· True if the insured's signature is on file

[`nineteen_reserved` ](#field-nineteen-reserved)· [`String` ](/reference/2026-01-01/scalars/string)· The value of the nineteen field

[`org_info` ](#field-org-info)· [`OrganizationInfo` ](/reference/2026-01-01/objects/organizationinfo)· The specific Organization Info in use on this claim

[`organization_info_id` ](#field-organization-info-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the Organization Info

[`orig_ref_number` ](#field-orig-ref-number)· [`String` ](/reference/2026-01-01/scalars/string)· The original reference number of the claim

[`paid_out_at` ](#field-paid-out-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The date that the claim was paid out to employees/contractors

[`patient` ](#field-patient)· [`User` ](/reference/2026-01-01/objects/user)· The patient for the CMS1500

[`patient_account_num` ](#field-patient-account-num)· [`String` ](/reference/2026-01-01/scalars/string)· The patient's account number

[`patient_id` ](#field-patient-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the patient

[`primary_plan_name` ](#field-primary-plan-name)· [`String` ](/reference/2026-01-01/scalars/string)· The primary insurance plan name for the CMS1500

[`reasons` ](#field-reasons)· [`ID` ](/reference/2026-01-01/scalars/id)· Rejected/Denied status reason

[`referral_info` ](#field-referral-info)· [`ReferralInfo` ](/reference/2026-01-01/objects/referralinfo)· The referral info for the CMS1500

[`reimbursed_at` ](#field-reimbursed-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The date that the claim was reimbursed

[`rendering_provider` ](#field-rendering-provider)· [`User` ](/reference/2026-01-01/objects/user)· The provider for the CMS1500

[`rendering_provider_other_id` ](#field-rendering-provider-other-id)· [`String` ](/reference/2026-01-01/scalars/string)· The Rendering Provider's other id number

[`rendering_provider_other_id_object` ](#field-rendering-provider-other-id-object)· [`OtherIdNumber` ](/reference/2026-01-01/objects/otheridnumber)· Other ID info in use for this render provider

[`resubmission_code` ](#field-resubmission-code)· [`String` ](/reference/2026-01-01/scalars/string)· The resubmission code of the claim

[`service_location` ](#field-service-location)· [`Location` ](/reference/2026-01-01/objects/location)· The service location for the CMS1500

[`service_location_id` ](#field-service-location-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the service location

[`status` ](#field-status)· [`Cms1500Status` ](/reference/2026-01-01/enums/cms1500status)· The status of the claim

[`tend_reserved` ](#field-tend-reserved)· [`String` ](/reference/2026-01-01/scalars/string)· The value of the ten d field

[`total_charge` ](#field-total-charge)· [`String` ](/reference/2026-01-01/scalars/string)· Total amount the claim was billed for

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The last date and time that the CMS1500 was updated

[`updated_by_sftp` ](#field-updated-by-sftp)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· True if the claim reimbursement info was updated via SFTP

[`use_indiv_npi` ](#field-use-indiv-npi)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, uses the individual npi in all npi fields

## Used By

[`Cms1500Edge.node`](/reference/2026-01-01/objects/cms1500edge)

[`Cms1500PaginationConnection.nodes`](/reference/2026-01-01/objects/cms1500paginationconnection)

[`Cms1500Policy.cms1500`](/reference/2026-01-01/objects/cms1500policy)

[`FormAnswerGroup.cms1500`](/reference/2026-01-01/objects/formanswergroup)

[`PatientEncounter.cms1500`](/reference/2026-01-01/objects/patientencounter)

[`ReferralInfo.cms1500`](/reference/2026-01-01/objects/referralinfo)

[`createCms1500Payload.cms1500`](/reference/2026-01-01/objects/createcms1500payload)

[`deleteCms1500Payload.cms1500`](/reference/2026-01-01/objects/deletecms1500payload)

[`updateCms1500Payload.cms1500`](/reference/2026-01-01/objects/updatecms1500payload)

[`uploadBatchToCandidHealthPayload.cms1500s`](/reference/2026-01-01/objects/uploadbatchtocandidhealthpayload)

[`uploadBatchToChangeHealthPayload.cms1500s`](/reference/2026-01-01/objects/uploadbatchtochangehealthpayload)

[`uploadBatchToOfficeallyPayload.cms1500s`](/reference/2026-01-01/objects/uploadbatchtoofficeallypayload)

[`uploadToIntegrationsPayload.cms1500s`](/reference/2026-01-01/objects/uploadtointegrationspayload)

[`Query.baseCms1500ForUser`](/reference/2026-01-01/queries/basecms1500foruser)

[`Query.cms1500`](/reference/2026-01-01/queries/cms1500)

[`Query.initialCms1500`](/reference/2026-01-01/queries/initialcms1500)

## Definition

```
"""
A CMS1500 claim
"""
type Cms1500 {
  """
  The provider agrees to accept assignment
  """
  accept_assignment: Boolean


  """
  Notes
  """
  additional_text: String


  """
  The insurance discount
  """
  adjustment: String


  """
  The amount that the client paid towards the claim
  """
  amount_paid: String


  """
  The amount that the insurance company reimbursed
  """
  amount_reimbursed: String


  """
  The billing provider for the CMS1500
  """
  billing_provider: Organization


  """
  The ID of the Billing Provider
  """
  billing_provider_id: String


  """
  Check numbers associated with a reimbursement from the claim. Imported via ERA
  """
  check_numbers: [String]


  """
  Most recent Claim MD rejection messages for this CMS1500
  """
  claim_md_rejection_messages: [ClaimMdMessage!]!


  """
  Info explaining why claim_md_rejection_messages field is empty
  """
  claim_md_rejection_messages_info: ClaimMdRejectionMessagesInfo


  """
  (Must be admin to view) A record of submission of events for this claim to different clearinghouse/RCM integrations.
  """
  claim_submissions: [ClaimSubmission!]


  """
  Amount the client owes
  """
  client_responsibility: String


  """
  True if the provider chose to remove client responsibility
  """
  client_responsibility_removed: Boolean


  """
  True if the client's signature is on file
  """
  client_sig_on_file: Boolean


  """
  Cms1500 policies in use for this claim
  """
  cms1500_policies(
    """
    True if requesting only Cms1500Policy objects with assigned policies
    """
    only_with_assigned_policies: Boolean = false
  ): [Cms1500Policy!]


  """
  The client's copay for the claim
  """
  copay: String


  """
  The amount of copay still owed
  """
  copay_still_owed: String


  """
  The comma separated list of cpt codes names
  """
  cpt_code_names: String


  """
  CPT codes in use for this claim
  """
  cpt_codes_cms1500s: [CptCodesCms1500!]


  """
  The creation date of the claim
  """
  created_at: ISO8601DateTime!


  """
  The claim's date of service
  """
  date_of_service: ISO8601DateTime


  """
  The ID of the rendering provider
  """
  dietitian_id: String
  eras(
    """
    Returns the elements in the list that come after the specified cursor.
    """
    after: String


    """
    Returns the elements in the list that come before the specified cursor.
    """
    before: String


    """
    Returns the first _n_ elements from the list.
    """
    first: Int


    """
    Returns the last _n_ elements from the list.
    """
    last: Int
  ): EraConnection!


  """
  Estimated fee for the specific cpt code based on previous use
  """
  estimated_cpt_fees_for_user: [CptCodesCms1500!]
    @deprecated(reason: "Use CptCodesCms1500.last_fee_amount")


  """
  Chart Note ID, if CMS1500 was exported from a Chart Note
  """
  form_answer_group_id: ID


  """
  Are there any submissions for this claim
  """
  has_been_submitted: Boolean


  """
  ICD codes in use for this claim
  """
  icd_codes_cms1500s: [IcdCodesCms1500!]


  """
  The unique identifier of the CMS1500
  """
  id: ID


  """
  When true, includes referrer information on the claim
  """
  include_referrer_information: Boolean


  """
  True if the insured's signature is on file
  """
  insured_sig_on_file: Boolean


  """
  The value of the nineteen field
  """
  nineteen_reserved: String


  """
  The specific Organization Info in use on this claim
  """
  org_info: OrganizationInfo


  """
  The ID of the Organization Info
  """
  organization_info_id: String


  """
  The original reference number of the claim
  """
  orig_ref_number: String


  """
  The date that the claim was paid out to employees/contractors
  """
  paid_out_at: ISO8601DateTime


  """
  The patient for the CMS1500
  """
  patient: User


  """
  The patient's account number
  """
  patient_account_num: String


  """
  The ID of the patient
  """
  patient_id: String


  """
  The primary insurance plan name for the CMS1500
  """
  primary_plan_name: String


  """
  Rejected/Denied status reason
  """
  reasons: ID


  """
  The referral info for the CMS1500
  """
  referral_info: ReferralInfo


  """
  The date that the claim was reimbursed
  """
  reimbursed_at: ISO8601DateTime


  """
  The provider for the CMS1500
  """
  rendering_provider: User


  """
  The Rendering Provider's other id number
  """
  rendering_provider_other_id: String


  """
  Other ID info in use for this render provider
  """
  rendering_provider_other_id_object: OtherIdNumber


  """
  The resubmission code of the claim
  """
  resubmission_code: String


  """
  The service location for the CMS1500
  """
  service_location: Location


  """
  The ID of the service location
  """
  service_location_id: String


  """
  The status of the claim
  """
  status: Cms1500Status


  """
  The value of the ten d field
  """
  tend_reserved: String


  """
  Total amount the claim was billed for
  """
  total_charge: String


  """
  The last date and time that the CMS1500 was updated
  """
  updated_at: ISO8601DateTime


  """
  True if the claim reimbursement info was updated via SFTP
  """
  updated_by_sftp: Boolean


  """
  When true, uses the individual npi in all npi fields
  """
  use_indiv_npi: Boolean
}
```
