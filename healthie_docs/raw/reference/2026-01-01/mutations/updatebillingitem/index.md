---
title: updateBillingItem | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatebillingitem/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatebillingitem/index.md
---

Update a BillingItem

## Arguments

[`input` ](#argument-input)· [`updateBillingItemInput` ](/reference/2026-01-01/input-objects/updatebillingiteminput)· Parameters for updateBillingItem

## Returns

[`updateBillingItemPayload`](/reference/2026-01-01/objects/updatebillingitempayload)

## Example

```
mutation updateBillingItem($input: updateBillingItemInput) {
  updateBillingItem(input: $input) {
    billingItem
    messages
  }
}
```
