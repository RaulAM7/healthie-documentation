---
title: IcdCodesPolicyInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/icdcodespolicyinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/icdcodespolicyinput/index.md
---

Payload for assigning a policy to an ICD code

## Fields

[`_destroy` ](#field--destroy)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the join table record will be deleted

[`icd_code_id` ](#field-icd-code-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the ICD code

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the join table record

[`policy_id` ](#field-policy-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the policy

## Used By

[`updatePolicyMutationInput.icd_codes_policies`](/reference/2026-01-01/input-objects/updatepolicymutationinput)

## Definition

```
"""
Payload for assigning a policy to an ICD code
"""
input IcdCodesPolicyInput {
  """
  If true, the join table record will be deleted
  """
  _destroy: Boolean


  """
  The ID of the ICD code
  """
  icd_code_id: String


  """
  The ID of the join table record
  """
  id: ID


  """
  The ID of the policy
  """
  policy_id: String
}
```
