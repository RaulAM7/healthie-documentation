---
title: updateChangeHealthAccount | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatechangehealthaccount/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatechangehealthaccount/index.md
---

Update ChangeHealthAccount (used for Labs)

## Arguments

[`input` ](#argument-input)· [`updateChangeHealthAccountInput` ](/reference/2026-01-01/input-objects/updatechangehealthaccountinput)· Parameters for updateChangeHealthAccount

## Returns

[`updateChangeHealthAccountPayload`](/reference/2026-01-01/objects/updatechangehealthaccountpayload)

## Example

```
mutation updateChangeHealthAccount($input: updateChangeHealthAccountInput) {
  updateChangeHealthAccount(input: $input) {
    messages
    success_string
  }
}
```
