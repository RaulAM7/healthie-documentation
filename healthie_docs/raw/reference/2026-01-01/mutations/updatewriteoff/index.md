---
title: updateWriteOff | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatewriteoff/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatewriteoff/index.md
---

Update a Write-off

## Arguments

[`input` ](#argument-input)· [`updateWriteOffInput` ](/reference/2026-01-01/input-objects/updatewriteoffinput)· Parameters for updateWriteOff

## Returns

[`updateWriteOffPayload`](/reference/2026-01-01/objects/updatewriteoffpayload)

## Example

```
mutation updateWriteOff($input: updateWriteOffInput) {
  updateWriteOff(input: $input) {
    messages
    writeOff
  }
}
```
