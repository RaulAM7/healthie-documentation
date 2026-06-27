---
title: createAvailability | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createavailability/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createavailability/index.md
---

Create availability

## Arguments

[`input` ](#argument-input)· [`createAvailabilityInput` ](/reference/2026-01-01/input-objects/createavailabilityinput)· Parameters for createAvailability

## Returns

[`createAvailabilityPayload`](/reference/2026-01-01/objects/createavailabilitypayload)

## Example

```
mutation createAvailability($input: createAvailabilityInput) {
  createAvailability(input: $input) {
    availability
    messages
  }
}
```
