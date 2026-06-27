---
title: createLabOrder | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createlaborder/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createlaborder/index.md
---

Create Lab Order

## Arguments

[`input` ](#argument-input)· [`createLabOrderInput` ](/reference/2026-01-01/input-objects/createlaborderinput)· Parameters for createLabOrder

## Returns

[`createLabOrderPayload`](/reference/2026-01-01/objects/createlaborderpayload)

## Example

```
mutation createLabOrder($input: createLabOrderInput) {
  createLabOrder(input: $input) {
    currentUserNotificationsCount
    lab_order
    messages
  }
}
```
