---
title: bulkDeleteAvailability | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/bulkdeleteavailability/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/bulkdeleteavailability/index.md
---

Bulk delete Availability records by IDs. Use with caution. This mutation does not trigger webhooks and bulk deleted availability is not recoverable. .

## Arguments

[`input` ](#argument-input)· [`BulkDeleteAvailabilityInput` ](/reference/2026-01-01/input-objects/bulkdeleteavailabilityinput)· Parameters for BulkDeleteAvailability

## Returns

[`BulkDeleteAvailabilityPayload`](/reference/2026-01-01/objects/bulkdeleteavailabilitypayload)

## Example

```
mutation bulkDeleteAvailability($input: BulkDeleteAvailabilityInput) {
  bulkDeleteAvailability(input: $input) {
    deleted_count
    messages
    success
  }
}
```
