---
title: ClientInsurancePlanInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/clientinsuranceplaninput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/clientinsuranceplaninput/index.md
---

Payload for an insurance plan

## Fields

[`id` ](#field-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the insurance plan

[`metadata` ](#field-metadata)· [`JSON` ](/reference/2026-01-01/scalars/json)· A serialized JSON string of metadata. Maximum character limit of 2,000.

[`payer_name` ](#field-payer-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the payer

## Used By

[`ClientPolicyInput.insurance_plan`](/reference/2026-01-01/input-objects/clientpolicyinput)

[`UserPolicyInput.insurance_plan`](/reference/2026-01-01/input-objects/userpolicyinput)

## Definition

```
"""
Payload for an insurance plan
"""
input ClientInsurancePlanInput {
  """
  The ID of the insurance plan
  """
  id: String


  """
  A serialized JSON string of metadata. Maximum character limit of 2,000.
  """
  metadata: JSON


  """
  The name of the payer
  """
  payer_name: String
}
```
