---
title: EraServiceLine | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/eraserviceline/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/eraserviceline/index.md
---

A service line for the claim

## Fields

[`billed_amount` ](#field-billed-amount)· [`Float!` ](/reference/2026-01-01/scalars/float)· required · The billed amount

[`contractual_obligation_adjustments` ](#field-contractual-obligation-adjustments)· [`[EraAdjustment!]` ](/reference/2026-01-01/objects/eraadjustment)· The contractual obligation adjustments

[`end_date` ](#field-end-date)· [`ISO8601Date` ](/reference/2026-01-01/scalars/iso8601date)· The end date of the service

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the service line

[`other_adjustments` ](#field-other-adjustments)· [`[EraAdjustment!]` ](/reference/2026-01-01/objects/eraadjustment)· Other adjustments

[`paid_amount` ](#field-paid-amount)· [`Float!` ](/reference/2026-01-01/scalars/float)· required · The paid amount for the service

[`patient_responsibility_adjustments` ](#field-patient-responsibility-adjustments)· [`[EraAdjustment!]` ](/reference/2026-01-01/objects/eraadjustment)· The patient responsibility adjustments

[`payer_initiated_adjustments` ](#field-payer-initiated-adjustments)· [`[EraAdjustment!]` ](/reference/2026-01-01/objects/eraadjustment)· Payer initiated adjustments

[`service_code` ](#field-service-code)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The service code

[`start_date` ](#field-start-date)· [`ISO8601Date!` ](/reference/2026-01-01/scalars/iso8601date)· required · The start date of the service

## Used By

[`EraServiceLineConnection.nodes`](/reference/2026-01-01/objects/eraservicelineconnection)

[`EraServiceLineEdge.node`](/reference/2026-01-01/objects/eraservicelineedge)

## Definition

```
"""
A service line for the claim
"""
type EraServiceLine {
  """
  The billed amount
  """
  billed_amount: Float!


  """
  The contractual obligation adjustments
  """
  contractual_obligation_adjustments: [EraAdjustment!]


  """
  The end date of the service
  """
  end_date: ISO8601Date


  """
  The unique identifier of the service line
  """
  id: ID!


  """
  Other adjustments
  """
  other_adjustments: [EraAdjustment!]


  """
  The paid amount for the service
  """
  paid_amount: Float!


  """
  The patient responsibility adjustments
  """
  patient_responsibility_adjustments: [EraAdjustment!]


  """
  Payer initiated adjustments
  """
  payer_initiated_adjustments: [EraAdjustment!]


  """
  The service code
  """
  service_code: String!


  """
  The start date of the service
  """
  start_date: ISO8601Date!
}
```
