---
title: CptCodesPolicy | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/cptcodespolicy/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/cptcodespolicy/index.md
---

cpt codes policies join table

## Fields

[`code` ](#field-code)· [`String` ](/reference/2026-01-01/scalars/string)· cpt code

[`cpt_code_id` ](#field-cpt-code-id)· [`ID` ](/reference/2026-01-01/scalars/id)· id of instance of joins between cpt\_code and policy

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · date created

[`description` ](#field-description)· [`String` ](/reference/2026-01-01/scalars/string)· cpt code description

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the join between cpt\_code and policy.

[`policy_id` ](#field-policy-id)· [`ID` ](/reference/2026-01-01/scalars/id)· policy id

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · date updated

## Used By

[`Policy.cpt_codes_policies`](/reference/2026-01-01/objects/policy)

## Definition

```
"""
cpt codes policies join table
"""
type CptCodesPolicy {
  """
  cpt code
  """
  code: String


  """
  id of instance of joins between cpt_code and policy
  """
  cpt_code_id: ID


  """
  date created
  """
  created_at: ISO8601DateTime!


  """
  cpt code description
  """
  description: String


  """
  The unique identifier of the join between cpt_code and policy.
  """
  id: ID!


  """
  policy id
  """
  policy_id: ID


  """
  date updated
  """
  updated_at: ISO8601DateTime!
}
```
