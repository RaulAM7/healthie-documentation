---
title: ClaimInsurancePlan | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/claiminsuranceplan/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/claiminsuranceplan/index.md
---

Frozen insurance plan data from a submitted claim snapshot

## Fields

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Insurance plan ID

[`name_and_id` ](#field-name-and-id)· [`String` ](/reference/2026-01-01/scalars/string)· Combined payer name and payer ID

[`payer_id` ](#field-payer-id)· [`String` ](/reference/2026-01-01/scalars/string)· Insurance payer ID

[`payer_name` ](#field-payer-name)· [`String` ](/reference/2026-01-01/scalars/string)· Insurance payer name

## Used By

[`ClaimPolicy.insurance_plan`](/reference/2026-01-01/objects/claimpolicy)

## Definition

```
"""
Frozen insurance plan data from a submitted claim snapshot
"""
type ClaimInsurancePlan {
  """
  Insurance plan ID
  """
  id: ID


  """
  Combined payer name and payer ID
  """
  name_and_id: String


  """
  Insurance payer ID
  """
  payer_id: String


  """
  Insurance payer name
  """
  payer_name: String
}
```
