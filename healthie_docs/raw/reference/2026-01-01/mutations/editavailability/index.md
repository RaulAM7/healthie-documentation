---
title: editAvailability | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/editavailability/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/editavailability/index.md
---

edit Availability

## Arguments

[`input` ](#argument-input)· [`editAvailabilityInput` ](/reference/2026-01-01/input-objects/editavailabilityinput)· Parameters for editAvailability

## Returns

[`editAvailabilityPayload`](/reference/2026-01-01/objects/editavailabilitypayload)

## Example

```
mutation editAvailability($input: editAvailabilityInput) {
  editAvailability(input: $input) {
    availability
    messages
  }
}
```
