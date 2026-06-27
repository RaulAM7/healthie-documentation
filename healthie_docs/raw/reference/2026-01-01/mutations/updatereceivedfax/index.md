---
title: updateReceivedFax | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatereceivedfax/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatereceivedfax/index.md
---

update a received fax

## Arguments

[`input` ](#argument-input)· [`updateReceivedFaxInput` ](/reference/2026-01-01/input-objects/updatereceivedfaxinput)· Parameters for updateReceivedFax

## Returns

[`updateReceivedFaxPayload`](/reference/2026-01-01/objects/updatereceivedfaxpayload)

## Example

```
mutation updateReceivedFax($input: updateReceivedFaxInput) {
  updateReceivedFax(input: $input) {
    messages
    receivedFax
  }
}
```
