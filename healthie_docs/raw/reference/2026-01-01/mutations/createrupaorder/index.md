---
title: createRupaOrder | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createrupaorder/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createrupaorder/index.md
---

Create a Rupa order

## Arguments

[`input` ](#argument-input)· [`createRupaOrderInput` ](/reference/2026-01-01/input-objects/createrupaorderinput)· Parameters for createRupaOrder

## Returns

[`createRupaOrderPayload`](/reference/2026-01-01/objects/createrupaorderpayload)

## Example

```
mutation createRupaOrder($input: createRupaOrderInput) {
  createRupaOrder(input: $input) {
    messages
    rupa_order_url
  }
}
```
