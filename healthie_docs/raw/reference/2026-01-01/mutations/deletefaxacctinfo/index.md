---
title: deleteFaxAcctInfo | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletefaxacctinfo/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletefaxacctinfo/index.md
---

destroy Fax Acct Info

## Arguments

[`input` ](#argument-input)· [`destroyFaxAcctInfoInput` ](/reference/2026-01-01/input-objects/destroyfaxacctinfoinput)· Parameters for destroyFaxAcctInfo

## Returns

[`destroyFaxAcctInfoPayload`](/reference/2026-01-01/objects/destroyfaxacctinfopayload)

## Example

```
mutation deleteFaxAcctInfo($input: destroyFaxAcctInfoInput) {
  deleteFaxAcctInfo(input: $input) {
    messages
    success_string
  }
}
```
