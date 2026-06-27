---
title: CancellationReasonTypeEnum | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/cancellationreasontypeenum/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/cancellationreasontypeenum/index.md
---

Type of cancellation reason based on who initiated the cancellation

## Used By

[`CancellationReason.reason_type`](/reference/2026-01-01/objects/cancellationreason)

[`Organization.cancellation_reasons`](/reference/2026-01-01/objects/organization)

[`CancellationReasonOptionInput.initiated_by`](/reference/2026-01-01/input-objects/cancellationreasonoptioninput)

## Definition

```
"""
Type of cancellation reason based on who initiated the cancellation
"""
enum CancellationReasonTypeEnum {
  """
  Returns all cancellation reasons regardless of type
  """
  all


  """
  Cancellation initiated by the client
  """
  client


  """
  Cancellation initiated by the provider
  """
  provider


  """
  Cancellation initiated by the organization
  """
  organization
}
```
