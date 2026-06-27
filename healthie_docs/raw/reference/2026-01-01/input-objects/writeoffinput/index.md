---
title: WriteOffInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/writeoffinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/writeoffinput/index.md
---

Payload for a writeoff

## Fields

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the write-off

[`amount` ](#field-amount)· [`Float!` ](/reference/2026-01-01/scalars/float)· required · The WriteOff amount

[`write_off_type` ](#field-write-off-type)· [`WriteOffType!` ](/reference/2026-01-01/enums/writeofftype)· required · The type of write-off

[`other_reason` ](#field-other-reason)· [`String` ](/reference/2026-01-01/scalars/string)· The other reason for the write-off

[`_destroy` ](#field--destroy)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, current write-off is deleted

## Used By

[`createRequestedPaymentInput.write_offs`](/reference/2026-01-01/input-objects/createrequestedpaymentinput)

[`updateRequestedPaymentInput.write_offs`](/reference/2026-01-01/input-objects/updaterequestedpaymentinput)

## Definition

```
"""
Payload for a writeoff
"""
input WriteOffInput {
  """
  The ID of the write-off
  """
  id: ID


  """
  The WriteOff amount
  """
  amount: Float!


  """
  The type of write-off
  """
  write_off_type: WriteOffType!


  """
  The other reason for the write-off
  """
  other_reason: String


  """
  When true, current write-off is deleted
  """
  _destroy: Boolean
}
```
