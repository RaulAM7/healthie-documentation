---
title: ClaimPolicy | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/claimpolicy/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/claimpolicy/index.md
---

Frozen policy data from a submitted claim snapshot

## Fields

[`group_number` ](#field-group-number)· [`String` ](/reference/2026-01-01/scalars/string)· Group number

[`holder` ](#field-holder)· [`ClaimPolicyHolder` ](/reference/2026-01-01/objects/claimpolicyholder)· Insurance subscriber (policyholder)

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Policy ID

[`insurance_plan` ](#field-insurance-plan)· [`ClaimInsurancePlan` ](/reference/2026-01-01/objects/claiminsuranceplan)· Insurance plan at time of submission

[`member_id` ](#field-member-id)· [`String` ](/reference/2026-01-01/scalars/string)· Member ID

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· Policy name

[`payer_location` ](#field-payer-location)· [`ClaimLocation` ](/reference/2026-01-01/objects/claimlocation)· Insurance company address at time of submission

[`policy_phone_number` ](#field-policy-phone-number)· [`String` ](/reference/2026-01-01/scalars/string)· Insurance company phone number

[`priority_type` ](#field-priority-type)· [`ClaimPolicyPriority` ](/reference/2026-01-01/enums/claimpolicypriority)· Policy priority

[`type_string` ](#field-type-string)· [`String` ](/reference/2026-01-01/scalars/string)· Policy type (e.g. Commercial, Medicare)

## Used By

[`Claim.policies`](/reference/2026-01-01/objects/claim)

## Definition

```
"""
Frozen policy data from a submitted claim snapshot
"""
type ClaimPolicy {
  """
  Group number
  """
  group_number: String


  """
  Insurance subscriber (policyholder)
  """
  holder: ClaimPolicyHolder


  """
  Policy ID
  """
  id: ID


  """
  Insurance plan at time of submission
  """
  insurance_plan: ClaimInsurancePlan


  """
  Member ID
  """
  member_id: String


  """
  Policy name
  """
  name: String


  """
  Insurance company address at time of submission
  """
  payer_location: ClaimLocation


  """
  Insurance company phone number
  """
  policy_phone_number: String


  """
  Policy priority
  """
  priority_type: ClaimPolicyPriority


  """
  Policy type (e.g. Commercial, Medicare)
  """
  type_string: String
}
```
