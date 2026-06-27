---
title: resyncRupaLabOrders | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/resyncrupalaborders/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/resyncrupalaborders/index.md
---

Resync existed rupa lab orders data for a specific rupa connection of the current user

## Arguments

[`input` ](#argument-input)· [`resyncRupaLabOrdersInput` ](/reference/2026-01-01/input-objects/resyncrupalabordersinput)· Parameters for resyncRupaLabOrders

## Returns

[`resyncRupaLabOrdersPayload`](/reference/2026-01-01/objects/resyncrupalaborderspayload)

## Example

```
mutation resyncRupaLabOrders($input: resyncRupaLabOrdersInput) {
  resyncRupaLabOrders(input: $input) {
    messages
    success
  }
}
```
