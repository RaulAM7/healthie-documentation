---
title: deleteCustomEmail | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletecustomemail/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletecustomemail/index.md
---

Destroy a Custom Email

## Arguments

[`input` ](#argument-input)· [`deleteCustomEmailInput` ](/reference/2026-01-01/input-objects/deletecustomemailinput)· Parameters for deleteCustomEmail

## Returns

[`deleteCustomEmailPayload`](/reference/2026-01-01/objects/deletecustomemailpayload)

## Example

```
mutation deleteCustomEmail($input: deleteCustomEmailInput) {
  deleteCustomEmail(input: $input) {
    customEmail
    messages
  }
}
```
