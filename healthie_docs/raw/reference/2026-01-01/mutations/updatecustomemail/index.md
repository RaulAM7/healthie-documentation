---
title: updateCustomEmail | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatecustomemail/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatecustomemail/index.md
---

Update a Custom Email

## Arguments

[`input` ](#argument-input)· [`updateCustomEmailInput` ](/reference/2026-01-01/input-objects/updatecustomemailinput)· Parameters for updateCustomEmail

## Returns

[`updateCustomEmailPayload`](/reference/2026-01-01/objects/updatecustomemailpayload)

## Example

```
mutation updateCustomEmail($input: updateCustomEmailInput) {
  updateCustomEmail(input: $input) {
    customEmail
    messages
  }
}
```
