---
title: Cms1500Policy | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/cms1500policy/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/cms1500policy/index.md
---

A CMS1500 policy

## Fields

[`cms1500` ](#field-cms1500)· [`Cms1500` ](/reference/2026-01-01/objects/cms1500)· The cms1500 for the cms1500 policy

[`cms1500_id` ](#field-cms1500-id)· [`String` ](/reference/2026-01-01/scalars/string)· The id of the cms1500 for the cms1500 policy

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The unique identifier of the policy

[`policy` ](#field-policy)· [`Policy` ](/reference/2026-01-01/objects/policy)· The policy for the cms1500 policy

[`policy_id` ](#field-policy-id)· [`String` ](/reference/2026-01-01/scalars/string)· The policy id of the cms1500 for the cms1500 policy

## Used By

[`Cms1500.cms1500_policies`](/reference/2026-01-01/objects/cms1500)

## Definition

```
"""
A CMS1500 policy
"""
type Cms1500Policy {
  """
  The cms1500 for the cms1500 policy
  """
  cms1500: Cms1500


  """
  The id of the cms1500 for the cms1500 policy
  """
  cms1500_id: String


  """
  The unique identifier of the policy
  """
  id: ID


  """
  The policy for the cms1500 policy
  """
  policy: Policy


  """
  The policy id of the cms1500 for the cms1500 policy
  """
  policy_id: String
}
```
