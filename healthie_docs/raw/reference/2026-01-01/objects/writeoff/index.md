---
title: WriteOff | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/writeoff/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/writeoff/index.md
---

An invoice (requested payment) write-off

## Fields

[`amount` ](#field-amount)· [`Float!` ](/reference/2026-01-01/scalars/float)· required · The amount of the write-off

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the write-off

[`other_reason` ](#field-other-reason)· [`String` ](/reference/2026-01-01/scalars/string)· Non-standard reason for the write-off

[`requested_payment` ](#field-requested-payment)· [`RequestedPayment!` ](/reference/2026-01-01/objects/requestedpayment)· required · The requested payment associated with this write-off

[`write_off_type` ](#field-write-off-type)· [`WriteOffType!` ](/reference/2026-01-01/enums/writeofftype)· required · The type of write-off

## Used By

[`Query.writeOff`](/reference/2026-01-01/queries/writeoff)

[`RequestedPayment.write_offs`](/reference/2026-01-01/objects/requestedpayment)

[`createWriteOffPayload.writeOff`](/reference/2026-01-01/objects/createwriteoffpayload)

[`deleteWriteOffPayload.write_off`](/reference/2026-01-01/objects/deletewriteoffpayload)

[`updateWriteOffPayload.writeOff`](/reference/2026-01-01/objects/updatewriteoffpayload)

## Definition

```
"""
An invoice (requested payment) write-off
"""
type WriteOff {
  """
  The amount of the write-off
  """
  amount: Float!


  """
  The unique identifier of the write-off
  """
  id: ID!


  """
  Non-standard reason for the write-off
  """
  other_reason: String


  """
  The requested payment associated with this write-off
  """
  requested_payment: RequestedPayment!


  """
  The type of write-off
  """
  write_off_type: WriteOffType!
}
```
