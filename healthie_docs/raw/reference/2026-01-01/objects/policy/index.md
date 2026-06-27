---
title: Policy | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/policy/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/policy/index.md
---

A policy

## Fields

[`benefits` ](#field-benefits)· [`[Benefit!]` ](/reference/2026-01-01/objects/benefit)· Benefits associated with policy

[`call_reference` ](#field-call-reference)· [`CallReference` ](/reference/2026-01-01/objects/callreference)· Call reference information associated with this policy

[`claim_eligibility_check_errors` ](#field-claim-eligibility-check-errors)· [`[ClaimEligibilityCheckErrors!]` ](/reference/2026-01-01/objects/claimeligibilitycheckerrors)· Returns a list of errors associated with the policy after doing a Change Health Insurance Eligibility Check

[`coinsurance_value` ](#field-coinsurance-value)· [`Int` ](/reference/2026-01-01/scalars/int)· Value if insurance billing method is coinsurance

[`copay_value` ](#field-copay-value)· [`Int` ](/reference/2026-01-01/scalars/int)· Value (in cents) if insurance billing method is copay

[`cpt_codes_policies` ](#field-cpt-codes-policies)· [`[CptCodesPolicy!]` ](/reference/2026-01-01/objects/cptcodespolicy)· CPT codes authorized for this policy

[`created_at` ](#field-created-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· Date policy was added

[`dob_to_use` ](#field-dob-to-use)· [`ISO8601Date` ](/reference/2026-01-01/scalars/iso8601date)· Holder's date of birth

[`effective_end` ](#field-effective-end)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· Date policy becomes inactive

[`effective_start` ](#field-effective-start)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· Date policy becomes active

[`group_num` ](#field-group-num)· [`String` ](/reference/2026-01-01/scalars/string)· policy group num

[`holder_address` ](#field-holder-address)· [`String` ](/reference/2026-01-01/scalars/string)· policy holder address

[`holder_dob` ](#field-holder-dob)· [`String` ](/reference/2026-01-01/scalars/string)· policy holder dob, required

[`holder_first` ](#field-holder-first)· [`String` ](/reference/2026-01-01/scalars/string)· holder first name

[`holder_gender` ](#field-holder-gender)· [`String` ](/reference/2026-01-01/scalars/string)· holder gender

[`holder_last` ](#field-holder-last)· [`String` ](/reference/2026-01-01/scalars/string)· holder last name

[`holder_location` ](#field-holder-location)· [`Location` ](/reference/2026-01-01/objects/location)· The address of the holder

[`holder_location_id` ](#field-holder-location-id)· [`String` ](/reference/2026-01-01/scalars/string)· holder location id

[`holder_mi` ](#field-holder-mi)· [`String` ](/reference/2026-01-01/scalars/string)· holder middle initial

[`holder_name` ](#field-holder-name)· [`String` ](/reference/2026-01-01/scalars/string)· policy holder name

[`holder_phone` ](#field-holder-phone)· [`String` ](/reference/2026-01-01/scalars/string)· holder phone number

[`holder_relationship` ](#field-holder-relationship)· [`String` ](/reference/2026-01-01/scalars/string)· policy holder relationship, required

[`icd_codes_policies` ](#field-icd-codes-policies)· [`[IcdCodesPolicy!]` ](/reference/2026-01-01/objects/icdcodespolicy)· ICD codes authorized for this policy

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the policy

[`insurance_authorization` ](#field-insurance-authorization)· [`InsuranceAuthorizationType` ](/reference/2026-01-01/objects/insuranceauthorizationtype)· Insurance authorization (eligibility) associated with policy

[`insurance_authorization_required` ](#field-insurance-authorization-required)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· True if insurance authorization is required

[`insurance_billing_method` ](#field-insurance-billing-method)· [`String` ](/reference/2026-01-01/scalars/string)· The insurance billing method for this policy (No billing method, Copay, Coinsurance, Unmet Deductible)

[`insurance_card_back_id` ](#field-insurance-card-back-id)· [`String` ](/reference/2026-01-01/scalars/string)· Document Id of insurance card image(back)

[`insurance_card_front_id` ](#field-insurance-card-front-id)· [`String` ](/reference/2026-01-01/scalars/string)· Document Id of insurance card image(front)

[`insurance_plan` ](#field-insurance-plan)· [`InsurancePlan` ](/reference/2026-01-01/objects/insuranceplan)· The insurance plan

[`insurance_plan_id` ](#field-insurance-plan-id)· [`String` ](/reference/2026-01-01/scalars/string)· policy plan id, required

[`last_eligibility_check` ](#field-last-eligibility-check)· [`ClaimEligibilityCheck` ](/reference/2026-01-01/objects/claimeligibilitycheck)· DEPRECATED. The last automated eligibility check run for this Change Health policy.

deprecated

Use \`latest\_eligibility\_check\` instead

[`latest_eligibility_check` ](#field-latest-eligibility-check)· [`EligibilityCheck` ](/reference/2026-01-01/objects/eligibilitycheck)· the most recent automated eligibility check run for this policy.

[`metadata` ](#field-metadata)· [`JSON` ](/reference/2026-01-01/scalars/json)· A serialized JSON string of metadata. Maximum character limit of 2,000.

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the policy

[`notes` ](#field-notes)· [`String` ](/reference/2026-01-01/scalars/string)· Notes in client profile recorded by provider user

[`num` ](#field-num)· [`String` ](/reference/2026-01-01/scalars/string)· policy num, required

[`payer_location` ](#field-payer-location)· [`Location` ](/reference/2026-01-01/objects/location)· The address of the insurance plan

[`payer_location_id` ](#field-payer-location-id)· [`String` ](/reference/2026-01-01/scalars/string)· payer location ID

[`policy_phone_number` ](#field-policy-phone-number)· [`String` ](/reference/2026-01-01/scalars/string)· policy phone number

[`priority_type` ](#field-priority-type)· [`String` ](/reference/2026-01-01/scalars/string)· Priority of policy for client (primary, secondary, or inactive)

[`referral` ](#field-referral)· [`Referral` ](/reference/2026-01-01/objects/referral)· Referral added to this policy. Optional field that should not be nil if referral\_required is true

[`referral_required` ](#field-referral-required)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· True if referral is required for policy

[`same_address_as_client` ](#field-same-address-as-client)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Same as client address toggle

[`type_string` ](#field-type-string)· [`String` ](/reference/2026-01-01/scalars/string)· Insurance plan type?

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· Date policy was last updated

[`user` ](#field-user)· [`User` ](/reference/2026-01-01/objects/user)· Owner of this policy

[`user_id` ](#field-user-id)· [`ID` ](/reference/2026-01-01/scalars/id)· user id, required

## Used By

[`ClaimEligibilityCheck.policy`](/reference/2026-01-01/objects/claimeligibilitycheck)

[`Cms1500Policy.policy`](/reference/2026-01-01/objects/cms1500policy)

[`EligibilityCheck.policy`](/reference/2026-01-01/objects/eligibilitycheck)

[`User.policies`](/reference/2026-01-01/objects/user)

[`User.policiesOrderAscending`](/reference/2026-01-01/objects/user)

[`User.primary_insurance_policy`](/reference/2026-01-01/objects/user)

[`updatePolicyMutationPayload.policy`](/reference/2026-01-01/objects/updatepolicymutationpayload)

[`Query.policy`](/reference/2026-01-01/queries/policy)

## Definition

```
"""
A policy
"""
type Policy {
  """
  Benefits associated with policy
  """
  benefits: [Benefit!]


  """
  Call reference information associated with this policy
  """
  call_reference: CallReference


  """
  Returns a list of errors associated with the policy after doing a Change Health Insurance Eligibility Check
  """
  claim_eligibility_check_errors: [ClaimEligibilityCheckErrors!]


  """
  Value if insurance billing method is coinsurance
  """
  coinsurance_value: Int


  """
  Value (in cents) if insurance billing method is copay
  """
  copay_value: Int


  """
  CPT codes authorized for this policy
  """
  cpt_codes_policies: [CptCodesPolicy!]


  """
  Date policy was added
  """
  created_at: ISO8601DateTime


  """
  Holder's date of birth
  """
  dob_to_use: ISO8601Date


  """
  Date policy becomes inactive
  """
  effective_end: ISO8601DateTime


  """
  Date policy becomes active
  """
  effective_start: ISO8601DateTime


  """
  policy group num
  """
  group_num: String


  """
  policy holder address
  """
  holder_address: String


  """
  policy holder dob, required
  """
  holder_dob: String


  """
  holder first name
  """
  holder_first: String


  """
  holder gender
  """
  holder_gender: String


  """
  holder last name
  """
  holder_last: String


  """
  The address of the holder
  """
  holder_location: Location


  """
  holder location id
  """
  holder_location_id: String


  """
  holder middle initial
  """
  holder_mi: String


  """
  policy holder name
  """
  holder_name: String


  """
  holder phone number
  """
  holder_phone: String


  """
  policy holder relationship, required
  """
  holder_relationship: String


  """
  ICD codes authorized for this policy
  """
  icd_codes_policies: [IcdCodesPolicy!]


  """
  The unique identifier of the policy
  """
  id: ID!


  """
  Insurance authorization (eligibility) associated with policy
  """
  insurance_authorization: InsuranceAuthorizationType


  """
  True if insurance authorization is required
  """
  insurance_authorization_required: Boolean


  """
  The insurance billing method for this policy (No billing method, Copay, Coinsurance, Unmet Deductible)
  """
  insurance_billing_method: String


  """
  Document Id of insurance card image(back)
  """
  insurance_card_back_id: String


  """
  Document Id of insurance card image(front)
  """
  insurance_card_front_id: String


  """
  The insurance plan
  """
  insurance_plan: InsurancePlan


  """
  policy plan id, required
  """
  insurance_plan_id: String


  """
  DEPRECATED. The last automated eligibility check run for this Change Health policy.
  """
  last_eligibility_check: ClaimEligibilityCheck
    @deprecated(reason: "Use `latest_eligibility_check` instead")


  """
  the most recent automated eligibility check run for this policy.
  """
  latest_eligibility_check: EligibilityCheck


  """
  A serialized JSON string of metadata. Maximum character limit of 2,000.
  """
  metadata: JSON


  """
  The name of the policy
  """
  name: String


  """
  Notes in client profile recorded by provider user
  """
  notes: String


  """
  policy num, required
  """
  num: String


  """
  The address of the insurance plan
  """
  payer_location: Location


  """
  payer location ID
  """
  payer_location_id: String


  """
  policy phone number
  """
  policy_phone_number: String


  """
  Priority of policy for client (primary, secondary, or inactive)
  """
  priority_type: String


  """
  Referral added to this policy. Optional field that should not be nil if referral_required is true
  """
  referral: Referral


  """
  True if referral is required for policy
  """
  referral_required: Boolean


  """
  Same as client address toggle
  """
  same_address_as_client: Boolean


  """
  Insurance plan type?
  """
  type_string: String


  """
  Date policy was last updated
  """
  updated_at: ISO8601DateTime


  """
  Owner of this policy
  """
  user: User


  """
  user id, required
  """
  user_id: ID
}
```
