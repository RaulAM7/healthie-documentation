---
title: CobServiceLineAdjustment | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/cobservicelineadjustment/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/cobservicelineadjustment/index.md
---

COB data for a single service line on a secondary claim

## Fields

[`adjustments` ](#field-adjustments)· [`[CobAdjustment!]!` ](/reference/2026-01-01/objects/cobadjustment)· required · Adjustments applied to this service line

[`cpt_code` ](#field-cpt-code)· [`String` ](/reference/2026-01-01/scalars/string)· CPT procedure code

[`has_manual_override` ](#field-has-manual-override)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether this line has a manual COB override

[`line_adjudication_date` ](#field-line-adjudication-date)· [`ISO8601Date` ](/reference/2026-01-01/scalars/iso8601date)· Date the primary payer adjudicated this line

[`line_paid_amount` ](#field-line-paid-amount)· [`Float` ](/reference/2026-01-01/scalars/float)· Amount paid by the primary payer for this line

[`service_date` ](#field-service-date)· [`ISO8601Date` ](/reference/2026-01-01/scalars/iso8601date)· Service date for this line

## Used By

[`CoordinationOfBenefits.service_line_adjustments`](/reference/2026-01-01/objects/coordinationofbenefits)

## Definition

```
"""
COB data for a single service line on a secondary claim
"""
type CobServiceLineAdjustment {
  """
  Adjustments applied to this service line
  """
  adjustments: [CobAdjustment!]!


  """
  CPT procedure code
  """
  cpt_code: String


  """
  Whether this line has a manual COB override
  """
  has_manual_override: Boolean!


  """
  Date the primary payer adjudicated this line
  """
  line_adjudication_date: ISO8601Date


  """
  Amount paid by the primary payer for this line
  """
  line_paid_amount: Float


  """
  Service date for this line
  """
  service_date: ISO8601Date
}
```
