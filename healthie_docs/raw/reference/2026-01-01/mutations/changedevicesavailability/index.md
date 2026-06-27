---
title: changeDevicesAvailability | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/changedevicesavailability/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/changedevicesavailability/index.md
---

disabled devices in video chat

## Arguments

[`input` ](#argument-input)· [`ChangeDevicesAvailabilityInput` ](/reference/2026-01-01/input-objects/changedevicesavailabilityinput)· Parameters for ChangeDevicesAvailability

## Returns

[`ChangeDevicesAvailabilityPayload`](/reference/2026-01-01/objects/changedevicesavailabilitypayload)

## Example

```
mutation changeDevicesAvailability($input: ChangeDevicesAvailabilityInput) {
  changeDevicesAvailability(input: $input) {
    messages
  }
}
```
