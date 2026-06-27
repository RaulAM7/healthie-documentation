---
title: createSentFax | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createsentfax/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createsentfax/index.md
---

create Sent Fax

## Arguments

[`input` ](#argument-input)· [`createSentFaxInput` ](/reference/2026-01-01/input-objects/createsentfaxinput)· Parameters for createSentFax

## Returns

[`createSentFaxPayload`](/reference/2026-01-01/objects/createsentfaxpayload)

## Example

```
mutation createSentFax($input: createSentFaxInput) {
  createSentFax(input: $input) {
    messages
    sent_fax
  }
}
```
