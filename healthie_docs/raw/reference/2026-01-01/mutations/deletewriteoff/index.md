---
title: deleteWriteOff | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletewriteoff/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletewriteoff/index.md
---

Delete a write-off

## Arguments

[`input` ](#argument-input)· [`deleteWriteOffInput` ](/reference/2026-01-01/input-objects/deletewriteoffinput)· Parameters for deleteWriteOff

## Returns

[`deleteWriteOffPayload`](/reference/2026-01-01/objects/deletewriteoffpayload)

## Example

```
mutation deleteWriteOff($input: deleteWriteOffInput) {
  deleteWriteOff(input: $input) {
    messages
    write_off
  }
}
```
