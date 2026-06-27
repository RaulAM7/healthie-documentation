---
title: deleteBillingItem | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletebillingitem/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletebillingitem/index.md
---

Destroy a Billing Item

## Arguments

[`input` ](#argument-input)· [`deleteBillingItemInput` ](/reference/2026-01-01/input-objects/deletebillingiteminput)· Parameters for deleteBillingItem

## Returns

[`deleteBillingItemPayload`](/reference/2026-01-01/objects/deletebillingitempayload)

## Example

```
mutation deleteBillingItem($input: deleteBillingItemInput) {
  deleteBillingItem(input: $input) {
    billingItem
    messages
  }
}
```
