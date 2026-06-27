---
title: Cms1500PolicyInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/cms1500policyinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/cms1500policyinput/index.md
---

Payload for associating a policy with a CMS 1500

## Fields

[`_destroy` ](#field--destroy)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the join table record will be deleted upon submission

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the join table record

[`policy` ](#field-policy)· [`PolicyInput` ](/reference/2026-01-01/input-objects/policyinput)· The associated policy

[`policy_id` ](#field-policy-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the policy

## Used By

[`createCms1500Input.cms1500_policies`](/reference/2026-01-01/input-objects/createcms1500input)

[`updateCms1500Input.cms1500_policies`](/reference/2026-01-01/input-objects/updatecms1500input)

## Definition

```
"""
Payload for associating a policy with a CMS 1500
"""
input Cms1500PolicyInput {
  """
  If true, the join table record will be deleted upon submission
  """
  _destroy: Boolean


  """
  The ID of the join table record
  """
  id: ID


  """
  The associated policy
  """
  policy: PolicyInput


  """
  The ID of the policy
  """
  policy_id: String
}
```
