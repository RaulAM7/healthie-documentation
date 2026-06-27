---
title: updateLabOrder | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatelaborder/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatelaborder/index.md
---

Update Lab Order

## Arguments

[`input` ](#argument-input)· [`updateLabOrderInput` ](/reference/2026-01-01/input-objects/updatelaborderinput)· Parameters for updateLabOrder

## Returns

[`updateLabOrderPayload`](/reference/2026-01-01/objects/updatelaborderpayload)

## Example

```
mutation updateLabOrder($input: updateLabOrderInput) {
  updateLabOrder(input: $input) {
    currentUserNotificationsCount
    lab_order
    messages
  }
}
```
