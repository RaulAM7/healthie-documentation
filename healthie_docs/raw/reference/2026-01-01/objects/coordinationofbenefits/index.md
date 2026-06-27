---
title: CoordinationOfBenefits | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/coordinationofbenefits/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/coordinationofbenefits/index.md
---

Coordination of Benefits data for a secondary claim, derived from primary claim ERA and manual overrides

## Fields

[`has_manual_overrides` ](#field-has-manual-overrides)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether any claim-level or line-level manual overrides exist

[`other_ins_dob` ](#field-other-ins-dob)· [`ISO8601Date` ](/reference/2026-01-01/scalars/iso8601date)· Primary subscriber date of birth

[`other_ins_first_name` ](#field-other-ins-first-name)· [`String` ](/reference/2026-01-01/scalars/string)· Primary subscriber first name

[`other_ins_group_num` ](#field-other-ins-group-num)· [`String` ](/reference/2026-01-01/scalars/string)· Primary insurance group number

[`other_ins_last_name` ](#field-other-ins-last-name)· [`String` ](/reference/2026-01-01/scalars/string)· Primary subscriber last name

[`other_ins_member_id` ](#field-other-ins-member-id)· [`String` ](/reference/2026-01-01/scalars/string)· Primary subscriber member ID

[`other_ins_relationship` ](#field-other-ins-relationship)· [`String` ](/reference/2026-01-01/scalars/string)· Patient relationship to primary subscriber

[`other_payer_id` ](#field-other-payer-id)· [`String` ](/reference/2026-01-01/scalars/string)· Payer ID of the primary insurance

[`other_payer_name` ](#field-other-payer-name)· [`String` ](/reference/2026-01-01/scalars/string)· Name of the primary insurance payer

[`primary_adjudication_date` ](#field-primary-adjudication-date)· [`ISO8601Date` ](/reference/2026-01-01/scalars/iso8601date)· Date the primary payer adjudicated the claim

[`primary_paid_amount` ](#field-primary-paid-amount)· [`Float` ](/reference/2026-01-01/scalars/float)· Total amount paid by the primary payer

[`service_line_adjustments` ](#field-service-line-adjustments)· [`[CobServiceLineAdjustment!]!` ](/reference/2026-01-01/objects/cobservicelineadjustment)· required · Per-service-line COB data

## Used By

[`Claim.coordination_of_benefits`](/reference/2026-01-01/objects/claim)

## Definition

```
"""
Coordination of Benefits data for a secondary claim, derived from primary claim ERA and manual overrides
"""
type CoordinationOfBenefits {
  """
  Whether any claim-level or line-level manual overrides exist
  """
  has_manual_overrides: Boolean!


  """
  Primary subscriber date of birth
  """
  other_ins_dob: ISO8601Date


  """
  Primary subscriber first name
  """
  other_ins_first_name: String


  """
  Primary insurance group number
  """
  other_ins_group_num: String


  """
  Primary subscriber last name
  """
  other_ins_last_name: String


  """
  Primary subscriber member ID
  """
  other_ins_member_id: String


  """
  Patient relationship to primary subscriber
  """
  other_ins_relationship: String


  """
  Payer ID of the primary insurance
  """
  other_payer_id: String


  """
  Name of the primary insurance payer
  """
  other_payer_name: String


  """
  Date the primary payer adjudicated the claim
  """
  primary_adjudication_date: ISO8601Date


  """
  Total amount paid by the primary payer
  """
  primary_paid_amount: Float


  """
  Per-service-line COB data
  """
  service_line_adjustments: [CobServiceLineAdjustment!]!
}
```
