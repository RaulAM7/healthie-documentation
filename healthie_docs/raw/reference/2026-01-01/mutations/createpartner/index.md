---
title: createPartner | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createpartner/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createpartner/index.md
---

Creates a Partner

## Arguments

[`input` ](#argument-input)· [`createPartnerInput` ](/reference/2026-01-01/input-objects/createpartnerinput)· Parameters for createPartner

## Returns

[`createPartnerPayload`](/reference/2026-01-01/objects/createpartnerpayload)

## Example

```
mutation createPartner($input: createPartnerInput) {
  createPartner(input: $input) {
    messages
    visitor
  }
}
```
