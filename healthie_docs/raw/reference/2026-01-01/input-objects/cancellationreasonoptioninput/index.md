---
title: CancellationReasonOptionInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/cancellationreasonoptioninput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/cancellationreasonoptioninput/index.md
---

Payload for a cancellation reason option

## Fields

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the cancellation reason option

[`initiated_by` ](#field-initiated-by)· [`CancellationReasonTypeEnum` ](/reference/2026-01-01/enums/cancellationreasontypeenum)· Who initiated the cancellation

[`other_cancellation_reason` ](#field-other-cancellation-reason)· [`String` ](/reference/2026-01-01/scalars/string)· The other cancellation reason text

## Used By

[`deleteAppointmentInput.cancellation_reason`](/reference/2026-01-01/input-objects/deleteappointmentinput)

## Definition

```
"""
Payload for a cancellation reason option
"""
input CancellationReasonOptionInput {
  """
  The ID of the cancellation reason option
  """
  id: ID


  """
  Who initiated the cancellation
  """
  initiated_by: CancellationReasonTypeEnum


  """
  The other cancellation reason text
  """
  other_cancellation_reason: String
}
```
