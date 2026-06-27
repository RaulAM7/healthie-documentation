---
title: createBillingItem | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createbillingitem/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createbillingitem/index.md
---

create billing item

## Arguments

[`input` ](#argument-input)· [`createBillingItemInput` ](/reference/2026-01-01/input-objects/createbillingiteminput)· Parameters for createBillingItem

## Returns

[`createBillingItemPayload`](/reference/2026-01-01/objects/createbillingitempayload)

## Example

```
mutation createBillingItem($input: createBillingItemInput) {
  createBillingItem(input: $input) {
    billingItem
    messages
    stripeError
  }
}
```
