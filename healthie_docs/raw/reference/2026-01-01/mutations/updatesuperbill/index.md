---
title: updateSuperBill | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatesuperbill/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatesuperbill/index.md
---

Update a SuperBill

## Arguments

[`input` ](#argument-input)· [`updateSuperBillInput` ](/reference/2026-01-01/input-objects/updatesuperbillinput)· Parameters for updateSuperBill

## Returns

[`updateSuperBillPayload`](/reference/2026-01-01/objects/updatesuperbillpayload)

## Example

```
mutation updateSuperBill($input: updateSuperBillInput) {
  updateSuperBill(input: $input) {
    messages
    superBill
  }
}
```
