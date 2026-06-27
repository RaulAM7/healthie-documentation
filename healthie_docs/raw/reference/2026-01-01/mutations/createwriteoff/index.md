---
title: createWriteOff | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createwriteoff/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createwriteoff/index.md
---

Create a Write-off

## Arguments

[`input` ](#argument-input)· [`createWriteOffInput` ](/reference/2026-01-01/input-objects/createwriteoffinput)· Parameters for createWriteOff

## Returns

[`createWriteOffPayload`](/reference/2026-01-01/objects/createwriteoffpayload)

## Example

```
mutation createWriteOff($input: createWriteOffInput) {
  createWriteOff(input: $input) {
    messages
    writeOff
  }
}
```
