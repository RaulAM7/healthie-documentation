---
title: IcdCodesPolicy | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/icdcodespolicy/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/icdcodespolicy/index.md
---

icd codes policies join table

## Fields

[`code` ](#field-code)· [`String` ](/reference/2026-01-01/scalars/string)· The ICD code

[`created_at` ](#field-created-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The date when the join was created

[`description` ](#field-description)· [`String` ](/reference/2026-01-01/scalars/string)· The description of the join

[`icd_code` ](#field-icd-code)· [`IcdCode` ](/reference/2026-01-01/objects/icdcode)· The ICD code object

[`icd_code_id` ](#field-icd-code-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the joined ICD code

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The unique identifier of the join between ICD code and policy.

[`policy_id` ](#field-policy-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the joined policy

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The date updated

## Used By

[`Policy.icd_codes_policies`](/reference/2026-01-01/objects/policy)

## Definition

```
"""
icd codes policies join table
"""
type IcdCodesPolicy {
  """
  The ICD code
  """
  code: String


  """
  The date when the join was created
  """
  created_at: ISO8601DateTime


  """
  The description of the join
  """
  description: String


  """
  The ICD code object
  """
  icd_code: IcdCode


  """
  The ID of the joined ICD code
  """
  icd_code_id: ID


  """
  The unique identifier of the join between ICD code and policy.
  """
  id: ID


  """
  The ID of the joined policy
  """
  policy_id: ID


  """
  The date updated
  """
  updated_at: ISO8601DateTime
}
```
