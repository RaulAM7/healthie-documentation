---
title: bulkApply | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/bulkapply/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/bulkapply/index.md
---

Apply selected tags on a specific user

## Arguments

[`input` ](#argument-input)· [`bulkApplyInput` ](/reference/2026-01-01/input-objects/bulkapplyinput)· Parameters for bulkApply

## Returns

[`bulkApplyPayload`](/reference/2026-01-01/objects/bulkapplypayload)

## Example

```
mutation bulkApply($input: bulkApplyInput) {
  bulkApply(input: $input) {
    messages
    tags
  }
}
```
