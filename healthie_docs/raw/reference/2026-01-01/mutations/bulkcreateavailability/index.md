---
title: bulkCreateAvailability | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/bulkcreateavailability/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/bulkcreateavailability/index.md
---

bulk create Availability

## Arguments

[`input` ](#argument-input)· [`bulkCreateAvailabilityInput` ](/reference/2026-01-01/input-objects/bulkcreateavailabilityinput)· Parameters for bulkCreateAvailability

## Returns

[`bulkCreateAvailabilityPayload`](/reference/2026-01-01/objects/bulkcreateavailabilitypayload)

## Example

```
mutation bulkCreateAvailability($input: bulkCreateAvailabilityInput) {
  bulkCreateAvailability(input: $input) {
    availabilities
    messages
  }
}
```
