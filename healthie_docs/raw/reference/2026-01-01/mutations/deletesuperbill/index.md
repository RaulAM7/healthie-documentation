---
title: deleteSuperBill | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletesuperbill/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletesuperbill/index.md
---

Destroy a Super Bill

## Arguments

[`input` ](#argument-input)· [`deleteSuperBillInput` ](/reference/2026-01-01/input-objects/deletesuperbillinput)· Parameters for deleteSuperBill

## Returns

[`deleteSuperBillPayload`](/reference/2026-01-01/objects/deletesuperbillpayload)

## Example

```
mutation deleteSuperBill($input: deleteSuperBillInput) {
  deleteSuperBill(input: $input) {
    messages
    superBill
  }
}
```
