---
title: ClientPolicyInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/clientpolicyinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/clientpolicyinput/index.md
---

Payload for a client policy

## Fields

[`copay_value` ](#field-copay-value)· [`Int` ](/reference/2026-01-01/scalars/int)· The value (in cents) if insurance billing method is copay

[`coinsurance_value` ](#field-coinsurance-value)· [`Int` ](/reference/2026-01-01/scalars/int)· The value if insurance billing method is coinsurance

[`_destroy` ](#field--destroy)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the policy will be deleted

[`group_num` ](#field-group-num)· [`String` ](/reference/2026-01-01/scalars/string)· The group number

[`holder_dob` ](#field-holder-dob)· [`String` ](/reference/2026-01-01/scalars/string)· The date of birth of the policy holder

[`holder_first` ](#field-holder-first)· [`String` ](/reference/2026-01-01/scalars/string)· The first name of the policy holder

[`holder_gender` ](#field-holder-gender)· [`String` ](/reference/2026-01-01/scalars/string)· The gender of the policy holder

[`holder_last` ](#field-holder-last)· [`String` ](/reference/2026-01-01/scalars/string)· The last name of the policy holder

[`holder_location` ](#field-holder-location)· [`ClientLocationInput` ](/reference/2026-01-01/input-objects/clientlocationinput)· The location of the policy holder

[`holder_mi` ](#field-holder-mi)· [`String` ](/reference/2026-01-01/scalars/string)· The middle initial of the policy holder

[`holder_phone` ](#field-holder-phone)· [`String` ](/reference/2026-01-01/scalars/string)· The phone number of the policy holder

[`holder_relationship` ](#field-holder-relationship)· [`String` ](/reference/2026-01-01/scalars/string)· The relationship of the policy holder to the client

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the policy

[`insurance_billing_method` ](#field-insurance-billing-method)· [`String` ](/reference/2026-01-01/scalars/string)· The insurance billing method for this policy (no\_billing\_method, copay, coinsurance, unmet\_deductible)

[`insurance_card_back` ](#field-insurance-card-back)· [`Upload` ](/reference/2026-01-01/scalars/upload)· The back of the insurance card

[`insurance_card_back_id` ](#field-insurance-card-back-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the back of the insurance card

[`insurance_card_front` ](#field-insurance-card-front)· [`Upload` ](/reference/2026-01-01/scalars/upload)· The front of the insurance card

[`insurance_card_front_id` ](#field-insurance-card-front-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the front of the insurance card

[`insurance_plan` ](#field-insurance-plan)· [`ClientInsurancePlanInput` ](/reference/2026-01-01/input-objects/clientinsuranceplaninput)· The insurance plan

[`insurance_plan_id` ](#field-insurance-plan-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the insurance plan

[`metadata` ](#field-metadata)· [`JSON` ](/reference/2026-01-01/scalars/json)· A serialized JSON string of metadata. Maximum character limit of 2,000.

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the policy

[`num` ](#field-num)· [`String` ](/reference/2026-01-01/scalars/string)· The policy number

[`payer_location` ](#field-payer-location)· [`ClientLocationInput` ](/reference/2026-01-01/input-objects/clientlocationinput)· The location of the payer

[`policy_phone_number` ](#field-policy-phone-number)· [`String` ](/reference/2026-01-01/scalars/string)· The policy-related phone number

[`priority_type` ](#field-priority-type)· [`String` ](/reference/2026-01-01/scalars/string)· The priority type of the policy

[`same_address_as_client` ](#field-same-address-as-client)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the policy holder has the same address as the client

[`type_string` ](#field-type-string)· [`String` ](/reference/2026-01-01/scalars/string)· The type of the policy

[`user_id` ](#field-user-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the user

## Used By

[`updateClientInput.policies`](/reference/2026-01-01/input-objects/updateclientinput)

## Definition

```
"""
Payload for a client policy
"""
input ClientPolicyInput {
  """
  The value (in cents) if insurance billing method is copay
  """
  copay_value: Int


  """
  The value if insurance billing method is coinsurance
  """
  coinsurance_value: Int


  """
  If true, the policy will be deleted
  """
  _destroy: Boolean


  """
  The group number
  """
  group_num: String


  """
  The date of birth of the policy holder
  """
  holder_dob: String


  """
  The first name of the policy holder
  """
  holder_first: String


  """
  The gender of the policy holder
  """
  holder_gender: String


  """
  The last name of the policy holder
  """
  holder_last: String


  """
  The location of the policy holder
  """
  holder_location: ClientLocationInput


  """
  The middle initial of the policy holder
  """
  holder_mi: String


  """
  The phone number of the policy holder
  """
  holder_phone: String


  """
  The relationship of the policy holder to the client
  """
  holder_relationship: String


  """
  The ID of the policy
  """
  id: ID


  """
  The insurance billing method for this policy (no_billing_method, copay, coinsurance, unmet_deductible)
  """
  insurance_billing_method: String


  """
  The back of the insurance card
  """
  insurance_card_back: Upload


  """
  The ID of the back of the insurance card
  """
  insurance_card_back_id: String


  """
  The front of the insurance card
  """
  insurance_card_front: Upload


  """
  The ID of the front of the insurance card
  """
  insurance_card_front_id: String


  """
  The insurance plan
  """
  insurance_plan: ClientInsurancePlanInput


  """
  The ID of the insurance plan
  """
  insurance_plan_id: String


  """
  A serialized JSON string of metadata. Maximum character limit of 2,000.
  """
  metadata: JSON


  """
  The name of the policy
  """
  name: String


  """
  The policy number
  """
  num: String


  """
  The location of the payer
  """
  payer_location: ClientLocationInput


  """
  The policy-related phone number
  """
  policy_phone_number: String


  """
  The priority type of the policy
  """
  priority_type: String


  """
  Whether the policy holder has the same address as the client
  """
  same_address_as_client: Boolean


  """
  The type of the policy
  """
  type_string: String


  """
  The ID of the user
  """
  user_id: String
}
```
