---
title: ClaimServiceLine | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/claimserviceline/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/claimserviceline/index.md
---

Frozen service line data from a submitted claim snapshot

## Fields

[`cpt_code` ](#field-cpt-code)· [`ClaimCptCode` ](/reference/2026-01-01/objects/claimcptcode)· CPT procedure code

[`epsdt` ](#field-epsdt)· [`String` ](/reference/2026-01-01/scalars/string)· EPSDT indicator

[`family_planning_service` ](#field-family-planning-service)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Family planning indicator

[`fee` ](#field-fee)· [`String` ](/reference/2026-01-01/scalars/string)· Fee amount

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Service line ID

[`mod1` ](#field-mod1)· [`String` ](/reference/2026-01-01/scalars/string)· Modifier 1

[`mod2` ](#field-mod2)· [`String` ](/reference/2026-01-01/scalars/string)· Modifier 2

[`mod3` ](#field-mod3)· [`String` ](/reference/2026-01-01/scalars/string)· Modifier 3

[`mod4` ](#field-mod4)· [`String` ](/reference/2026-01-01/scalars/string)· Modifier 4

[`pointers` ](#field-pointers)· [`[Int!]` ](/reference/2026-01-01/scalars/int)· Diagnosis pointers (0-indexed)

[`service_date` ](#field-service-date)· [`String` ](/reference/2026-01-01/scalars/string)· Service date

[`service_end_date` ](#field-service-end-date)· [`String` ](/reference/2026-01-01/scalars/string)· Service end date

[`units` ](#field-units)· [`Int` ](/reference/2026-01-01/scalars/int)· Number of units

## Used By

[`Claim.service_lines`](/reference/2026-01-01/objects/claim)

## Definition

```
"""
Frozen service line data from a submitted claim snapshot
"""
type ClaimServiceLine {
  """
  CPT procedure code
  """
  cpt_code: ClaimCptCode


  """
  EPSDT indicator
  """
  epsdt: String


  """
  Family planning indicator
  """
  family_planning_service: Boolean


  """
  Fee amount
  """
  fee: String


  """
  Service line ID
  """
  id: ID


  """
  Modifier 1
  """
  mod1: String


  """
  Modifier 2
  """
  mod2: String


  """
  Modifier 3
  """
  mod3: String


  """
  Modifier 4
  """
  mod4: String


  """
  Diagnosis pointers (0-indexed)
  """
  pointers: [Int!]


  """
  Service date
  """
  service_date: String


  """
  Service end date
  """
  service_end_date: String


  """
  Number of units
  """
  units: Int
}
```
