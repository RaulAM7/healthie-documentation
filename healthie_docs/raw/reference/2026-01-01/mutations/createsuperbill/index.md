---
title: createSuperBill | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createsuperbill/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createsuperbill/index.md
---

create super bill

## Arguments

[`input` ](#argument-input)· [`createSuperBillInput!` ](/reference/2026-01-01/input-objects/createsuperbillinput)· required · Parameters for createSuperBill

## Returns

[`createSuperBillPayload`](/reference/2026-01-01/objects/createsuperbillpayload)

## Example

```
mutation createSuperBill($input: createSuperBillInput!) {
  createSuperBill(input: $input) {
    messages
    superBill
  }
}
```
