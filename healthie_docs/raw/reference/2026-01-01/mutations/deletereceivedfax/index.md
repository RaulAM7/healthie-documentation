---
title: deleteReceivedFax | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletereceivedfax/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletereceivedfax/index.md
---

Destroy a received fax

## Arguments

[`input` ](#argument-input)· [`deleteReceivedFaxInput` ](/reference/2026-01-01/input-objects/deletereceivedfaxinput)· Parameters for deleteReceivedFax

## Returns

[`deleteReceivedFaxPayload`](/reference/2026-01-01/objects/deletereceivedfaxpayload)

## Example

```
mutation deleteReceivedFax($input: deleteReceivedFaxInput) {
  deleteReceivedFax(input: $input) {
    messages
    receivedFax
  }
}
```
