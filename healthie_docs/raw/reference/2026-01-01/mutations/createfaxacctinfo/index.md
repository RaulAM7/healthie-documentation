---
title: createFaxAcctInfo | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createfaxacctinfo/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createfaxacctinfo/index.md
---

create Fax Acct Info

## Arguments

[`input` ](#argument-input)· [`createFaxAcctInfoInput` ](/reference/2026-01-01/input-objects/createfaxacctinfoinput)· Parameters for createFaxAcctInfo

## Returns

[`createFaxAcctInfoPayload`](/reference/2026-01-01/objects/createfaxacctinfopayload)

## Example

```
mutation createFaxAcctInfo($input: createFaxAcctInfoInput) {
  createFaxAcctInfo(input: $input) {
    messages
    success_string
  }
}
```
