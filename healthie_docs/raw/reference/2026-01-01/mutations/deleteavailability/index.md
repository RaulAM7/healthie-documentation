---
title: deleteAvailability | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteavailability/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteavailability/index.md
---

delete Availability

## Arguments

[`input` ](#argument-input)· [`deleteAvailabilityInput` ](/reference/2026-01-01/input-objects/deleteavailabilityinput)· Parameters for deleteAvailability

## Returns

[`deleteAvailabilityPayload`](/reference/2026-01-01/objects/deleteavailabilitypayload)

## Example

```
mutation deleteAvailability($input: deleteAvailabilityInput) {
  deleteAvailability(input: $input) {
    availability
    messages
  }
}
```
