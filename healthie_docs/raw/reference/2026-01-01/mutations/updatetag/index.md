---
title: updateTag | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatetag/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatetag/index.md
---

Update a custom user tag

## Arguments

[`input` ](#argument-input)· [`updateTagInput` ](/reference/2026-01-01/input-objects/updatetaginput)· Parameters for updateTag

## Returns

[`updateTagPayload`](/reference/2026-01-01/objects/updatetagpayload)

## Example

```
mutation updateTag($input: updateTagInput) {
  updateTag(input: $input) {
    messages
    tag
  }
}
```
