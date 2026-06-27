---
title: OfferingLabOption | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/offeringlaboption/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/offeringlaboption/index.md
---

Offering Lab Option

## Fields

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · created at

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the lab option

[`lab_option` ](#field-lab-option)· [`LabOption` ](/reference/2026-01-01/objects/laboption)· lab option

[`lab_option_id` ](#field-lab-option-id)· [`ID` ](/reference/2026-01-01/scalars/id)· id of related appointment type

[`offering_id` ](#field-offering-id)· [`ID` ](/reference/2026-01-01/scalars/id)· id of related offering

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · updated at

## Used By

[`Offering.offering_lab_options`](/reference/2026-01-01/objects/offering)

## Definition

```
"""
Offering Lab Option
"""
type OfferingLabOption {
  """
  created at
  """
  created_at: ISO8601DateTime!


  """
  The unique identifier of the lab option
  """
  id: ID!


  """
  lab option
  """
  lab_option: LabOption


  """
  id of related appointment type
  """
  lab_option_id: ID


  """
  id of related offering
  """
  offering_id: ID


  """
  updated at
  """
  updated_at: ISO8601DateTime!
}
```
