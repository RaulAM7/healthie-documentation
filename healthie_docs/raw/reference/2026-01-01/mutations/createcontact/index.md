---
title: createContact | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createcontact/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createcontact/index.md
---

Creates a Contact

## Arguments

[`input` ](#argument-input)· [`createContactInput` ](/reference/2026-01-01/input-objects/createcontactinput)· Parameters for createContact

## Returns

[`createContactPayload`](/reference/2026-01-01/objects/createcontactpayload)

## Example

```
mutation createContact($input: createContactInput) {
  createContact(input: $input) {
    messages
    visitor
  }
}
```
