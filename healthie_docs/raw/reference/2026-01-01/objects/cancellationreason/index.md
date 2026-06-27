---
title: CancellationReason | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/cancellationreason/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/cancellationreason/index.md
---

An appointment cancellation reasons

## Fields

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the cancellation reason

[`label` ](#field-label)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The label of the cancellation reason

[`reason_type` ](#field-reason-type)· [`CancellationReasonTypeEnum!` ](/reference/2026-01-01/enums/cancellationreasontypeenum)· required · The type of cancellation reason

## Used By

[`Appointment.cancellation_reason`](/reference/2026-01-01/objects/appointment)

[`Organization.cancellation_reasons`](/reference/2026-01-01/objects/organization)

## Definition

```
"""
An appointment cancellation reasons
"""
type CancellationReason {
  """
  The unique identifier of the cancellation reason
  """
  id: ID!


  """
  The label of the cancellation reason
  """
  label: String!


  """
  The type of cancellation reason
  """
  reason_type: CancellationReasonTypeEnum!
}
```
