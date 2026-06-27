---
title: PolicyInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/policyinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/policyinput/index.md
---

Payload for a policy

## Fields

[`group_num` ](#field-group-num)· [`String` ](/reference/2026-01-01/scalars/string)· The group number

[`holder_dob` ](#field-holder-dob)· [`String` ](/reference/2026-01-01/scalars/string)· The date of birth of the holder

[`holder_first` ](#field-holder-first)· [`String` ](/reference/2026-01-01/scalars/string)· The first name of the holder

[`holder_gender` ](#field-holder-gender)· [`String` ](/reference/2026-01-01/scalars/string)· The gender of the holder

[`holder_last` ](#field-holder-last)· [`String` ](/reference/2026-01-01/scalars/string)· The last name of the holder

[`holder_location` ](#field-holder-location)· [`LocationInput` ](/reference/2026-01-01/input-objects/locationinput)· The location of the holder

[`holder_mi` ](#field-holder-mi)· [`String` ](/reference/2026-01-01/scalars/string)· The middle initial of the holder

[`holder_phone` ](#field-holder-phone)· [`String` ](/reference/2026-01-01/scalars/string)· The phone number of the holder

[`holder_relationship` ](#field-holder-relationship)· [`String` ](/reference/2026-01-01/scalars/string)· The relationship of the holder to the client

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the policy

[`insurance_card_back_id` ](#field-insurance-card-back-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the insurance card back

[`insurance_card_front_id` ](#field-insurance-card-front-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the insurance card front

[`insurance_plan` ](#field-insurance-plan)· [`InsurancePlanInput` ](/reference/2026-01-01/input-objects/insuranceplaninput)· The insurance plan associated with the policy

[`insurance_plan_id` ](#field-insurance-plan-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the insurance plan

[`metadata` ](#field-metadata)· [`JSON` ](/reference/2026-01-01/scalars/json)· A serialized JSON string of metadata. Maximum character limit of 2,000.

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the policy

[`num` ](#field-num)· [`String` ](/reference/2026-01-01/scalars/string)· The policy number

[`payer_location` ](#field-payer-location)· [`LocationInput` ](/reference/2026-01-01/input-objects/locationinput)· The location of the payer

[`policy_phone_number` ](#field-policy-phone-number)· [`String` ](/reference/2026-01-01/scalars/string)· The phone number of the policy

[`priority_type` ](#field-priority-type)· [`String` ](/reference/2026-01-01/scalars/string)· The priority type of the policy

[`same_address_as_client` ](#field-same-address-as-client)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the holder has the same address as the client

[`type_string` ](#field-type-string)· [`String` ](/reference/2026-01-01/scalars/string)· The type of policy

[`user_id` ](#field-user-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the user associated with the policy

## Used By

[`Cms1500PolicyInput.policy`](/reference/2026-01-01/input-objects/cms1500policyinput)

[`PatientInput.policies`](/reference/2026-01-01/input-objects/patientinput)

## Definition

```
"""
Payload for a policy
"""
input PolicyInput {
  """
  The group number
  """
  group_num: String


  """
  The date of birth of the holder
  """
  holder_dob: String


  """
  The first name of the holder
  """
  holder_first: String


  """
  The gender of the holder
  """
  holder_gender: String


  """
  The last name of the holder
  """
  holder_last: String


  """
  The location of the holder
  """
  holder_location: LocationInput


  """
  The middle initial of the holder
  """
  holder_mi: String


  """
  The phone number of the holder
  """
  holder_phone: String


  """
  The relationship of the holder to the client
  """
  holder_relationship: String


  """
  The ID of the policy
  """
  id: ID


  """
  The ID of the insurance card back
  """
  insurance_card_back_id: String


  """
  The ID of the insurance card front
  """
  insurance_card_front_id: String


  """
  The insurance plan associated with the policy
  """
  insurance_plan: InsurancePlanInput


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
  payer_location: LocationInput


  """
  The phone number of the policy
  """
  policy_phone_number: String


  """
  The priority type of the policy
  """
  priority_type: String


  """
  Whether the holder has the same address as the client
  """
  same_address_as_client: Boolean


  """
  The type of policy
  """
  type_string: String


  """
  The ID of the user associated with the policy
  """
  user_id: String
}
```
