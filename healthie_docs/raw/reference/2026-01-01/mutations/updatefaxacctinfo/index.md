---
title: updateFaxAcctInfo | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatefaxacctinfo/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatefaxacctinfo/index.md
---

update Fax Acct Info

## Arguments

[`input` ](#argument-input)· [`updateFaxAcctInfoInput` ](/reference/2026-01-01/input-objects/updatefaxacctinfoinput)· Parameters for updateFaxAcctInfo

## Returns

[`updateFaxAcctInfoPayload`](/reference/2026-01-01/objects/updatefaxacctinfopayload)

## Example

```
mutation updateFaxAcctInfo($input: updateFaxAcctInfoInput) {
  updateFaxAcctInfo(input: $input) {
    messages
    success_string
  }
}
```
