---
title: createCustomEmail | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createcustomemail/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createcustomemail/index.md
---

create custom email

## Arguments

[`input` ](#argument-input)· [`createCustomEmailInput` ](/reference/2026-01-01/input-objects/createcustomemailinput)· Parameters for createCustomEmail

## Returns

[`createCustomEmailPayload`](/reference/2026-01-01/objects/createcustomemailpayload)

## Example

```
mutation createCustomEmail($input: createCustomEmailInput) {
  createCustomEmail(input: $input) {
    customEmail
    messages
  }
}
```
