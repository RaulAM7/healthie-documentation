---
title: CptCodesPolicyInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/cptcodespolicyinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/cptcodespolicyinput/index.md
---

Properties assigning a policy to a CPT code

## Fields

[`_destroy` ](#field--destroy)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the CPT codes policy will be deleted

[`cpt_code_id` ](#field-cpt-code-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the CPT code

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the join table record

[`policy_id` ](#field-policy-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the policy

## Used By

[`updatePolicyMutationInput.cpt_codes_policies`](/reference/2026-01-01/input-objects/updatepolicymutationinput)

## Definition

```
"""
Properties assigning a policy to a CPT code
"""
input CptCodesPolicyInput {
  """
  If true, the CPT codes policy will be deleted
  """
  _destroy: Boolean


  """
  The ID of the CPT code
  """
  cpt_code_id: String


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
